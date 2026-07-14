from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

PROFILE = "SCCERT-1-D01-EXP-A"
ACTION_PROFILE = "SCCERT-ACTION-1-D01-EXP-A"
CHAIN_PROFILE = "SCCERT-CHAIN-1-D01-EXP-A"
AUDIT_PROFILE = "SCCERT-AUDIT-1-D01-EXP-A"
JSON_PROFILE = "SCCERT-CANONICAL-JSON-1-D01-EXP-A"
STATE_PROFILE = "SCSTATE-1-D01"
RANK_PROFILE = "SCRANK-1-D01-EXP-A"
KERNEL_PROFILE = "SC-KERNEL-1-D01-EXP-A"
TARGET_PROFILE = "SC-KERNEL-TARGET-1-D01-EXP-A"
COMPILER_PROFILE = "SC-KERNEL-COMPILER-1-D01-EXP-A"
SHADOW_PROFILE = "SC-KERNEL-SHADOW-RESOLVER-1-D01-EXP-A"
PRIMARY_PROFILE = "SC-KERNEL-PRIMARY-RESOLVER-1-D01-EXP-A"
BUNDLE_PROFILE = "SCCERT-CORPUS-1-D01-EXP-A"
CORPUS_MANIFEST_PROFILE = "SCCERT-CORPUS-MANIFEST-1-D01-EXP-A"
CORPUS_AUDIT_PROFILE = "SCCERT-CORPUS-AUDIT-1-D01-EXP-A"
CORPUS_RUNNER_PROFILE = "SCCERT-CORPUS-RUNNER-1-D01-EXP-A"
BUNDLE_ROOT_PROFILE = "SHA256_CANONICAL_JSON_EXCLUDING_BUNDLE_ROOT"
FACES = ["U", "R", "F", "D", "L", "B"]
FACE_OFFSET = {"U": 0, "R": 9, "F": 18, "D": 27, "L": 36, "B": 45}
SOLVED = "".join(face * 9 for face in FACES)
CORNER_FACELETS = [[8, 9, 20], [6, 18, 38], [0, 36, 47], [2, 45, 11], [29, 26, 15], [27, 44, 24], [33, 53, 42], [35, 17, 51]]
CORNER_COLORS = [["U", "R", "F"], ["U", "F", "L"], ["U", "L", "B"], ["U", "B", "R"], ["D", "F", "R"], ["D", "L", "F"], ["D", "B", "L"], ["D", "R", "B"]]
EDGE_FACELETS = [[5, 10], [7, 19], [3, 37], [1, 46], [32, 16], [28, 25], [30, 43], [34, 52], [23, 12], [21, 41], [50, 39], [48, 14]]
EDGE_COLORS = [["U", "R"], ["U", "F"], ["U", "L"], ["U", "B"], ["D", "R"], ["D", "F"], ["D", "L"], ["D", "B"], ["F", "R"], ["F", "L"], ["B", "L"], ["B", "R"]]
BASE_SPECS = {
    "U": ("y", [1], -1), "R": ("x", [1], -1), "F": ("z", [1], -1), "D": ("y", [-1], 1), "L": ("x", [-1], 1), "B": ("z", [-1], 1),
    "M": ("x", [0], 1), "E": ("y", [0], 1), "S": ("z", [0], -1),
    "x": ("x", [-1, 0, 1], -1), "y": ("y", [-1, 0, 1], -1), "z": ("z", [-1, 0, 1], -1),
    "u": ("y", [0, 1], -1), "r": ("x", [0, 1], -1), "f": ("z", [0, 1], -1), "d": ("y", [-1, 0], 1), "l": ("x", [-1, 0], 1), "b": ("z", [-1, 0], 1),
}


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def index_geometry(face: str, row: int, col: int) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    if face == "U":
        return (col - 1, 1, row - 1), (0, 1, 0)
    if face == "R":
        return (1, 1 - row, 1 - col), (1, 0, 0)
    if face == "F":
        return (col - 1, 1 - row, 1), (0, 0, 1)
    if face == "D":
        return (col - 1, -1, 1 - row), (0, -1, 0)
    if face == "L":
        return (-1, 1 - row, col - 1), (-1, 0, 0)
    return (1 - col, 1 - row, -1), (0, 0, -1)


def rotate_vector(vector: tuple[int, int, int], axis: str, turns: int) -> tuple[int, int, int]:
    x, y, z = vector
    for _ in range(turns % 4):
        if axis == "x":
            y, z = -z, y
        elif axis == "y":
            x, z = z, -x
        else:
            x, y = -y, x
    return x, y, z


GEOMETRY: list[tuple[tuple[int, int, int], tuple[int, int, int]]] = [((0, 0, 0), (0, 0, 0)) for _ in range(54)]
GEOMETRY_TO_INDEX: dict[tuple[tuple[int, int, int], tuple[int, int, int]], int] = {}
for face in FACES:
    for row in range(3):
        for col in range(3):
            index = FACE_OFFSET[face] + row * 3 + col
            geometry = index_geometry(face, row, col)
            GEOMETRY[index] = geometry
            GEOMETRY_TO_INDEX[geometry] = index


def make_permutation(axis: str, layers: list[int], quarter_turns: int) -> list[int]:
    layer_set = set(layers)
    axis_index = 0 if axis == "x" else 1 if axis == "y" else 2
    permutation = list(range(54))
    for old_index, (position, normal) in enumerate(GEOMETRY):
        if position[axis_index] in layer_set:
            new_position = rotate_vector(position, axis, quarter_turns)
            new_normal = rotate_vector(normal, axis, quarter_turns)
            new_index = GEOMETRY_TO_INDEX[(new_position, new_normal)]
            permutation[new_index] = old_index
    return permutation


BASE_PERMUTATIONS = {name: make_permutation(*spec) for name, spec in BASE_SPECS.items()}


def parse_algorithm(value: Any) -> list[str]:
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    text = str(value or "").strip()
    if not text:
        return []
    output: list[str] = []
    for token in text.split():
        base = token[0] if token else ""
        suffix = token[1:]
        if base not in BASE_SPECS or suffix not in ("", "2", "'"):
            raise ValueError(f"UNSUPPORTED_MOVE:{token}")
        output.append(token)
    return output


def apply_permutation(state: str, permutation: list[int]) -> str:
    return "".join(state[permutation[index]] for index in range(54))


