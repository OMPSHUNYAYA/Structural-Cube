# ⚡ **Structural Cube — Quickstart**

## **Dependency-Governed Resolution for a 3 x 3 x 3 Cube**

### **Open the Cube • Verify the Evidence • Reproduce the Result**

**Structure proposes. Verification checks. Every completed action must descend.**

`state -> structure -> action -> evidence -> descent -> solved state`

---

# **1. Purpose**

This guide provides the shortest reliable path for using and verifying **Structural Cube v1.0.2**.

The repository contains:

- one self-contained browser application;
- one committed `P100` certificate bundle;
- one browser producer report;
- one independent Python verifier;
- one independent verification report;
- one version manifest;
- one version report;
- three technical specifications;
- reader documentation;
- SHA-256 identity records.

The complete evidence path is:

`browser application -> producer certificates -> portable bundle -> independent verifier -> version manifest -> version report`

The exact browser application is identified separately through `verify/SHA256SUMS.txt`.

---

# **2. Repository Structure**

```text
README.md
LICENSE

demo/
    Structural_Cube_v1_0_2.html

docs/
    QUICKSTART.md
    FAQ.md
    ARCHITECTURE.md
    EVIDENCE_AND_VERIFICATION.md
    CLAIM_BOUNDARY.md
    Structural_Cube_Architecture_Diagram_v1_0_2.png

    specifications/
        SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt
        Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt
        Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt

outputs/
    Structural_Cube_v1_0_2_Certificate_Bundle.json
    Structural_Cube_v1_0_2_Certificate_Manifest.txt
    Structural_Cube_v1_0_2_Independent_Verification_Report.json
    Structural_Cube_v1_0_2_Manifest.txt
    Structural_Cube_v1_0_2_Producer_Verification_Report.json
    Structural_Cube_v1_0_2_Report.json

verify/
    Structural_Cube_v1_0_2_Verifier.py
    VERIFY.md
    SHA256SUMS.txt
```

The repository keeps one canonical copy of each application, evidence, specification, and verification file.

---

# **3. Requirements**

## **Browser application**

Required:

- a current browser with JavaScript enabled;
- approximately `6.1 MB` of local storage for the HTML file.

Not required:

- installation;
- administrator rights;
- network access;
- browser extension;
- external solver;
- external dataset;
- API key;
- database.

## **Independent verification**

Required:

- Python **3.9 or later**;
- approximately `11 MB` of local storage for the certificate bundle;
- enough memory to load and verify the bundle.

Not required:

- third-party Python packages;
- network access;
- administrator rights;
- the browser application running at the same time.

Check Python:

```bash
python --version
```

On systems where Python is exposed as `python3`:

```bash
python3 --version
```

---

# **4. Fastest Use Path**

1. Download or clone the repository.
2. Download the HTML file if GitHub does not display it.
3. Open [`../demo/Structural_Cube_v1_0_2.html`](../demo/Structural_Cube_v1_0_2.html) locally.
4. Choose **Random** or mix the cube manually.
5. Choose **Auto Resolve**, **With Hint**, or **Solve Myself**.
6. Open the **Technical** tab when formulas and evidence are needed.

The application is a single HTML file.

GitHub may show a message that the file is too large to display. **Download it and open it locally in a modern browser.**

---

# **5. Opening the Browser Application**

## **Windows Command Prompt**

From the repository root:

```bat
start "" "demo\Structural_Cube_v1_0_2.html"
```

## **Windows PowerShell**

```powershell
Start-Process ".\demo\Structural_Cube_v1_0_2.html"
```

## **Linux**

```bash
xdg-open demo/Structural_Cube_v1_0_2.html
```

## **macOS**

```bash
open demo/Structural_Cube_v1_0_2.html
```

You may also open the file directly through the file manager.

---

# **6. Browser Security-Origin Notice**

A Chromium-based browser may log a message similar to:

```text
'file:' URLs are treated as unique security origins
```

This notice can appear when a local HTML file is opened through `file:`.

It does not by itself indicate that Structural Cube failed.

Use the following as the meaningful evidence:

- the application audit result;
- route completion;
- strict `W` descent;
- final solved state;
- certificate verification;
- SHA-256 identity checks.

---

# **7. First Cube Run**

## **Step 1 — Create a State**

Choose one of the following:

- **Random** — generates a deterministic seeded scramble;
- **Manual** — begins from a state entered through legal turns;
- direct cube interaction — drag a row or column, or tap a face and choose a turn.

The committed corpus uses:

`generator = xorshift32`

`scramble_length = 22`

`seed_set = 1..100`

