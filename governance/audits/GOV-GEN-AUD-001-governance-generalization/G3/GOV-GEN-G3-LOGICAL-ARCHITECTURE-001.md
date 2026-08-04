---
document_id: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001
version: 0.1.0
program_id: GOV-GEN-AUD-001
phase: G3
contract: GOV-GEN-G3-CONTRACT-001/0.1.0
status: G3_READY_FOR_PROJECT_OWNER_REVIEW
authority: logical_layering_assessment_not_physical_architecture_selection
supersedes: null
---

# GOV-GEN-G3 — Logical Architecture and Layering Assessment

## 0. Scope statement

This document answers one question: how should reusable general-governance
capabilities be logically separated, related, queried, projected, and
bounded, *before* any physical extraction architecture is selected. It
organizes the 88 capabilities and 6 gaps already classified and accepted
under `GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0` into a proposed
logical layer model. It does not reclassify any capability, redispose any
gap, select a target physical architecture, decide kernel repository
ownership, create `general-governance` or any other repository, extract or
migrate any file, implement Delegated Operational Authority or
Provider-Neutral Governance, implement any recorded gap, or modify
`AGENTS.md`, `CLAUDE.md`, AET, CWG, or SVP.

## 1. Execution verification (contract §2.2)

```yaml
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
head_before: 2a11f63897301c3457272e60675224094e7d4100
worktree_status_before: clean
git_user: Brian Ferreira <sugar144@uoc.edu>
g2_controlling_result: GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0 (ACCEPTED_BY_PROJECT_OWNER, GOV-GEN-DECISION-006/0.1.0)
post_baseline_delta: GOV-GEN-G2-POST-BASELINE-DELTA-001/0.1.0 (G2_POST_BASELINE_DELTA_CUSTODIED, GOV-GEN-DECISION-007/0.1.0)
g3_prior_state: NOT_STARTED_NOT_AUTHORIZED (before this contract/execution)
```

Matches the contract's `expected_starting_commit`. No baseline drift.

## 2. Evidence base and method

Primary evidence: `GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md` (base, immutable)
read together with `GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1.md` (controlling
correction) for every capability's `generality`, `reuse_readiness`,
`coupling`, `duplication_status`, and `material_limitation`, and
`GOV-GEN-G2-POST-BASELINE-DELTA-001.md` for the carried-forward
unresolved-question narrowing (§8 below).

**Targeted lookup performed (per contract §2.1):** the accepted G1B
Governance Capability Map (`G1B/GOV-GEN-G1B-CAPABILITY-MAP-001.md`) was read
for each of the 88 capabilities' `obligation` and `realized_by` fields. G2's
own classification schema deliberately carries these by reference rather
than restating them (G2 contract §5), so allocating a capability to a
logical layer accurately — which depends on what the capability *is*, not
only how G2 classified it — required this one bounded, complete pass over
G1B's already-accepted `obligation`/`realized_by` fields for all 88 records.
This is a single named lookup over already-accepted evidence, not a
re-derivation of G1B's own findings or a reopening of G1A.

**Method.** A capability's logical layer is derived from its *structural
role* (what kind of thing it is: a binding rule, a configurable mechanism,
an optional module, a project instance, an executor binding, evidence, a
deterministic check, or an orientation surface) — not from its G2
`generality` value alone. §9.4 of the accepted G2 matrix already
established that generality-by-obligation-text is unreliable and
realization must be checked; the same discipline applies here one level up:
layer-by-generality-alone would conflate *how portable a capability's
content is* with *what functional responsibility it discharges*, which are
independent axes (see Principle P4, §3). Where role and generality point to
the same layer, allocation is direct. Where they diverge, the item is
flagged explicitly in §5 rather than forced.

## 3. Architectural principles

1. **P1 — Classify by realization, not by obligation text.** Extends G2's
   own finding (matrix §18 item 4): the same discipline that kept G2 from
   trusting generic-sounding obligations applies to layering. A capability's
   logical layer follows what it actually does, not how its stated purpose
   reads.

2. **P2 — Canonical completeness and model context surface are different
   concerns, and this repository already proves it independently.** The
   client-facing methodology's own `CLAUDE.md` invariant #2 states a
   four-layer precedence (evidence → canonical data → human documents →
   operational views) for an entirely different system (client
   requirements engineering). Governance and methodology arrived at
   structurally the same idea — separate the exhaustive canonical source
   from what gets read — independently. That convergence is evidence this
   principle is a property of how this codebase is actually organized, not
   a novel proposal invented for G3.

3. **P3 — Authority decisions and deterministic mechanics are different
   layers with different actors.** G2 §19 already found every `tools/`
   capability carries `authority_layer_observed: BOUNDED_DISCRETION`
   (deterministic work proceeds without a per-invocation Owner gate once
   its governing contract bounds it), while no capability records an
   *enforced* boundary between "inside authorized scope, proceed" and
   "outside it, ask." The logical model must keep the layer that runs
   without a gate distinct from the layer that decides the gate's bounds.

4. **P4 — Structural shape is more portable than instantiated content.**
   G2 §18 item 6 observed one packaging shape (`README.md` +
   `*-modes.yaml` + `protocols/README.md` + versioned prompt templates)
   shared by three `PROJECT_SPECIFIC` role-protocol capabilities
   (`CAP-NAV04-005/006/007`). Shape and content classify differently and
   must be allowed to sit in different layers even when they are realized
   by files in the same directory.

5. **P5 — Provider/executor binding is a thin, located adapter surface,
   not core semantics.** Of 88 capabilities, only 5 are `EXECUTOR_SPECIFIC`,
   concentrated in exactly two places (G2 §18 item 5): the 4 packaged
   skills' `agents/openai.yaml` bindings and one obsolete Codex-branded raw
   file. The normative core (`AGENTS.md`, the operating contract, the
   learning and prompt-custody contracts) is already
   `IMPLICIT_TOOL_AGNOSTIC`. The layer model must keep this adapter surface
   thin and located, not let it leak into core semantics.