def apply_algorithm(state: str, algorithm: Any) -> str:
    output = state
    for token in parse_algorithm(algorithm):
        count = 2 if token.endswith("2") else 3 if token.endswith("'") else 1
        for _ in range(count):
            output = apply_permutation(output, BASE_PERMUTATIONS[token[0]])
    return output


def permutation_parity(permutation: list[int]) -> int:
    inversions = 0
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if permutation[i] > permutation[j]:
                inversions += 1
    return inversions & 1


def extract_cubies(state: str) -> dict[str, list[int]]:
    if len(state) != 54:
        raise ValueError("FACELET_LENGTH")
    counts = {face: state.count(face) for face in FACES}
    if any(char not in FACES for char in state):
        raise ValueError("UNKNOWN_COLOUR")
    if any(counts[face] != 9 for face in FACES):
        raise ValueError("COLOUR_COUNT")
    if [state[4], state[13], state[22], state[31], state[40], state[49]] != FACES:
        raise ValueError("CENTRE_ORIENTATION")
    cp = [0] * 8
    co = [0] * 8
    ep = [0] * 12
    eo = [0] * 12
    corner_seen = [False] * 8
    edge_seen = [False] * 12
    for position in range(8):
        orientation = 0
        while orientation < 3 and state[CORNER_FACELETS[position][orientation]] not in ("U", "D"):
            orientation += 1
        if orientation == 3:
            raise ValueError("CORNER_ORIENTATION_MISSING")
        c1 = state[CORNER_FACELETS[position][(orientation + 1) % 3]]
        c2 = state[CORNER_FACELETS[position][(orientation + 2) % 3]]
        piece = next((index for index, colors in enumerate(CORNER_COLORS) if colors[1] == c1 and colors[2] == c2), -1)
        if piece < 0:
            raise ValueError("UNKNOWN_CORNER")
        if corner_seen[piece]:
            raise ValueError("DUPLICATE_CORNER")
        corner_seen[piece] = True
        cp[position] = piece
        co[position] = orientation % 3
    for position in range(12):
        a = state[EDGE_FACELETS[position][0]]
        b = state[EDGE_FACELETS[position][1]]
        piece = -1
        orientation = 0
        for index, colors in enumerate(EDGE_COLORS):
            if colors[0] == a and colors[1] == b:
                piece = index
                orientation = 0
                break
            if colors[0] == b and colors[1] == a:
                piece = index
                orientation = 1
                break
        if piece < 0:
            raise ValueError("UNKNOWN_EDGE")
        if edge_seen[piece]:
            raise ValueError("DUPLICATE_EDGE")
        edge_seen[piece] = True
        ep[position] = piece
        eo[position] = orientation
    if sum(co) % 3 != 0:
        raise ValueError("CORNER_TWIST_PARITY")
    if sum(eo) % 2 != 0:
        raise ValueError("EDGE_FLIP_PARITY")
    if permutation_parity(cp) != permutation_parity(ep):
        raise ValueError("PERMUTATION_PARITY")
    return {"ep": ep, "eo": eo, "cp": cp, "co": co}


def state_hash(state: str) -> str:
    extract_cubies(state)
    return sha256_hex(f"{STATE_PROFILE}\n{state}\n")


def cycle_stats(permutation: list[int]) -> tuple[int, int]:
    seen = [False] * len(permutation)
    cycle_count = 0
    two_cycle_count = 0
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        cycle_count += 1
        if length == 2:
            two_cycle_count += 1
    return cycle_count, two_cycle_count


def rank_from_cubies(cubies: dict[str, list[int]]) -> dict[str, Any]:
    edge_cycles, tau_e = cycle_stats(cubies["ep"])
    corner_cycles, tau_c = cycle_stats(cubies["cp"])
    edge_parity = permutation_parity(cubies["ep"])
    corner_parity = permutation_parity(cubies["cp"])
    rho = edge_parity
    d_e = 12 - edge_cycles
    d_c = 8 - corner_cycles
    f = sum(1 for value in cubies["eo"] if value != 0)
    t = sum(min(value, 3 - value) for value in cubies["co"])
    w = 24 * rho + 4 * (d_e + d_c) + tau_e + tau_c + f + t
    phi = [rho, d_e + d_c, tau_e + tau_c, f, t]
    canonical_text = f"{RANK_PROFILE}\nRHO={rho}\nD_E={d_e}\nD_C={d_c}\nTAU_E={tau_e}\nTAU_C={tau_c}\nF={f}\nT={t}\nW={w}\n"
    return {
        "profile": RANK_PROFILE,
        "convention": "POSITION_TO_PERM_POSITION_INDEXED_ORIENTATION",
        "rho": rho,
        "edge_parity": edge_parity,
        "corner_parity": corner_parity,
        "D_e": d_e,
        "D_c": d_c,
        "tau_e": tau_e,
        "tau_c": tau_c,
        "F": f,
        "T": t,
        "W": w,
        "phi": phi,
        "solved_equivalence": w == 0,
        "bound_status": "PASS" if 0 <= w <= 126 else "FAIL",
        "canonical_text": canonical_text,
        "rank_hash": sha256_hex(canonical_text),
        "legality_invariants": {
            "edge_orientation_sum_mod_2": sum(cubies["eo"]) % 2,
            "corner_orientation_sum_mod_3": sum(cubies["co"]) % 3,
            "parity_agreement": edge_parity == corner_parity,
        },
    }


def rank_state(state: str) -> dict[str, Any]:
    return rank_from_cubies(extract_cubies(state))


def lex_compare(left: list[int], right: list[int]) -> int:
    for a, b in zip(left, right):
        if a < b:
            return -1
        if a > b:
            return 1
    return len(left) - len(right)


def clone_cubies(cubies: dict[str, list[int]]) -> dict[str, list[int]]:
    return {key: value[:] for key, value in cubies.items()}


def apply_position_cycle(cubies: dict[str, list[int]], cubie_type: str, positions: list[int], direction: str) -> dict[str, list[int]]:
    output = clone_cubies(cubies)
    source_perm = cubies["ep"] if cubie_type == "EDGE" else cubies["cp"]
    source_ori = cubies["eo"] if cubie_type == "EDGE" else cubies["co"]
    target_perm = output["ep"] if cubie_type == "EDGE" else output["cp"]
    target_ori = output["eo"] if cubie_type == "EDGE" else output["co"]
    step = -1 if direction == "REVERSE" else 1
    size = len(positions)
    for index, old_position in enumerate(positions):
        new_position = positions[(index + step + size) % size]
        target_perm[new_position] = source_perm[old_position]
        target_ori[new_position] = source_ori[old_position]
    return output


