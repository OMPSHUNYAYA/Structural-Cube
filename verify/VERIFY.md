# ✅ **Structural Cube — Verification Guide**

## **Structural Cube v1.0.2**

### **Verify the Browser Application • Reconstruct Certificates • Confirm Structural Authority**

`application identity -> certificate reconstruction -> aggregate root -> bundle root -> version evidence`

---

# **1. Purpose**

This guide defines the recommended verification procedure for **Structural Cube v1.0.2**.

The repository contains one integrated browser application, one committed P100 evidence bundle, one independent Python verifier, generated evidence files, technical specifications, and reader documentation.

The verification model intentionally separates two tasks:

`SHA256SUMS.txt -> simple browser-application identity`

`Python verifier -> complete certificate-bundle reconstruction`

This guide focuses on:

- browser-application identity;
- independent Python reconstruction;
- strict structural-rank descent;
- exact action replay;
- graph-governed target selection;
- reference-route isolation;
- zero fallback activation;
- aggregate-root and bundle-root agreement;
- producer and independent-result agreement;
- tamper rejection;
- claim-boundary review;
- falsification testing.

---

# **2. Repository Paths**

From the repository root, the relevant files are:

```text
demo/
    Structural_Cube_v1_0_2.html

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

Reader documentation is under:

`docs/`

Technical specifications are under:

`docs/specifications/`

---

# **3. Requirements**

Required:

- Python **3.9 or later**;
- Windows Command Prompt, PowerShell, Linux shell, or macOS Terminal;
- local file-system access;
- enough memory to load an approximately `11 MB` certificate bundle.

Not required:

- administrator rights;
- third-party Python packages;
- network access;
- external cube solver;
- external dataset;
- API key;
- cloud service;
- database;
- browser execution during independent verification.

Check Python:

```bash
python --version
```

or:

```bash
python3 --version
```

Expected:

```text
Python 3.9 or later
```

---

# **4. Recommended Verification Order**

1. Confirm the Python version.
2. Verify the SHA-256 of the browser application.
3. Run the independent Python verifier.
4. Confirm `100/100` certificates pass.
5. Confirm the realization catalogue root.
6. Confirm the certificate aggregate root.
7. Confirm the certificate bundle root.
8. Confirm strict `W` descent.
9. Confirm final `W = 0`.
10. Confirm current-state reference-route access is `NONE`.
11. Confirm current-state reference-distance access is `NONE`.
12. Confirm fallback activation is `NONE`.
13. Confirm the producer and independent reports both record `PASS`.
14. Confirm tamper rejection is `PASS`.
15. Review the architecture and claim boundary.
16. Attempt the documented falsification targets.

Accept the package as verified only when the required identities and reconstructed results agree.

---

# **5. Verify the Browser Application**

The checksum file intentionally contains only:

`demo/Structural_Cube_v1_0_2.html`

Expected SHA-256:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab
```

Expected `verify/SHA256SUMS.txt` content:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

## **Windows Command Prompt**

```bat
certutil -hashfile "demo\Structural_Cube_v1_0_2.html" SHA256
```

## **Windows PowerShell**

```powershell
Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256
```

## **Linux**

```bash
sha256sum demo/Structural_Cube_v1_0_2.html
```

## **macOS**

```bash
shasum -a 256 demo/Structural_Cube_v1_0_2.html
```

Interpretation:

`matching checksum = matching browser-application identity`

It does not by itself verify the complete certificate chain.

---

# **6. Verify the Checksum File**

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
$expected = "f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab"
$actual = (Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256).Hash.ToLower()
if ($actual -eq $expected) {
    "PASS"
} else {
    "FAIL"
}
```

Expected result:

```text
PASS
```

---

# **7. Run Independent Verification**

From the repository root:

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

On systems using `python3`:

```bash
python3 verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

Expected principal output:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

Expected exit code:

```text
0
```

Expected runtime:

```text
approximately one minute
```

The browser producer run recorded approximately:

```text
52 seconds
```

Runtime depends on processor, storage, operating system, Python build, and available memory.

Runtime is informational only.

`wall_clock_authority = NONE`

---

# **8. Verifier Scope**

The verifier independently reconstructs:

- legal face-turn permutations;
- canonical facelet states;
- edge and corner extraction;
- reachability conditions;
- structural-rank components;
- `Phi(C)`;
- `W(C)`;
- SCGS-derived graph views;
- graph scores;
- deterministic target pools;
- top-four candidate selection;
- depth-four economy comparison;
- pure-kernel effects;
- compiled action transitions;
- action-chain continuity;
- certificate roots;
- certificate-manifest aggregate root;
- certificate-bundle root;
- final solved states.

