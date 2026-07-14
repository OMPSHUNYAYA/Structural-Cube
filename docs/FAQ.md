# ❓ **FAQ — Structural Cube**

## **Dependency-Governed Resolution for a 3 x 3 x 3 Cube**

### **Structure Proposes. Verification Checks. Every Action Must Descend.**

`state -> structure -> action -> evidence -> descent -> solved state`

---

# **SECTION A — Core Understanding**

## **A1. What is Structural Cube?**

Structural Cube is an interactive browser application and verification system for a standard `3 x 3 x 3` cube.

It resolves a legal cube state through:

- canonical cubie extraction;
- a structural rank;
- an observed obligation graph;
- exact pure-kernel action contracts;
- graph-governed target selection;
- deterministic move-cost comparison;
- exact replay verification;
- strict rank descent after every completed action.

Its main resolution chain is:

`canonical state -> rank -> graph -> admitted target -> compiled turns -> replay -> strict descent -> rebuild -> solved state`

---

## **A2. What is the core idea in one line?**

`a move is admitted only when its target, exact effect, and structural descent can be verified`

---

## **A3. Is Structural Cube a normal cube solver with different labels?**

No such claim is made merely because the interface uses structural language.

The intended authority order is:

`state -> structure -> action contract -> verification -> route -> lesson`

not:

`state -> route first -> explanation afterward`

The selected kernel target, compiled turns, before-and-after state, rank transition, and action identity are recorded so the structural claim can be inspected.

---

## **A4. Does Structural Cube use the scramble history?**

No.

The current state is the authority input.

`solve_input = canonical(C_current)`

`history_dependency = NONE`

A seeded scramble is retained for reproducibility, but the resolver does not need the earlier move history to resolve the current cube.

---

## **A5. Does Structural Cube reject established cube mathematics?**

No.

Standard legal turns, permutations, orientations, commutators, conjugates, and known cube mathematics remain valid.

Structural Cube changes the authority relation and evidence visibility.

It asks:

**Which structural residue is present now, which exact action can change it, and can that action be verified before the next one is chosen?**

---

## **A6. What does “structural” mean here?**

A structural action has:

- a declared source state;
- a declared unresolved residue;
- a deterministic target;
- a pure-effect contract;
- an exact compiled turn sequence;
- a replayed target state;
- a verified rank reduction;
- a linked action identity.

Compactly:

`action = target + exact effect + verified transition + strict descent`

---

## **A7. What version is documented here?**

The current version is:

**Structural Cube v1.0.2**

Its version class is:

`EXPERIMENTAL`

Its declared evidence boundary is:

`COMMITTED_P100`

---

# **SECTION B — Using the Browser Application**

## **B1. Where is the application?**

The application is:

[`../demo/Structural_Cube_v1_0_2.html`](../demo/Structural_Cube_v1_0_2.html)

Download the file and open it locally in a current browser with JavaScript enabled. Chromium-based browsers are the tested reference environment.

---

## **B2. Why might GitHub say the HTML file is too large to display?**

The single-file application is approximately `6.1 MB`.

GitHub may decline to render a file of that size in the ordinary file view.

This does not prevent use of the application.

**Download the HTML file and open it locally.**

---

## **B3. Does the application require installation?**

No formal installer is required.

The application is one HTML file.

Typical use:

1. Download the HTML file.
2. Open it in a current browser with JavaScript enabled. Chromium-based browsers are the tested reference environment.
3. Choose **Random**, **Manual**, or begin turning the cube.
4. Choose **Auto Resolve**, **With Hint**, or **Solve Myself**.

---

## **B4. Is a network connection required?**

No.

The browser application and Python verification path are designed to operate without network access.

---

## **B5. Does it use a third-party cube solver?**

The supplied application contains its own cube model, legal transformations, scramble generator, resolver logic, evidence generation, and verification routines.

The graph-aware primary route declares:

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

`fallback_activation = NONE`

---

