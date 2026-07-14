# 🧭 **Structural Cube — Architecture**

## **Dependency-Governed Resolution for a 3 x 3 x 3 Cube**

### **State • Structure • Action • Evidence • Descent**

**Structure proposes. Verification checks. Every completed action must descend.**

`canonical state -> structural rank -> observed graph -> kernel target -> compiled turns -> exact replay -> strict descent -> solved state`

---

# **1. Architectural Purpose**

Structural Cube explores whether a standard `3 x 3 x 3` cube can be resolved and taught through explicit structural authority rather than through a hidden route chosen first and explained afterward.

The central architectural question is:

> **Can the current cube state be converted into visible obligations, deterministic structural targets, exact action contracts, replayable transitions, and a solved route whose authority can be independently verified?**

The primary resolution chain is:

`canonical cube state`

↓

`legal-state validation`

↓

`structural rank`

↓

`observed obligation graph`

↓

`deterministic kernel targets`

↓

`graph-governed economy selection`

↓

`exact kernel compilation`

↓

`action replay`

↓

`strict rank descent`

↓

`graph rebuild`

↓

`solved cube`

The learning chain is:

`verified structural purpose -> Strategy -> Plan -> Move`

The evidence chain is:

`state identity -> graph identity -> action identity -> certificate identity -> aggregate root -> bundle root -> version manifest -> version report`

The architecture is designed so that:

- action selection is deterministic under the declared profiles;
- current-state reference routes do not select the primary action;
- exact action effects are replayed before acceptance;
- rank decreases at every completed action boundary;
- learner-facing messages remain tied to checked evidence;
- portable certificates can be verified outside the browser.

---

# **2. Architectural Position**

Structural Cube does not reject established cube mathematics.

It uses standard legal cube transformations and cubie structure.

Its architectural contribution lies in the authority relation:

`state -> structure -> action contract -> verification -> route -> lesson`

not:

`state -> route first -> structural story afterward`

A conventional route may still be mathematically valid.

Structural Cube asks whether the selected action can be justified through declared structural evidence before that action is carried out.

The architecture therefore separates:

- **what the current cube state is;**
- **what structural residue is present;**
- **which exact kernel target is admissible;**
- **which target is selected under the graph and economy policy;**
- **how that target is compiled into face turns;**
- **whether replay produces the exact expected state;**
- **whether the structural rank strictly decreases;**
- **how the same evidence becomes learner guidance;**
- **how an independent verifier reconstructs the result.**

---

# **3. Architectural Planes**

Structural Cube v1.0.2 is organized into nine logical planes.

## **3.1 Interaction Plane**

Handles:

- cube display;
- face and slice interaction;
- view rotation;
- Random and Manual starts;
- Auto Resolve;
- With Hint;
- Solve Myself;
- pause and resume;
- learner-facing Strategy, Plan, and Move;
- Technical view.

## **3.2 State and Legality Plane**

Handles:

- canonical facelet representation;
- cubie extraction;
- edge and corner permutations;
- edge and corner orientations;
- colour-count validation;
- centre-orientation validation;
- reachability invariants.

## **3.3 Structural Rank Plane**

Computes:

- permutation parity;
- cycle-distance terms;
- two-cycle counts;
- edge-flip residue;
- corner-twist residue;
- lexicographic potential `Phi`;
- integer rank `W`;
- rank hashes and transitions.

## **3.4 Observed Graph Plane**

Builds:

- direction obligations;
- home obligations;
- direction-before-home dependencies;
- final-closure relations;
- edge cycle couplings;
- corner cycle couplings;
- canonical SCGS bytes and graph hash.

## **3.5 Target and Kernel Plane**

Generates:

- exact `EF` targets;
- exact `CT` targets;
- exact `E3` targets;
- exact `C3` targets;
- exact `PB` targets;
- deterministic target ordering;
- predicted rank transitions.

## **3.6 Economy Selection Plane**

Applies:

- full graph scoring;
- a top-four admitted target pool;
- deterministic depth-four continuation comparison;
- declared compiled move-cost comparison;
- one primary target selection.

## **3.7 Compiler and Execution Plane**

