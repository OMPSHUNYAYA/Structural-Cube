# ⚖️ **Claim Boundary — Structural Cube**

## **Structural Cube v1.0.2**

### **Documented claims must remain inside the demonstrated evidence boundary.**

`validated evidence scope -> permitted claim scope`

---

# **1. Purpose**

This document defines what **Structural Cube v1.0.2** demonstrates, what it does not demonstrate, and how its claims should be interpreted.

Structural Cube is an interactive browser application, structural resolver, certificate producer, and independently verifiable evidence system for a standard `3 x 3 x 3` cube.

Its principal chain is:

`canonical state -> structural rank -> observed graph -> kernel target -> compiled turns -> exact replay -> strict descent -> solved state`

Its evidence chain is:

`producer certificate -> certificate manifest -> bundle root -> independent verification -> version manifest -> version report`

The documented claim scope must not exceed the demonstrated evidence scope.

---

# **2. Demonstrated Scope**

For the committed `P100` corpus, Structural Cube v1.0.2 establishes:

- deterministic seeded starting states;
- canonical cube-state extraction;
- legal-state validation;
- graph-governed structural target selection;
- exact pure-kernel action contracts;
- deterministic compilation of selected kernel effects;
- exact replay of every completed action;
- strict structural-rank descent at every completed action boundary;
- solved closure for all `100` committed starting states;
- final `W = 0` for all `100` routes;
- zero current-state reference-route access;
- zero current-state reference-distance access;
- zero fallback activation;
- lower move count on every tested seed relative to the declared earlier full-graph selector;
- portable `SCCERT-1-D02-EXP-A` certificates;
- browser verification of all `100` certificates;
- independent Python verification of all `100` certificates;
- tamper rejection;
- reproducible SHA-256 identities for the committed evidence chain.

The core action law is:

`W(C_(i+1)) < W(C_i)`

The solved-state law is:

`W(C) = 0 iff C = SOLVED`

The authority boundary is:

`reference_route_access = NONE`

`current_state_reference_distance_access = NONE`

`fallback_activation = NONE`

---

# **3. Corpus Boundary**

The demonstrated corpus is:

`COMMITTED_P100`

with:

`seed_set = 1..100`

`scramble_length = 22`

`generator = xorshift32`

The corpus result applies to:

- the declared source states;
- Structural Cube v1.0.2;
- the declared graph profile;
- the declared economy policy;
- the declared kernel profiles;
- the declared compiler behavior;
- the declared certificate profile;
- the declared verification procedures.

The correct interpretation is:

`100 committed states passed under the declared version and profiles`

It is not:

`every legal cube state has been formally proved`

---

# **4. Route-Economy Boundary**

The graph-aware economy policy was compared with the declared earlier full-graph selector on the same `P100` starting states.

Measured result:

| Property | Result |
|---|---:|
| Seeds improved | **100** |
| Seeds equal | **0** |
| Seeds regressed | **0** |
| Earlier full-graph selector mean moves | **193.99** |
| Graph-aware economy mean moves | **174.58** |
| Graph-aware economy median moves | **172** |
| Graph-aware economy `p95` moves | **207** |
| Graph-aware economy maximum moves | **223** |
| Total move reduction | **1,941** |

This supports the claim:

> **The graph-aware economy policy used fewer move tokens on all 100 committed starting states than the declared earlier full-graph selector.**

It does not support the claim:

> **Structural Cube always produces the shortest possible cube solution.**

The route-economy boundary is:

`measured improvement on P100 != global route optimality`

---

# **5. Structural-Rank Boundary**

The declared rank is:

`W(C) = 24*rho + 4*(D_e + D_c) + tau_e + tau_c + F + T`

For the declared legal-state model:

`0 <= W(C) <= 126`

and:

`W(C) = 0 iff C = SOLVED`

Structural Cube uses `W` as a **termination rank**.

It does not claim that `W` is:

- the shortest face-turn distance;
- the shortest quarter-turn distance;
- God's number;
- a competition timing metric;
- a universal heuristic for every cube method;
- a replacement for established optimal-solution metrics.

Correct distinction:

`structural descent rank != shortest-route distance`

---

# **6. Graph Boundary**

The base observed obligation graph is serialized under:

`SCGS-1-D02`

The graph records declared structural evidence including:

- direction obligations;
- home obligations;
- direction-before-home dependencies;
- final-closure relations;
- edge cycle couplings;
- corner cycle couplings.

The graph is a **declared observed structural model**.

It is not claimed as:

- the only valid dependency graph for cube solving;
- the complete mathematical structure of every legal cube state;
- the unique representation required by all cube methods;
- a proof that all established solving systems are structurally inferior.

Correct distinction:

`declared graph authority != unique universal graph`

---

# **7. Kernel Boundary**

Structural Cube uses five declared pure-effect kernel families:

- `EF(i,j)`
- `CT(i,j)`
- `E3(i,j,k)`
- `C3(i,j,k)`
- `PB(i,j;k,l)`

For the committed evidence, the system verifies:

- deterministic target selection;
- exact pure-effect contracts;
- exact compiled realization;
- exact replayed target state;
- strict `W` descent.

This supports the claim:

`declared kernel target -> exact verified effect`

It does not establish:

- a separately reviewed universal completeness theorem for every legal cube state;
- that these five names define new classical cube transformations;
- that established commutators or conjugates have been mathematically replaced;
- that every future compiler implementation will preserve the same guarantees.

---

# **8. Compiler Boundary**

The compiler is permitted to search for a realization of an isolated pure effect.

Its declared authority input is:

`compiler_search_input = ISOLATED_PURE_KERNEL_EFFECT_ONLY`

It is not permitted to use a current-state reference route or current-state reference distance to choose the structural target.

The correct distinction is:

`search used to realize an already selected pure effect != reference solver used to choose the structural action`

The project does not claim:

- globally optimal kernel realizations;
- minimum move length for every compiled kernel;
- universal compilation speed;
- identical performance on all browsers and computers.

---

# **9. Certificate Boundary**

Structural Cube uses:

`SCCERT-1-D02-EXP-A`

A certificate binds declared evidence such as:

- source state;
- source-state hash;
- source rank;
- selected kernel target;
- graph-governed decision;
- compiled turns;
- exact replay;
- target state;
- target-state hash;
- rank transition;
- action-chain continuity;
- final solved state;
- certificate root.

A matching certificate establishes conformity to the declared certificate contract under the implemented verifier.

It does not mean:

- regulatory certification;
- standards-body accreditation;
- governmental approval;
- university endorsement;
- laboratory accreditation;
- third-party organizational approval;
- legal or commercial authorization.

Correct distinction:

`computational certificate != institutional certification`

---

# **10. Independent Verification Boundary**

The supplied Python verifier independently reconstructs:

- cube transformations;
- canonical states;
- cubie extraction;
- legality conditions;
- structural rank;
- graph views;
- target pools;
- economy decisions;
- pure-kernel effects;
- action transitions;
- action chains;
- certificate roots;
- aggregate root;
- bundle root;
- final solved states.

The independent verifier is a separate implementation path.

It is not claimed to be:

- independently authored by an unrelated organization;
- independently accredited;
- a formal proof assistant;
- a complete substitute for mathematical peer review;
- immune to shared specification errors.

Correct distinction:

`independent implementation path != independent institutional endorsement`

---

# **11. Determinism Boundary**

The intended reproducibility law is:

`same canonical state + same versioned profiles + same deterministic budgets -> same certified result`

Wall-clock time is not permitted to choose the route or verdict.

`wall_clock_authority = NONE`

Elapsed time may vary because of:

- processor;
- storage;
- browser;
- operating system;
- Python build;
- available memory.

Therefore:

`same certified result does not require identical elapsed time`

---

# **12. Learning Boundary**

Structural Cube presents:

- **Strategy**
- **Plan**
- **Move**

The learning design aims to derive guidance from the same evidence that supports the selected action.

This version demonstrates:

- evidence-linked guidance;
- separation of learner-facing and technical views;
- route-aware instruction;
- deterministic action context.

It does not establish:

- measured learning superiority;
- faster mastery than established teaching methods;
- universal suitability for every learner;
- formal educational accreditation;
- replacement of teachers, coaches, or established instruction.

Correct distinction:

`evidence-linked explanation != measured educational outcome`

---

# **13. Browser Boundary**

The application is a single HTML file and operates locally in a modern browser.

It does not currently provide:

- camera-based physical-cube recognition;
- automatic detection of sticker colours from a photograph;
- cloud synchronization;
- remote multi-user sessions;
- mobile-app-store packaging;
- support for every browser engine;
- automatic support for every twisty puzzle.

A browser security-origin notice related to `file:` does not by itself prove success or failure.

The relevant evidence is:

- application audit;
- route verification;
- strict descent;
- solved closure;
- certificate verification;
- file identities.

---

# **14. Security Boundary**

SHA-256 identities detect changes relative to the declared files and canonical subjects.

They do not by themselves prove:

- authorship;
- absence of malware;
- secure hosting;
- secure download transport;
- absence of all software defects;
- resistance to every attack;
- authenticity of evidence created outside the repository.

Correct distinction:

`matching hash = matching identity`

`matching hash != complete security proof`

---

# **15. Performance Boundary**

The current evidence includes route-length and execution-time observations.

The project does not claim:

- competition-speed performance;
- constant runtime on every computer;
- real-time guarantees;
- minimum memory use;
- optimal browser responsiveness;
- superiority over specialist cube engines;
- suitability for timing-sensitive competitive solving.

Runtime is operational telemetry.

`runtime -/-> mathematical verdict`

---

# **16. Scope Exclusions**

Structural Cube v1.0.2 does **not** establish:

- shortest-route optimality;
- competition-speed superiority;
- universal totality over every legal cube state;
- superiority over every established cube method;
- a new ownership claim over standard cube mathematics;
- exhaustive defect detection;
- exhaustive mutation coverage;
- immunity from shared implementation errors;
- universal compiler completeness;
- universal browser compatibility;
- measured learner-outcome superiority;
- camera-assisted physical-cube capture;
- support for every twisty puzzle;
- safety-critical qualification;
- regulatory or institutional certification;
- authentication of evidence originating outside the repository.

---

# **17. Appropriate Claims**

The following formulations are supported by the current evidence:

> **Structural Cube v1.0.2 solved all 100 committed P100 states with strict structural-rank descent, zero current-state reference-route access, zero current-state reference-distance access, and zero fallback activation.**

> **The graph-aware economy policy used fewer move tokens than the declared earlier full-graph selector on all 100 committed starting states.**

> **All 100 portable SCCERT certificates passed browser verification and independent Python verification.**

> **The browser and Python evidence agree on the realization catalogue root, certificate aggregate root, and certificate bundle root.**

> **The supplied evidence is deterministic under the declared states, profiles, policies, and verification procedures.**

---

# **18. Claims That Should Not Be Made**

The following formulations exceed the current evidence:

> **Structural Cube has formally proved every legal `3 x 3 x 3` cube state.**

> **Structural Cube always finds the shortest solution.**

> **Structural Cube is faster than every established cube solver.**

> **Structural Cube has replaced traditional cube mathematics.**

> **The five kernel families are universally proved complete by independent institutions.**

> **The certificate is equivalent to regulatory or standards certification.**

> **The Python verifier eliminates every possible shared error.**

> **Structural Cube has been proved to teach every learner more effectively.**

---

# **19. Evidence Identities**

Principal identities include:

| Identity | SHA-256 |
|---|---|
| Source corpus manifest hash | `9c19312da2dc9832630b78f26ff305c82e7b26e8d93257c1143de649e7404bdd` |
| Realization catalogue root | `e4171e3dbfe128041ac8498b97d5729764de9a52b23e58135f14676431d66ac4` |
| Certificate aggregate root | `d4487b83847f17d89e433d6bde768a7000602f918857f1b3040f8f47bc2bc472` |
| Certificate bundle root | `c9433aa2070d3a0f23b2df78b386c7e425dcb2382455befb72494793d6ca62a7` |
| Version manifest root | `74a6b3f92de7fe8e9d42ea5ee05ba7e54908ff2cdcbfcec31c3312f6d8e64ea2` |
| Version report canonical root | `eb911576bbfbb7dd8ce6f9293ba81f361bce112f30450ead9d7c69ea0fc69225` |
| Version report file SHA-256 | `10af21b336753f020dd911f5e60c4d0f87c891b3aedd2a1d9afd1f6fda457221` |

These identities bind declared files or canonical subjects.

The version report carries two distinct identities. The canonical root binds the canonical report object excluding its root field, while the file SHA-256 binds the exact stored bytes. Their difference is expected and illustrates:

`raw file SHA-256 != canonical object root`

These identities do not expand the claim boundary.

---

# **20. Broadening the Evidence**

Stronger future claims would require additional evidence such as:

- larger committed corpora;
- independently generated legal states;
- constructed edge cases;
- orientation-heavy states;
- long-cycle states;
- independent verifier implementations in other languages;
- formal review of rank properties;
- formal review of kernel completeness;
- broader mutation campaigns;
- independently designed falsification attempts;
- measured learner studies;
- physical-cube capture validation where introduced.

The governing rule remains:

`new claim -> new evidence -> new verification -> new version identity`

---

# **21. Falsification Boundary**

Reviewers are encouraged to attempt to produce:

- same canonical state -> different route under identical profiles;
- accepted action -> exact effect mismatch;
- completed action -> `W_after >= W_before`;
- selected target -> reconstructed graph selector disagreement;
- broken action chain -> accepted certificate;
- changed certificate -> unchanged root;
- changed certificate manifest -> unchanged aggregate root;
- changed bundle -> unchanged bundle root;
- presentation-only change -> certified structural target changes;
- current-state reference-route access -> authority PASS;
- current-state reference-distance access -> authority PASS;
- nonzero fallback -> authority PASS;
- non-solved final state -> certificate PASS;
- one failed certificate -> P100 summary PASS.

Primary falsification target:

`invalid structural transition -> valid SCCERT certificate`

A reproducible prohibited result should be used to:

- correct the implementation;
- strengthen the verifier;
- revise the specification;
- narrow the documented claim;
- replace affected evidence;
- increment the version.

---

# **22. Documentation**

- [README](../README.md)
- [Quickstart](QUICKSTART.md)
- [FAQ](FAQ.md)
- [Architecture](ARCHITECTURE.md)
- [Evidence and Verification](EVIDENCE_AND_VERIFICATION.md)
- [Verification Procedure](../verify/VERIFY.md)
- [Resolver Architecture Specification](specifications/Structural_Cube_Resolver_Architecture_and_Deployment_Direction_v1_0_2.txt)
- [Corpus and Telemetry Specification](specifications/Structural_Cube_Corpus_Telemetry_and_Resolver_Improvement_Specification_v1_0_2.txt)
- [SCGS-1-D02 Specification](specifications/SCGS-1-D02_Canonical_Graph_Serialization_Conformance_Specification_v0_2_5.txt)

---

# **23. Final Boundary Statement**

Structural Cube v1.0.2 demonstrates a deterministic, graph-governed, certificate-backed structural resolution process for the committed P100 corpus.

It establishes:

`declared state -> declared authority -> exact action -> strict descent -> solved closure -> independently verified evidence`

It does not establish:

`limited corpus result -> universal proof`

The governing rule is:

**Document only what the evidence directly supports.**

`validated evidence scope -> permitted claim scope`