The verifier does not merely trust:

- stored `PASS` fields;
- browser-generated action descriptions;
- route summaries;
- final-state labels.

The verifier retains earlier D01 constants for compatibility.

The active v1.0.2 path verifies:

`SCCERT-1-D02-EXP-A`

---

# **9. Structural-Rank Verification**

The declared cube state is:

`C = (P_e, O_e, P_c, O_c)`

Legal states satisfy:

`sum(O_e) mod 2 = 0`

`sum(O_c) mod 3 = 0`

`parity(P_e) = parity(P_c)`

The lexicographic potential is:

`Phi(C) = (rho, D_e + D_c, tau_e + tau_c, F, T)`

The integer rank is:

`W(C) = 24*rho + 4*(D_e + D_c) + tau_e + tau_c + F + T`

Expected range:

`0 <= W(C) <= 126`

Expected solved-state relation:

`W(C) = 0 iff C = SOLVED`

Every completed primary action must satisfy:

`W(C_after) < W(C_before)`

A route must fail verification when any completed action violates strict descent.

---

# **10. Kernel Verification**

The verifier recognizes five exact pure-effect kernel families:

- `EF(i,j)`
- `CT(i,j)`
- `E3(i,j,k)`
- `C3(i,j,k)`
- `PB(i,j;k,l)`

For each action, the verifier checks:

1. the selected kernel type;
2. the selected target cubies;
3. the declared pure effect;
4. the compiled face-turn sequence;
5. the observed source-to-target transition;
6. the predicted target state;
7. the observed target state;
8. exact equality between predicted and observed states;
9. strict `W` descent.

Expected relation:

`declared kernel target -> exact observed effect`

---

# **11. Graph-Governed Economy Verification**

The active policy is:

`FULL_GRAPH -> TOP_4_TARGET_POOL -> DEPTH_4_LOOKAHEAD -> LOWEST_COMPILED_MOVE_COST`

The verifier reconstructs:

1. exact strict-descent targets;
2. graph-aware scores;
3. canonical target order;
4. top-four admitted pool;
5. deterministic depth-four continuations;
6. declared compiled move cost;
7. selected first action.

Expected profiles:

```text
interactive_authority = GRAPH_GOVERNED_ECONOMY_PRIMARY_AUTHORITY
route_authority = REFERENCE_FREE_STRUCTURAL_KERNEL_AUTHORITY
graph_authority = FULL_GRAPH
economy_policy = TOP_4_GRAPH_POOL_DEPTH_4
```

The policy does not claim globally shortest routes.

---

# **12. Action-Chain Verification**

For every adjacent action pair:

`target_state_hash_i = source_state_hash_(i+1)`

The verifier also checks:

- source and target facelets;
- source and target cubie states;
- source and target ranks;
- action order;
- action root;
- predecessor link;
- route move concatenation.

A broken chain must invalidate the certificate.

---

# **13. Route-Level Verification**

A route passes only when:

- source state is legal;
- every action passes;
- every action strictly descends;
- action-chain continuity passes;
- no current-state reference route is accessed;
- no current-state reference distance is accessed;
- no fallback is activated;
- the final state is solved;
- final `W = 0`;
- the certificate root reconstructs.

Compact relation:

`all actions valid + chain continuous + authority isolated + final solved -> route certificate valid`

---

# **14. Corpus-Level Verification**

Expected corpus profile:

`SCCERT-ECONOMY-CORPUS-1-D01-EXP-A`

Expected certificate profile:

`SCCERT-1-D02-EXP-A`

Expected corpus result:

```text
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

The verifier also checks:

- unique certificate roots;
- certificate-manifest count;
- certificate-manifest order;
- source corpus identity;
- realization catalogue identity;
- certificate aggregate root;
- certificate bundle root;
- P100 summary consistency.

---

# **15. Expected Evidence Roots**

Source corpus manifest hash:

```text
9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd
```

Realization catalogue root:

```text
e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4
```

Certificate aggregate root:

```text
d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472
```

Certificate bundle root:

```text
c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7
```

Version manifest root:

```text
74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2
```

Version report canonical root:

```text
eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225
```

These are evidence identities carried by the committed outputs.

They are not entries in `verify/SHA256SUMS.txt`.

---

# **16. Expected P100 Result**

| Property | Expected result |
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
| Seeds improved against earlier full-graph selector | **100** |
| Equal seeds | **0** |
| Regressed seeds | **0** |
| Mean moves | **174.58** |
| Median moves | **172** |
| `p95` moves | **207** |
| Maximum moves | **223** |
| Total move reduction | **1,941** |

These values apply to the committed P100 corpus and the declared earlier full-graph selector.

---

# **17. Producer Verification Result**

Inspect:

`outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json`

Expected:

```text
status = PASS
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
browser_bundle_verification = PASS
tamper_rejection = PASS
expected_root_match = PASS
```

Expected producer profile:

`SCCERT-ECONOMY-AUDIT-1-D01-EXP-A`

Expected source manifest hash:

`9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd`

Expected bundle root:

`c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7`

---

# **18. Independent Verification Result**

Inspect:

`outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json`

Expected:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

It must agree with the producer report on:

- realization catalogue root;
- certificate aggregate root;
- certificate bundle root;
- certificate count;
- pass count;
- fail count.

---

# **19. Version Evidence**

Inspect:

`outputs/Structural_Cube_v1_0_2_Manifest.txt`

and:

`outputs/Structural_Cube_v1_0_2_Report.json`

The manifest and report provide the deeper version-evidence chain.

They are not included in `verify/SHA256SUMS.txt`.

The intended separation is:

`SHA256SUMS.txt -> browser application identity`

`version manifest and report -> retained version evidence`

`Python verifier -> certificate-bundle reconstruction`

A future GitHub workflow can automate the complete chain.

---

# **20. Tamper-Rejection Check**

The producer evidence records:

`tamper_rejection = PASS`

A relevant evidence-package mutation should cause one or more of the following to fail:

- source-state hash;
- graph identity;
- kernel target;
- compiled action;
- target-state hash;
- rank transition;
- action-chain link;
- certificate root;
- aggregate root;
- bundle root.

A changed bundle must not retain a passing bundle-root verification.

A changed browser HTML file is detected separately through the browser-application checksum recorded in `verify/SHA256SUMS.txt`.

---

# **21. Identity Interpretation**

Different identities bind different subjects.

## **Browser-application SHA-256**

`SHA256(exact HTML file bytes)`

## **Canonical object root**

`SHA256(canonical object excluding its own root field)`

## **Certificate aggregate root**

Binds the exact ordered certificate manifest.

## **Certificate bundle root**

Binds the canonical certificate bundle object.

## **Version manifest root**

`SHA256(exact version manifest bytes)`

Binds the exact stored version-manifest file.

## **Version report canonical root**

Binds the canonical report object before its root field is added.

Therefore:

`application checksum != complete certificate verification`

and:

`raw file identity != canonical object root in every format`

---

# **22. Failure Interpretation**

## **Browser-application checksum mismatch**

Possible causes:

- partial download;
- accidental edit;
- changed line endings;
- wrong version;
- changed HTML content.

Action:

- restore the exact HTML file;
- recalculate the checksum;
- do not treat the application as byte-identical until the expected checksum matches.

---

## **Verifier usage error**

Possible causes:

- Python older than `3.9`;
- incorrect command;
- missing verifier;
- missing certificate bundle;
- invalid output path.

Action:

- check `python --version`;
- confirm repository-root execution;
- confirm file paths.

---

## **Certificate failure**

Possible causes:

- illegal source state;
- rank mismatch;
- graph mismatch;
- target-selection mismatch;
- pure-effect mismatch;
- compiled-transition mismatch;
- non-descending action;
- broken chain;
- non-solved final state;
- certificate-root mismatch.

Action:

- preserve the failing local report;
- inspect the first failed certificate and action;
- do not replace the local failure with the committed passing report.

---

## **Bundle-root failure**

Possible causes:

- changed certificate;
- changed manifest;
- changed realization catalogue;
- changed authority declaration;
- changed summary;
- changed JSON object.

Action:

- preserve the bundle;
- compare the earliest reported mismatch;
- restore or regenerate through the declared process.

---

# **23. Evidence Preservation**

Treat files under `outputs/` as generated evidence.

Do not:

- edit JSON indentation;
- reorder object fields;
- change line endings;
- add notes inside evidence files;
- remove the final newline;
- alter certificate order;
- modify roots manually;
- replace one artifact without regenerating dependent identities.

A formatting-only change may alter a raw file identity even when the visible information appears unchanged.

---

# **24. Independent Review Checklist**

A reviewer should confirm:

- [ ] Python is version `3.9` or later.
- [ ] The browser-application checksum matches.
- [ ] The local Python verifier returns exit code `0`.
- [ ] The locally generated report records `status = PASS`.
- [ ] Certificate count is `100`.
- [ ] Passed certificate count is `100`.
- [ ] Failed certificate count is `0`.
- [ ] Source corpus manifest hash matches.
- [ ] Realization catalogue root matches.
- [ ] Certificate aggregate root matches.
- [ ] Certificate bundle root matches.
- [ ] The producer report status is `PASS`.
- [ ] The independent report status is `PASS`.
- [ ] Current-state reference-route access is `NONE`.
- [ ] Current-state reference-distance access is `NONE`.
- [ ] Fallback activation is `NONE`.
- [ ] Wall-clock authority is `NONE`.
- [ ] Tamper rejection is `PASS`.
- [ ] The claim boundary matches the demonstrated evidence.

---

# **25. Falsification Targets**

Attempt to produce:

- same canonical source state -> different route under identical profiles;
- selected target -> reconstructed graph selector disagrees;
- accepted kernel -> exact pure effect differs;
- completed action -> `W_after >= W_before`;
- compiled algorithm -> target-state mismatch;
- broken action chain -> certificate accepted;
- modified certificate -> unchanged certificate root;
- modified certificate manifest -> unchanged aggregate root;
- modified bundle -> unchanged bundle root;
- current-state reference-route access -> authority PASS;
- current-state reference-distance access -> authority PASS;
- nonzero fallback -> zero-fallback PASS;
- non-solved final state -> certificate PASS;
- one failed certificate -> P100 PASS;
- changed HTML -> original browser-application checksum;
- documentation claiming more than the evidence supports.

Primary falsification target:

`invalid structural transition -> valid SCCERT certificate`

A reproducible prohibited outcome invalidates the affected guarantee until it is corrected or narrowed.

---

# **26. Scope Boundary**

Structural Cube v1.0.2 demonstrates the documented properties for the committed P100 corpus.

It does not establish:

- shortest-route optimality;
- competition-speed superiority;
- universal totality over every legal cube state;
- superiority over every established cube method;
- exhaustive defect detection;
- exhaustive mutation coverage;
- immunity from shared specification errors;
- independent institutional accreditation;
- measured learner-outcome superiority;
- camera-based cube capture;
- support for every twisty puzzle.

Correct distinction:

`committed corpus evidence != universal proof`

`computational certificate != institutional certification`

---

# **27. Documents to Review**

- `README.md`
- `docs/QUICKSTART.md`
- `docs/FAQ.md`
- `docs/ARCHITECTURE.md`
- `docs/EVIDENCE_AND_VERIFICATION.md`
- `docs/CLAIM_BOUNDARY.md`
- `docs/specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt`
- `docs/specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt`
- `docs/specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt`
- `LICENSE`

---

# **28. Future GitHub Workflow**

A future GitHub Actions workflow can automate:

- browser-application SHA-256 verification;
- Python syntax validation;
- independent certificate-bundle verification;
- confirmation of `100/100` certificate passes;
- confirmation of catalogue, aggregate, and bundle roots;
- authority-field checks;
- failure on any unexpected identity or verification result.

This keeps the manually maintained checksum file simple while preserving a deeper automated verification path.

---

# **29. Final Acceptance Rule**

The committed Structural Cube v1.0.2 package should be accepted under its declared evidence boundary only when:

- the browser-application checksum matches;
- the independent Python verifier passes;
- `100/100` certificates pass;
- strict `W` descent passes;
- all routes finish solved with final `W = 0`;
- realization catalogue root matches;
- certificate aggregate root matches;
- certificate bundle root matches;
- producer and independent reports both pass;
- current-state reference-route access is `NONE`;
- current-state reference-distance access is `NONE`;
- fallback activation is `NONE`;
- tamper rejection is `PASS`;
- documentation matches the verified system;
- claim boundaries remain explicit.

Expected acceptance class:

`STRUCTURAL_CUBE_V1_0_2_PASS`

---

# **30. Closing Principle**

A matching browser checksum confirms the application file.

A passing independent verifier confirms the committed certificate bundle.

The complete verification chain is:

`browser application identity`

`-> legal source state`

`-> deterministic structural target`

`-> exact compiled action`

`-> exact replayed state`

`-> strict rank descent`

`-> continuous action chain`

`-> solved final state`

`-> portable certificate`

`-> matching aggregate and bundle roots`

**The cube moves locally. The evidence closes globally.**