6. **P6 — Evidence and its projections are different layers with different
   mutability.** `project-operating-contract.md`'s durable-truth ordering
   (immutable evidence → decisions → accepted registries → versioned
   methodology → generated views) and the `traceability` rule's precedence
   (evidence → canonical data → human documents → operational views, per
   root `CLAUDE.md`) both already draw this line for this repository. The
   logical model reuses it rather than inventing a new one.

7. **P7 — Project-specific and cross-project-configurable content are
   first-class layers, not residue.** 20 of 88 capabilities (23%) are
   `PROJECT_SPECIFIC` or partly so, and 16 (18%) are
   `CROSS_PROJECT_CONFIGURABLE`. A model that treats everything as either
   "universal core" or "trivial glue" would misrepresent over a third of
   the accepted evidence.

8. **P8 — Self-reuse inside this one repository is the strongest available
   evidence, and it already spans two of the eight proposed layers.** G2
   §18 item 1 found `CAP-NAV07-001` (run packaging) independently reapplied
   by `CAP-NAV08-012`, and `CAP-NAV08-001`'s charter+status pattern
   independently reapplied by `GOV-GEN-AUD-001`'s own scaffold — two
   internal programs generalizing the same mechanics with zero extraction.
   Both are configurable-mechanism (L1) capabilities; the layer model
   should expect this same evidence to recur as more capabilities mature
   toward `READY`.

## 4. Proposed logical layers

Eight layers. `MODEL_ENTRYPOINT` / `QUERY_ON_DEMAND` / `CANONICAL_MACHINE_SOURCE`
/ `HISTORICAL_EVIDENCE_ONLY` (§7) is a second, orthogonal axis — a layer is
not equivalent to one context-efficiency class; several layers contain
surfaces of more than one class.

```yaml
layer: L0 — Canonical Governance Semantics / Core
purpose: >-
  State the invariant, provider-neutral rules that define what governance
  IS for any adopting project: authority boundaries, status vocabulary, ID
  and versioned-correction grammar, evidence-immutability discipline.
owns: [governance/AGENTS.md (CAP-NAV01-011), methodology/project-operating-contract.md (CAP-NAV04-001), the raw-source custody invariant (CAP-NAV11-001)]
does_not_own: [project-specific clause content, specific phase/run identities, executor bindings, any single project's configuration values]
inputs: [Owner constitutional/ratification decisions to change core rules]
outputs: [normative constraints every other layer must not silently contradict]
authority_boundary: Owner-reserved to change; every layer and every agent session consumes it read-only
consumers: [all layers L1-L7]
portability: UNIVERSAL — smallest layer by count (3 capabilities) but the one every other layer's authority derives from
```

```yaml
layer: L1 — Configurable Cross-Project Policy
purpose: >-
  Host mechanisms that are shared across any adopting project but require
  per-project parameterization: run/program packaging templates, phase
  roadmap shape, projection wiring, checkpoint/routing policy, protocol
  contracting discipline.
owns: [run-packaging template (CAP-NAV07-001/002), program charter+status+checkpoint+routing+contracting pattern (CAP-NAV08-003/004/005/006/008/009/011/013), phase-roadmap and projection-wiring specs (CAP-NAV01-004/005), the kernel-design-closure loop mechanism (CAP-NAV04-004)]
does_not_own: [the literal per-project parameter values themselves (L3); the deterministic tools that execute against a config (L6); whether to adopt a given policy at all (L2 decides adoption, L1 defines the shared mechanism)]
inputs: [L0 rules, plus one project's configuration values]
outputs: [bound/instantiated policy consumed by L3 projections and L2 modules]
authority_boundary: Owner-reserved per adopting project to set values; the shared mechanism itself is common
consumers: [L2, L3, L6]
portability: mostly CROSS_PROJECT_CONFIGURABLE (14 of 14 capabilities here carry that generality) — the layer with the strongest doubly-proven internal self-reuse evidence (P8)
```

```yaml
layer: L2 — Optional Governance Modules/Extensions
purpose: >-
  Host self-contained, separately adoptable capability families that build
  on L0 but are not required for L0 to function: the learning system, the
  prompt-custody convention, the skill-custody convention, review-bundling.
owns: [learning triage rule (CAP-NAV03-005), prompt-custody convention (CAP-NAV05-001), skill-custody convention (CAP-NAV10-001), review-bundle-profile mechanism (CAP-NAV06-001)]
does_not_own: [core authority semantics (L0); the module's own accumulated evidence, which is L5; the module's deterministic tooling, which is L6]
inputs: [L0, an adoption decision]
outputs: [module-governed evidence records consumed by L5; module-specific query surfaces consumed by L6]
authority_boundary: adoption is an architecture/Owner-level decision; once adopted, the module's own internal rules apply without a further per-use gate
consumers: [L5, L6, L7]
portability: UNIVERSAL by generality (4 of 4), but adoption-optional by design — this is the layer G2's evaluation of Delegated Operational Authority (§19) and this document's boundary model (§6) both treat as "core vs optional"
```

```yaml
layer: L3 — Project-Specific Projections
purpose: >-
  Hold the concrete instantiation of L0/L1/L2 for one project: kernel
  clause text, role-protocol content, this repository's own phase/run
  identities and adoption plan.
owns: [ratified kernel clause set (CAP-NAV02-001), the three role-protocol content bodies (CAP-NAV04-005/006/007), S0A/S1 adoption plan (CAP-NAV01-009), the one review prompt bound to a specific identity (CAP-NAV05-003)]
does_not_own: [the packaging shape/template those role protocols share (L1/L2, per Principle P4); core authority rules (L0)]
inputs: [L0 + L1 + L2 + this project's own Owner decisions]
outputs: [the operative governance instance actually in force for this one project]
authority_boundary: fully project/Owner-controlled; nothing here binds any other adopting project
consumers: [executors (L4), evidence (L5), human reviewers]
portability: PROJECT_SPECIFIC by definition (6 capabilities) — smallest non-adapter layer; not reusable as-is, but the *layer boundary* around it is exactly what makes L0-L2 reusable
```