The reproducibility law is:

`same seed + same generator version + same scramble length -> same scramble`

---

## **Step 2 — Choose a Mode**

### **Auto Resolve**

The application prepares and carries out a graph-governed structural route.

### **With Hint**

The application presents the next verified instruction while the user performs the move.

### **Solve Myself**

The application removes move guidance so the cube can be explored without hints.

---

## **Step 3 — Read the Guidance**

The main guidance is separated into:

- **Strategy** — the larger structural goal;
- **Plan** — why the next action belongs to that goal;
- **Move** — the immediate turn instruction.

The learning relation is:

`verified structural purpose -> Strategy -> Plan -> Move`

---

## **Step 4 — Inspect Technical Evidence**

Open the **Technical** tab to inspect items such as:

- canonical state;
- structural rank;
- graph profile;
- kernel target;
- compiled action;
- action-boundary rank transition;
- route and certificate identities.

---

# **8. Core Structural Relations**

The cubie state is:

`C = (P_e, O_e, P_c, O_c)`

Legal states satisfy:

`sum(O_e) mod 2 = 0`

`sum(O_c) mod 3 = 0`

`parity(P_e) = parity(P_c)`

The structural potential is:

`Phi(C) = (rho, D_e + D_c, tau_e + tau_c, F, T)`

The integer rank is:

`W(C) = 24*rho + 4*(D_e + D_c) + tau_e + tau_c + F + T`

For the declared legal-state convention:

`0 <= W(C) <= 126`

and:

`W(C) = 0 iff C = SOLVED`

Every completed primary action must satisfy:

`W(C_(i+1)) < W(C_i)`

---

# **9. Five Structural Kernel Families**

| Kernel | Declared purpose |
|---|---|
| `EF(i,j)` | Correct a paired edge-orientation residue |
| `CT(i,j)` | Correct a paired corner-twist residue |
| `E3(i,j,k)` | Apply an exact three-edge permutation cycle |
| `C3(i,j,k)` | Apply an exact three-corner permutation cycle |
| `PB(i,j;k,l)` | Bridge the shared edge-corner permutation parity |

The action chain is:

`current state -> deterministic kernel target -> exact pure-effect contract -> compiled turns -> replay -> strict W descent`

The compiler boundary is:

`compiler_search_input = ISOLATED_PURE_KERNEL_EFFECT_ONLY`

The primary authority declarations are:

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

`fallback_activation = NONE`

---

# **10. Graph-Governed Economy Selection**

At each action boundary, the v1.0.2 selector:

1. enumerates exact strict-descent targets;
2. ranks them under the full observed graph;
3. retains the strongest four admitted targets;
4. compares continuations to depth four;
5. selects the lowest declared compiled move cost;
6. replays and verifies the selected action.

Compact relation:

`full graph -> top 4 targets -> depth 4 comparison -> lowest declared compiled move cost`

Profiles:

`PRIMARY_AUTHORITY = GRAPH_GOVERNED_ECONOMY_PRIMARY_AUTHORITY`

`ROUTE_AUTHORITY = REFERENCE_FREE_STRUCTURAL_KERNEL_AUTHORITY`

`ECONOMY_POLICY = TOP_4_GRAPH_POOL_DEPTH_4`

---

# **11. Verify the Browser Application**

The manually maintained checksum file covers:

[`../verify/SHA256SUMS.txt`](../verify/SHA256SUMS.txt)

It identifies:

`demo/Structural_Cube_v1_0_2.html`

Expected entry:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

## **Windows**

From the repository root:

```bat
certutil -hashfile "demo\Structural_Cube_v1_0_2.html" SHA256
```

## **Windows PowerShell**

```powershell
Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256
```

## **Linux**

```bash
sha256sum -c verify/SHA256SUMS.txt
```

## **macOS**

```bash
shasum -a 256 -c verify/SHA256SUMS.txt
```

Interpretation:

`matching HTML checksum = matching browser-application identity`

`matching checksum != complete behavioral verification`

The checksum identifies the exact browser HTML. The certificate bundle, version manifest, version report, and independent verifier preserve the deeper evidence chain.

---

# **12. Run Independent Verification**

From the repository root:

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

On systems using `python3`:

```bash
python3 verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

The command verifies the exact certificate bundle committed in `outputs/`.

Expected principal result:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

Expected execution time is approximately one minute on a typical current desktop or laptop.

Runtime depends on:

- processor;
- storage;
- operating system;
- Python build.

Runtime is informational only.

`wall_clock_authority = NONE`

---

# **13. What the Python Verifier Reconstructs**

The verifier does not merely read the producer's PASS label.

It reconstructs and checks:

- cube move permutations;
- canonical facelet states;
- cubie extraction;
- legal-state invariants;
- structural-rank values;
- SCGS graph views;
- graph scores;
- target pools;
- depth-four economy decisions;
- pure-kernel effects;
- compiled action transitions;
- action-chain continuity;
- certificate roots;
- certificate aggregate root;
- certificate bundle root;
- final solved states.

The verifier retains earlier D01 constants for compatibility.

The active v1.0.2 path verifies:

`SCCERT-1-D02-EXP-A`

and the graph-aware economy certificate bundle.

---

# **14. Expected Certificate Identities**

| Identity | SHA-256 |
|---|---|
| Source corpus manifest | `9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd` |
| Realization catalogue root | `e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4` |
| Certificate aggregate root | `d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472` |
| Certificate bundle root | `c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7` |
| Version manifest root | `74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2` |
| Version report canonical root | `eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225` |

Distinguish:

`raw file SHA-256 != canonical object root in every format`

---

# **15. P100 Result Summary**

The committed P100 evidence reports:

| Property | Result |
|---|---:|
| Requested states | **100** |
| Completed states | **100** |
| Solved states | **100/100** |
| Strict `W` descent | **PASS** |
| Final `W = 0` | **100/100** |
| Current-state reference-route access | **NONE** |
| Current-state reference-distance access | **NONE** |
| Fallback activation | **NONE** |
| Browser certificate verification | **100/100 PASS** |
| Independent Python verification | **100/100 PASS** |
| Tamper rejection | **PASS** |
| Seeds improved against the earlier full-graph route | **100** |
| Equal seeds | **0** |
| Regressed seeds | **0** |
| Mean moves | **174.58** |
| Median moves | **172** |
| `p95` moves | **207** |
| Maximum moves | **223** |
| Total move reduction across P100 | **1,941** |

These results apply to the committed corpus, application version, profiles, and comparison boundary.

They do not establish shortest-route optimality or universal totality.

---

# **16. Inspect the Evidence Files**

## **Certificate bundle**

[`../outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json`](../outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json)

Contains:

- source corpus records;
- realization catalogue;
- 100 portable certificates;
- aggregate certificate manifest;
- summary;
- authority declarations;
- certificate bundle root.

## **Certificate manifest**

[`../outputs/Structural_Cube_v1_0_2_Certificate_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Certificate_Manifest.txt)

Binds the 100 certificate roots.

## **Producer verification report**

[`../outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json`](../outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json)

Records:

- browser bundle verification;
- expected-root agreement;
- tamper rejection;
- producer status.

## **Independent verification report**

[`../outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json`](../outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json)

Records the separate Python verification result.

## **Version manifest**