## **B6. What does the browser `file:` warning mean?**

Some Chromium-based browsers may log a message similar to:

`'file:' URLs are treated as unique security origins`

This is a browser security-origin notice caused by opening a local file.

It does not by itself mean that Structural Cube failed.

The relevant tests are the application audit, route checks, certificate checks, and downloaded evidence identities.

---

## **B7. Can I mix the cube manually?**

Yes.

You can:

- drag a row or column of three squares;
- tap a face and choose its turn;
- rotate the view from the dark edge;
- continue from a different legal move;
- ask the resolver to calculate again from the new current state.

---

## **B8. What is Random mode?**

Random mode uses a declared deterministic seed.

The relation is:

`same seed + same generator version + same scramble length -> same scramble`

The committed P100 corpus uses:

`generator = xorshift32`

`scramble_length = 22`

`seed_set = 1..100`

---

## **B9. What is Auto Resolve?**

Auto Resolve prepares a graph-governed economy route from the current state and carries out the verified actions.

Before each move sequence, the learning panel presents:

- **Strategy**
- **Plan**
- **Move**

---

## **B10. What is With Hint?**

With Hint shows the next guided move while allowing the user to perform it manually.

If the user makes another legal move, Structural Cube can resolve from the new current state.

---

## **B11. What is Solve Myself?**

Solve Myself removes guided move instructions so the cube can be explored without hints.

Guidance can be enabled later.

---

## **B12. What happens when the sequence is paused?**

Pause preserves the current guided state, including:

- Strategy;
- Plan;
- Move;
- cube highlight;
- current action position.

Pause is an execution state.

It does not alter the mathematical route verdict.

---

# **SECTION C — Cube State and Legality**

## **C1. How is the cube represented?**

The cubie state is:

`C = (P_e, O_e, P_c, O_c)`

where:

- `P_e` is the edge permutation;
- `O_e` is the edge orientation;
- `P_c` is the corner permutation;
- `O_c` is the corner orientation.

---

## **C2. What legality conditions are checked?**

A legal reachable state must satisfy:

`sum(O_e) mod 2 = 0`

`sum(O_c) mod 3 = 0`

`parity(P_e) = parity(P_c)`

The application also checks:

- facelet count;
- colour counts;
- centre orientation;
- corner identity and duplication;
- edge identity and duplication.

---

## **C3. What happens when a state is illegal?**

The application must not force a route for an illegal or unreachable state.

The refusal principle is:

`illegal or unreachable state -> no valid structural route claim`

---

## **C4. What is a canonical state?**

A canonical state uses the declared face and centre orientation:

`U, R, F, D, L, B`

Canonicalization allows the same physical cube position to have one declared state identity before graph construction, ranking, hashing, or certificate generation.

---

## **C5. What is SCGS-1-D02?**

`SCGS-1-D02` is the canonical serialization profile for the base observed obligation graph.

It defines:

- accepted canonical facelet input;
- cubie extraction;
- obligation nodes;
- dependency edges;
- permutation-cycle couplings;
- ASCII record grammar;
- byte-wise sorting;
- LF line endings;
- SHA-256 graph hashing;
- refusal order.

The specification is available at:

[`specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt`](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# **SECTION D — Structural Rank**

## **D1. What is the structural rank?**

The structural rank summarizes declared permutation and orientation residues.

The lexicographic potential is:

`Phi(C) = (rho, D_e + D_c, tau_e + tau_c, F, T)`

The integer rank is:

`W(C) = 24*rho + 4*(D_e + D_c) + tau_e + tau_c + F + T`

---

## **D2. What do the rank components mean?**

- `rho` records the common edge-corner permutation-parity condition.
- `D_e` records edge transposition distance through permutation cycles.
- `D_c` records corner transposition distance through permutation cycles.
- `tau_e` counts edge two-cycles.
- `tau_c` counts corner two-cycles.
- `F` counts flipped-edge residue.
- `T` records corner-twist distance.

---

## **D3. What is the range of `W`?**

For the declared legal-state convention:

`0 <= W(C) <= 126`

and:

`W(C) = 0 iff C = SOLVED`

---

## **D4. Why must `W` decrease?**

Every completed primary action must satisfy:

`W(C_(i+1)) < W(C_i)`

This prevents an accepted action from ending at an equal or greater structural rank.

The finite-descent relation is:

`finite non-negative W + strict action-boundary descent -> finite action count`

For the committed P100 routes, continued admitted-action availability, exact replay, and final-state verification establish solved closure.

---

## **D5. Is `W` the shortest move distance?**

No.

`W` is a structural termination rank.

It is not claimed to equal:

- God's number;
- optimal face-turn distance;
- optimal quarter-turn distance;
- competition solution length;
- a shortest-route heuristic.

---

## **D6. Can one action contain many cube turns?**

Yes.

An action is one verified structural contract.

Its compiled realization may contain multiple normalized move tokens.

Therefore:

`action_count != face_turn_count`

The P100 route evidence reports both.

---

# **SECTION E — Pure Structural Kernels**

## **E1. What are the five kernel families?**

Structural Cube uses five pure-effect kernel families:

| Kernel | Declared purpose |
|---|---|
| `EF(i,j)` | Correct a paired edge-orientation residue |
| `CT(i,j)` | Correct a paired corner-twist residue |
| `E3(i,j,k)` | Apply an exact three-edge permutation cycle |
| `C3(i,j,k)` | Apply an exact three-corner permutation cycle |
| `PB(i,j;k,l)` | Bridge the shared edge-corner permutation parity |

---

## **E2. What does “pure effect” mean?**

A pure-effect contract declares the complete cubie transformation expected from the action.

The compiled turns are admitted only when replay produces exactly that effect.

`compiled sequence + current state -> exact declared target state`

---

## **E3. How is a kernel target selected?**

The deterministic target logic follows the current structural residue.

Examples include:

- shared odd permutation parity -> `PB`;
- permutation cycle of length at least three -> `E3` or `C3`;
- paired two-cycle structure -> deterministic three-cycle target;
- edge-orientation residue -> `EF`;
- corner-twist residue -> `CT`.

---

## **E4. Does the compiler solve the current cube by reference search?**

The compiler searches for a face-turn realization of the isolated pure-effect target.

Its declared input boundary is:

`compiler_search_input = ISOLATED_PURE_KERNEL_EFFECT_ONLY`

It does not use a current-state reference route or current-state reference distance to choose the structural action.

---

## **E5. What is the realization catalogue?**

The SCCERT evidence bundle contains a deterministic realization catalogue for the kernel effects used by the P100 routes.

The v1.0.2 catalogue contains:

`realization_catalog_entries = 2292`

Its root is:

`e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4`

---

# **SECTION F — Observed Graph and Economy Policy**

## **F1. What does the observed graph contain?**

The base graph records:

- unresolved direction obligations;
- unresolved home obligations;
- direction-before-home dependencies;
- final-closure relations;
- edge permutation-cycle couplings;
- corner permutation-cycle couplings.

---

## **F2. Is this claimed to be the only possible cube dependency graph?**

No.

The graph is a declared observed obligation model used by this implementation.

It is not claimed as the unique or complete dependency graph for every cube-solving method.

---

## **F3. How does graph-aware economy selection work?**

At each action boundary, the selector:

1. enumerates exact strict-descent kernel targets;
2. ranks them under the full observed graph;
3. retains the strongest four admitted targets;
4. compares structural continuations to depth four;
5. selects the lowest declared compiled move cost;
6. replays and verifies the selected action.

Compactly:

`full graph -> top 4 admitted targets -> depth 4 lookahead -> lowest declared compiled move cost`

---

## **F4. What is the primary interactive authority?**

`GRAPH_GOVERNED_ECONOMY_PRIMARY_AUTHORITY`

The route authority is:

`REFERENCE_FREE_STRUCTURAL_KERNEL_AUTHORITY`

The economy policy is:

`TOP_4_GRAPH_POOL_DEPTH_4`

---

## **F5. Does the graph always produce the shortest route?**

No.

The graph affects target selection, but the current policy does not claim global shortest-route optimality.

Its measured claim is limited to the committed P100 comparison.

---

## **F6. Why compare four targets instead of every possible continuation?**

The policy deliberately uses a declared finite candidate pool and lookahead depth.

This preserves:

- deterministic selection;
- inspectable policy identity;
- manageable execution;
- reproducible evidence.

A different pool or depth would be a different declared policy.

---

# **SECTION G — Learning and Explanation**

## **G1. Why separate Strategy, Plan, and Move?**

They answer different questions.

**Strategy** explains the larger structural goal.

**Plan** explains why the next action belongs to that goal.

**Move** gives the immediate turn instruction.

The learning law is:

`verified structural purpose -> Strategy -> Plan -> Move`

---

## **G2. Are the messages generated from the same evidence as the action?**

That is the intended design boundary.

A precise message must be supported by before-and-after state evidence.

If the evidence does not support a precise claim, the application should use general guidance rather than invent a purpose.

---

## **G3. Why is there a separate Technical tab?**

The Technical tab keeps formulas, state identities, and certificate information separate from the learner-facing guidance.

This allows the main message panel to remain readable while preserving technical visibility.

---

## **G4. Is Structural Cube intended only for experts?**

No.

The main interface uses plain guidance.

The deeper rank, graph, kernel, hash, and certificate details are available for advanced inspection.

---

## **G5. Does the current evidence prove that people learn faster with Structural Cube?**

No.

The current evidence validates deterministic computation, route behavior, certificate construction, and independent verification.

Measured learner-outcome studies remain a separate research direction.

---

# **SECTION H — Determinism and Reproducibility**

## **H1. What does deterministic mean here?**

For the same declared state, source, policy, budgets, and profiles, the system is expected to reproduce the same structural result and evidence identities.

`same canonical state + same versioned rules -> same certified route`

---

## **H2. Can elapsed time change the route?**

No such authority is permitted.

`wall_clock_authority = NONE`

Elapsed time may be recorded as execution telemetry, but it must not choose a candidate, activate fallback, or change the route verdict.

---

## **H3. What happens when the user cancels an operation?**

Cancellation stops execution.

It does not create a mathematical failure or success verdict for a route that was not completed.

`user cancellation -> execution state`

---

## **H4. Is seed 42 expected to reproduce exactly?**

Yes, under the same generator, scramble length, application version, resolver profiles, and evidence rules.

The P100 evidence also contains a deterministic repeatability check.

---

## **H5. Why are hashes used?**

Hashes bind exact identities.

Structural Cube uses SHA-256 for items such as:

- source states;
- graphs;
- contracts;
- compiled actions;
- routes;
- certificates;
- manifests;
- reports.

A matching hash confirms matching bytes or matching canonical content under the declared profile.

It does not by itself prove every mathematical claim.

---

# **SECTION I — P100 Evidence**

## **I1. What is P100?**

P100 is the committed 100-seed corpus used for the v1.0.2 evaluation.

`seed_set = 1..100`

`scramble_length = 22`

`generator = xorshift32`

Each entry binds:

- seed;
- exact scramble;
- canonical starting facelets;
- source-state SHA-256.

---

## **I2. What were the principal P100 results?**

| Property | Result |
|---|---:|
| Requested states | **100** |
| Completed states | **100** |
| Solved states | **100/100** |
| Strict `W` descent | **PASS** |
| Final `W = 0` | **100/100** |
| Reference-route access | **NONE** |
| Current-state reference-distance access | **NONE** |
| Fallback activation | **NONE** |
| Lower move count than the declared earlier full-graph selector | **100/100 seeds** |
| Equal seeds | **0** |
| Regressed seeds | **0** |

---

## **I3. What were the move-count results?**

Declared earlier full-graph selector:

- mean: `193.99`
- median: `194.5`
- `p95`: `233`
- maximum: `252`

Graph-aware economy selector:

- mean: `174.58`
- median: `172`
- `p95`: `207`
- maximum: `223`

Total reduction across the 100 routes:

`1,941 move tokens`

---

## **I4. How much did each route improve?**

Across P100:

- mean reduction: `19.41` move tokens;
- median reduction: `19` move tokens;
- largest reduction: `38` move tokens;
- smallest reduction: `2` move tokens;
- every tested seed used fewer moves;
- no tested seed used the same or more moves.

These results are specific to the committed corpus and declared earlier full-graph selector.

---

## **I5. Did action count also decrease?**

Not materially.

Earlier mean action count:

`13.41`

Graph-aware economy mean action count:

`13.42`

The economy gain came mainly from lower compiled face-turn cost within the selected structural action sequence.

---

## **I6. Does P100 prove behavior for every legal cube state?**

No.

It proves the reported behavior for the 100 committed starting states under the declared version and profiles.

The project does not claim universal totality from this corpus alone.

---

# **SECTION J — SCCERT Certificates**

## **J1. What is SCCERT?**

SCCERT is the portable route-certificate family used to describe and verify a complete Structural Cube route.

The v1.0.2 profile is:

`SCCERT-1-D02-EXP-A`

---

## **J2. What does one certificate contain?**

A certificate binds:

- source facelets and source-state hash;
- source rank;
- graph-governed target decision;
- exact kernel contract;
- compiled algorithm;
- realization catalogue identity;
- source and target action states;
- rank before and after;
- strict descent;
- action-chain continuity;
- final solved state;
- certificate root.

---

## **J3. How many certificates are in the bundle?**

`certificate_count = 100`

Browser producer result:

`passed_certificate_count = 100`

`failed_certificate_count = 0`

Independent verifier result:

`passed_certificate_count = 100`

`failed_certificate_count = 0`

---

## **J4. What are the main certificate roots?**

Realization catalogue root:

`e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4`

Aggregate certificate root:

`d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472`

Certificate bundle root:

`c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7`

---

## **J5. Does “certificate” mean institutional certification?**

No.

A Structural Cube certificate is a deterministic computational evidence artifact under a declared profile.

It is not accreditation by a regulator, standards body, laboratory, university, government, or unrelated organization.

---

## **J6. Where are the certificate files?**

- [Certificate bundle](../outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json)
- [Certificate manifest](../outputs/Structural_Cube_v1_0_2_Certificate_Manifest.txt)
- [Producer verification report](../outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json)
- [Independent verification report](../outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json)

---

# **SECTION K — Independent Verification**

## **K1. What software is required?**

- Python **3.9 or later**
- Python standard library only
- no third-party package
- no network connection

---

## **K2. How do I verify the certificate bundle?**

From the repository root:

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

On systems using `python3`:

```bash
python3 verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

---

## **K3. What output should I expect?**

Principal expected fields:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

---

## **K4. How long does verification take?**

Normally about one minute on a typical current desktop or laptop.

The recorded browser producer run took approximately `52 seconds` on one tested machine.

Runtime depends on processor, storage, operating system, and Python build.

Runtime is informational only.

`wall_clock_authority = NONE`

---

## **K5. Does the Python verifier call the browser resolver?**

No.

The verifier independently reconstructs the declared cube transformations, state extraction, rank, graph views, target selection, economy decisions, kernel effects, action transitions, chains, aggregate root, bundle root, and solved final states.

---

## **K6. Why does the verifier retain D01 constants?**

Earlier D01 constants are retained for compatibility with earlier evidence families.

The active v1.0.2 path verifies:

`SCCERT-1-D02-EXP-A`

and the graph-aware economy bundle.

---

## **K7. Can verification write a report to another folder?**

Yes.

The `--json-report` argument accepts a chosen output path.

Example:

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report verify/LOCAL_RESULT.json
```

---

## **K8. What do verifier exit codes mean?**

The command-line convention is:

- `0` -> verification passed;
- `1` -> evidence verification failed;
- `2` -> command usage or execution error.

---

# **SECTION L — Manifests, Reports, and Checksums**

## **L1. What is the version manifest?**

The version manifest binds the principal application and evidence files by SHA-256.

It records identities for:

- HTML application;
- certificate bundle;
- certificate manifest;
- producer report;
- Python verifier;
- independent verification report.

File:

[`../outputs/Structural_Cube_v1_0_2_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Manifest.txt)

---

## **L2. What is the version report?**

The version report binds:

- the version manifest root;
- producer verification result;
- independent verification result;
- authority declarations;
- certificate identities;
- artifact file hashes;
- claim boundary.

File:

[`../outputs/Structural_Cube_v1_0_2_Report.json`](../outputs/Structural_Cube_v1_0_2_Report.json)

---

## **L3. What checksum identifies the browser application?**

The manually maintained checksum file is:

[`../verify/SHA256SUMS.txt`](../verify/SHA256SUMS.txt)

It contains:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

This checksum identifies the exact browser HTML.

It does not by itself verify the certificate bundle or the complete evidence chain. The version manifest, version report, certificate bundle, and independent verifier preserve the deeper evidence identities.

---

## **L4. What is the version manifest root?**

`74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2`

This is also the SHA-256 of the exact manifest text file bytes.

---

## **L5. What is the version report canonical root?**

`eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225`

This is calculated from the canonical report object before the `version_report_root` field is added.

---

## **L6. Why can a raw file SHA-256 differ from a canonical root?**

They bind different subjects.

`raw file hash = SHA256(exact stored file bytes)`

`canonical object root = SHA256(canonical object under its declared profile)`

A raw file hash can change because of formatting, whitespace, field order, line endings, or a final newline. A canonical root is calculated under the canonicalization rules declared for that object.

---

## **L7. Does a matching hash prove the whole system is correct?**

No.

A matching hash proves identity relative to the referenced digest.

Correctness claims also depend on:

- legality checks;
- exact replay;
- strict descent;
- target-selection reconstruction;
- chain verification;
- final solved-state verification;
- independent implementation review.

---

# **SECTION M — Integrity and Tamper Detection**

## **M1. Is tamper rejection tested?**

Yes.

The producer audit includes a controlled mutation and requires rejection.

The recorded tamper result is:

`tamper_rejection = PASS`

---

## **M2. What happens if one certificate is changed?**

A relevant mutation should cause one or more of the following to fail:

- certificate root;
- action chain;
- aggregate manifest root;
- bundle root;
- independent verification result.

---

## **M3. What happens if the certificate manifest is changed?**

The certificate manifest file SHA-256 must equal the aggregate certificate root.

A changed manifest should break that identity.

---

## **M4. What happens if the bundle root field is changed?**

The verifier recalculates the canonical bundle root with the root field excluded and compares it with the declared value.

A mismatch must fail verification.

---

## **M5. What happens if a route reaches a non-solved final state?**

The certificate must fail.

A passing certificate requires final solved-state verification and final `W = 0`.

---

## **M6. What happens if an action does not strictly descend?**

The action and certificate must fail.

Required relation:

`W_after < W_before`

---

# **SECTION N — Scope and Claim Boundaries**

## **N1. Does Structural Cube claim shortest solutions?**

No.

`shortest_route_optimality = NOT_CLAIMED`

---

## **N2. Does it claim competition-speed superiority?**

No.

`competition_speed = NOT_CLAIMED`

---

## **N3. Does P100 prove universal totality?**

No.

`universal_totality = NOT_CLAIMED`

---

## **N4. Does it claim to own established cube mathematics?**

No.

The project does not claim ownership of standard cube transformations, established methods, or classical cube mathematics.

Its contribution is the declared structural authority, evidence, verification, and learning architecture.

---

## **N5. Is Structural Cube ready for safety-critical use?**

No such claim is made.

It is a cube-resolution and verification research system, not a safety-critical control system.

---

## **N6. Does independent verification mean independent organizational endorsement?**

No.

The Python verifier is a separate implementation path that independently reconstructs the declared evidence.

It is not an endorsement by an unrelated organization.

---

## **N7. Does the current version support camera capture?**

No.

The supplied version does not automatically read a physical cube through a camera.

---

## **N8. Does it support every twisty puzzle?**

No.

The current application supports the standard `3 x 3 x 3` cube.

---

# **SECTION O — Common Skeptic Questions**

## **O1. Could the browser producer and Python verifier share the same conceptual mistake?**

Yes.

Independent code paths reduce some implementation risks, but a shared specification error or conceptual mistake remains possible.

Useful next evidence includes:

- separately authored verifiers;
- additional legal-state corpora;
- targeted adversarial states;
- formal review of rank and kernel completeness;
- broader mutation campaigns;
- independent mathematical analysis.

---

## **O2. Is the result circular because the verifier reads producer certificates?**

The verifier reads the producer's claimed evidence but reconstructs the declared mathematics and decision path.

It does not merely accept the stored PASS label.

It checks:

- source states;
- legal turns;
- rank;
- graph;
- target pool;
- economy decision;
- pure effect;
- action replay;
- chains;
- roots;
- solved final state.

---

## **O3. Why not verify only the final solved cube?**

A solved final state alone does not prove:

- how the route was chosen;
- whether reference information entered selection;
- whether every action matched its declared target;
- whether rank descended at each boundary;
- whether the certificate chain is continuous.

Structural Cube verifies the route action by action.

---

## **O4. Could a long route still pass?**

Yes.

A route may pass structural and certificate checks without being shortest.

Route correctness and route optimality are separate questions.

---

## **O5. Why is zero fallback important?**

Zero fallback means the evaluated primary routes did not silently switch to an undeclared secondary authority.

For the committed P100 evidence:

`fallback_activation = NONE`

This does not imply that every conceivable implementation or future state is universally covered.

---

## **O6. Why is reference-route isolation important?**

It prevents a current-state reference solution from choosing the structural target and then being described afterward as a structural decision.

The declared P100 authority boundary is:

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

---

## **O7. Could all 100 seeds be unusually easy?**

A committed seeded corpus is reproducible and useful, but it is still a limited sample.

Broader evidence should include:

- additional seed ranges;
- constructed parity-edge cases;
- orientation-heavy states;
- long-cycle states;
- independent state generators;
- all-state proof or exhaustive analysis where feasible.

---

## **O8. Why not claim universal correctness after 100 passes?**

Because corpus evidence and universal proof are different.

`100 tested routes pass != every legal state formally proved`

The documentation keeps those claims separate.

---

# **SECTION P — Falsification**

## **P1. Can Structural Cube be challenged?**

Yes.

Independent replay, mutation, reimplementation, mathematical review, and falsification are encouraged.

---

## **P2. What are useful falsification targets?**

Attempt to produce:

- same canonical source state -> different route under identical profiles;
- selected target -> graph-aware selector disagrees;
- accepted kernel -> observed pure effect differs;
- accepted action -> `W_after >= W_before`;
- compiled algorithm -> target state mismatch;
- changed certificate -> root still accepted;
- broken action chain -> certificate still accepted;
- changed certificate manifest -> aggregate root still accepted;
- changed bundle -> bundle root still accepted;
- presentation-only change -> certified structural target changes;
- nonzero fallback -> authority status still passes;
- current-state reference-route access -> authority status still passes;
- current-state reference-distance access -> authority status still passes;
- non-solved final state -> certificate still passes;
- one failed certificate -> P100 summary still passes.

Primary target:

`invalid structural transition -> valid SCCERT certificate`

---

## **P3. What should happen when a falsification succeeds?**

A reproducible prohibited outcome should lead to one or more of the following:

- correct the implementation;
- strengthen the verifier;
- revise the specification;
- expand the test corpus;
- narrow the documented claim;
- replace affected evidence files;
- increment the version.

---

## **P4. Does one defect invalidate the entire structural idea?**

Not necessarily.

A defect identifies the limit of the current implementation, specification, or claim.

A useful evidence system should make that limit visible and correctable.

---

# **SECTION Q — Extension Directions**

## **Q1. Can the corpus be expanded?**

Yes.

Additional corpora can cover:

- larger seed ranges;
- manually constructed legal states;
- long permutation cycles;
- orientation-heavy states;
- parity-transition states;
- compiler stress cases.

Each corpus should have its own identity and manifest.

---

## **Q2. Can another verifier be written?**

Yes.

A high-value extension would be an independently authored verifier in another language that reconstructs the same SCCERT profile and roots.

---

## **Q3. Can route economy improve further?**

Yes.

Possible directions include:

- larger graph-ranked target pools;
- deeper structural lookahead;
- better compiled-kernel cost models;
- compatible adjacent-action composition;
- deterministic catalogue reduction;
- independently verified route compression.

Every change should preserve exact effect, strict descent, reference isolation, zero fallback, and reproducibility.

---

## **Q4. Can Structural Cube support other puzzles?**

Potentially.

Another puzzle would require its own:

- canonical state;
- legality rules;
- graph model;
- structural rank;
- kernel contracts;
- compiler;
- certificate profile;
- independent verifier.

The current evidence applies only to the standard `3 x 3 x 3` cube.

---

# **SECTION R — Short Answers**

## **R1. Is Structural Cube deterministic?**

Yes, under the same declared state, version, policy, profiles, and budgets.

---

## **R2. Is it offline?**

Yes.

---

## **R3. Does it require administrator rights?**

No.

---

## **R4. Does the application require Python?**

No.

Python is needed only for independent certificate verification.

---

## **R5. Does verification require third-party packages?**

No.

The verifier uses the Python standard library.

---

## **R6. Does the primary P100 route use a current-state reference solution?**

No.

`reference_route_access = NONE`

---

## **R7. Does the primary P100 route activate fallback?**

No.

`fallback_activation = NONE`

---

## **R8. Did all P100 routes solve?**

Yes.

`100 / 100`

---

## **R9. Did all portable certificates pass browser verification?**

Yes.

`100 / 100`

---

## **R10. Did all portable certificates pass independent Python verification?**

Yes.

`100 / 100`

---

## **R11. Is shortest-route optimality claimed?**

No.

---

## **R12. What checksum identifies the browser application?**

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

---

# **Documentation**

- [README](../README.md)
- [Quickstart](QUICKSTART.md)
- [FAQ](FAQ.md) (this document)
- [Architecture](ARCHITECTURE.md)
- [Evidence and Verification](EVIDENCE_AND_VERIFICATION.md)
- [Claim Boundary](CLAIM_BOUNDARY.md)
- [Verification Procedure](../verify/VERIFY.md)
- [Resolver Architecture Specification](specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt)
- [Corpus and Telemetry Specification](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt)
- [SCGS-1-D02 Specification](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# ⭐ **Final One-Line Summary**

Structural Cube resolves a legal cube state through graph-governed pure-kernel actions whose exact effects, rank descent, route identities, and final solved state can be replayed and independently verified.

---

# 🌌 **Final Insight**

A cube can move in many legal ways.

Structural Cube asks a stricter question:

**Does every accepted action belong to a visible and verifiable path of structural closure?**

`state -> structure -> action -> evidence -> descent -> solved state`

**The cube moves locally. The structure closes globally.**