```yaml
layer: L4 — Provider/Executor Adapters
purpose: >-
  Bind L0-L3 governance semantics to one concrete AI provider or tool
  without becoming an independent source of normative content.
owns: [the 4 packaged skills' agents/openai.yaml bindings (CAP-NAV10-002/003/004/005)]
does_not_own: [any normative rule — an adapter must project L0-L3 content into one executor's mechanism, never originate governance semantics of its own]
inputs: [L0-L3 content the adapter must expose to its bound executor]
outputs: [executor-consumable projections (skill definitions, tool manifests)]
authority_boundary: adapter implementation is bounded-discretion/delegatable; adding a new adapter for a second executor is an architecture-level decision, not a routine one
consumers: [the one named executor at runtime]
portability: EXECUTOR_SPECIFIC by definition (4 capabilities; a 5th, CAP-NAV11-005, is an obsolete historical artifact allocated to L5, not an active adapter) — the smallest layer, concentrated in exactly two places per G2 §18 item 5, which is itself evidence that the *adapter pattern* (one core, N adapters) is the right shape rather than evidence the whole system is provider-locked
```

```yaml
layer: L5 — Canonical Evidence and Historical Custody
purpose: >-
  Hold the append-only, immutable record of what actually happened: runs,
  decisions, prompts, raw sources, failure/lesson records, review dossiers.
owns: [DECISION_LOG.md (CAP-NAV01-002), IMPORT_REPORT.md (CAP-NAV01-006), archive/README.md (CAP-NAV01-012), learning records and event narratives (CAP-NAV03-002/003), HP-PROMPT-*.md records (CAP-NAV05-002), review evidence (CAP-NAV06-002/003/006), all per-run evidence (CAP-NAV07-003/004/005/006), audit-program input manifest and Owner records (CAP-NAV08-002/007), the executed audit-pass run instance (CAP-NAV08-012), and all raw sources (CAP-NAV11-002/003/004/005)]
does_not_own: [current/derived state summaries (L7); queryable structured indexes over this evidence (L6, though L6 indexes point back here)]
inputs: [events from every other layer as they occur]
outputs: [durable evidence consumed by L6 for indexing and by humans/auditors directly]
authority_boundary: append-only; no rewrite; correction is a new versioned record (`<BASE>-R<N>`) — an L0 rule instantiated here
consumers: [L6 query/index, historical audits, dispute resolution]
portability: the largest layer (20 capabilities); its *mechanism* (append-only + versioned correction) is UNIVERSAL even where its *content* is project-specific (G2 §18 item 7) — mechanism and content again classify separately (Principle P4)
```

```yaml
layer: L6 — Deterministic Validation/Query Tooling
purpose: >-
  Mechanically derive facts from L3/L5 — schema validation, hashing,
  manifest checks, state replay, indexing — without deciding authority.
owns: [CURRENT_STATE.md's index role via ARTIFACT_REGISTRY.yaml (CAP-NAV01-003), SOURCE_CHECKSUMS.sha256 (CAP-NAV01-008), FAILURE_AND_LESSONS_INDEX.md (CAP-NAV03-001), the two deterministic-validation obligations (CAP-NAV06-004/005), the audit-program prompt index (CAP-NAV08-010), all 9 schemas (CAP-NAV09-001..009 minus the orientation README, i.e. CAP-NAV09-001..008), all 4 test capabilities (CAP-NAV12-001..004), and all 11 tools/_lib capabilities (CAP-NAV13-001..011)]
does_not_own: [authority decisions (Owner/L0); narrative interpretation; project-specific configuration values it must not embed (see §6 boundary model — this is exactly where G2 found CAP-NAV13-008 hardcoding literals that belong to L1/L3)]
inputs: [L3/L5 raw state, L1 configuration where properly externalized]
outputs: [deterministic PASS/FAIL, generated indexes/manifests feeding L7]
authority_boundary: BOUNDED_DISCRETION — runs without a per-invocation Owner gate once its own governing contract/schema bounds it (G2 §19, directly observed)
consumers: [L7 bounded projections, CI/agents, Owner review]
portability: the largest single layer (29 capabilities); the pure-infrastructure sublayer (`_lib`, the record-type schemas) is immediately READY (G2 §18 item 2); the project-bound sublayer (validators encoding this project's literal expectations) is NEEDS_MODEL_CHANGE and is the concrete site of G2 §21 UQ4
```

```yaml
layer: L7 — Bounded Model/Agent Context Projections
purpose: >-
  Provide task-relevant, size-bounded views an agent reads to orient
  without loading the full corpus.
owns: [CURRENT_STATE.md (CAP-NAV01-001), OPEN_IMPORT_QUESTIONS.md (CAP-NAV01-007), governance/README.md (CAP-NAV01-010), kernel/README.md (CAP-NAV02-002), lessons-by-category.md (CAP-NAV03-004), METHODOLOGY_BACKLOG.md (CAP-NAV04-002), methodology/loops orientation (CAP-NAV04-003), validation/README.md (CAP-NAV09-009)]
does_not_own: [canonical truth — on conflict with L3/L5 the higher (evidence) layer wins, never this one, per the repository's own traceability rule]
inputs: [L6 query output, L0 rules about what must be surfaced at session start]
outputs: [what an agent actually reads before or during a task]
authority_boundary: none — informational only
consumers: [agents and humans, at session start or task boundary]
portability: 8 capabilities; the entrypoint *pattern* (an `AGENTS.md`-style file read first) is itself UNIVERSAL even though several instances here (README orientation files) are content-light and easy to reproduce per adopting project
```