[`../outputs/Structural_Cube_v1_0_2_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Manifest.txt)

Binds the principal application and evidence files by SHA-256.

## **Version report**

[`../outputs/Structural_Cube_v1_0_2_Report.json`](../outputs/Structural_Cube_v1_0_2_Report.json)

Binds:

- version manifest root;
- producer result;
- independent result;
- authority declarations;
- artifact identities;
- claim boundary.

---

# **17. Verify the Browser Checksum**

The repository checksum file is:

[`../verify/SHA256SUMS.txt`](../verify/SHA256SUMS.txt)

It intentionally covers only the browser application.

## **Linux**

```bash
sha256sum -c verify/SHA256SUMS.txt
```

## **macOS**

```bash
shasum -a 256 -c verify/SHA256SUMS.txt
```

## **Windows PowerShell**

```powershell
Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256
```

Expected SHA-256:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab
```

Detailed verification instructions are provided in:

[`../verify/VERIFY.md`](../verify/VERIFY.md)

---

# **18. Keep Generated Evidence Unchanged**

Treat files inside `outputs/` as generated evidence.

After verification:

- do not edit JSON formatting;
- do not change line endings;
- do not rename fields;
- do not reorder canonical records;
- do not save through an editor that changes bytes;
- do not replace a file without rebuilding its dependent manifest and report.

A harmless visual formatting change can still alter a raw file SHA-256.

---

# **19. Failure Interpretation**

## **Browser-application checksum mismatch**

Possible causes:

- wrong application version;
- partial download;
- accidental HTML editing;
- changed file bytes;
- incorrect repository path.

Action:

- restore the intended browser application;
- recalculate its SHA-256;
- confirm the file path;
- treat a mismatching file as a different browser artifact.

---

## **Missing certificate bundle**

Expected path:

```text
outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json
```

Action:

- restore the file from the repository package;
- confirm its name and path;
- rerun the verifier.

---

## **Python version error**

Required:

`Python >= 3.9`

Action:

- install or select a compatible Python interpreter;
- run `python --version` or `python3 --version`;
- rerun the command.

---

## **Verification status FAIL**

Action:

- preserve the generated local report;
- inspect the first reported failure;
- compare the bundle and checksum identities;
- do not replace the result with a stored PASS report;
- follow the detailed procedure in [`../verify/VERIFY.md`](../verify/VERIFY.md).

---

## **Browser route stops**

Possible causes:

- user cancellation;
- browser tab suspension;
- insufficient available memory;
- interrupted local execution.

Action:

- keep the tab active;
- avoid system sleep;
- rerun from the same declared state or seed;
- distinguish execution interruption from a mathematical verdict.

---

# **20. Recommended Review Order**

1. Read [`../README.md`](../README.md).
2. Follow this Quickstart.
3. Open the browser application.
4. Run one seeded state.
5. Inspect Strategy, Plan, and Move.
6. Open the Technical tab.
7. Verify the browser-application SHA-256.
8. Run the Python verifier.
9. Confirm `100/100` certificate passes.
10. Read [`FAQ.md`](FAQ.md).
11. Read [`ARCHITECTURE.md`](ARCHITECTURE.md).
12. Read [`EVIDENCE_AND_VERIFICATION.md`](EVIDENCE_AND_VERIFICATION.md).
13. Read [`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md).
14. Read the technical specifications.
15. Attempt the documented falsification targets.

---

# **21. Technical Specifications**

## **Resolver architecture**

[`specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt`](specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt)

## **Corpus, telemetry, and improvement measurement**

[`specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt`](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt)

## **Canonical graph serialization**

[`specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt`](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# **22. Claim Boundary**

Structural Cube v1.0.2 establishes, for the committed P100 corpus:

- deterministic graph-governed structural selection;
- strict rank descent at every completed action boundary;
- solved closure for all 100 starting states;
- zero current-state reference-route access;
- zero current-state reference-distance access;
- zero fallback activation;
- lower route move count on all 100 tested seeds relative to the declared earlier route;
- portable certificate generation;
- browser certificate verification;
- independent Python verification;
- tamper rejection;
- reproducible SHA-256 identities.

It does not claim:

- shortest-route optimality;
- competition-speed superiority;
- universal totality over every legal cube state;
- superiority over every established cube method;
- independent institutional endorsement;
- measured learner-outcome superiority;
- camera-based physical-cube capture;
- support for every twisty puzzle.

The version class is:

`EXPERIMENTAL`

The evidence boundary is:

`COMMITTED_P100`

---

# **23. Falsification Entry Points**

Useful challenge targets include:

- same canonical state -> different route under identical profiles;
- selected target -> reconstructed graph selector disagrees;
- accepted kernel -> observed pure effect differs;
- completed action -> `W_after >= W_before`;
- compiled algorithm -> target-state mismatch;
- broken action chain -> certificate accepted;
- modified certificate -> root accepted;
- modified manifest -> aggregate root accepted;
- modified bundle -> bundle root accepted;
- current-state reference access -> authority status accepted;
- nonzero fallback -> authority status accepted;
- non-solved final state -> certificate accepted;
- one failed certificate -> P100 summary accepted.

Primary falsification target:

`invalid structural transition -> valid SCCERT certificate`

A reproducible prohibited outcome should be preserved and used to correct the implementation, strengthen verification, or narrow the stated guarantee.

---

# **24. Quick Commands**

## **Open the application on Windows**

```bat
start "" "demo\Structural_Cube_v1_0_2.html"
```

## **Verify the browser application on Windows**

```bat
certutil -hashfile "demo\Structural_Cube_v1_0_2.html" SHA256
```

## **Run independent verification**

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

## **Expected verification summary**

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

---

# **25. Final Quickstart Summary**

## **Use**

`download HTML -> open locally -> mix cube -> choose mode -> follow verified guidance`

## **Verify**

`check browser HTML SHA-256 -> run Python verifier -> confirm 100/100 PASS`

## **Structural chain**

`state -> rank -> graph -> kernel target -> compiled turns -> replay -> strict descent`

## **Evidence chain**

`certificate -> aggregate root -> bundle root -> manifest root -> version report`

## **Primary principle**

**A legal turn is not automatically a useful structural action.**

**A structural action must declare its target, reproduce its exact effect, and end at a lower verified rank.**

**The cube moves locally. The structure closes globally.**
