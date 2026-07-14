# 🧾 **Structural Cube — Evidence and Verification**

## **Structural Cube v1.0.2**

### **Reproduce the State • Reconstruct the Route • Verify the Certificate Chain**

`state identity -> structural action -> route certificate -> aggregate root -> bundle root -> version evidence`

---

# **1. Purpose**

This document explains how Structural Cube v1.0.2 records, connects, and verifies its computational evidence.

The system is designed so that a reviewer can move through four distinct questions:

1. **Is this the expected application and evidence package?**
2. **Does each certificate reconstruct the declared cube mathematics and route decision?**
3. **Do all 100 certificates agree with the committed manifest and bundle roots?**
4. **Do the browser producer and independent Python verifier reach the same result?**

The complete verification chain is:

`canonical source state`

↓

`legal-state validation`

↓

`structural rank`

↓

`observed graph`

↓

`deterministic kernel target`

↓

`graph-governed economy decision`

↓

`compiled face-turn sequence`

↓

`exact replay`

↓

`strict rank descent`

↓

`portable certificate`

↓

`certificate aggregate root`

↓

`certificate bundle root`

↓

`independent verification`

↓

`version manifest`

↓

`version report`

The browser application identity is checked separately through `verify/SHA256SUMS.txt`.

---

# **2. Evidence Principles**

Structural Cube follows six evidence principles.

## **2.1 Identity Is Explicit**

Each important subject has a declared SHA-256 identity.

Examples include:

- source states;
- observed graphs;
- kernel contracts;
- compiled actions;
- action chains;
- route certificates;
- certificate manifests;
- certificate bundles;
- version manifests;
- version reports.

---

## **2.2 Verification Is Reconstructive**

The independent verifier does not merely read a stored `PASS` value.

It reconstructs the declared:

- cube transformations;
- canonical state;
- cubie extraction;
- legality conditions;
- structural rank;
- observed graph;
- target pool;
- graph-aware ordering;
- economy decision;
- pure-kernel effect;
- compiled transition;
- action chain;
- certificate root;
- aggregate root;
- bundle root;
- final solved state.

---

## **2.3 Route Authority Is Declared**

The committed P100 evidence declares:

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

`fallback_activation = NONE`

The selected structural action is determined from the current canonical state, declared graph, rank, kernel contracts, isolated pure-kernel realization costs, and economy policy.

---

## **2.4 Every Completed Action Must Descend**

For every completed primary action:

`W(C_(i+1)) < W(C_i)`

Final acceptance also requires:

`W(C_final) = 0`

and:

`C_final = SOLVED`

---

## **2.5 Evidence Layers Have Separate Roles**

`browser producer != independent verifier`

`certificate root != aggregate root`

`aggregate root != bundle root`

`canonical object root != raw file SHA-256`

`identity check != complete mathematical verification`

---

## **2.6 Wall-Clock Time Is Not Authority**

Runtime may be measured, but it must not choose the route or verdict.

`wall_clock_authority = NONE`

---

# **3. Evidence Files**

The principal evidence files are stored under:

[`../outputs/`](../outputs/)

## **3.1 Certificate Bundle**

[`../outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json`](../outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json)

Contains:

- bundle profile;
- certificate profile;
- source corpus manifest;
- realization catalogue;
- certificate manifest;
- 100 portable route certificates;
- route and authority summaries;
- bundle root.

---

## **3.2 Certificate Manifest**

[`../outputs/Structural_Cube_v1_0_2_Certificate_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Certificate_Manifest.txt)

Contains the committed list of certificate identities.

Its exact file SHA-256 is also the certificate aggregate root.

---

## **3.3 Producer Verification Report**

[`../outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json`](../outputs/Structural_Cube_v1_0_2_Producer_Verification_Report.json)

Records the browser-side result, including:

- certificate count;
- pass and fail counts;
- source manifest hash;
- realization catalogue root;
- aggregate root;
- bundle root;
- browser bundle verification;
- tamper rejection;
- expected-root agreement;
- elapsed time.

---

## **3.4 Independent Verification Report**

[`../outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json`](../outputs/Structural_Cube_v1_0_2_Independent_Verification_Report.json)

Records the result produced by the standard-library Python verifier.

---

## **3.5 Version Manifest**

[`../outputs/Structural_Cube_v1_0_2_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Manifest.txt)

Binds the principal application and evidence artifacts by raw SHA-256.

It records identities for:

- HTML application;
- certificate bundle;
- certificate manifest;
- producer report;
- Python verifier;
- independent verification report.

---

## **3.6 Version Report**

[`../outputs/Structural_Cube_v1_0_2_Report.json`](../outputs/Structural_Cube_v1_0_2_Report.json)

Binds:

- version manifest root;
- producer verification result;
- independent verification result;
- authority declarations;
- artifact hashes;
- certificate identities;
- claim boundary;
- version report canonical root.

---

# **4. Verification Tool**

The independent verifier is:

[`../verify/Structural_Cube_v1_0_2_Verifier.py`](../verify/Structural_Cube_v1_0_2_Verifier.py)

Requirements:

- Python **3.9 or later**;
- Python standard library only;
- no third-party package;
- no network connection;
- no browser process required.

The verifier retains earlier D01 constants for compatibility.

The active v1.0.2 verification path uses:

`SCCERT-1-D02-EXP-A`

and verifies the graph-aware economy certificate bundle.

---

# **5. Fast Verification Command**

From the repository root:

```bash
python verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

On systems where the executable name is `python3`:

```bash
python3 verify/Structural_Cube_v1_0_2_Verifier.py outputs/Structural_Cube_v1_0_2_Certificate_Bundle.json --json-report Structural_Cube_v1_0_2_Local_Verification_Report.json
```

Expected principal result:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

Expected command-line exit codes are:

```text
0 = verification passed
1 = evidence verification failed
2 = command usage or execution error
```

Expected runtime is roughly one minute on a typical current desktop or laptop.

Runtime depends on:

- processor;
- storage;
- operating system;
- Python build;
- available memory.

Runtime is informational only.

`wall_clock_authority = NONE`

---

# **6. Recommended Verification Order**

## **Step 1 — Verify the Browser Application**

The manually maintained checksum file covers:

`demo/Structural_Cube_v1_0_2.html`

Expected value:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

### **Linux**

```bash
sha256sum -c verify/SHA256SUMS.txt
```

### **macOS**

```bash
shasum -a 256 -c verify/SHA256SUMS.txt
```

### **Windows**

```bat
certutil -hashfile "demo\Structural_Cube_v1_0_2.html" SHA256
```

### **Windows PowerShell**

```powershell
Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256
```

Interpretation:

`matching HTML checksum = matching browser-application identity`

The checksum confirms the exact browser HTML. It does not by itself verify the certificate bundle or the complete evidence chain.

---

## **Step 2 — Inspect the Version Report**

Confirm:

```text
status = PASS
acceptance_class = STRUCTURAL_CUBE_V1_0_2_PASS
certificate_count = 100
```

Confirm that both verification sections report:

```text
producer_verification.status = PASS
independent_verification.status = PASS
```

Confirm the authority declarations:

```text
reference_route_access = NONE
current_state_reference_distance_access = NONE
fallback_activation = NONE
wall_clock_authority = NONE
```

---

## **Step 3 — Verify the Manifest Root**

Expected version manifest root:

```text
74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2
```

The report must contain this value as:

`version_manifest_root`

The exact `Structural_Cube_v1_0_2_Manifest.txt` file SHA-256 must match the same value.

---

## **Step 4 — Verify the Principal Artifact Hashes**

The version manifest binds:

| Artifact | SHA-256 |
|---|---|
| `Structural_Cube_v1_0_2.html` | `f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab` |
| `Structural_Cube_v1_0_2_Certificate_Bundle.json` | `6dcc9788760f4e4d809016d86c8257854dc2f8fd5454fb6dcfb193f5a69e1895` |
| `Structural_Cube_v1_0_2_Certificate_Manifest.txt` | `d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472` |
| `Structural_Cube_v1_0_2_Producer_Verification_Report.json` | `81e7ed5ec93d44d002d3c765fc5259d45d4a300e8e13825e3c5eb48dc4290e75` |
| `Structural_Cube_v1_0_2_Verifier.py` | `f7ff56500fd3eae8ea2df0da8b6cdc9b16cc5c958298b60e580321f0f43517a3` |
| `Structural_Cube_v1_0_2_Independent_Verification_Report.json` | `c39468d4e133855deddbc20067f811a20a6cb9ae4c909e7ee405662129a67472` |

A checksum mismatch should be treated as a different artifact.

---

## **Step 5 — Run the Python Verifier**

Use the command in Section 5.

Preserve the generated local report when verification fails.

Do not replace a failing local result with the stored passing report.

---

## **Step 6 — Compare the Principal Roots**

Expected roots:

| Identity | SHA-256 |
|---|---|
| Source corpus manifest hash | `9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd` |
| Realization catalogue root | `e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4` |
| Certificate aggregate root | `d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472` |
| Certificate bundle root | `c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7` |
| Version manifest root | `74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2` |
| Version report canonical root | `eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225` |

The producer report, independent report, bundle, manifest, and version report must agree where the same root is declared.

---

# **7. What One SCCERT Certificate Verifies**

The active certificate profile is:

`SCCERT-1-D02-EXP-A`

One route certificate binds:

- certificate profile;
- source corpus identity;
- seed;
- scramble;
- source facelets;
- source-state SHA-256;
- source structural rank;
- ordered action list;
- graph-governed target decisions;
- kernel types and targets;
- realization catalogue references;
- compiled move sequences;
- source and target action states;
- rank before and after;
- strict-descent checks;
- action-chain links;
- final solved facelets;
- final `W = 0`;
- certificate root.

A certificate passes only when the verifier reconstructs the same declared result.

---

# **8. Action-Level Verification**

For every action, the verifier reconstructs:

## **8.1 Source State**

`source_facelets -> cubie extraction -> legal state`

## **8.2 Source Rank**

`source cubie state -> Phi(C_before) -> W(C_before)`

## **8.3 Graph View**

`source cubie state -> SCGS-derived graph view`

## **8.4 Candidate Pool**

`legal strict-descent targets -> graph scores -> canonical ordering`

## **8.5 Economy Decision**

`top 4 targets -> depth 4 continuation comparison -> selected target`

## **8.6 Kernel Contract**

`selected target -> exact pure-effect contract`

## **8.7 Compiled Transition**

`source state + compiled moves -> observed target state`

## **8.8 Exact Effect**

`observed target state = declared target state`

## **8.9 Strict Descent**

`W(C_after) < W(C_before)`

## **8.10 Chain Continuity**

`target_state_hash_i = source_state_hash_(i+1)`

A failure in any required field invalidates the route certificate.

---

# **9. Route-Level Verification**

A complete route passes only when:

- every action passes;
- action order is continuous;
- route moves equal the concatenated action moves;
- every action strictly descends;
- no fallback is activated;
- no current-state reference route is accessed;
- no current-state reference distance is accessed;
- the final state is solved;
- final `W = 0`;
- the certificate root reconstructs.

Compact relation:

`all actions valid + chain continuous + final solved -> route certificate valid`

---

# **10. Corpus-Level Verification**

The P100 bundle contains exactly:

`certificate_count = 100`

Expected corpus result:

```text
passed_certificate_count = 100
failed_certificate_count = 0
```

The corpus-level verifier also checks:

- certificate-root uniqueness;
- manifest count;
- manifest ordering;
- manifest aggregate root;
- bundle summary;
- authority declarations;
- source corpus identity;
- realization catalogue identity;
- bundle root;
- expected P100 pass count.

---

# **11. Producer Verification**

The browser producer report records:

```text
status = PASS
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
browser_bundle_verification = PASS
tamper_rejection = PASS
expected_root_match = PASS
```

The producer run also recorded:

```text
elapsed_ms = 52108
wall_clock_authority = NONE
```

The elapsed time is not part of route authority.

---

# **12. Independent Verification**

The Python report records:

```text
status = PASS
failure_count = 0
certificate_count = 100
passed_certificate_count = 100
failed_certificate_count = 0
```

It agrees with the producer on:

- realization catalogue root;
- certificate aggregate root;
- certificate bundle root;
- certificate count;
- pass count;
- fail count.

This agreement supports:

`browser producer result + independent Python reconstruction -> matching declared roots, counts, and verification status`

within the declared certificate profile and implementation scope.

It does not imply independent institutional endorsement.

---

# **13. Tamper-Rejection Model**

Structural Cube includes controlled tamper rejection.

A relevant mutation should cause at least one of the following to fail:

- source-state identity;
- graph identity;
- kernel target;
- compiled action;
- target-state identity;
- rank transition;
- action-chain continuity;
- certificate root;
- manifest aggregate root;
- bundle root;
- version artifact hash.

Recorded result:

`tamper_rejection = PASS`

---

# **14. Hash and Root Semantics**

Different identities bind different subjects.

## **14.1 Raw File SHA-256**

`SHA256(exact stored bytes)`

This changes when bytes change, including:

- line endings;
- whitespace;
- JSON indentation;
- field order;
- final newline.

---

## **14.2 Canonical Object Root**

`SHA256(canonical object excluding its own root field)`

This binds a declared logical object under its canonicalization rule.

---

## **14.3 Certificate Aggregate Root**

Binds the committed ordered certificate manifest.

---

## **14.4 Bundle Root**

Binds the canonical bundle object with its root field excluded.

---

## **14.5 Version Manifest Root**

Binds the exact version manifest bytes.

---

## **14.6 Version Report Canonical Root**

Binds the canonical version report object before its root field is added.

---

## **14.7 Browser-Application Checksum**

The exact browser application is identified by:

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

---

# **15. Checksum File**

The repository checksum file is:

[`../verify/SHA256SUMS.txt`](../verify/SHA256SUMS.txt)

## **Linux**

```bash
sha256sum -c verify/SHA256SUMS.txt
```

## **macOS**

```bash
shasum -a 256 -c verify/SHA256SUMS.txt
```

## **Windows PowerShell**

For an individual file:

```powershell
Get-FileHash ".\demo\Structural_Cube_v1_0_2.html" -Algorithm SHA256
```

Detailed verification instructions are provided in:

[`../verify/VERIFY.md`](../verify/VERIFY.md)

---

# **16. P100 Evidence Summary**

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
| Seeds improved against earlier full-graph selector | **100** |
| Equal seeds | **0** |
| Regressed seeds | **0** |
| Mean moves | **174.58** |
| Median moves | **172** |
| `p95` moves | **207** |
| Maximum moves | **223** |
| Total move reduction | **1,941** |

These values apply to the committed P100 corpus and declared earlier full-graph selector.

---

# **17. Authority Verification**

The committed bundle declares:

```text
interactive_authority = GRAPH_GOVERNED_ECONOMY_PRIMARY_AUTHORITY
route_authority = REFERENCE_FREE_STRUCTURAL_KERNEL_AUTHORITY
graph_authority = FULL_GRAPH
economy_policy = TOP_4_GRAPH_POOL_DEPTH_4
reference_route_access = NONE
current_state_reference_distance_access = NONE
fallback_activation = NONE
compiler_search_input = ISOLATED_PURE_KERNEL_EFFECT_ONLY
wall_clock_authority = NONE
```

A verifier must reject evidence that contradicts the declared authority fields.

---

# **18. Failure Interpretation**

## **18.1 Browser-Application Checksum Mismatch**

Possible causes:

- partial download;
- wrong application version;
- accidental HTML editing;
- line-ending or byte-level changes;
- verification of the wrong file.

Action:

- restore the intended browser application;
- recalculate its SHA-256;
- confirm the relative path;
- treat a mismatching file as a different browser artifact.

---

## **18.2 Manifest Hash Mismatch**

Possible causes:

- one bound artifact changed;
- the manifest itself changed;
- the wrong manifest was selected.

Action:

- compare each artifact SHA-256;
- restore the intended artifacts;
- regenerate dependent evidence only through the declared process.

---

## **18.3 Bundle Root Mismatch**

Possible causes:

- changed certificate;
- changed source corpus entry;
- changed realization catalogue entry;
- changed summary;
- changed authority declaration;
- changed JSON object.

Action:

- preserve the failing bundle;
- inspect the first verifier failure;
- compare against the committed bundle identity.

---

## **18.4 Certificate Failure**

Possible causes:

- illegal source state;
- rank mismatch;
- graph mismatch;
- target-selection mismatch;
- kernel-effect mismatch;
- compiled transition mismatch;
- non-descending action;
- broken chain;
- non-solved final state;
- certificate-root mismatch.

Action:

- preserve the failing certificate and report;
- inspect the earliest failing action;
- do not replace the failure with a stored PASS result.

---

## **18.5 Python Usage Error**

Check:

```bash
python --version
```

Required:

`Python >= 3.9`

Confirm that both the verifier and bundle paths are correct.

---

# **19. Evidence Preservation Rules**

Files under `outputs/` should be treated as generated evidence.

Do not:

- edit JSON formatting;
- reorder fields;
- convert line endings;
- add explanatory text;
- remove the final newline;
- change certificate order;
- rename internal profiles;
- modify hashes manually.

A formatting-only edit can change the raw file SHA-256.

When an evidence file changes legitimately, every dependent identity must be regenerated and reverified.

---

# **20. Reproduction Boundary**

The route-evidence reproducibility law is:

`same canonical source state + same resolver artifact + same profiles + same deterministic budgets -> same structural route evidence`

The certificate reproducibility law is:

`same committed source record + same artifacts + same profiles + same deterministic budgets -> same certificate`

The corpus-package reproducibility law is:

`same committed corpus + same artifacts + same profiles + same deterministic budgets -> same certificate aggregate root and bundle root`

The following may vary without changing the mathematical result:

- elapsed time;
- processor load;
- local output path;
- operating-system scheduling;
- browser rendering speed.

For the same declared route subject, the following must not vary:

- canonical source state;
- selected target;
- compiled action;
- action result;
- rank trajectory;
- route hash.

For the same declared certificate subject, the certificate root must not vary.

For the same declared corpus package, the certificate aggregate root and bundle root must not vary.

---

# **21. Verification Limits**

The supplied evidence does not establish:

- shortest-route optimality;
- competition-speed superiority;
- universal totality over every legal cube state;
- exhaustive defect detection;
- exhaustive mutation coverage;
- immunity from shared specification errors;
- independent institutional accreditation;
- measured learner-outcome superiority;
- support for every browser or twisty puzzle.

The evidence boundary is:

`COMMITTED_P100`

The version class is:

`EXPERIMENTAL`

The complete claim boundary is documented in:

[`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md)