Provides:

- isolated pure-effect compilation;
- realization-catalogue lookup and construction;
- exact face-turn algorithms;
- action replay;
- target-state comparison;
- strict-descent enforcement;
- graph rebuild.

## **3.8 Learning and Presentation Plane**

Transforms verified action evidence into:

- Strategy;
- Plan;
- Move;
- Technical details;
- highlights;
- sequence pacing.

## **3.9 Evidence and Verification Plane**

Produces and verifies:

- action certificates;
- route certificates;
- SCCERT portable certificates;
- certificate manifest;
- aggregate root;
- bundle root;
- producer report;
- independent Python report;
- version manifest;
- version report.

These planes are related but not interchangeable.

---

# **4. Core Architectural Invariants**

## **4.1 Legal-State Invariant**

The cubie state is:

`C = (P_e, O_e, P_c, O_c)`

A legal reachable state must satisfy:

`sum(O_e) mod 2 = 0`

`sum(O_c) mod 3 = 0`

`parity(P_e) = parity(P_c)`

An illegal state must not receive a valid structural route claim.

`illegal state -> no admitted resolution certificate`

---

## **4.2 Canonical-State Invariant**

The same physical state must enter the structural pipeline through one declared canonical representation.

`same physical state + same orientation convention -> same canonical state identity`

Canonicalization occurs before:

- legality validation;
- graph construction;
- rank calculation;
- target selection;
- hashing;
- certificate generation.

---

## **4.3 Strict-Descent Invariant**

Every completed primary action must satisfy:

`W(C_(i+1)) < W(C_i)`

An action that ends at equal or greater rank is not admitted as a completed primary action.

---

## **4.4 Solved-State Invariant**

For the declared legal-state model:

`W(C) = 0 iff C = SOLVED`

Final acceptance requires:

- solved canonical facelets;
- solved cubie state;
- final `W = 0`;
- complete action-chain continuity.

---

## **4.5 Exact-Effect Invariant**

A compiled action is admitted only when replay produces the declared pure effect and target state.

`compiled sequence + source state -> exact declared target state`

Approximate matching is not sufficient.

---

## **4.6 Reference-Isolation Invariant**

The primary structural selector must not read a current-state reference route or current-state reference distance.

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

---

## **4.7 Fallback Invariant**

For the committed v1.0.2 P100 evidence:

`fallback_activation = NONE`

A future implementation that activates fallback must declare and evidence it explicitly.

---

## **4.8 Determinism Invariant**

`same canonical state + same profiles + same deterministic budgets -> same certified result`

Elapsed time is not permitted to choose the result.

`wall_clock_authority = NONE`

---

## **4.9 Evidence-Chain Invariant**

Every accepted action must connect to the previous accepted action.

`target_state_hash_i = source_state_hash_(i+1)`

The same continuity rule applies to action-chain identities.

---

## **4.10 Anti-Disguise Invariant**

The lesson must follow the same evidence that governed action selection.

`selected structural action -> verified evidence -> learner explanation`

not:

`unrelated route -> explanation added afterward`

---

# **5. State Representation and Legality**

The browser application begins with a canonical 54-facelet representation.

The declared face order is:

`U, R, F, D, L, B`

The solved facelet state is:

`UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB`

Cubie extraction produces:

- edge permutation `P_e`;
- edge orientation `O_e`;
- corner permutation `P_c`;
- corner orientation `O_c`.

The legality layer checks:

- exact facelet length;
- accepted colour symbols;
- nine facelets of each colour;
- canonical centre signature;
- valid corner identities;
- valid edge identities;
- duplicate cubies;
- corner-twist parity;
- edge-flip parity;
- matching permutation parity.

The refusal law is:

`incomplete OR contradictory OR unreachable state -> no graph authority -> no certificate`

---

# **6. Structural Rank Architecture**

The rank plane converts the legal cubie state into a declared finite structural potential.

Components:

`rho = common permutation-parity flag`

`D_e = 12 - cycles(P_e)`

`D_c = 8 - cycles(P_c)`

`tau_e = number of edge 2-cycles`