def apply_transpose(cubies: dict[str, list[int]], cubie_type: str, a: int, b: int) -> dict[str, list[int]]:
    return apply_position_cycle(cubies, cubie_type, [a, b], "FORWARD")


def apply_ef(cubies: dict[str, list[int]], a: int, b: int) -> dict[str, list[int]]:
    output = clone_cubies(cubies)
    output["eo"][a] = (output["eo"][a] + 1) % 2
    output["eo"][b] = (output["eo"][b] + 1) % 2
    return output


def apply_ct(cubies: dict[str, list[int]], a: int, b: int, power: int) -> dict[str, list[int]]:
    output = clone_cubies(cubies)
    q = power % 3
    output["co"][a] = (output["co"][a] + q) % 3
    output["co"][b] = (output["co"][b] + 3 - q) % 3
    return output


def canonical_cycle(cycle: list[int]) -> list[int]:
    pivot = min(range(len(cycle)), key=lambda index: cycle[index])
    return cycle[pivot:] + cycle[:pivot]


def nontrivial_cycles(permutation: list[int]) -> list[list[int]]:
    seen = [False] * len(permutation)
    cycles: list[list[int]] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        cycle: list[int] = []
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = permutation[current]
        if len(cycle) > 1:
            cycles.append(canonical_cycle(cycle))
    cycles.sort(key=lambda cycle: "-".join(f"{value:02d}" for value in cycle))
    return cycles




def kernel_legality(cubies: dict[str, list[int]]) -> str:
    edge_sum = sum(cubies["eo"]) % 2
    corner_sum = sum(cubies["co"]) % 3
    return "PASS" if edge_sum == 0 and corner_sum == 0 and permutation_parity(cubies["ep"]) == permutation_parity(cubies["cp"]) else "FAIL"

CERT_PROFILE = "SCCERT-1-D02-EXP-A"
CERT_ACTION_PROFILE = "SCCERT-ECONOMY-ACTION-1-D01-EXP-A"
CERT_CHAIN_PROFILE = "SCCERT-ECONOMY-CHAIN-1-D01-EXP-A"
BUNDLE_PROFILE_V102 = "SCCERT-ECONOMY-CORPUS-1-D01-EXP-A"
MANIFEST_PROFILE_V102 = "SCCERT-ECONOMY-MANIFEST-1-D01-EXP-A"
CATALOG_PROFILE_V102 = "SCCERT-ECONOMY-REALIZATION-CATALOG-1-D01-EXP-A"
AUDIT_PROFILE_V102 = "SCCERT-ECONOMY-AUDIT-1-D01-EXP-A"
GRAPH_PROFILE = "SC-GRAPH-AUTHORITY-1-D01-EXP-A"
ECONOMY_PROFILE = "SC-GRAPH-ECONOMY-1-D01-EXP-A"
POLICY_PROFILE = "SC-GRAPH-ECONOMY-POLICY-1-D01-EXP-A"
ROUTE_PROFILE = "SC-GRAPH-ECONOMY-ROUTE-1-D01-EXP-A"
ECONOMY_ACTION_PROFILE = "SC-GRAPH-ECONOMY-ACTION-1-D01-EXP-A"
ECONOMY_COMPILER_PROFILE = "SC-GRAPH-ECONOMY-COMPILER-1-D01-EXP-A"
KERNEL_CONTRACT_PROFILE = "SC-KERNEL-1-D01-EXP-A"
GRAPH_POOL_SIZE = 4
LOOKAHEAD_DEPTH = 4


def cubies_to_facelets(cubies: dict[str, list[int]]) -> str:
    state = list(SOLVED)
    for position in range(8):
        piece = cubies["cp"][position]
        orientation = cubies["co"][position]
        indices = CORNER_FACELETS[position]
        colors = CORNER_COLORS[piece]
        state[indices[orientation]] = colors[0]
        state[indices[(orientation + 1) % 3]] = colors[1]
        state[indices[(orientation + 2) % 3]] = colors[2]
    for position in range(12):
        piece = cubies["ep"][position]
        orientation = cubies["eo"][position]
        indices = EDGE_FACELETS[position]
        colors = EDGE_COLORS[piece]
        state[indices[0]] = colors[1 if orientation else 0]
        state[indices[1]] = colors[0 if orientation else 1]
    text = "".join(state)
    extract_cubies(text)
    return text


def cubies_equal(left: dict[str, list[int]], right: dict[str, list[int]]) -> bool:
    return all(left[key] == right[key] for key in ("ep", "eo", "cp", "co"))


def parse_target(kernel: str, text: str) -> dict[str, Any]:
    parts = text.split("|")
    fields = dict(part.split("=", 1) for part in parts)
    if kernel == "PB":
        return {"edge_positions": [int(x) for x in fields["EDGE"].split("-")], "corner_positions": [int(x) for x in fields["CORNER"].split("-")]}
    if kernel == "CT":
        return {"type": "CORNER", "positions": [int(x) for x in fields["CORNER"].split("-")], "power": int(fields["POWER"])}
    key = "EDGE" if "EDGE" in fields else "CORNER"
    target: dict[str, Any] = {"type": key, "positions": [int(x) for x in fields[key].split("-")]}
    if "DIRECTION" in fields:
        target["direction"] = fields["DIRECTION"]
    return target


def pure_effect(kernel: str, target: dict[str, Any]) -> dict[str, list[int]]:
    cubies = {"ep": list(range(12)), "eo": [0] * 12, "cp": list(range(8)), "co": [0] * 8}
    if kernel == "PB":
        cubies = apply_transpose(cubies, "EDGE", *target["edge_positions"])
        cubies = apply_transpose(cubies, "CORNER", *target["corner_positions"])
    elif kernel in ("E3", "C3"):
        cubies = apply_position_cycle(cubies, target["type"], target["positions"], target["direction"])
    elif kernel == "EF":
        cubies = apply_ef(cubies, *target["positions"])
    elif kernel == "CT":
        cubies = apply_ct(cubies, target["positions"][0], target["positions"][1], target["power"])
    else:
        raise ValueError("UNSUPPORTED_KERNEL")
    return cubies