---

# **22. Independent Review Checklist**

A reviewer should confirm:

- [ ] the browser-application SHA-256 matches `verify/SHA256SUMS.txt`;
- [ ] the version report status is `PASS`;
- [ ] the version manifest root matches;
- [ ] all bound artifact hashes match;
- [ ] the producer report status is `PASS`;
- [ ] the independent report status is `PASS`;
- [ ] certificate count is `100`;
- [ ] passed certificate count is `100`;
- [ ] failed certificate count is `0`;
- [ ] source corpus manifest hash matches;
- [ ] realization catalogue root matches;
- [ ] certificate aggregate root matches;
- [ ] certificate bundle root matches;
- [ ] reference-route access is `NONE`;
- [ ] current-state reference-distance access is `NONE`;
- [ ] fallback activation is `NONE`;
- [ ] wall-clock authority is `NONE`;
- [ ] the local Python verifier returns exit code `0`;
- [ ] the locally generated report records `status = PASS`.

---

# **23. Falsification Targets**

Useful challenge targets include:

- same canonical source state -> different route under identical profiles;
- graph-aware target -> independent reconstruction disagrees;
- accepted kernel -> exact effect mismatch;
- completed action -> `W_after >= W_before`;
- compiled algorithm -> target-state mismatch;
- broken action chain -> certificate accepted;
- changed certificate -> certificate root unchanged;
- changed certificate manifest -> aggregate root unchanged;
- changed bundle -> bundle root unchanged;
- presentation-only change -> certified structural target changes;
- current-state reference-route access -> authority PASS;
- current-state reference-distance access -> authority PASS;
- nonzero fallback -> authority PASS;
- non-solved final state -> certificate PASS;
- one failed certificate -> P100 PASS.