`tau_c = number of corner 2-cycles`

`F = number of flipped edges`

`T = sum_i min(O_c[i], 3 - O_c[i])`

The lexicographic potential is:

`Phi(C) = (rho, D_e + D_c, tau_e + tau_c, F, T)`

The integer rank is:

`W(C) = 24*rho + 4*(D_e + D_c) + tau_e + tau_c + F + T`

Declared range:

`0 <= W(C) <= 126`

The rank is used for:

- target admission;
- target direction choice;
- strict-descent verification;
- finite-descent and action-count reasoning;
- route evidence;
- certificate reconstruction.

The rank is not used as a claim of shortest move distance.

`structural rank != optimal face-turn distance`

---

# **7. Observed Graph Architecture**

The observed graph is serialized under:

`SCGS-1-D02`

The graph contains three record classes:

- `NODES`
- `EDGES`
- `COUPLINGS`

## **7.1 Obligation Nodes**

Direction obligations represent unresolved orientation.

Examples:

`EDGE_DIRECTION:05:1`

`CORNER_DIRECTION:03:2`

Home obligations represent unresolved placement.

Examples:

`EDGE_HOME:05`

`CORNER_HOME:03`

---

## **7.2 Dependency Edges**

A dependency edge:

`a>b`

means:

`a is a prerequisite for b`

Example:

`EDGE_DIRECTION:05:1>EDGE_HOME:05`

The graph also records final-closure dependencies.

---

## **7.3 Cycle Couplings**

Permutation cycles are represented as canonical couplings.

Examples:

`EDGE_CYCLE:00-08-04-11`

`CORNER_CYCLE:00-04-07-03`

Traversal follows:

`position -> perm[position]`

---

## **7.4 Canonical Serialization**

SCGS fixes:

- ASCII encoding;
- identifier grammar;
- two-digit indices;
- section order;
- byte-wise record ordering;
- LF line endings;
- final LF;
- SHA-256 graph hashing;
- validation and refusal order.

The graph identity law is:

`same canonical state -> same canonical graph bytes -> same graph hash`

The graph is a declared observed model.

It is not claimed as the unique graph for every cube method.

---

# **8. Pure-Kernel Architecture**

The resolver operates through five exact pure-effect kernel families.

## **8.1 `EF(i,j)`**

Corrects a paired edge-orientation residue.

## **8.2 `CT(i,j)`**

Corrects a paired corner-twist residue.

## **8.3 `E3(i,j,k)`**

Applies an exact three-edge permutation cycle.

## **8.4 `C3(i,j,k)`**

Applies an exact three-corner permutation cycle.

## **8.5 `PB(i,j;k,l)`**

Bridges the shared edge-corner permutation parity.

Each kernel contract declares:

- kernel type;
- target cubies;
- orientation or permutation effect;
- legality preservation;
- expected target state;
- predicted rank;
- strict-descent requirement.

The kernel relation is:

`current structural residue -> deterministic pure-effect target -> exact verified transition`

---

# **9. Deterministic Target Selection**

Target selection follows the current structural residue.

The declared sequence includes:

1. shared odd permutation parity -> `PB`;
2. cycle of length at least three -> `E3` or `C3`;
3. paired two-cycle residue -> deterministic three-cycle target;
4. edge-orientation residue -> `EF`;
5. corner-twist residue -> `CT`.

For multiple legal target directions, the implementation uses the declared predicted-rank and graph rules to preserve deterministic ordering.

The target selector does not ask:

`which complete reference route solves the current cube?`

It asks:

`which exact structural residue can be closed by an admitted pure effect?`

---

# **10. Graph-Governed Economy Selection**

The v1.0.2 primary selector adds graph-governed route economy above the exact target layer.

The declared policy is:

`FULL_GRAPH -> TOP_4_TARGET_POOL -> DEPTH_4_LOOKAHEAD -> LOWEST_COMPILED_MOVE_COST`

Detailed sequence:

1. generate all exact strict-descent kernel targets;
2. calculate graph-aware target scores;
3. order candidates deterministically;
4. retain the strongest four admitted targets;
5. evaluate deterministic continuations to depth four;
6. calculate declared compiled move cost;
7. choose the lowest-cost admissible continuation;
8. break ties under the declared canonical ordering;
9. compile and replay the selected first action;
10. rebuild rank and graph.

Profiles:

`PRIMARY_AUTHORITY = GRAPH_GOVERNED_ECONOMY_PRIMARY_AUTHORITY`

`ROUTE_AUTHORITY = REFERENCE_FREE_STRUCTURAL_KERNEL_AUTHORITY`

`ECONOMY_POLICY = TOP_4_GRAPH_POOL_DEPTH_4`

The policy does not claim global shortest-route optimality.

---

# **11. Kernel Compiler Architecture**

The compiler turns an already selected pure-effect contract into legal face turns.

Its authority boundary is:

`compiler_search_input = ISOLATED_PURE_KERNEL_EFFECT_ONLY`

The compiler may use deterministic bounded search to realize the isolated effect.

It may not use a current-state reference solution to select the action.

The compiler pipeline is:

`pure-effect target`

↓

`canonical isolated target state`

↓

`deterministic realization search or catalogue retrieval`

↓

`compiled face-turn sequence`

↓

`exact isolated-effect verification`

↓

`compiler certificate`

The committed SCCERT bundle contains:

`realization_catalog_entries = 2292`

Realization catalogue root:

`e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4`

---

# **12. Action Execution Architecture**

One action contains:

- source state;
- source rank;
- source graph;
- selected target;
- selected kernel;
- compiled turn sequence;
- predicted target state;
- observed target state;
- target rank;
- action evidence;
- action-chain link.

Execution sequence:

`source state -> apply compiled turns -> observed state -> compare target -> recompute rank -> require strict descent -> accept action`

If any required comparison fails:

`action -> reject`

An accepted action becomes the source boundary for the next action.

---

# **13. Learning Architecture**

The learner-facing panel separates three levels.

## **13.1 Strategy**

Answers:

**What larger structural goal is being pursued?**

## **13.2 Plan**

Answers:

**Why does the next action belong to that goal?**

## **13.3 Move**

Answers:

**Which turn should be carried out now?**

The message pipeline is:

`action certificate -> supported structural purpose -> Strategy -> Plan -> Move`

The Technical tab remains separate so the main panel can stay readable.

The architecture does not require every user to read:

- rank components;
- graph identifiers;
- certificate roots;
- compiler traces.

Those remain available for inspection.

---

# **14. Interaction and Replanning Architecture**

The browser supports three principal user paths.

## **14.1 Auto Resolve**

The application prepares a complete route and executes it under the declared pacing controls.

## **14.2 With Hint**

The application exposes the next verified move while the user performs the turn.

## **14.3 Solve Myself**

The user explores without guided move instructions.

If the user makes a different legal move:

`new current state -> rebuild canonical state -> recompute rank -> rebuild graph -> select again`

The application does not require restoration of the earlier route.

---

# **15. Pause and Execution-State Architecture**

Pause preserves:

- current Strategy;
- current Plan;
- current Move;
- cube highlight;
- action position;
- sequence position.

Pause is operational.

`pause -> execution state`

It does not change:

- source state identity;
- selected action identity;
- certificate identity;
- mathematical verdict.

Similarly:

`user cancellation -> execution state, not solved-or-failed proof state`

---

# **16. Browser Worker Boundary**

Heavy route preparation is separated from the visible interaction loop through browser-worker execution.

The worker performs:

- target generation;
- graph scoring;
- economy comparison;
- kernel compilation;
- route construction;
- audit construction.

The interface remains responsible for:

- status;
- progress;
- animation;
- learner messages;
- pause;
- user interaction.

The architectural separation is:

`computation authority != presentation timing`

---

# **17. Evidence Architecture**

Structural Cube uses layered evidence.

## **17.1 State Evidence**

Binds:

- canonical facelets;
- cubie state;
- state SHA-256.

## **17.2 Graph Evidence**

Binds:

- SCGS canonical text;
- graph SHA-256.

## **17.3 Action Evidence**

Binds:

- source state;
- kernel target;
- compiled algorithm;
- observed state;
- rank transition;
- action-chain identity.

## **17.4 Route Evidence**

Binds:

- ordered action sequence;
- ordered move sequence;
- complete rank trajectory;
- final solved state;
- route identity.

## **17.5 Portable Certificate Evidence**

Uses:

`SCCERT-1-D02-EXP-A`

The committed bundle contains:

`certificate_count = 100`

## **17.6 Version Evidence**

The version manifest binds the browser application, certificate bundle, certificate manifest, producer verification report, independent verifier, and independent verification report by SHA-256.

The version report binds:

- version manifest root;
- producer result;
- independent result;
- authority declarations;
- artifact hashes;
- claim boundary.

---

# **18. Certificate Bundle Architecture**

The portable bundle contains:

- bundle profile;
- certificate profile;
- source corpus manifest;
- realization catalogue;
- certificate manifest;
- `100` route certificates;
- authority declarations;
- P100 summary;
- bundle root.

The root chain includes:

`certificate root`

↓

`certificate aggregate root`

↓

`bundle root`

Principal roots:

`CERTIFICATE_AGGREGATE_ROOT = d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472`

`CERTIFICATE_BUNDLE_ROOT = c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7`

---

# **19. Producer Verification Architecture**

The browser producer verifies:

- certificate construction;
- root reconstruction;
- expected-root agreement;
- bundle verification;
- tamper rejection;
- P100 pass counts.

Recorded producer result:

`status = PASS`

`certificate_count = 100`

`passed_certificate_count = 100`

`failed_certificate_count = 0`

`browser_bundle_verification = PASS`

`tamper_rejection = PASS`

`expected_root_match = PASS`

---

# **20. Independent Python Verification Architecture**

The independent verifier is:

[`../verify/Structural_Cube_v1_0_2_Verifier.py`](../verify/Structural_Cube_v1_0_2_Verifier.py)

It reconstructs:

- cube-turn permutations;
- canonical facelet states;
- cubie extraction;
- legality;
- structural rank;
- graph views;
- target pools;
- graph-aware ordering;
- depth-four economy decisions;
- pure-kernel effects;
- compiled action transitions;
- action chains;
- certificate roots;
- aggregate root;
- bundle root;
- final solved state.

The verifier does not call the browser resolver.

Its active v1.0.2 path verifies:

`SCCERT-1-D02-EXP-A`

Earlier D01 constants remain for compatibility.

Independent result:

`status = PASS`

`certificate_count = 100`

`passed_certificate_count = 100`

`failed_certificate_count = 0`

---

# **21. Version Identity Architecture**

The version manifest is:

[`../outputs/Structural_Cube_v1_0_2_Manifest.txt`](../outputs/Structural_Cube_v1_0_2_Manifest.txt)

It binds:

- HTML application;
- certificate bundle;
- certificate manifest;
- producer report;
- Python verifier;
- independent verification report.

Version manifest root:

`74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2`

The version report is:

[`../outputs/Structural_Cube_v1_0_2_Report.json`](../outputs/Structural_Cube_v1_0_2_Report.json)

Version report canonical root:

`eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225`

The manually maintained browser-application checksum is recorded in:

[`../verify/SHA256SUMS.txt`](../verify/SHA256SUMS.txt)

```text
f039ae4f14ac041b14bf04e79bf0a4d476bdcf86ab9fcb0c8d3c5fb1ae81e1ab  demo/Structural_Cube_v1_0_2.html
```

This checksum covers only the browser HTML. The version manifest, version report, certificate bundle, and independent verifier preserve the deeper evidence chain.

---

# **22. P100 Measurement Architecture**

The committed corpus uses:

`seed_set = 1..100`

`scramble_length = 22`

`generator = xorshift32`

The source corpus manifest hash is:

`9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd`

The P100 measurement boundary records:

- requested states;
- completed states;
- solved states;
- action counts;
- move counts;
- rank trajectories;
- strict-descent status;
- fallback status;
- reference-isolation status;
- route-economy comparisons;
- certificate identities;
- repeatability;
- tamper rejection.

---

# **23. P100 Architectural Result**