def scgs_records(cubies: dict[str, list[int]]) -> dict[str, list[str]]:
    nodes: set[str] = set()
    edges: set[str] = set()
    couplings: set[str] = set()
    for cubie_type, perm, ori in [("EDGE", cubies["ep"], cubies["eo"]), ("CORNER", cubies["cp"], cubies["co"])]:
        for pos, piece in enumerate(perm):
            index = f"{piece:02d}"
            direction = f"{cubie_type}_DIRECTION:{index}:{ori[pos]}" if ori[pos] != 0 else ""
            home = f"{cubie_type}_HOME:{index}" if pos != piece else ""
            if direction:
                nodes.add(direction)
            if home:
                nodes.add(home)
            if direction and home:
                edges.add(direction + ">" + home)
        for cycle in nontrivial_cycles(perm):
            couplings.add(cubie_type + "_CYCLE:" + "-".join(f"{x:02d}" for x in cycle))
    if nodes:
        base = list(nodes)
        nodes.add("FINAL_CLOSURE")
        for node in base:
            edges.add(node + ">FINAL_CLOSURE")
    return {"nodes": sorted(nodes), "edges": sorted(edges), "couplings": sorted(couplings)}


def graph_view(cubies: dict[str, list[int]]) -> dict[str, Any]:
    records = scgs_records(cubies)
    nodes = records["nodes"]
    direct_edges = [x for x in records["edges"] if not x.endswith(">FINAL_CLOSURE")]
    closure_edges = [x for x in records["edges"] if x.endswith(">FINAL_CLOSURE")]
    couplings = records["couplings"]
    local_nodes = [x for x in nodes if x != "FINAL_CLOSURE"]
    canonical = "\n".join([GRAPH_PROFILE, "MODE=FULL_GRAPH", "NODES", *nodes, "DIRECT_EDGES", *direct_edges, "CLOSURE_EDGES", *closure_edges, "COUPLINGS", *couplings, ""])
    burden = sum(max(0, len(row.split(":", 1)[1].split("-")) - 1) for row in couplings)
    scgs_text = "SCGS-1-D02\nNODES\n" + "".join(x + "\n" for x in nodes) + "EDGES\n" + "".join(x + "\n" for x in records["edges"]) + "COUPLINGS\n" + "".join(x + "\n" for x in couplings)
    return {"view_hash": sha256_hex(canonical), "source_scgs_hash": sha256_hex(scgs_text), "local_node_count": len(local_nodes), "direction_node_count": sum("_DIRECTION:" in x for x in local_nodes), "home_node_count": sum("_HOME:" in x for x in local_nodes), "direct_edge_count": len(direct_edges), "closure_edge_count": len(closure_edges), "coupling_count": len(couplings), "coupling_burden": burden}


def graph_delta(before: dict[str, Any], after: dict[str, Any]) -> tuple[dict[str, int], int, int]:
    delta = {
        "local_nodes_removed": before["local_node_count"] - after["local_node_count"],
        "direction_nodes_removed": before["direction_node_count"] - after["direction_node_count"],
        "home_nodes_removed": before["home_node_count"] - after["home_node_count"],
        "direct_edges_removed": before["direct_edge_count"] - after["direct_edge_count"],
        "closure_edges_removed": before["closure_edge_count"] - after["closure_edge_count"],
        "couplings_removed": before["coupling_count"] - after["coupling_count"],
        "coupling_burden_removed": before["coupling_burden"] - after["coupling_burden"],
    }
    score = delta["coupling_burden_removed"] * 100000 + delta["couplings_removed"] * 25000 + delta["direct_edges_removed"] * 10000 + delta["direction_nodes_removed"] * 2500 + delta["home_nodes_removed"] * 1500 + delta["local_nodes_removed"] * 500 + delta["closure_edges_removed"] * 100
    balanced = delta["coupling_burden_removed"] * 12 + delta["couplings_removed"] * 8 + delta["direction_nodes_removed"] * 5 + delta["home_nodes_removed"] * 3 + delta["direct_edges_removed"] * 2 + delta["local_nodes_removed"]
    return delta, score, balanced


def kernel_target_text(kernel: str, target: dict[str, Any]) -> str:
    if kernel == "PB":
        return "EDGE=" + "-".join(f"{x:02d}" for x in target["edge_positions"]) + "|CORNER=" + "-".join(f"{x:02d}" for x in target["corner_positions"])
    if kernel == "CT":
        return "CORNER=" + "-".join(f"{x:02d}" for x in target["positions"]) + "|POWER=" + str(target["power"])
    return target["type"] + "=" + "-".join(f"{x:02d}" for x in target["positions"]) + ("|DIRECTION=" + target["direction"] if target.get("direction") else "")


def contract(source_key: str, case_name: str, kernel: str, target: dict[str, Any], before: dict[str, list[int]], after: dict[str, list[int]]) -> dict[str, Any]:
    br = rank_from_cubies(before)
    ar = rank_from_cubies(after)
    delta_w = ar["W"] - br["W"]
    text = kernel_target_text(kernel, target)
    canonical = f"{KERNEL_CONTRACT_PROFILE}\nSOURCE={source_key}\nCASE={case_name}\nKERNEL={kernel}\nTARGET={text}\nBEFORE_RANK={br['rank_hash']}\nAFTER_RANK={ar['rank_hash']}\nDELTA_W={delta_w}\nSTRICT_DESCENT={1 if delta_w < 0 else 0}\nLEX_DESCENT={1 if lex_compare(ar['phi'], br['phi']) < 0 else 0}\nLEGALITY={kernel_legality(after)}\nCOMPILER=NOT_RUN\n"
    return {"case": case_name, "kernel": kernel, "target": target, "target_text": text, "before_rank": br, "after_rank": ar, "after_cubies": after, "delta_W": delta_w, "contract_hash": sha256_hex(canonical)}