## 5. Capability allocation

### 5.1 Summary by layer

| Layer | Capabilities | Share |
|---|---|---|
| L0 — Core | 3 | 3% |
| L1 — Configurable policy | 14 | 16% |
| L2 — Optional modules | 4 | 5% |
| L3 — Project-specific projections | 6 | 7% |
| L4 — Provider/executor adapters | 4 | 5% |
| L5 — Canonical evidence | 20 | 23% |
| L6 — Deterministic tooling | 29 | 33% |
| L7 — Bounded projections | 8 | 9% |
| **Total** | **88** | **100%** |

Gap disposition by layer (6 gaps; a gap is allocated to the layer whose
responsibility it currently fails to discharge):

| Gap | Layer(s) | Note |
|---|---|---|
| GAP-001 | L3 / L5 boundary | ratified kernel text (L3 content) has no single L5 custody location — a custody problem, not a classification problem |
| GAP-002 | L6 | governance-validation-record schema is `PLANNED_NOT_IMPLEMENTED` |
| GAP-003 | L6 / L5 | the schema (L6) has zero populated evidence instances (L5) |
| GAP-004 | L4 | the core Provider-Neutral Governance gap — all 4 skills bind only one executor |
| GAP-005 | L6 | three prompt registries are unreconciled query indexes over the same L5 evidence |
| GAP-006 | Owner-authority boundary, adjacent to L1 | contracts exist for phases beyond the currently authorized one — a boundary-enforcement gap, not itself a layer-classification gap |

### 5.2 Cross-layer / ambiguous items (named explicitly, not forced)