Route-economy rows compare against the declared earlier full-graph selector, whose P100 mean was `193.99` moves. The baseline and comparison method are documented in the [Corpus, Telemetry, and Resolver Improvement Specification](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt).

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
| Seeds improved against the declared earlier full-graph selector | **100** |
| Equal seeds | **0** |
| Regressed seeds | **0** |
| Earlier full-graph selector mean moves | **193.99** |
| Graph-aware economy mean moves | **174.58** |
| Median moves | **172** |
| `p95` moves | **207** |
| Maximum moves | **223** |
| Total move reduction | **1,941** |

The result supports the committed P100 claim boundary.

It does not establish universal totality or global route optimality.

---

# **24. Authority Firewall**

The architecture preserves distinct authority lanes.

## **24.1 State Lane**

Determines the legal canonical state.

## **24.2 Structural Lane**

Computes rank, graph, and exact kernel targets.

## **24.3 Economy Lane**

Chooses among admitted structural targets under the declared graph and cost policy.

## **24.4 Compiler Lane**

Realizes the already selected pure effect.

## **24.5 Verification Lane**

Replays the result and checks exact state and strict descent.

## **24.6 Measurement Lane**

Records counts, distributions, runtime, and evidence identities.

## **24.7 Presentation Lane**

Shows Strategy, Plan, Move, animation, and Technical details.

The non-interference laws include:

`presentation timing -/-> structural target`

`learner-facing explanation -/-> structural target`

`elapsed time -/-> structural target`

`measurement -/-> structural target`

`current-state reference route -/-> structural target`

`current-state reference distance -/-> structural target`

---

# **25. Trust Boundaries**

## **25.1 Input Boundary**

Only a canonical legal state enters structural resolution.

## **25.2 Graph Boundary**

SCGS graph bytes are derived from the legal canonical state.

## **25.3 Target Boundary**

Only exact strict-descent targets enter economy selection.

## **25.4 Compiler Boundary**

The compiler realizes the selected pure effect but does not choose the structural residue.

## **25.5 Action Boundary**

An action is accepted only after exact replay and strict descent.

## **25.6 Certificate Boundary**

A certificate is accepted only when all declared identities and transitions reconstruct.

## **25.7 Version Boundary**

The version manifest and report bind the supplied application and evidence files.

## **25.8 Repository Boundary**

Evidence generated outside the supplied package requires its own identity and provenance checks.

---

# **26. Failure Containment**

The architecture fails closed.

Examples:

- illegal state -> no route certificate;
- graph serialization failure -> no graph authority;
- no strict-descent target -> no accepted primary action;
- compiler mismatch -> action rejected;
- replay mismatch -> action rejected;
- `W_after >= W_before` -> action rejected;
- broken action chain -> certificate rejected;
- certificate-root mismatch -> certificate rejected;
- aggregate-root mismatch -> bundle rejected;
- bundle-root mismatch -> bundle rejected;
- non-solved final state -> certificate rejected;
- current-state reference-route access -> authority audit fails;
- current-state reference-distance access -> authority audit fails;
- fallback activation -> declared zero-fallback result fails.

Failure is not converted into a passing result.

---

# **27. Repository Architecture**

The maintained repository structure is documented in:

[Quickstart](QUICKSTART.md)

The Quickstart is the single source for repository layout, file locations, and startup paths.

---

# **28. Architectural Extension Directions**

## **28.1 Larger Corpora**

Add:

- wider seed ranges;
- constructed parity cases;
- long-cycle states;
- orientation-heavy states;
- independently generated legal states.

Each corpus requires its own identity and report.

---

## **28.2 Independent Verifiers**

Add separately authored implementations in other languages.

Each verifier should reconstruct:

- state;
- rank;
- graph;
- target selection;
- action effects;
- route chain;
- certificate roots.

---

## **28.3 Economy Improvements**

Potential directions include:

- larger target pools;
- deeper deterministic lookahead;
- stronger graph scoring;
- improved compiled-cost prediction;
- adjacent-action composition;
- certificate-preserving route compression.

Every change must preserve:

`exact effect + strict descent + reference isolation + deterministic replay`