def enumerate_candidates(cubies: dict[str, list[int]], source_key: str) -> list[dict[str, Any]]:
    before = clone_cubies(cubies)
    br = rank_from_cubies(before)
    bg = graph_view(before)
    edge_cycles = nontrivial_cycles(before["ep"])
    corner_cycles = nontrivial_cycles(before["cp"])
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    def add(case_name: str, kernel: str, target: dict[str, Any], after: dict[str, list[int]]) -> None:
        c = contract(source_key, case_name, kernel, target, before, after)
        if c["delta_W"] >= 0 or lex_compare(c["after_rank"]["phi"], br["phi"]) >= 0 or kernel_legality(after) != "PASS":
            return
        key = kernel + "|" + c["target_text"]
        if key in seen:
            return
        seen.add(key)
        ag = graph_view(after)
        delta, score, balanced = graph_delta(bg, ag)
        out.append({"case": case_name, "kernel": kernel, "target": target, "target_text": c["target_text"], "contract": c, "after_graph": ag, "graph_delta": delta, "graph_score": score, "balanced_graph_score": balanced, "decision_key": key})
    if br["rho"] == 1:
        edge_pairs = [[cycle[i], cycle[(i + 1) % len(cycle)]] for cycle in edge_cycles for i in range(len(cycle))]
        corner_pairs = [[cycle[i], cycle[(i + 1) % len(cycle)]] for cycle in corner_cycles for i in range(len(cycle))]
        for ep in edge_pairs:
            for cp in corner_pairs:
                after = apply_transpose(before, "EDGE", ep[0], ep[1])
                after = apply_transpose(after, "CORNER", cp[0], cp[1])
                add("PARITY_BRIDGE", "PB", {"edge_positions": ep, "corner_positions": cp}, after)
    else:
        long_rows = [(typ, cycle) for typ, cycles in [("EDGE", edge_cycles), ("CORNER", corner_cycles)] for cycle in cycles if len(cycle) >= 3]
        if long_rows:
            for typ, cycle in long_rows:
                for i in range(len(cycle)):
                    positions = [cycle[i], cycle[(i + 1) % len(cycle)], cycle[(i + 2) % len(cycle)]]
                    for direction in ("FORWARD", "REVERSE"):
                        add("CYCLE_LENGTH_AT_LEAST_3", "E3" if typ == "EDGE" else "C3", {"type": typ, "positions": positions, "direction": direction, "source_cycle": typ + ":" + "-".join(f"{x:02d}" for x in cycle)}, apply_position_cycle(before, typ, positions, direction))
        else:
            paired = [(typ, [c for c in cycles if len(c) == 2]) for typ, cycles in [("EDGE", edge_cycles), ("CORNER", corner_cycles)] if len([c for c in cycles if len(c) == 2]) >= 2]
            if paired:
                for typ, cycles in paired:
                    for a in range(len(cycles)):
                        for b in range(a + 1, len(cycles)):
                            for bridge in cycles[b]:
                                positions = [cycles[a][0], cycles[a][1], bridge]
                                for direction in ("FORWARD", "REVERSE"):
                                    add("PAIRED_2_CYCLES", "E3" if typ == "EDGE" else "C3", {"type": typ, "positions": positions, "direction": direction, "first_cycle": "-".join(f"{x:02d}" for x in cycles[a]), "second_cycle": "-".join(f"{x:02d}" for x in cycles[b])}, apply_position_cycle(before, typ, positions, direction))
            elif br["F"] > 0:
                flipped = [i for i, v in enumerate(before["eo"]) if v != 0]
                for i in range(len(flipped)):
                    for j in range(i + 1, len(flipped)):
                        positions = [flipped[i], flipped[j]]
                        add("EDGE_ORIENTATION_RESIDUE", "EF", {"type": "EDGE", "positions": positions}, apply_ef(before, *positions))
            elif br["T"] > 0:
                twisted = [i for i, v in enumerate(before["co"]) if v != 0]
                for i in range(len(twisted)):
                    for j in range(i + 1, len(twisted)):
                        for power in (1, 2):
                            positions = [twisted[i], twisted[j]]
                            add("CORNER_TWIST_RESIDUE", "CT", {"type": "CORNER", "positions": positions, "power": power}, apply_ct(before, positions[0], positions[1], power))
    out.sort(key=lambda x: (-x["graph_score"], x["contract"]["after_rank"]["W"], x["contract"]["after_rank"]["phi"], x["decision_key"]))
    return out


def cubie_key(cubies: dict[str, list[int]]) -> str:
    return ",".join(map(str, cubies["ep"])) + "|" + ",".join(map(str, cubies["eo"])) + "|" + ",".join(map(str, cubies["cp"])) + "|" + ",".join(map(str, cubies["co"]))