- **CAP-NAV01-004/005** (`RUNTIME_PROJECTION_MAP.yaml`, `GOVERNANCE_MASTER_PLAN.md`): the *mechanism* (declaring which surfaces canonical state feeds; the phase-roadmap shape) is L1; `GOVERNANCE_MASTER_PLAN.md`'s *current content* names this project's own GOV-0..GOV-9 phase identities, which is L3. Both files sit at the L1/L3 seam.
- **CAP-NAV04-004** / `CAP-NAV09-004` (kernel-design-closure loop): the generic loop mechanism is L1; it is also, today, this project's one adopted closure-loop module, functioning as an L2 instance. Allocated to L1 primarily because the mechanism is what G2 classified `CROSS_PROJECT_CONFIGURABLE`.
- **CAP-NAV04-005/006/007** (role-protocol content): allocated to L3 (content), with their shared packaging shape cross-referenced to L1/L2 per Principle P4 — see §3 item 4 and G2 §18 item 6.
- **CAP-NAV06-004** (`validate_governance_state.py`'s obligation) and its realizing tool `CAP-NAV13-008`: the *obligation* (validate cross-surface consistency) is L6 by role; G2 already found the *realization* hardcodes this-project literals that should be L1/L3 configuration read by the L6 mechanism, not embedded in it. This is the single clearest concrete instance of the boundary model's third bullet (§6) and of G2 §21 UQ4.
- **CAP-NAV08-001** (program charter+status+decisions pattern): allocated to L1 as a configurable structural template; it is simultaneously the strongest self-reuse evidence in the whole map (Principle P8) because `GOV-GEN-AUD-001` itself reused it without extraction.
- **CAP-NAV11-005** (obsolete Codex-branded raw source): `EXECUTOR_SPECIFIC` by G2 generality, but allocated to L5 (historical evidence), not L4, because it is `OBSOLETE` and not an active adapter binding.
- **CAP-NAV07-001/CAP-NAV08-012**: the packaging template is L1; one specific executed instance of it (`CAP-NAV08-012`, an audit-pass run) is L5 evidence. Same shape/content split as Principle P4.

### 5.3 Full 88-capability annex

`G` = G2 generality (`U`niversal / `C`ross-project-configurable /
`P`roject-specific / `E`xecutor-specific). Rows are grouped by NAV family;
capability descriptions are not restated — see G1B/G2 by reference.

```text
NAV-01 (ROOT+archive)
  CAP-NAV01-001 U  L7   CURRENT_STATE.md — MODEL_ENTRYPOINT
  CAP-NAV01-002 U  L5   DECISION_LOG.md — append-only
  CAP-NAV01-003 U  L6   ARTIFACT_REGISTRY.yaml — queryable registry
  CAP-NAV01-004 C  L1   RUNTIME_PROJECTION_MAP.yaml — see §5.2
  CAP-NAV01-005 C  L1   GOVERNANCE_MASTER_PLAN.md — see §5.2
  CAP-NAV01-006 U  L5   IMPORT_REPORT.md
  CAP-NAV01-007 U  L7   OPEN_IMPORT_QUESTIONS.md — Owner working queue
  CAP-NAV01-008 U  L6   SOURCE_CHECKSUMS.sha256 — verification data
  CAP-NAV01-009 P  L3   S0A_S1_ADOPTION_PLAN.md
  CAP-NAV01-010 U  L7   governance/README.md
  CAP-NAV01-011 U  L0   governance/AGENTS.md — core
  CAP-NAV01-012 U  L5   archive/README.md — HISTORICAL_EVIDENCE_ONLY

NAV-02 (kernel)
  CAP-NAV02-001 P  L3   ratified kernel clause set (GAP-001)
  CAP-NAV02-002 U  L7   kernel/README.md

NAV-03 (learning)
  CAP-NAV03-001 U  L6   FAILURE_AND_LESSONS_INDEX.md — queryable index
  CAP-NAV03-002 U  L5   HP-FAIL-*.yaml records
  CAP-NAV03-003 U  L5   learning event narratives
  CAP-NAV03-004 U  L7   lessons-by-category.md — synthesized projection
  CAP-NAV03-005 U  L2   learning/README.md — module definition

NAV-04 (methodology)
  CAP-NAV04-001 U  L0   project-operating-contract.md — core
  CAP-NAV04-002 U  L7   METHODOLOGY_BACKLOG.md — non-authoritative
  CAP-NAV04-003 U  L7   methodology/loops orientation
  CAP-NAV04-004 C  L1   kernel-design-closure loop mechanism — see §5.2
  CAP-NAV04-005 P  L3   Enforcement Engineer role-protocol content
  CAP-NAV04-006 P  L3   Kernel Adversary role-protocol content
  CAP-NAV04-007 P  L3   Kernel Designer role-protocol content

NAV-05 (prompts)
  CAP-NAV05-001 U  L2   prompts/README.md — module definition
  CAP-NAV05-002 U  L5   HP-PROMPT-*.md records
  CAP-NAV05-003 P  L3   one review prompt bound to a specific identity

NAV-06 (reviews)
  CAP-NAV06-001 U  L2   review-bundle-profile mechanism
  CAP-NAV06-002 U  L5   implementation-report per review
  CAP-NAV06-003 U  L5   Owner decision dossier
  CAP-NAV06-004 C  L6   cross-surface validation obligation — see §5.2
  CAP-NAV06-005 C  L6   package-readiness validation obligation
  CAP-NAV06-006 P  L5   one-off architecture report

NAV-07 (runs)
  CAP-NAV07-001 C  L1   run-packaging template — proven doubly self-reused
  CAP-NAV07-002 C  L1   progressive input/output contract hardening
  CAP-NAV07-003 U  L5   Controller state-transition record
  CAP-NAV07-004 U  L5   independent-evaluation package custody
  CAP-NAV07-005 U  L5   execution-authorization record
  CAP-NAV07-006 U  L5   run-internal provenance evidence

NAV-08 (audits)
  CAP-NAV08-001 U  L1   charter+status pattern — see §5.2, strongest P8 evidence
  CAP-NAV08-002 U  L5   baseline input manifest
  CAP-NAV08-003 U  L1   artifact custody contract
  CAP-NAV08-004 U  L1   Owner-checkpoint scheduling — DOA-relevant primitive
  CAP-NAV08-005 U  L1   model/session-routing policy
  CAP-NAV08-006 U  L1   audit methodology/review protocol definition
  CAP-NAV08-007 U  L5   Owner decision records
  CAP-NAV08-008 U  L1   per-pass independent contracting rule (GAP-006-adjacent)
  CAP-NAV08-009 U  L1   independent-review execution package spec
  CAP-NAV08-010 U  L6   audit-program prompt index (GAP-005)
  CAP-NAV08-011 U  L1   per-pass prompt template
  CAP-NAV08-012 U  L5   one executed audit-pass run instance
  CAP-NAV08-013 U  L1   adversarial-review execution package spec

NAV-09 (schemas + validation)
  CAP-NAV09-001 U  L6   controller-transition schema
  CAP-NAV09-002 U  L6   failure/lesson schema
  CAP-NAV09-003 U  L6   governance-validation-record schema (GAP-002/003)
  CAP-NAV09-004 C  L6   kernel-design-closure schema — see §5.2
  CAP-NAV09-005 U  L6   review-bundle-config schema
  CAP-NAV09-006 P  L6   GOV-PROTOCOL-002 schema — schema role constant, content project-specific
  CAP-NAV09-007 P  L6   GOV-PROTOCOL-003 schema
  CAP-NAV09-008 P  L6   GOV-PROTOCOL-004 schema pair — correction discipline is L0-level (P4)
  CAP-NAV09-009 U  L7   validation/README.md

NAV-10 (skills)
  CAP-NAV10-001 U  L2   skill-custody convention — module definition
  CAP-NAV10-002 E  L4   agent-session-reviewer + openai.yaml binding
  CAP-NAV10-003 E  L4   formal-governance-run-preparer + binding
  CAP-NAV10-004 E  L4   governance-result-importer + binding
  CAP-NAV10-005 E  L4   governance-review-packager + binding

NAV-11 (sources)
  CAP-NAV11-001 U  L0   raw-source custody convention — operationalizes evidence-immutability
  CAP-NAV11-002 P  L5   kernel-intake checkpoint raw source (OBSOLETE)
  CAP-NAV11-003 P  L5   research-corpus raw source (OBSOLETE)
  CAP-NAV11-004 C  L5   bootstrap package zips (OBSOLETE)
  CAP-NAV11-005 E  L5   Codex-branded bootstrap prompt — see §5.2 (obsolete, not active L4)

NAV-12 (tests)
  CAP-NAV12-001 U  L6   Controller state-machine tests
  CAP-NAV12-002 C  L6   fixture corpora
  CAP-NAV12-003 C  L6   per-phase regression coverage
  CAP-NAV12-004 U  L6   bounded test-runner entrypoint

NAV-13 (tools)
  CAP-NAV13-001 U  L6   _lib shared library
  CAP-NAV13-002 U  L6   apply_loop_transition.py
  CAP-NAV13-003 U  L6   build_review_bundle.py
  CAP-NAV13-004 U  L6   manage_learning.py
  CAP-NAV13-005 P  L6   prepare enforcement-analysis run + correction
  CAP-NAV13-006 C  L6   validate audit methodology/scaffold
  CAP-NAV13-007 C  L6   validate closure loop
  CAP-NAV13-008 C  L6   validate_governance_state.py — see §5.2, G2 §21 UQ4
  CAP-NAV13-009 C  L6   validate numbered audit pass
  CAP-NAV13-010 U  L6   validate_prompts.py
  CAP-NAV13-011 U  L6   validate_run_package.py
```

Row count verified: 12+2+5+7+3+6+6+13+9+5+5+4+11 = 88. Layer totals verified:
L0=3, L1=14, L2=4, L3=6, L4=4, L5=20, L6=29, L7=8; sum=88.

## 6. Boundary model

- **Normative semantics and project configuration (L0 vs. L1/L3).** L0 owns
  exactly two documents (`AGENTS.md`, `project-operating-contract.md`) plus
  the raw-source custody invariant. Everything that reads as a rule but
  names this project's own values, phases, or run identities is L1 (shared
  mechanism) or L3 (this project's instance), never L0. `AGENTS.md`
  (`CAP-NAV01-011`) naming `project-operating-contract.md`
  (`CAP-NAV04-001`) as canonical operating semantics is the one place this
  split is currently `DELIBERATE_SEPARATION` but *unreconciled* — see G2
  §21 UQ2 and §8 below.

- **Core and optional modules (L0 vs. L2).** A module (learning,
  prompt-custody, skill-custody, review-bundling) may be entirely absent
  from a minimal adopting project without breaking L0. The test: does
  removing this capability family change what "governance" *means* (L0), or
  only remove one adoptable capability (L2)? Learning, prompt-custody, and
  skill-custody all pass this test as L2; `AGENTS.md` and the operating
  contract do not.

- **Governance logic and provider adapters (L0-L3 vs. L4).** An adapter
  (L4) must expose L0-L3 content to one executor; it must never originate a
  rule L0-L3 does not already state. `GAP-004` is the observed instance of
  this boundary being asymmetric today: L4 has exactly one adapter
  (`agents/openai.yaml`) and zero for a second executor, not a case of L4
  leaking normative content into itself.

- **Authority decisions and deterministic mechanics (Owner vs. L6).** Every
  `tools/` capability is `BOUNDED_DISCRETION` (G2 §19): it runs without a
  per-use Owner gate once its contract bounds it. The boundary is: L6 may
  decide *whether a check passes*, never *whether an action is
  authorized*. `CAP-NAV13-008`/`CAP-NAV06-004` currently blur this by
  embedding literal project facts inside an L6 tool rather than reading
  them from an L1/L3 configuration surface — a boundary violation G2 already
  flagged (§21 UQ4), not a new G3 finding.

- **Canonical evidence and generated/model-facing projections (L5 vs.
  L7, mediated by L6).** L7 must never be treated as authoritative over L5
  on conflict — this is the repository's own `traceability` rule, applied
  here rather than restated. `CURRENT_STATE.md` (L7) is explicitly
  documented elsewhere as "follows evidence; it never leads or fabricates
  it" (`project-operating-contract.md`), which is exactly this boundary in
  force today.

- **Repository governance and client/runtime methodology.** This entire
  L0-L7 model describes `governance/` only. The root `CLAUDE.md`
  invariants govern an unrelated system — the client-facing methodology
  runtime consumed by client sessions — with its own four-layer precedence
  (evidence → canonical data → human documents → operational views) that
  independently corroborates Principle P2 (§3) without being part of this
  model. Root `AGENTS.md` already states this firewall ("A
  repository-maintenance rule does not automatically become client
  methodology, and a client-runtime rule does not automatically authorize
  repository maintenance"); this document does not relax or restate that
  rule, only notes it bounds this layer model's scope.

## 7. Context-efficiency model

`canonical completeness != model context surface`: a layer being the
exhaustive, authoritative source of a fact (L5, and parts of L6) does not
mean every session should read it in full. The four classes below are
orthogonal to the L0-L7 layers — several layers contain surfaces of more
than one class.

```text
MODEL_ENTRYPOINT         — read at every governance session start, regardless of task
QUERY_ON_DEMAND           — consulted only when the task touches that specific surface
CANONICAL_MACHINE_SOURCE  — exhaustive source of truth for a deterministic tool; not read wholesale by an agent
HISTORICAL_EVIDENCE_ONLY  — immutable, consulted only for audit/dispute, never for routine orientation
```

| Class | Representative surfaces | Layer(s) |
|---|---|---|
| `MODEL_ENTRYPOINT` | `AGENTS.md`, `governance/AGENTS.md`, `CURRENT_STATE.md`, `governance/README.md`, program charter/status files | L0, L7 |
| `QUERY_ON_DEMAND` | `ARTIFACT_REGISTRY.yaml`, `FAILURE_AND_LESSONS_INDEX.md`, prompt registries, schemas (when validating a specific artifact type), `GOVERNANCE_MASTER_PLAN.md`/`RUNTIME_PROJECTION_MAP.yaml` (when the task concerns phase sequencing or projection wiring) | L1, L6 |
| `CANONICAL_MACHINE_SOURCE` | full `DECISION_LOG.md`/learning-record corpus, the 679-row G1A index, raw sources, the full G1B/G2 documents, `_lib`/tool internals (as opposed to their PASS/FAIL output) | L5, L6 |
| `HISTORICAL_EVIDENCE_ONLY` | `archive/README.md`, `OBSOLETE`-marked raw sources (`CAP-NAV11-002/003/004/005`), superseded run artifacts, resolved learning-event narratives | L5 |

**The required pipeline**, stated once and reused rather than re-derived
per layer:

```text
canonical storage (L5)
  → deterministic query/index (L6)
    → task-relevant bounded projection (L7)
      → model/agent consumption
```

L0 sits alongside this pipeline rather than inside it: it is read at both
the entrypoint stage (as `MODEL_ENTRYPOINT`) and consulted on demand when a
specific rule must be checked (`QUERY_ON_DEMAND`), because it is the
authority every other stage's output must not contradict. L5's exhaustive
corpus (the full 679-row G1A index; the complete `learning/records/`
directory) is deliberately never read in full by a session unless the task
*is* a historical audit — G1A itself remains at `~/Downloads/GOV-GEN-G1A-001/`
rather than duplicated into the repository precisely because its role is
`CANONICAL_MACHINE_SOURCE`, not `MODEL_ENTRYPOINT`. A future L6 query/index
tool (not built by G3 — §9 below) is what would let an agent ask "what does
G1A say about NAV-04" without reading all 679 rows; the *responsibility*
for that tool is placed here (L6), not its implementation.

## 8. G2 unresolved-question disposition

Taxonomy: `LOGICALLY_RESOLVED_BY_G3` / `NARROWED_BUT_OWNER_DECISION_REQUIRED`
/ `DEFER_TO_PHYSICAL_ARCHITECTURE` / `DEFER_TO_IMPLEMENTATION_DESIGN` /
`UNCHANGED`.

1. **UQ1 — consolidate the ratified kernel text (GAP-001) before
   extraction?** `DEFER_TO_PHYSICAL_ARCHITECTURE`. This document places
   kernel content at L3 with a custody gap toward L5 (§5.1 gap table), but
   *where* it is consolidated is exactly the repository-ownership/topology
   decision G3 is barred from making.

2. **UQ2 — collapse `AGENTS.md`/`project-operating-contract.md`, or
   formalize a stable two-layer model?** `LOGICALLY_RESOLVED_BY_G3`. Do not
   collapse. Formalize: both are L0, with `AGENTS.md` functioning as the
   `MODEL_ENTRYPOINT` binding surface and `project-operating-contract.md`
   as the deeper semantic specification it references — the split G1B/G2
   already observed as `DELIBERATE_SEPARATION` is exactly this shape, not
   an accidental duplication. Owner acceptance of this document as a whole
   is the outstanding step, not a further open architecture question.

3. **UQ3 — should the 4 skills gain a Claude Code binding, or is
   one-provider binding intentional?** `NARROWED_BUT_OWNER_DECISION_REQUIRED`.
   The logical shape is now explicit (§4 L4: one core, N adapters, adapters
   carry no normative content), but whether to build a second adapter is a
   product/Owner decision this document does not make.

4. **UQ4 — should hardcoded validators move to a declarative,
   data-driven model?** `LOGICALLY_RESOLVED_BY_G3` for the boundary
   principle: L6 mechanism must not embed L1/L3-owned literals (§6, fourth
   bullet); `CAP-NAV13-008` is the concrete violation. The mechanical
   rewrite itself is `DEFER_TO_IMPLEMENTATION_DESIGN` — this document does
   not design the declarative schema or touch the tool.

5. **UQ5 — what mechanism, if any, should formalize Delegated
   Operational Authority as an enforced boundary?** `NARROWED_BUT_OWNER_DECISION_REQUIRED`,
   consistent with the post-baseline delta's `STILL_REQUIRES_ARCHITECTURE_DECISION`.
   This document narrows further only by locating the candidate mechanism
   at L6 (a `BOUNDED_DISCRETION` gate consuming L0 authority rules, per
   Principle P3/§6 fourth bullet) — it does not design or implement one
   (forbidden by contract §4.3).

6. **UQ6 — unify the three prompt registries (GAP-005), and at what
   layer?** `NARROWED_BUT_OWNER_DECISION_REQUIRED`. All three are L6
   `QUERY_ON_DEMAND` indexes over the same L5 evidence class (§5.3:
   `CAP-NAV05-001`, `CAP-NAV08-010`, and the per-run embedded copies under
   `CAP-NAV07-001`'s pattern). Whether one shared L1 schema replaces all
   three, or each remains a project-level (L3) index reading a shared L1
   shape, is an architecture decision this document surfaces without
   choosing.

7. **UQ7 — does GAP-006 reflect a defect or a benign convenience, and
   should next-phase-only contracting gain enforcement?** Three components,
   each carried forward rather than re-resolved (this document does not
   redispose any G2 gap): next-phase-only contracting direction —
   `UNCHANGED` (already `NEW_EVIDENCE_NARROWS_DECISION_SPACE` per the
   post-baseline delta; this document adds only that its natural home is
   the same Owner-authority/L1 seam as UQ5, per §5.1's gap table);
   enforcement — `NARROWED_BUT_OWNER_DECISION_REQUIRED`, same disposition
   and same reasoning as UQ5; retrospective GAP-006 defect-vs-convenience
   classification — `UNCHANGED` (G2 §16's disposition stands; this document
   does not reopen it).

## 9. Candidate architecture

**Recommended: the eight-layer model in §4, adopted as the target logical
shape independent of where it physically lives.** Justification: it is
derived directly from, and fully accounts for, all 88 accepted G2
classifications and all 6 gap dispositions (§5); it reuses the repository's
own already-stated precedence and authority rules rather than inventing new
ones (Principles P2, P3, P6); and two of its layers (L1, L2) already have
direct internal proof of working self-reuse without extraction (Principle
P8) — a materially stronger evidentiary basis than a purely theoretical
layering would have.

**Alternative considered and rejected: collapse L1/L2/L3 into one
undifferentiated "core plus per-project glue."** This would simplify the
model from eight layers to roughly four, but Principle P7 (§3) shows 33 of
88 capabilities (38%) are `CROSS_PROJECT_CONFIGURABLE` or
`PROJECT_SPECIFIC`. Collapsing them would force either over-generalizing
project-specific content (kernel clause text, role-protocol bodies) into a
false "universal" bucket, or under-generalizing genuinely shared mechanisms
(run packaging, program scaffolding — Principle P8's own strongest
evidence) into "project-specific," losing the exact distinction the Owner
asked G3 to assess. Rejected as a materially worse fit to the accepted
evidence, not merely a stylistic alternative.

**Alternative considered and rejected: merge L7 into L6 (no separate
bounded-projection layer).** This would treat entrypoint files as just
another query target. It is rejected because it directly contradicts the
`canonical completeness != model context surface` principle this document
was explicitly asked to assess (§7): without a layer whose defining
property is "always read, deliberately small," either entrypoints bloat
toward exhaustiveness or orientation information hides behind
query-on-demand lookups a session may not know to make.

No other alternative in the evidence base represents a materially
different tradeoff; this document does not manufacture additional options
for their own sake (contract §4.3 forbids inflating scope).

## 10. Future physical-architecture inputs

This document does not decide any of the following; it states what a later,
separately authorized phase (G4/G5/GR, per the program's phase plan) must
resolve, using the L0-L7 shape as the frame those decisions should respect:

- **Repository ownership.** Whether L0-L2 (and the L6 infrastructure
  sublayer already `READY`) move to a new shared repository, stay in
  HugePlanning as a to-be-referenced source, or something else — not
  addressed here (forbidden by contract §4.3; this is exactly G2 §21 UQ1's
  domain).
- **Filesystem/package topology.** How the eight layers map to directories,
  packages, or repositories once ownership (above) is decided; this
  document's `owns`/`does_not_own` fields are logical responsibilities, not
  paths.
- **Extraction/migration boundaries.** Which specific L1/L2/L6 capabilities
  move first, and how `NEEDS_NORMALIZATION`/`NEEDS_MODEL_CHANGE` items
  (66% of the map, per G2 §21.2) are normalized before or during a move.
- **Adapter packaging (L4).** How a second executor adapter, if the Owner
  decides to build one (UQ3), is packaged and versioned relative to L0-L3
  — this document only states that it must not originate normative content.
- **Tooling implementation.** The actual declarative rewrite of hardcoded
  L6 validators (UQ4) and any future L6 query/index tool over L5 (§7) — both
  named here as responsibilities, neither designed or built by G3.
- **Historical evidence custody.** Where L5's exhaustive corpus (learning
  records, the G1A index, raw sources) is physically custodied once a
  target architecture exists, and how `HISTORICAL_EVIDENCE_ONLY` material
  is distinguished from actively queried L5 content at that scale.

## 11. Self-check against contract §6

| # | Required check | Result |
|---|---|---|
| 1 | Worktree clean before/after outside authorized paths; no Git command beyond §2.2's read-only set was run beyond publication (§8) | PASS — verified §1; only files under `G3/` and the minimum reconciliation surfaces named in the contract were written |
| 2 | All 88 accepted capabilities allocated to a layer or explicitly marked cross-layer/ambiguous | PASS — §5.3, 88/88; ambiguous items named in §5.2 |
| 3 | All 6 accepted gaps allocated or explicitly marked | PASS — §5.1 gap table, 6/6 |
| 4 | All eight required deliverable sections present | PASS — §3 (principles), §4 (layers), §5 (allocation), §6 (boundary model), §7 (context-efficiency model), §8 (unresolved-question disposition), §9 (candidate architecture), §10 (future physical-architecture inputs) |
| 5 | No target physical-architecture selection, kernel-ownership decision, or DOA/PNG/gap implementation exists anywhere in the output | PASS — §9/§10 explicitly defer all such decisions; §4/§6 evaluate DOA/PNG placement only, per contract §4.3 |
| 6 | Exactly one principal deliverable exists, unless a split was triggered and recorded | PASS — one deliverable; no split triggered |
| 7 | Hash manifest verifies | PASS — see `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.manifest.sha256`, generated after this file was finalized |
| 8 | Applicable repository validators pass | see completion disposition (§12) |

No split trigger was encountered: no genuinely independent decision,
authority, validation, acceptance, or material-risk boundary arose during
this execution that this contract does not already grant.

## 12. Completion disposition

```yaml
completion:
  status: G3_READY_FOR_PROJECT_OWNER_REVIEW
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  worktree_clean_outside_g3_and_reconciliation_surfaces: true
  capability_count_allocated: 88
  gap_count_allocated: 6
  layer_counts: {L0: 3, L1: 14, L2: 4, L3: 6, L4: 4, L5: 20, L6: 29, L7: 8}
  cross_layer_items_named: 7
  unresolved_question_dispositions:
    UQ1: DEFER_TO_PHYSICAL_ARCHITECTURE
    UQ2: LOGICALLY_RESOLVED_BY_G3
    UQ3: NARROWED_BUT_OWNER_DECISION_REQUIRED
    UQ4: LOGICALLY_RESOLVED_BY_G3_BOUNDARY_DEFER_MECHANICS_TO_IMPLEMENTATION_DESIGN
    UQ5: NARROWED_BUT_OWNER_DECISION_REQUIRED
    UQ6: NARROWED_BUT_OWNER_DECISION_REQUIRED
    UQ7: MIXED_UNCHANGED_AND_NARROWED_BUT_OWNER_DECISION_REQUIRED
  candidate_architecture_recommended: true
  alternatives_recorded: 2
  targeted_lookups_performed: 1
  self_check: PASS
  split_triggered: false
  next_authority_required: OWNER_REVIEW_AND_ACCEPTANCE_OF_G3
```

The executor does not accept this output. Owner acceptance, rejection, or a
request for bounded correction is a separate, subsequent act, exactly as
under `GOV-GEN-G2-CONTRACT-001/0.1.0` §11 and `GOV-GEN-G1B-CONTRACT-001/0.1.0`
§10. No target physical-architecture selection, kernel repository ownership
decision, `general-governance` or other repository creation, extraction or
migration, Delegated Operational Authority or Provider-Neutral Governance
implementation, gap implementation, capability reclassification, or gap
redisposition occurred or is implied by this document. No push has been
performed; the one bounded local commit authorized by this contract's §8
follows this deliverable's finalization.