Primary falsification target:

`invalid structural transition -> valid SCCERT certificate`

A reproducible prohibited result should be preserved and used to:

- correct the implementation;
- strengthen the verifier;
- revise the specification;
- narrow the claim;
- regenerate affected evidence;
- increment the version.

---

# **24. Related Documentation**

- [README](../README.md)
- [Quickstart](QUICKSTART.md)
- [FAQ](FAQ.md)
- [Architecture](ARCHITECTURE.md)
- [Evidence and Verification](EVIDENCE_AND_VERIFICATION.md) (this document)
- [Claim Boundary](CLAIM_BOUNDARY.md)
- [Verification Procedure](../verify/VERIFY.md)
- [Resolver Architecture Specification](specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt)
- [Corpus and Telemetry Specification](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt)
- [SCGS-1-D02 Specification](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# **25. Final Verification Summary**

## **Identity**

`browser application SHA-256 -> browser-application identity`

`version report -> version manifest -> bound artifacts`

## **Mathematics**

`source state -> legality -> rank -> graph -> target -> exact transition -> strict descent`

## **Certificate**

`action chain -> route certificate -> certificate manifest -> aggregate root -> bundle root`

## **Independent Review**

`browser producer PASS + Python reconstruction PASS + matching roots`

## **Primary Principle**

**A solved final state alone is not enough.**

**The route must also preserve exact action identity, strict descent, authority isolation, and certificate continuity.**

`state -> evidence -> verification -> solved closure`