class EconomyVerifier:
    def __init__(self, catalog: dict[str, dict[str, Any]]):
        self.catalog = catalog
        self.memo: dict[tuple[int, str], int] = {}

    def realization(self, candidate: dict[str, Any]) -> dict[str, Any]:
        key = candidate["decision_key"]
        if key not in self.catalog:
            raise ValueError("CATALOG_MISSING:" + key)
        return self.catalog[key]

    def future_cost(self, cubies: dict[str, list[int]], depth: int) -> int:
        if rank_from_cubies(cubies)["W"] == 0 or depth <= 0:
            return 0
        key = (depth, cubie_key(cubies))
        if key in self.memo:
            return self.memo[key]
        pool = enumerate_candidates(cubies, "LOOKAHEAD|FULL_GRAPH|" + str(depth) + "|" + cubie_key(cubies))[:GRAPH_POOL_SIZE]
        best = min(self.realization(c)["move_count"] + self.future_cost(c["contract"]["after_cubies"], depth - 1) for c in pool)
        self.memo[key] = best
        return best

    def select(self, cubies: dict[str, list[int]], source_key: str) -> dict[str, Any]:
        candidates = enumerate_candidates(cubies, source_key)
        bg = graph_view(cubies)
        pool = candidates[:GRAPH_POOL_SIZE]
        evaluated = []
        for rank_index, candidate in enumerate(pool, 1):
            realization = self.realization(candidate)
            future = self.future_cost(candidate["contract"]["after_cubies"], LOOKAHEAD_DEPTH - 1)
            evaluated.append({"candidate": candidate, "graph_rank": rank_index, "realization": realization, "future_cost": future, "planning_cost": realization["move_count"] + future})
        evaluated.sort(key=lambda row: (row["planning_cost"], -row["candidate"]["balanced_graph_score"], -row["candidate"]["graph_score"], row["candidate"]["contract"]["after_rank"]["W"], row["realization"]["move_count"], row["candidate"]["contract"]["after_rank"]["phi"], row["candidate"]["decision_key"]))
        selected = evaluated[0]
        canonical_rows = []
        for row in sorted(evaluated, key=lambda x: x["graph_rank"]):
            canonical_rows.append("|".join([f"{row['graph_rank']:02d}", row["candidate"]["decision_key"], str(row["candidate"]["graph_score"]), str(row["candidate"]["balanced_graph_score"]), str(row["realization"]["move_count"]), str(row["future_cost"]), str(row["planning_cost"])]))
        pool_text = "\n".join(canonical_rows) + "\n"
        c = selected["candidate"]
        decision_text = "\n".join([POLICY_PROFILE, "MODE=FULL_GRAPH", "SOURCE=" + source_key, "GRAPH_VIEW=" + bg["view_hash"], "CANDIDATE_COUNT=" + str(len(candidates)), "GRAPH_POOL_SIZE=" + str(len(evaluated)), "LOOKAHEAD_DEPTH=" + str(LOOKAHEAD_DEPTH), "SELECTED_GRAPH_RANK=" + str(selected["graph_rank"]), "SELECTED=" + c["decision_key"], "SELECTED_MOVE_COUNT=" + str(selected["realization"]["move_count"]), "SELECTED_FUTURE_COST=" + str(selected["future_cost"]), "SELECTED_PLANNING_COST=" + str(selected["planning_cost"]), "SELECTED_GRAPH_SCORE=" + str(c["graph_score"]), "SELECTED_BALANCED_GRAPH_SCORE=" + str(c["balanced_graph_score"]), "POOL_HASH=" + sha256_hex(pool_text), "REFERENCE_ROUTE_ACCESS=NONE", "CURRENT_STATE_REFERENCE_DISTANCE_ACCESS=NONE", ""])
        return {**selected, "candidate_count": len(candidates), "graph_pool_count": len(evaluated), "graph_pool_hash": sha256_hex(pool_text), "decision_hash": sha256_hex(decision_text), "before_graph": bg}


def certificate_chain_genesis(source_hash: str, rank_hash: str, w: int) -> str:
    return f"{CERT_CHAIN_PROFILE}\nCERTIFICATE_PROFILE={CERT_PROFILE}\nSOURCE_STATE_HASH={source_hash}\nINITIAL_RANK_HASH={rank_hash}\nINITIAL_W={w}\n"


def certificate_action_text(action: dict[str, Any]) -> str:
    return "\n".join([CERT_ACTION_PROFILE, "CERTIFICATE_PROFILE=" + CERT_PROFILE, "STEP=" + f"{action['step']:03d}", "SOURCE_STATE_HASH=" + action["source_state_hash"], "TARGET_STATE_HASH=" + action["target_state_hash"], "GRAPH_BEFORE_HASH=" + action["graph_before_hash"], "GRAPH_AFTER_HASH=" + action["graph_after_hash"], "GRAPH_POOL_HASH=" + action["graph_pool_hash"], "GRAPH_RANK=" + str(action["graph_rank"]), "LOOKAHEAD_DEPTH=" + str(action["lookahead_depth"]), "PLANNING_COST=" + str(action["planning_cost"]), "DECISION_HASH=" + action["decision_hash"], "KERNEL=" + action["kernel"], "CASE=" + action["case"], "TARGET=" + action["target_text"], "W_BEFORE=" + str(action["before_rank"]["W"]), "W_AFTER=" + str(action["after_rank"]["W"]), "DELTA_W=" + str(action["delta_W"]), "ALGORITHM=" + (action["algorithm"] or "I"), "MOVE_COUNT=" + str(action["move_count"]), "CONTRACT_HASH=" + action["contract_hash"], "COMPILER_HASH=" + action["compiler_hash"], "EXACT_EFFECT=" + ("1" if action["exact_effect"] else "0"), "EXACT_TARGET_STATE=" + ("1" if action["exact_target_state"] else "0"), "STRICT_W_DESCENT=" + ("1" if action["strict_W_descent"] else "0"), "LEXICOGRAPHIC_DESCENT=" + ("1" if action["lexicographic_descent"] else "0"), "PREVIOUS_CHAIN=" + action["previous_certificate_chain"], ""])


def economy_compiler_hash(action: dict[str, Any]) -> str:
    text = "\n".join([ECONOMY_COMPILER_PROFILE, "POLICY=" + POLICY_PROFILE, "MODE=FULL_GRAPH", "DECISION=" + action["decision_hash"], "CONTRACT=" + action["contract_hash"], "SOURCE=" + action["source_state_hash"], "TARGET=" + action["target_state_hash"], "ALGORITHM=" + (action["algorithm"] or "I"), "MOVE_COUNT=" + str(action["move_count"]), "EXACT_EFFECT=1", "EXACT_STATE=1", "STRICT_DESCENT=1", "LEXICOGRAPHIC_DESCENT=1", "COMPILER_SEARCH_INPUT=ISOLATED_PURE_KERNEL_EFFECT_ONLY", "REFERENCE_ROUTE_ACCESS=NONE", ""])
    return sha256_hex(text)


def economy_action_chain(action: dict[str, Any], previous: str) -> str:
    text = "\n".join([ECONOMY_ACTION_PROFILE, "POLICY=" + POLICY_PROFILE, "MODE=FULL_GRAPH", "STEP=" + f"{action['step']:03d}", "SOURCE=" + action["source_state_hash"], "TARGET=" + action["target_state_hash"], "GRAPH_BEFORE=" + action["graph_before_hash"], "GRAPH_AFTER=" + action["graph_after_hash"], "GRAPH_POOL_HASH=" + action["graph_pool_hash"], "GRAPH_RANK=" + str(action["graph_rank"]), "LOOKAHEAD_DEPTH=" + str(action["lookahead_depth"]), "PLANNING_COST=" + str(action["planning_cost"]), "DECISION=" + action["decision_hash"], "KERNEL=" + action["kernel"], "TARGET_TEXT=" + action["target_text"], "W_BEFORE=" + str(action["before_rank"]["W"]), "W_AFTER=" + str(action["after_rank"]["W"]), "ALGORITHM=" + action["algorithm"], "COMPILER_HASH=" + action["compiler_hash"], "LEARNING=" + action["learning_hash"], "PREVIOUS_CHAIN=" + previous, ""])
    return sha256_hex(text)