---

## **28.4 Learning Evaluation**

Future learner studies may measure:

- comprehension;
- retention;
- error recovery;
- confidence;
- route explanation quality;
- difference between hint and no-hint modes.

These require evidence separate from computational verification.

---

## **28.5 Physical Cube Capture**

A future camera adapter would require:

- colour recognition;
- orientation normalization;
- uncertainty handling;
- illegal-state diagnosis;
- user correction;
- capture provenance.

The current browser application does not include this layer.

---

# **29. Claim Boundary**

Structural Cube v1.0.2 demonstrates the documented properties for the committed P100 corpus.

It does not claim:

- shortest-route optimality;
- competition-speed superiority;
- universal totality over every legal cube state;
- superiority over every established cube method;
- universal compiler completeness;
- exhaustive defect detection;
- independent institutional endorsement;
- measured learning superiority;
- support for every twisty puzzle.

The complete boundary is documented in:

[`CLAIM_BOUNDARY.md`](CLAIM_BOUNDARY.md)

---

# **30. Falsification Architecture**

High-value challenge targets include:

- same canonical state -> different route under identical profiles;
- selected target -> independent graph selector disagrees;
- accepted kernel -> exact effect mismatch;
- completed action -> `W_after >= W_before`;
- compiled algorithm -> target-state mismatch;
- broken action chain -> certificate accepted;
- changed certificate -> root unchanged;
- changed certificate manifest -> aggregate root unchanged;
- changed bundle -> bundle root unchanged;
- presentation-only change -> certified structural target changes;
- current-state reference-route access -> authority PASS;
- current-state reference-distance access -> authority PASS;
- fallback activation -> zero-fallback PASS;
- non-solved final state -> certificate PASS;
- one failed certificate -> P100 PASS.

Primary target:

`invalid structural transition -> valid SCCERT certificate`

A reproducible prohibited result should lead to:

- implementation correction;
- verifier strengthening;
- specification revision;
- narrower claims;
- new version identity.

---

# **31. Documentation**

Reader guides:

- [README](../README.md)
- [Quickstart](QUICKSTART.md)
- [FAQ](FAQ.md)
- [Architecture](ARCHITECTURE.md) (this document)
- [Architecture Diagram](Structural_Cube_Architecture_Diagram_v1_0_2.png)
- [Evidence and Verification](EVIDENCE_AND_VERIFICATION.md)
- [Claim Boundary](CLAIM_BOUNDARY.md)
- [Verification Procedure](../verify/VERIFY.md)

Technical specifications:

- [Resolver Architecture and Deployment Direction](specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt)
- [Corpus, Telemetry, and Resolver Improvement Specification](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt)
- [SCGS-1-D02 Canonical Graph Serialization Conformance Specification](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# **32. Architectural Summary**

The architecture answers nine questions.

### **Question 1 — What is the current cube state?**

Answered by canonical state extraction and legality validation.

### **Question 2 — What structural residue remains?**

Answered by rank and graph construction.

### **Question 3 — Which exact structural actions are admissible?**

Answered by the five pure-kernel target families.

### **Question 4 — Which admitted action should be selected?**

Answered by graph-governed economy comparison.

### **Question 5 — How is the action realized?**

Answered by the isolated pure-effect compiler.

### **Question 6 — Did the action do exactly what it declared?**

Answered by exact replay and target-state comparison.

### **Question 7 — Did the structure progress?**

Answered by strict `W` descent.

### **Question 8 — How is the action explained?**

Answered by Strategy, Plan, and Move derived from checked evidence.

### **Question 9 — Can another implementation verify the result?**

Answered by SCCERT and the independent Python verifier.

The complete architecture is:

`state -> legality -> rank -> graph -> target -> economy -> compiler -> replay -> descent -> lesson -> certificate`

---

# **33. Closing Principle**

A cube permits many legal turns.

Structural Cube requires more than legality.

It requires:

`declared target + exact effect + strict descent + replay identity`

The result is an architecture in which resolution, verification, and learning are derived from the same declared structural process.

**The cube moves locally. The structure closes globally.**