def verify_catalog(catalog_obj: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], list[str]]:
    failures: list[str] = []
    entries = catalog_obj.get("entries", [])
    if sha256_hex(canonical_json(entries)) != catalog_obj.get("catalog_root"):
        failures.append("CATALOG_ROOT")
    catalog: dict[str, dict[str, Any]] = {}
    for entry in entries:
        try:
            if entry["key"] != entry["kernel"] + "|" + entry["target_text"]:
                failures.append("CATALOG_KEY:" + entry["key"])
            target = parse_target(entry["kernel"], entry["target_text"])
            expected = pure_effect(entry["kernel"], target)
            observed = extract_cubies(apply_algorithm(SOLVED, entry["algorithm"]))
            if not cubies_equal(expected, observed):
                failures.append("CATALOG_EFFECT:" + entry["key"])
            if len(parse_algorithm(entry["algorithm"])) != entry["move_count"] or parse_algorithm(entry["algorithm"]) != entry["moves"]:
                failures.append("CATALOG_MOVES:" + entry["key"])
            if state_hash(cubies_to_facelets(expected)) != entry["pure_effect_state_hash"]:
                failures.append("CATALOG_STATE_HASH:" + entry["key"])
            catalog[entry["key"]] = entry
        except Exception as exc:
            failures.append("CATALOG_EXCEPTION:" + entry.get("key", "UNKNOWN") + ":" + str(exc))
    if len(catalog) != catalog_obj.get("entry_count"):
        failures.append("CATALOG_COUNT")
    return catalog, failures


def verify_certificate_v102(certificate: dict[str, Any], economy: EconomyVerifier) -> dict[str, Any]:
    failures: list[str] = []
    try:
        if certificate.get("profile") != CERT_PROFILE:
            failures.append("PROFILE")
        root_payload = dict(certificate)
        root_payload.pop("certificate_root", None)
        if sha256_hex(canonical_json(root_payload)) != certificate.get("certificate_root"):
            failures.append("CERTIFICATE_ROOT")
        state = certificate["source"]["facelets"]
        if state_hash(state) != certificate["source"]["state_hash"]:
            failures.append("SOURCE_HASH")
        rank = rank_state(state)
        if rank["rank_hash"] != certificate["source"]["rank"]["rank_hash"]:
            failures.append("SOURCE_RANK")
        cert_chain = sha256_hex(certificate_chain_genesis(certificate["source"]["state_hash"], rank["rank_hash"], rank["W"]))
        route_genesis = "\n".join([ROUTE_PROFILE, "POLICY=" + POLICY_PROFILE, "MODE=FULL_GRAPH", "SOURCE=" + certificate["source"]["state_hash"], "INITIAL_RANK=" + rank["rank_hash"], "INITIAL_W=" + str(rank["W"]), "GRAPH_POOL_SIZE=4", "LOOKAHEAD_DEPTH=4", ""])
        economy_chain = sha256_hex(route_genesis)
        route_moves: list[str] = []
        trajectory = [rank["W"]]
        decisions: list[str] = []
        learning_hashes: list[str] = []
        for index, action in enumerate(certificate["actions"], 1):
            before_state = state
            before_cubies = extract_cubies(before_state)
            before_rank = rank_from_cubies(before_cubies)
            selected = economy.select(before_cubies, state_hash(before_state))
            candidate = selected["candidate"]
            realization = selected["realization"]
            checks = {
                "STEP": action["step"] == index,
                "SOURCE": action["source_facelets"] == before_state and action["source_state_hash"] == state_hash(before_state),
                "KERNEL": action["kernel"] == candidate["kernel"],
                "CASE": action["case"] == candidate["case"],
                "TARGET": action["target_text"] == candidate["target_text"],
                "DECISION": action["decision_hash"] == selected["decision_hash"],
                "POOL": action["graph_pool_hash"] == selected["graph_pool_hash"] and action["graph_rank"] == selected["graph_rank"],
                "COST": action["future_cost"] == selected["future_cost"] and action["planning_cost"] == selected["planning_cost"],
                "CONTRACT": action["contract_hash"] == candidate["contract"]["contract_hash"],
                "ALGORITHM": action["algorithm"] == realization["algorithm"] and action["move_count"] == realization["move_count"],
            }
            for name, ok in checks.items():
                if not ok:
                    failures.append(name + "_" + str(index))
            state = apply_algorithm(state, action["algorithm"])
            after_cubies = extract_cubies(state)
            after_rank = rank_from_cubies(after_cubies)
            if state != action["target_facelets"] or state_hash(state) != action["target_state_hash"]:
                failures.append("TARGET_STATE_" + str(index))
            if not cubies_equal(after_cubies, candidate["contract"]["after_cubies"]):
                failures.append("EXACT_EFFECT_" + str(index))
            if after_rank["W"] >= before_rank["W"] or action["delta_W"] != after_rank["W"] - before_rank["W"]:
                failures.append("RANK_DESCENT_" + str(index))
            if action["compiler_hash"] != economy_compiler_hash(action):
                failures.append("COMPILER_HASH_" + str(index))
            if action["economy_previous_chain"] != economy_chain:
                failures.append("ECONOMY_PREVIOUS_" + str(index))
            economy_chain = economy_action_chain(action, economy_chain)
            if economy_chain != action["economy_evidence_chain"]:
                failures.append("ECONOMY_CHAIN_" + str(index))
            if action["previous_certificate_chain"] != cert_chain or action["canonical_text"] != certificate_action_text(action):
                failures.append("CERT_TEXT_" + str(index))
            cert_chain = sha256_hex(action["canonical_text"])
            if cert_chain != action["certificate_chain_hash"]:
                failures.append("CERT_CHAIN_" + str(index))
            route_moves.extend(parse_algorithm(action["algorithm"]))
            trajectory.append(after_rank["W"])
            decisions.append(action["decision_key"])
            learning_hashes.append(action["learning_hash"])
        if state != SOLVED or rank_state(state)["W"] != 0:
            failures.append("FINAL_STATE")
        route = certificate["route"]
        if route["moves"] != route_moves or route["algorithm"] != " ".join(route_moves) or route["W_trajectory"] != trajectory or route["certificate_chain_tail"] != cert_chain or route["economy_evidence_chain_tail"] != economy_chain:
            failures.append("ROUTE_SUMMARY")
        route_text = "\n".join([ROUTE_PROFILE, "POLICY=" + POLICY_PROFILE, "MODE=FULL_GRAPH", "SOURCE=" + certificate["source"]["state_hash"], "TARGET=" + state_hash(state), "INITIAL_W=" + str(trajectory[0]), "FINAL_W=0", "ACTIONS=" + str(len(certificate["actions"])), "MOVES=" + str(len(route_moves)), "GRAPH_POOL_SIZE=4", "LOOKAHEAD_DEPTH=4", "DECISIONS=" + sha256_hex("\n".join(decisions) + "\n"), "LEARNING=" + sha256_hex("\n".join(learning_hashes) + "\n"), "W_TRAJECTORY=" + ",".join(map(str, trajectory)), "CHAIN_TAIL=" + economy_chain, "STRICT_TRAJECTORY=1", "SOLVED=1", "REFERENCE_ROUTE_ACCESS=NONE", "CURRENT_STATE_REFERENCE_DISTANCE_ACCESS=NONE", "FALLBACK_ACTIVATION=NONE", ""])
        if sha256_hex(route_text) != route["economy_route_hash"]:
            failures.append("ECONOMY_ROUTE_HASH")
    except Exception as exc:
        failures.append("EXCEPTION:" + str(exc))
    return {"status": "PASS" if not failures else "FAIL", "failure_count": len(failures), "failures": failures, "certificate_root": certificate.get("certificate_root", "NONE")}


def aggregate_manifest_text_v102(records: list[dict[str, Any]], source: dict[str, Any], catalog: dict[str, Any]) -> str:
    lines = [MANIFEST_PROFILE_V102, "VERSION=1.0.2", "BUNDLE_PROFILE=" + BUNDLE_PROFILE_V102, "CERTIFICATE_PROFILE=" + CERT_PROFILE, "SOURCE_MANIFEST_HASH=" + source["manifest_hash"], "REALIZATION_CATALOG_ROOT=" + catalog["catalog_root"], "REALIZATION_CATALOG_ENTRIES=" + str(catalog["entry_count"]), "SEED_COUNT=" + str(len(records))]
    for r in records:
        lines.append(f"SEED={r['seed']:03d}|SOURCE_STATE_HASH={r['source_state_hash']}|CERTIFICATE_ROOT={r['certificate_root']}|ROUTE_HASH={r['economy_route_hash']}|ACTIONS={r['action_count']}|MOVES={r['move_count']}|FINAL_W={r['final_W']}|VERIFY={r['browser_verification']}")
    return "\n".join(lines) + "\n"


def verify_bundle_v102(bundle: dict[str, Any]) -> dict[str, Any]:
    failures: list[str] = []
    certificate_results: list[dict[str, Any]] = []
    try:
        if bundle.get("profile") != BUNDLE_PROFILE_V102:
            failures.append("BUNDLE_PROFILE")
        root_payload = dict(bundle)
        root_payload.pop("bundle_root", None)
        if sha256_hex(canonical_json(root_payload)) != bundle.get("bundle_root"):
            failures.append("BUNDLE_ROOT")
        source = bundle["source_manifest"]
        if sha256_hex(source["canonical_text"]) != source["manifest_hash"] or source["seed_count"] != 100:
            failures.append("SOURCE_MANIFEST")
        catalog_map, catalog_failures = verify_catalog(bundle["realization_catalog"])
        failures.extend(catalog_failures)
        economy = EconomyVerifier(catalog_map)
        records: list[dict[str, Any]] = []
        for entry, source_row, manifest_row in zip(bundle["certificates"], source["records"], bundle["manifest"]["records"]):
            cert = entry["certificate"]
            if entry["seed"] != source_row["seed"] or cert["source"]["state_hash"] != source_row["state_hash"]:
                failures.append("SEED_SOURCE_" + str(source_row["seed"]))
            result = verify_certificate_v102(cert, economy)
            certificate_results.append({"seed": source_row["seed"], **result})
            record = {"seed": source_row["seed"], "source_state_hash": cert["source"]["state_hash"], "certificate_root": cert["certificate_root"], "economy_route_hash": cert["route"]["economy_route_hash"], "action_count": cert["route"]["action_count"], "move_count": cert["route"]["move_count"], "final_W": cert["final"]["rank"]["W"], "strict_W_trajectory": cert["route"]["strict_W_trajectory"], "browser_verification": "PASS"}
            records.append(record)
            if canonical_json(record) != canonical_json(manifest_row):
                failures.append("MANIFEST_ROW_" + str(source_row["seed"]))
            if result["status"] != "PASS":
                failures.append("CERTIFICATE_" + str(source_row["seed"]))
        text = aggregate_manifest_text_v102(records, source, bundle["realization_catalog"])
        if text != bundle["manifest"]["canonical_text"] or sha256_hex(text) != bundle["manifest"]["aggregate_root"]:
            failures.append("AGGREGATE_MANIFEST")
    except Exception as exc:
        failures.append("EXCEPTION:" + str(exc))
    return {"profile": AUDIT_PROFILE_V102, "status": "PASS" if not failures else "FAIL", "failure_count": len(failures), "failures": failures, "certificate_count": len(certificate_results), "passed_certificate_count": sum(r["status"] == "PASS" for r in certificate_results), "failed_certificate_count": sum(r["status"] != "PASS" for r in certificate_results), "aggregate_root": bundle.get("manifest", {}).get("aggregate_root", "NONE"), "bundle_root": bundle.get("bundle_root", "NONE"), "realization_catalog_root": bundle.get("realization_catalog", {}).get("catalog_root", "NONE"), "certificates": certificate_results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact")
    parser.add_argument("--json-report")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    try:
        artifact = json.loads(Path(args.artifact).read_text(encoding="utf-8"))
        report = verify_bundle_v102(artifact)
        report_text = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
        if args.json_report:
            Path(args.json_report).write_text(report_text, encoding="utf-8", newline="\n")
        if not args.quiet:
            print(report_text, end="")
        return 0 if report["status"] == "PASS" else 1
    except Exception as exc:
        if not args.quiet:
            print(json.dumps({"status": "ERROR", "error": str(exc)}, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
