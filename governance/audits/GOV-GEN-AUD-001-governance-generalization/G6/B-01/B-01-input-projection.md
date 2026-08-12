{"frozen_revision": "8f08ad2ea47613d8d7dd93976f2563351bc2234e", "projection": "GOV-GEN-G6-B-01"}
--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md §4 ---
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


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md §6 ---
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


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md §7 ---
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


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md §8 ---
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


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md §10 ---
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


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md all ---
---
document_id: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1
title: HugePlanning Governance Generalization — G3 Logical Architecture — Bounded Owner-Review Correction 1
program_id: GOV-GEN-AUD-001
phase: G3
base_deliverable: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001/0.1.0
base_deliverable_sha256: be5c8ceb008e38579419b38f8813c9ac737f7c1842f2f5bd170667a6f1c5582b
correction_index: 1
version: 0.1.0
status: G3_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE
authority: BOUNDED_OWNER_REVIEW_CORRECTION_ONLY_NO_RECLASSIFICATION_NO_GAP_REDISPOSITION_NO_LAYER_REDESIGN_NO_ARCHITECTURE_SELECTION
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
source_prompt: HP-PROMPT-048/0.1.0
---

# GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1 — Bounded Owner-Review Correction

## 0. Scope and boundary statement

This document is a bounded prospective correction of the already Owner-reviewed
and immutable `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001/0.1.0` (§1), following the
convention established by `GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0`
(`GOV-GEN-DECISION-005/0.1.0`). It corrects exactly the six Owner-review
findings named in `HP-PROMPT-048/0.1.0`: a closed-enum violation in the
completion-disposition summary (§2), an unclarified current-vs-target
relationship for the context-efficiency model (§3), an ambiguous instruction-
surface reference (§4), a quantitative mis-statement (§5), a schema-count
mis-statement (§6), and an incomplete self-check evidence pointer (§7). It
performs no other change.

It does **not**: redo G3; change the eight-layer candidate architecture;
reallocate any of the 88 capabilities or reclassify any G2 capability;
redispose any of the 6 G2 gaps; reopen G2; select a target physical
architecture or decide kernel repository ownership; implement Delegated
Operational Authority, Provider-Neutral Governance, any provider/executor
adapter, or any query/projection tooling; define, scope, or authorize G4;
modify `AGENTS.md` or `CLAUDE.md`; or accept the G3 Logical Architecture
(base or corrected) on the Project Owner's behalf. The substantive layer
model, capability allocation, gap allocation, boundary model, and candidate-
architecture recommendation recorded in the base deliverable are unaffected
and are not re-derived here.

## 1. Base artifact identity and immutability

The base deliverable —
`governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md`,
SHA-256 `be5c8ceb008e38579419b38f8813c9ac737f7c1842f2f5bd170667a6f1c5582b`
(`GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.manifest.sha256`) — is treated as
historical execution evidence and is **not modified** by this correction. It
remains custodied unchanged. This file is the authoritative corrected layer
to be read together with the base deliverable; it does not supersede or
replace it, consistent with
`governance/methodology/project-operating-contract.md` ("Correct methodology
prospectively through new versions and append-only events. Supersede; do not
rewrite history to match a newer method.") and with
`.claude/rules/change-control.md` ("Approved artifacts are superseded, never
rewritten").

## 2. Finding 1 — Closed-enum UQ dispositions (UQ4, UQ7)

`GOV-GEN-G3-CONTRACT-001/0.1.0` §5 requires the G2 §21 unresolved-question
disposition to use "the five-value taxonomy in the orchestration prompt" —
`HP-PROMPT-047/0.1.0`'s taxonomy, restated in the base deliverable's own §8
opening line:

```text
LOGICALLY_RESOLVED_BY_G3
NARROWED_BUT_OWNER_DECISION_REQUIRED
DEFER_TO_PHYSICAL_ARCHITECTURE
DEFER_TO_IMPLEMENTATION_DESIGN
UNCHANGED
```

This is a closed enum: no sixth value, and no composite of two values joined
together, is a valid disposition.

**What is and is not defective.** The base deliverable's §8 body text for
items 4 and 7 already disposes each subcomponent using only valid enum
tokens — it is not defective and is not changed here. Only the §12
completion-disposition summary block collapses those already-valid
subcomponent tokens into two non-enum composite strings:

| Field | Base deliverable (§12, as written) | Contract enum member? |
|---|---|---|
| `UQ4` | `LOGICALLY_RESOLVED_BY_G3_BOUNDARY_DEFER_MECHANICS_TO_IMPLEMENTATION_DESIGN` | No — not one of the five values |
| `UQ7` | `MIXED_UNCHANGED_AND_NARROWED_BUT_OWNER_DECISION_REQUIRED` | No — not one of the five values |

**Corrected `§12` values**, using only contract-enum members:

```yaml
unresolved_question_dispositions:
  UQ4: LOGICALLY_RESOLVED_BY_G3
  UQ7: NARROWED_BUT_OWNER_DECISION_REQUIRED
```

**UQ4 — preserved subcomponent distinction** (base §8 item 4, unchanged,
quoted for traceability): "`LOGICALLY_RESOLVED_BY_G3` for the boundary
principle: L6 mechanism must not embed L1/L3-owned literals (§6, fourth
bullet); `CAP-NAV13-008` is the concrete violation. The mechanical rewrite
itself is `DEFER_TO_IMPLEMENTATION_DESIGN` — this document does not design
the declarative schema or touch the tool." The overall disposition is
`LOGICALLY_RESOLVED_BY_G3` because the base deliverable's own required
action (state and apply the boundary principle) is complete; the
`DEFER_TO_IMPLEMENTATION_DESIGN` element describes a *different*, not-yet-
started downstream task (the mechanical rewrite), not an unresolved part of
what G3 itself was asked to do. Collapsing both into one summary token lost
this distinction; restating it as prose in this section restores it without
altering the base document.

**UQ7 — preserved subcomponent distinction** (base §8 item 7, unchanged,
quoted for traceability): "Three components, each carried forward rather
than re-resolved (this document does not redispose any G2 gap): next-phase-
only contracting direction — `UNCHANGED` (...); enforcement —
`NARROWED_BUT_OWNER_DECISION_REQUIRED`, same disposition and same reasoning
as UQ5; retrospective GAP-006 defect-vs-convenience classification —
`UNCHANGED` (...)." The overall disposition is
`NARROWED_BUT_OWNER_DECISION_REQUIRED` because that is the least-resolved
of the three subcomponents and an Owner decision on enforcement remains the
governing open item; the two `UNCHANGED` subcomponents do not reduce the
overall item below that threshold. This mirrors how UQ5's single-component
disposition of `NARROWED_BUT_OWNER_DECISION_REQUIRED` is already used
elsewhere in §12 without composition.

No other `unresolved_question_dispositions` value (`UQ1`, `UQ2`, `UQ3`,
`UQ5`, `UQ6`) is defective; none is changed.

## 3. Finding 2 — Current vs. target context-efficiency model

`governance/AGENTS.md` (current, controlling) states: "Before material
governance work read `README.md`, `CURRENT_STATE.md`,
`GOVERNANCE_MASTER_PLAN.md`, the applicable methodology/role contract, and
the exact run, review, decision, or task inputs required for the current
result." This is an unconditional, currently binding read requirement.

The base deliverable's §7 context-efficiency table places
`GOVERNANCE_MASTER_PLAN.md` (with `RUNTIME_PROJECTION_MAP.yaml`) under
`QUERY_ON_DEMAND` — "consulted only when the task touches that specific
surface." Read without qualification, this appears to contradict
`governance/AGENTS.md`'s current unconditional mandate.

This correction clarifies, without altering §7's table or reallocating any
capability, that no contradiction is intended or in force:

1. **The context-efficiency classification (base §7) is a recommended
   *target logical consumption model*** — what an agent *should* need to
   read once the L0-L7 layering and a future query/index tool (base §7,
   "The required pipeline") exist — not a description of what any current
   surface currently requires or permits an agent to skip.
2. **Current repository instructions remain controlling until separately
   changed.** `governance/AGENTS.md`'s unconditional requirement to read
   `GOVERNANCE_MASTER_PLAN.md` before material governance work is unaffected
   by this document, by the base deliverable, and by G3 generally. This
   correction does not modify `governance/AGENTS.md` or `AGENTS.md`, per
   `HP-PROMPT-048/0.1.0`'s explicit prohibition and `GOV-GEN-G3-CONTRACT-001/0.1.0`
   §4.3.
3. **The mismatch itself is an identified implementation/normalization gap
   between a current, unconditionally-mandatory read and its target
   `QUERY_ON_DEMAND` classification** — a fact for a later, separately
   authorized phase to take up (in the same spirit as base §10's "Tooling
   implementation" item: the query/index tool that would make
   `QUERY_ON_DEMAND` actually sufficient in practice does not yet exist).
   This correction records the gap; it does not resolve it, schedule it, or
   authorize any work toward it.
4. **G3 acceptance alone does not modify current instruction behavior.**
   Project Owner acceptance of `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001/0.1.0`
   together with this correction accepts a target logical model as a
   *reference for future architecture work*; it is not, and is not to be
   read as, an instruction change to `governance/AGENTS.md`, which continues
   to govern what must actually be read in any current governance session
   until the Owner separately and explicitly changes it.

No change is made to base §7's table, to any layer's `owns`/`does_not_own`
content, or to any capability allocation.

## 4. Finding 3 — Disambiguating `governance/AGENTS.md` from root `AGENTS.md`

`CAP-NAV01-011` is, and has always been in this correction, exactly
`governance/AGENTS.md` — the base deliverable already states this precisely
at §4 (L0 `owns`: "`governance/AGENTS.md` (CAP-NAV01-011)") and at §5.3
("`CAP-NAV01-011 U L0 governance/AGENTS.md — core`"). Those two lines are
correct and unchanged.

The defect is that several other passages in the base deliverable use the
bare token `` `AGENTS.md` `` where context leaves it ambiguous whether
`governance/AGENTS.md` (`CAP-NAV01-011`, the L0-allocated file) or root
`` `AGENTS.md` `` (the repository-root file, distinct from `CAP-NAV01-011`
and not allocated to any G1B/G2 capability record) is meant — most visibly
in base §7's `MODEL_ENTRYPOINT` row, which lists `` `AGENTS.md` `` and
`` `governance/AGENTS.md` `` side by side without stating that they are two
different files serving two different scopes, and in base §6's L0
boundary-model bullet ("L0 owns exactly two documents (`AGENTS.md`,
`project-operating-contract.md`)"), where the bare `` `AGENTS.md` `` in fact
means `governance/AGENTS.md` (matching §4's `owns` list), not root
`AGENTS.md`.

**Disambiguation (clarifies wording only; changes no allocation, no layer,
no capability count):**

- **`governance/AGENTS.md` (`CAP-NAV01-011`)** is the L0-allocated capability:
  the repository-scoped realization/binding surface for `GOV-GEN-AUD-001`'s
  governance program specifically, read together with
  `methodology/project-operating-contract.md` (`CAP-NAV04-001`, also L0).
  Base §6's L0 bullet's bare `` `AGENTS.md` `` reference, and base §7's
  `MODEL_ENTRYPOINT` row entry `` `governance/AGENTS.md` ``, both refer to
  this file.
- **Root `AGENTS.md`** (repository root, distinct path) is *not*
  `CAP-NAV01-011` and is not part of L0's `owns` list (base §4). It is
  repository-wide post-baseline instruction evidence — the subject of the
  Post-G2 Instruction Delta Assessment
  (`GOV-GEN-G2-POST-BASELINE-DELTA-001/0.1.0`, `GOV-GEN-DECISION-007/0.1.0`)
  — and, independently of any G2/G3 capability allocation, a current model
  entrypoint an agent session reads at repository-session start. Base §7's
  `MODEL_ENTRYPOINT` row entry `` `AGENTS.md` `` (bare, listed first, before
  `` `governance/AGENTS.md` ``) refers to this separate file. Both are
  `MODEL_ENTRYPOINT`-class surfaces; neither collapses into the other, and
  root `AGENTS.md` carries no L0 `owns` allocation under this document's
  logical model, which is scoped to `governance/` (base §6, last bullet:
  "This entire L0-L7 model describes `governance/` only").
- **L0 semantic framing, refined.** L0 (base §4) owns the *semantic
  responsibility* for invariant, provider-neutral governance rules — not a
  specific file as such. `governance/AGENTS.md` and
  `project-operating-contract.md` are that responsibility's current
  *realization/binding surfaces* for `GOV-GEN-AUD-001`'s own governance
  scope; root `AGENTS.md` is a separate, repository-wide realization surface
  that this L0-L7 model, being scoped to `governance/`, does not allocate.
  L0's `owns` count is unchanged at 3 capabilities
  (`governance/AGENTS.md`, `project-operating-contract.md`, the raw-source
  custody invariant); no capability is added, removed, or reallocated by
  this clarification.

Where UQ2 (base §8 item 2) discusses "both are L0, with `AGENTS.md`
functioning as the `MODEL_ENTRYPOINT` binding surface" — that `AGENTS.md`
reference means `governance/AGENTS.md`, consistent with UQ2's subject (the
`governance/AGENTS.md` / `project-operating-contract.md` split), not root
`AGENTS.md`. UQ2's disposition (`LOGICALLY_RESOLVED_BY_G3`, unaffected by
§2 above) is unchanged by this clarification.

## 5. Finding 4 — Corrected quantitative statement (P7 collapse alternative, base §9)

Base §9, "Alternative considered and rejected: collapse L1/L2/L3...",
states: "Principle P7 (§3) shows 33 of 88 capabilities (38%) are
`CROSS_PROJECT_CONFIGURABLE` or `PROJECT_SPECIFIC`." No combination of
figures in the accepted G2 record produces 33 or 38%.

The accepted `GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0` generality counts
(§18, and confirmed by `01-program-status.yaml`'s `G2.generality_counts` and
by a direct count of the base matrix's own `generality:` fields) are:

```text
UNIVERSAL: 54
CROSS_PROJECT_CONFIGURABLE: 16
PROJECT_SPECIFIC: 13
EXECUTOR_SPECIFIC: 5
UNRESOLVED: 0
```

`16 + 13 = 29` of `88`, which is `29/88 = 32.95...%`, approximately `33%` —
not `33` of `88` (`38%`).

**Corrected statement**, preserving the architectural argument this figure
supports: "Principle P7 (§3) and the accepted G2 generality counts together
show 16 `CROSS_PROJECT_CONFIGURABLE` plus 13 `PROJECT_SPECIFIC` capabilities
— 29 of 88, approximately 33% — that are neither `UNIVERSAL` nor
`EXECUTOR_SPECIFIC`. Collapsing L1/L2/L3 would force either
over-generalizing project-specific content (kernel clause text, role-
protocol bodies) into a false 'universal' bucket, or under-generalizing
genuinely shared mechanisms (run packaging, program scaffolding —
Principle P8's own strongest evidence) into 'project-specific,' losing the
exact distinction the Owner asked G3 to assess. Rejected as a materially
worse fit to the accepted evidence, not merely a stylistic alternative." The
qualifier "over a third" in the base text is replaced by "approximately a
third" / "close to a third," since 29/88 rounds to a third rather than
exceeding it; the rejection argument itself is unaffected by this change,
because the argument's force comes from the category being non-trivial
(neither near-zero nor the whole set), which holds at 33% exactly as it did
at the erroneous 38%.

This finding is scoped exactly to the base §9 sentence identified above.
Base §3's Principle P7 sentence ("20 of 88 capabilities (23%) are
`PROJECT_SPECIFIC` or partly so, and 16 (18%) are
`CROSS_PROJECT_CONFIGURABLE`") states a different, broader metric — capability
records that are `PROJECT_SPECIFIC` *or partly so* (a superset including
ambiguous/partial items), not the strict generality-tag count used above —
and was not identified as defective by Owner review; it is not touched by
this correction, consistent with the boundary against reallocating capability
counts except where strictly required by an identified contradiction.

## 6. Finding 5 — Corrected schema count (base §4, L6 layer)

Base §4's L6 layer `owns` list states: "all 9 schemas
(`CAP-NAV09-001..009` minus the orientation README, i.e.
`CAP-NAV09-001..008`)". The parenthetical already correctly excludes the
orientation README and correctly cites the range `CAP-NAV09-001..008`, but
the leading phrase "all 9 schemas" is factually wrong: only 8 of the 9
`CAP-NAV09-*` records are schemas (`CAP-NAV09-001..008`); the ninth,
`CAP-NAV09-009`, is `validation/README.md`, an orientation document, not a
schema, and is correctly allocated to L7 (base §4 L7 `owns`; base §5.3:
"`CAP-NAV09-009 U L7 validation/README.md`").

**Corrected phrase:** "8 schema capabilities (`CAP-NAV09-001..008`)" in
place of "all 9 schemas (`CAP-NAV09-001..009` minus the orientation README,
i.e. `CAP-NAV09-001..008`)". `CAP-NAV09-009` remains, unchanged, the
orientation README allocated to L7.

This is a wording correction only. It changes no count: L6's total of 29
capabilities already counted exactly 8 `CAP-NAV09-*` schema records (not 9),
and L7's total of 8 capabilities already included `CAP-NAV09-009`. Base
§5.1's summary table (`L6: 29`, `L7: 8`) and base §12's `layer_counts` are
unaffected and unchanged.

## 7. Finding 6 — Check-8 validator evidence, honestly recorded

Base §11's self-check table, check #8 ("Applicable repository governance
validators ... pass"), reads: "see completion disposition (§12)." Base §12,
however, records only `self_check: PASS` — a summary conclusion, not the
underlying command output. `GOV-GEN-DECISION-008/0.1.0`'s own
`reviewed_evidence.self_check_result` similarly records only `'PASS (G3
contract §6, checks 1-8)'`. Neither the base deliverable, the decision
record, `governance/DECISION_LOG.md`'s `GOV-DEC-034` entry, nor the G3
commit message (`d9cc0e74584e1c8c7aa83894621f3d9ede77bdea`) contains a
durable, concrete execution-time record — command text and output — for
check #8's validator run at original G3 execution time. This correction
does **not** fabricate or retrospectively construct such a record. Exactly
as with G2's own check-8 finding (`GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0`
§3.2), the gap is recorded here as what it is: a historical evidence-custody
limitation in the original G3 execution's recorded self-check, not a defect
introduced by this correction.

**Owner-review revalidation evidence** (not a reconstruction of what the
original G3 executor ran; a fresh, independent revalidation performed
during this correction session against the exact G3 base-deliverable
candidate commit, with the working tree unchanged before and after,
confirmed clean both before this correction's writes began and immediately
before this command sequence ran):

```text
candidate: d9cc0e74584e1c8c7aa83894621f3d9ede77bdea

python governance/tools/validate_prompts.py
→ {"lineages":42,"prompts":44,"valid":true}
→ exit status 0

python governance/tools/validate_governance_state.py
→ {"diagnostics":[],"result":"VALID"}
→ exit status 0

sha256sum -c governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.manifest.sha256
→ GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md: OK
→ exit status 0
```

Note: `validate_prompts.py`'s counts (`42` lineages, `44` prompts) reflect
the full prompt corpus as of this correction session — including
`HP-PROMPT-048` itself once written — not the corpus as it stood at original
G3 execution time; this is expected and is not evidence of drift in the G3
deliverable itself, which the accompanying manifest check independently
confirms is byte-identical to its original hash.

**This correction's own validation evidence** is recorded separately in §9
below, run against the fully corrected working tree at commit time, distinct
from the Owner-review revalidation above.

Neither evidence set is presented as, or substitutes for, a contemporaneous
record of what the original G3 execution ran for check 8. Both are recorded
as what they honestly are: later, independent revalidations, of the base
candidate and of this correction respectively.

## 8. What this correction changes outside G3/

Minimum current-state reconciliation only, consistent with
`governance/AGENTS.md`'s completion-reconciliation requirement and the
convention already used by `GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0`
§4:

- `governance/audits/GOV-GEN-AUD-001-governance-generalization/01-program-status.yaml` —
  record this correction under `G3.correction`; reconcile
  `G3.unresolved_question_dispositions.UQ4`/`UQ7` to the corrected enum
  values (finding 1).
- `governance/audits/GOV-GEN-AUD-001-governance-generalization/00-program-charter.md` —
  note the correction's existence and pending disposition.
- `governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-009-g3-correction-r1-v0.1.0.yaml` —
  new decision record for this correction.
- `governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/README.md` —
  append paragraph.
- `governance/DECISION_LOG.md` — new append-only `GOV-DEC-035` entry.
  `GOV-DEC-034` (the original G3 execution entry) is not rewritten.
- `governance/CURRENT_STATE.md` — reconcile the G3 status paragraph and
  status-table `UQ4`/`UQ7` fields to the corrected enum values.
- `governance/ARTIFACT_REGISTRY.yaml` — add this file, its manifest, the new
  decision record, and `HP-PROMPT-048` to custody.
- `governance/README.md` — note the correction's existence.

No other path is touched. `governance/AGENTS.md` and root `AGENTS.md` are
not modified anywhere by this correction, per `HP-PROMPT-048/0.1.0` and
`GOV-GEN-G3-CONTRACT-001/0.1.0` §4.3.

## 9. Correction-session validation

1. Worktree clean before this correction's writes began; expected starting
   commit `d9cc0e74584e1c8c7aa83894621f3d9ede77bdea` on branch
   `governance/kernel-designer-revision-v0.1`; no Git command beyond
   read-only inspection was run outside this correction's authorized paths.
2. No capability classification, gap disposition, layer allocation, layer
   count, boundary-model content, or candidate-architecture recommendation
   was changed anywhere.
3. No target-architecture selection, kernel-ownership decision, or
   implementation of Delegated Operational Authority, Provider-Neutral
   Governance, any adapter, or any query/projection tooling exists anywhere
   in this correction.
4. `governance/AGENTS.md` and root `AGENTS.md` are unmodified.
5. Exactly one correction artifact (this file) plus its manifest exists for
   the base deliverable; minimum current-state reconciliation paths listed
   in §8 are the only other paths touched.
6. Hash manifest for this file verifies
   (`GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.manifest.sha256`).
7. `python governance/tools/validate_prompts.py` and
   `python governance/tools/validate_governance_state.py` pass against the
   corrected working tree — see completion disposition (§10) for the actual
   run result of this correction session.

## 10. Completion disposition

```yaml
completion:
  status: G3_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  base_head: d9cc0e74584e1c8c7aa83894621f3d9ede77bdea
  corrections_applied: 6
  base_deliverable_modified: false
  layer_reallocation_performed: false
  capability_reclassification_performed: false
  gap_redisposition_performed: false
  g2_reopened: false
  agents_md_modified: false
  corrected_unresolved_question_dispositions:
    UQ4: LOGICALLY_RESOLVED_BY_G3
    UQ7: NARROWED_BUT_OWNER_DECISION_REQUIRED
  next_authority_required: OWNER_ACCEPTANCE_OF_G3_CORRECTION_R1
```

The executor does not accept this correction. Project Owner acceptance,
rejection, or a request for further bounded correction is a separate,
subsequent act, exactly as under the base deliverable (§12) and under
`GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0` §6. No push has been
performed.

`GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1/0.1.0 G3_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE`

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2.md all ---
---
document_id: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2
title: HugePlanning Governance Generalization — G3 Logical Architecture — Bounded Factual Correction 2
program_id: GOV-GEN-AUD-001
phase: G3
base_deliverable: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001/0.1.0
base_deliverable_sha256: be5c8ceb008e38579419b38f8813c9ac737f7c1842f2f5bd170667a6f1c5582b
prior_controlling_correction: GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1/0.1.0
prior_controlling_correction_sha256: fd0294f60fd45249c087448851712721aa8a91b21e22fff35e4d8237faba1eb6
correction_index: 2
version: 0.1.0
status: G3_CORRECTION_R2_READY_FOR_PROJECT_OWNER_ACCEPTANCE
authority: BOUNDED_PROJECT_OWNER_FACTUAL_REFERENCE_CORRECTION_ONLY_NO_G3_REOPENING_OR_REDESIGN
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
source_authority: Project Owner direct task “GOV-GEN — Bounded G3 Factual Correction”
---

# GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2 — Bounded Factual Correction

## 0. Scope and boundary statement

This is one minimal prospective correction of the accepted controlling G3
result: the base deliverable `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001/0.1.0`
read together with its accepted correction
`GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1/0.1.0`. It corrects only the factual
and reference defect in base §10's extraction/migration-boundaries bullet.
R1 did not touch §10.

It does **not** reconstruct, reopen, or redesign G3; change the accepted
eight-layer architecture, capability allocations, gap allocations,
unresolved-question dispositions, boundary model, context-efficiency model,
or candidate-architecture recommendation; alter G4 or G5; or authorize GR
or G6. The base deliverable and R1 remain unmodified historical evidence.

## 1. Exact targeted lookup and calculation

One targeted lookup into the accepted G2 evidence was performed for this
correction: `GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0` §17.2, *By reuse
readiness*, and §23, `reuse_readiness_counts`. Both record:

```text
READY: 39
NEEDS_NORMALIZATION: 27
NEEDS_MODEL_CHANGE: 10
NOT_REUSABLE_AS_IS: 12
total: 88
```

The applicable non-`READY` population is therefore
`27 + 10 + 12 = 49`; `49 / 88 = 55.6818...%`, reported as **55.7%**. G2 §21
is a flat seven-item unresolved-question list and has no §21.2 subsection;
it is not a valid source for this figure.

## 2. Corrected G3 §10 passage

Only this base §10 bullet is corrected:

> **Extraction/migration boundaries.** Which specific L1/L2/L6 capabilities
> move first, and how the 49 non-`READY` capabilities (55.7% of the
> 88-capability map — 27 `NEEDS_NORMALIZATION`, 10 `NEEDS_MODEL_CHANGE`, and
> 12 `NOT_REUSABLE_AS_IS`, per G2 §17.2/§23) are normalized before or during
> a move.

This replaces the base wording "`NEEDS_NORMALIZATION`/`NEEDS_MODEL_CHANGE`
items (66% of the map, per G2 §21.2)". No other G3 text, result, allocation,
or disposition is changed.

## 3. Correction disposition

```yaml
completion:
  status: G3_CORRECTION_R2_READY_FOR_PROJECT_OWNER_ACCEPTANCE
  targeted_lookups_performed_by_this_correction: 1
  factual_reference_defects_corrected: 1
  base_deliverable_modified: false
  prior_controlling_correction_modified: false
  eight_layer_architecture_changed: false
  capability_reallocation_performed: false
  gap_redisposition_performed: false
  unresolved_question_disposition_changed: false
  boundary_model_changed: false
  context_efficiency_model_changed: false
  g4_modified: false
  g5_modified: false
  gr_authorized: false
  g6_authorized: false
  next_governed_state: PROJECT_OWNER_ACCEPTANCE_OR_REJECTION_OR_FURTHER_BOUNDED_CORRECTION
```

The next action is Project Owner acceptance, rejection, or a further bounded
correction request for this corrected G3 result. This artifact does not
perform that acceptance.

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001.md §9 ---
## 9. Architecture pressures carried to G5

```yaml
- id: AP-1
  statement: L0 distribution mechanics (copy vs. reference vs. centrally-read) must be decided before any physical repository-topology option is chosen.
  carries: [RD-C1, RD-C6]
- id: AP-2
  statement: A concurrency-safe ID allocation mechanism is a precondition for any physical topology permitting simultaneous multi-branch, multi-worktree, or multi-repository ID allocation.
  carries: [RD-B3, RD-C6]
- id: AP-3
  statement: An enforced (not merely classified) Delegated Operational Authority boundary is required before delegated routine mechanics or high-volume independent review can be claimed as a benefit of adopting this model.
  carries: [RD-B4, RD-C8]
- id: AP-4
  statement: A deterministic L6 query/index capability over L5/L6 evidence is required before large-evidence-volume consumers are viable, and materially improves concurrent-agent consumers; it is unnecessary for a single-owner, low-volume consumer.
  carries: [RD-B5, RD-C4, RD-C5, RD-C7]
- id: AP-5
  statement: A second real executor/provider adapter, or a provider-neutral binding abstraction at L1, is required before "provider-neutral" or "multi-executor" can be claimed rather than merely evaluated.
  carries: [RD-B1]
- id: AP-6
  statement: Program-scoped state, registry, and log separation (or a federating query layer over them) is required before more than a small number of concurrent programs/teams can share one repository's L6/L7 surfaces without those surfaces growing unboundedly; this repository's own CURRENT_STATE.md already shows the strain at two programs.
  carries: [RD-C2, RD-C4, RD-C5]
```

None of AP-1 through AP-6 is decided, designed, or implemented by this
document; each is stated as a requirement a later, separately authorized
phase must resolve, using the accepted G3 L0-L7 shape as the frame those
decisions should respect — the same posture G3 §10 already took toward its
own future physical-architecture inputs, extended here to the requirements
those inputs must additionally satisfy once real second/third/Nth consumers
are modeled.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md §4 ---
## 4. Finding 3 — Category-mismatched evidence citation (RD-B3, RD-C6)

The independent review found that register entries RD-B3 and RD-C6 cite
`.claude/rules/id-and-status-conventions.md`'s single-writer ID-allocation
limitation as evidence for a defect in GOV-GEN's own L0-L7 governance model.
That file, however, is explicitly scoped by `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1/0.1.0`
§6's own accepted boundary statement ("This entire L0-L7 model describes
`governance/` only... Root `CLAUDE.md` invariants govern an unrelated
system") to a different, root-level, client-facing methodology system: its
own preamble ties it to client-engagement stage S0a and lists ID prefixes
(`OBJ`/`FR`/`NFR`/`TASK`/`BUG`/`CR`, etc.) unrelated to GOV-GEN's actual
`CAP-NAV*`/`GAP-*`/`RD-*`/`AP-*` vocabulary, and its "single writer" claim
describes that system's `project.yaml` counter mechanism, not anything
documented about how `governance/`'s own IDs are allocated. Citing it as
evidence for a GOV-GEN model defect conflates two systems G3 itself already
firewalled apart — this document must observe the same firewall it relies
on elsewhere (base §3's own profile-definitions section states this
explicitly for profile sourcing; the register entries did not apply it
consistently to evidence sourcing).

**What is and is not defective.** The underlying substantive concern —
that a sequentially-allocated ID scheme is vulnerable to collision when two
branches independently compute "next ID" from the same last-seen value — is
not itself wrong; it is a generic, observable property of any
read-then-increment allocation pattern under concurrent writers. What was
defective is the citation: GOV-GEN's own IDs (`GOV-DEC-*`, `GOV-GEN-DECISION-*`,
`HP-PROMPT-*`, and the `CAP-NAV*`/`GAP-*` records G1A/G1B fixed once during
indexing) are, by observed practice in this repository, allocated by reading
the highest existing entry in an append-only log (`governance/DECISION_LOG.md`,
`decisions/README.md`, the `HP-PROMPT-*` sequence under
`governance/prompts/orchestration/`) and incrementing — with no documented
concurrency safeguard of its own, but also with no formal "single writer"
rule anyone has written down for this specific scheme, unlike the
methodology repository's explicit, documented rule.

**Corrected entries** (only the `observed_pressure` and `evidence_refs`
fields change; `requirement_delta`, `severity`, and `architecture_relevance`
are unchanged for both, since the underlying concern independently supports
them once correctly grounded):

```yaml
- id: RD-B3
  profile: BETA
  affected_layer: L6
  affected_capabilities: [CAP-NAV01-003]
  assumption_under_test: globally unique un-namespaced identifiers allocated by a single writer
  observed_pressure: "GOV-GEN's own IDs (GOV-DEC-*, GOV-GEN-DECISION-*, HP-PROMPT-*) are, by this repository's own observed practice, allocated by reading the highest existing entry in an append-only log and incrementing, with no documented concurrency safeguard of its own; two branches independently reading the same last-seen value and computing the same next ID will collide deterministically -- this is a structural property of the observed mechanism, not a documented rule, but Profile BETA's defining trait (branch/worktree concurrency) makes it load-bearing rather than theoretical either way"
  requirement_delta: a concurrency-safe allocation mechanism (e.g. reserved ranges per branch/worktree, or deterministic allocate-on-merge with automated collision resolution) is required before concurrent branches can safely allocate IDs independently
  severity: BLOCKS_REUSE
  architecture_relevance: logical_architecture_defect
  evidence_refs: ["GOV-GEN's own observed sequential-allocation practice (governance/DECISION_LOG.md, decisions/README.md, governance/prompts/orchestration/HP-PROMPT-* sequence)"]

- id: RD-C6
  profile: GAMMA
  affected_layer: [L1, L6]
  affected_capabilities: []
  assumption_under_test: globally unique un-namespaced identifiers
  observed_pressure: "GOV-GEN's own <TYPE>-<NNN>-shaped IDs (CAP-NAV*, GAP-*, GOV-DEC-*, GOV-GEN-DECISION-*, HP-PROMPT-*) are unique only within this one repository's own sequence; Profile GAMMA needs cross-repository citation (e.g. an L0 rule cited by ID from a second repository) with no repository/program-qualifying prefix defined anywhere in the observed grammar"
  requirement_delta: a namespace qualifier prepended or appended to the existing grammar shape (not a redesign of the shape itself) is required for cross-repository reference
  severity: REQUIRES_PARAMETERIZATION
  architecture_relevance: architecture_pressure_not_g4_decision
  evidence_refs: ["GOV-GEN's own observed ID grammar (CAP-NAV*, GAP-*, GOV-DEC-*, GOV-GEN-DECISION-*, HP-PROMPT-*)"]
```

`.claude/rules/id-and-status-conventions.md` is removed from both entries'
`evidence_refs`; it is not cited anywhere else in the base document.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md §7 ---
## 7. Correction-session validation

1. Worktree clean before this G4 governed unit's writes began; no Git
   command beyond read-only inspection was run outside this unit's
   authorized paths.
2. No consumer profile added, removed, or merged; no G3 capability
   reallocated; no G2 capability reclassified; no G2 gap redisposed; G2 and
   G3 are not reopened.
3. No target-architecture selection, kernel-ownership decision, or
   implementation of Delegated Operational Authority, Provider-Neutral
   Governance, any adapter, or any query/projection tooling exists anywhere
   in this correction — including in the corrected §2 paragraph, which
   states a requirement every physical candidate must satisfy without
   comparing or favoring any candidate.
4. `governance/AGENTS.md` and root `AGENTS.md` are unmodified.
5. Exactly one correction artifact (this file) plus its manifest exists for
   the base deliverable; minimum current-state reconciliation paths listed
   in §6 are the only other paths touched.
6. Hash manifest for this file verifies
   (`GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.manifest.sha256`).
7. `python governance/tools/validate_prompts.py` and
   `python governance/tools/validate_governance_state.py` pass against the
   fully corrected working tree — see completion disposition (§8) for the
   actual run result.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G4/GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md §8 ---
## 8. Completion disposition

```yaml
completion:
  status: G4_READY_FOR_PROJECT_OWNER_REVIEW
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  base_head: abb3efaed8a900bce2c7f308cc6f21783bb53151
  material_findings_corrected: 3
  bounded_observations_normalized: 1
  bounded_observations_not_corrected: 2
  base_deliverable_modified: false
  profile_count_changed: false
  g3_capability_reallocation_performed: false
  g2_capability_reclassification_performed: false
  g2_gap_redisposition_performed: false
  g3_reopened: false
  g2_reopened: false
  agents_md_modified: false
  requirements_delta_entries_total_after_correction: 16
  severity_counts_after_correction: {BLOCKS_REUSE: 6, REQUIRES_PARAMETERIZATION: 6, REQUIRES_IMPLEMENTATION_SUPPORT: 4, OPTIONAL_PROFILE_REQUIREMENT: 0}
  next_authority_required: OWNER_REVIEW_AND_ACCEPTANCE_OF_G4_CORRECTED_R1_RESULT
```

The executor does not accept this correction. Project Owner acceptance,
rejection, or a request for further bounded correction is a separate,
subsequent act, exactly as under the base deliverable (§14) and under
`GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1/0.1.0` §10. No push has been
performed.

`GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1/0.1.0 G4_READY_FOR_PROJECT_OWNER_REVIEW`

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §3 ---
## 3. Finding F2 — Two wrong "G3 §21 UQ4" citations

The independent review found that base §4.2 (Option B,
`config_projection_boundary`) and base §8 (Recommended candidate) each cite
"G3 §21 UQ4" as the source of the L6 boundary principle Option B's package
boundary is said to functionally resolve the "visibility half" of. This is
defective: `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md` has no §21 (its highest
section is §12, Completion disposition); `UQ4` is defined and dispositioned in
G3 §8 ("G2 unresolved-question disposition"), item 4. "§21" is G2's own
unresolved-questions section (`GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md` §21),
not G3's — the two documents' numbering was conflated.

**Both citations are corrected from "G3 §21 UQ4" to "G3 §8 UQ4"**, with no
other change to either sentence:

- §4.2, Option B, `config_projection_boundary`: "...directly answering
  G3 §21 UQ4's boundary principle without performing the declarative L6
  rewrite itself" → "...directly answering G3 §8 UQ4's boundary principle
  without performing the declarative L6 rewrite itself."
- §8, Recommended candidate: "...functionally resolving the *visibility*
  half of G3 §21 UQ4 without yet performing its declarative rewrite" →
  "...functionally resolving the *visibility* half of G3 §8 UQ4 without yet
  performing its declarative rewrite."

The substantive claim both sentences make — that Option B's package boundary
functionally answers UQ4's boundary-*visibility* principle without performing
its declarative-rewrite *mechanics* — is independently accurate against the
corrected location (G3 §8's UQ4 disposition, "`LOGICALLY_RESOLVED_BY_G3`" for
the boundary principle, mechanics deferred) and is unaffected by this
citation fix.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §7 ---
## 7. Correction-session validation

1. Worktree clean before this correction's writes began; no Git command
   beyond read-only inspection (including the one targeted G2 lookup, §2) was
   run outside this correction's authorized paths.
2. G5-A is not redone; no option is added, removed, or redefined; no L0–L7
   mapping cell outside §4's citation fix is changed; no G3 capability is
   reallocated; no G2 capability is reclassified; no G2 gap is redisposed; G2,
   G3, and G4 are not reopened.
3. No target-architecture selection, kernel-ownership decision, or
   implementation of any G4 requirement, architecture pressure, Delegated
   Operational Authority, Provider-Neutral Governance, adapter, or
   query/projection tooling exists anywhere in this correction.
4. This correction is not independently reviewed, and G5 (base or corrected)
   is not accepted, rejected, or self-accepted anywhere in this document.
5. `governance/AGENTS.md` and root `AGENTS.md` are unmodified.
6. Exactly one correction artifact (this file) plus its manifest exists for
   the base deliverable; the minimum current-state reconciliation paths
   listed in §6 are the only other paths touched.
7. Hash manifest for this file verifies
   (`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.manifest.sha256`), and
   the base deliverable's own manifest independently re-verifies unmodified
   (`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001.manifest.sha256`,
   SHA-256 `a57d34c73e64495214db96278f9d9176898ca68a14263db63bf77b10cd806e2e`,
   unchanged from the independent review's own recorded
   `reviewed_candidate_sha256`).
8. `python governance/tools/validate_prompts.py` and
   `python governance/tools/validate_governance_state.py` pass against the
   fully corrected working tree — see completion disposition (§8) for the
   actual run result.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §8 ---
## 8. Completion disposition

```yaml
completion:
  status: G5_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  base_head: f25f7fba4aecf382f1124971474f24ecbbc72574
  findings_corrected: 4
  finding_ids: [GOV-GEN-G5-IR-001-F1, GOV-GEN-G5-IR-001-F2, GOV-GEN-G5-IR-001-F3, GOV-GEN-G5-IR-001-F4]
  base_deliverable_modified: false
  base_deliverable_sha256: a57d34c73e64495214db96278f9d9176898ca68a14263db63bf77b10cd806e2e
  correction_manifest: GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.manifest.sha256
  targeted_lookups_performed_by_this_correction: 1
  targeted_lookup_target: "GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md §17.2 and §23 (reuse_readiness_counts)"
  options_added_removed_or_redefined: 0
  l0_l7_mapping_cells_changed: 0
  requirements_compliance_cells_changed: 1
  requirements_compliance_cell_changed_id: RD-C5
  requirements_compliance_cell_change: STRUCTURALLY_ENABLED_to_NOT_ADDRESSED
  blocks_reuse_entries_individually_reasoned: 6
  recommendation_shape_unchanged: true
  recommended_candidate_shape: STAGED_SEQUENCE_B_THEN_OPTIONAL_D_THEN_DEFERRED_C_WITH_A_AS_FALLBACK
  g3_capability_reallocation_performed: false
  g2_capability_reclassification_performed: false
  g2_gap_redisposition_performed: false
  g2_g3_g4_reopened: false
  target_architecture_selected: false
  repository_created: false
  file_extracted_or_migrated: false
  agents_md_modified: false
  correction_independently_reviewed: false
  g5_accepted_or_rejected: false
  next_authority_required: OWNER_ACCEPTANCE_OF_G5_CORRECTED_R1_RESULT
```

The executor does not accept this correction, does not independently review
it, and does not accept, reject, or select among G5's options. Project Owner
acceptance, rejection, or a request for further bounded correction is a
separate, subsequent act, exactly as under the base deliverable (§12 of the
base) and under `GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1/0.1.0` §8. No
push has been performed.

`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1/0.1.0 G5_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE`

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md §3 ---
## 3. Adversarial assessment

### B: reusable boundary versus HugePlanning coupling

The strongest case against B is that an internal package can be a cosmetic
directory move: one consumer, one repository, and project literals still
silently embedded in tooling. G5 itself names this as its principal B failure
mode and requires boundary validation rather than assuming separation. G3
locates the relevant rule at the L1/L3-versus-L6 boundary, while retaining
L3 and L5 under the consuming project's Owner and custody. Therefore B is not
evidence of external reuse or provider neutrality; it is a reversible,
testable boundary experiment. The recommendation does not claim more.

### D: pilot value and its deliberately narrow evidence

D cannot validate L0–L2 semantic/configuration separation, a second adapter,
DOA enforcement, registry federation, program entrypoints, or the L5→L6→L7
query capability. G5 expressly says so. It nevertheless exposes a distinct
unresolved risk that B cannot: history-preserving cross-repository extraction
and reference/version mechanics on a small READY L6 slice. This makes D a
useful optional pilot only when read as a provenance/distribution rehearsal;
its evidence must not be generalized to C's semantic boundary.

### C: evidence-based deferral

C is the only option that makes L0 distribution structurally satisfiable and
permits a real second consumer. It makes all AP-1–AP-6 load-bearing while
resolving neither concurrent ID allocation, DOA, registry federation, program
entrypoints, deterministic bounded query, nor a second adapter. The
controlling R1 correction also removes the earlier
incorrect credit that C advanced RD-C5. Deferral is thus based on the
accepted requirements, not implementation convenience.

### A, L0 distribution, and the six blockers

A remains a credible fallback precisely for the stated condition that no real
second consumer exists or is imminent; it is not presented as a solution to
reuse. B only partially structures L0 distribution, C supplies its possible
shape but not its mechanism, and D does not address L0. Across B/C/D, none of
the six `BLOCKS_REUSE` requirements is represented as resolved. B leaving
them deferred is accurate; C makes several urgent; D exercises only a small
subset of cross-repository mechanics. This is an architecture-sequencing
tradeoff for the Owner, not an unsupported claim that topology implements the
requirements.

### Provider neutrality, namespacing, federation, and query scaling

The synthesis correctly reserves provider neutrality for a second adapter or
L1 binding, namespacing and concurrent allocation for AP-1/AP-2, federation
and state separation for AP-6, and deterministic bounded projection for AP-4.
No option is credited with implementing these. The absence of an additional
physical option is not a defect: distribution mechanism and workspace tooling
are axes within B/C/D, while a fifth topology would not remove the identified
requirements or improve the present lack of a second consumer.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md §4 ---
## 4. Findings

No `BLOCKING`, `MATERIAL`, or `MINOR` finding is recorded. The adversarial
cases identify three implementation requirements correctly deferred (B
boundary conformance validation; D pilot success criteria; AP-1–AP-6
resolution paths before C), and the Owner tradeoff of whether a second
consumer is sufficiently imminent. They are not factual defects or unsupported
inferences in the accepted G5 recommendation.

```yaml
findings:
  blocking: []
  material: []
  minor: []
```


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md §5 ---
## 5. Verdict and stop condition

**GR_SUPPORTS_OWNER_ARCHITECTURE_DECISION**

The recommendation survives. Its strongest adversarial cases do not overturn
it because B is described as a bounded in-place experiment requiring boundary
validation rather than proof of reuse; D is explicitly limited to extraction/provenance
mechanics; C's deferral follows the accepted unresolved requirements and lack
of a real consumer; and A is retained only as the honest no-demand fallback.
No architecture is selected, no G5 result is corrected, and no G6 work is
authorized. The next action is the Project Owner's decision whether to adopt,
alter, or reject the non-binding staged architecture recommendation.

```yaml
completion:
  status: EXECUTED_READY_FOR_PROJECT_OWNER_ARCHITECTURE_DECISION
  targeted_drill_downs_performed: 5
  findings_blocking: 0
  findings_material: 0
  findings_minor: 0
  g5_recommendation_survives: true
  architecture_selected: false
  g5_modified: false
  g6_started_or_authorized: false
  verdict: GR_SUPPORTS_OWNER_ARCHITECTURE_DECISION
  next_authority_required: PROJECT_OWNER_ARCHITECTURE_DECISION
```

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md §1 ---
## 1. Decision-preserving result

Option B's minimum reusable physical boundary is an in-place, versioned
**L0–L2 core contract surface plus a declared L1 configuration seam**. It
must have no dependency on HugePlanning's L3 values, L5 evidence, or literal
project paths. L3 stays in HugePlanning as the adopting project's projection;
L5 stays there as its append-only evidence and historical custody. L4 remains
outside the core as provider-specific adapters. L6 is split only where a
capability is already infrastructure-pure; project-bound validation and all
L7 entrypoints remain project-owned until separately designed.

This is a physical boundary, not a claim of external reuse, provider
neutrality, distributed L0, or resolution of AP-1–AP-6. HugePlanning becomes
the first adopter by consuming the in-place core through an explicit local
binding while retaining its Owner, current L3 projections, L5 custody, and
existing governance instructions until a later authorized, semantics-proven
adoption change.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md §2 ---
## 2. Dependency order and readiness

`B-01 → B-02 → B-03 → B-04 → B-05 → B-06 → B-07 → B-08`.

The safest first packet is **B-01**, a read-only boundary inventory and
semantic-baseline package. It changes no active behavior and makes B-02's
source/target boundary falsifiable before any artifact moves.

`READY` capability families that may move after B-01/B-02 boundary proof,
without semantic redesign, are pure L6 infrastructure (`CAP-NAV13-001` and
the record-type schema/tool helpers it supports), plus the reusable existing
mechanics represented by READY custody/manifest/check primitives. Their
individual inclusion is still determined by B-02's literal-dependency scan;
`READY` never authorizes a project-bound caller to move with them.

`NEEDS_NORMALIZATION` items require B-03's declared L1 configuration seam
first: run/program packaging (`CAP-NAV07-001/002`), phase/projection wiring
(`CAP-NAV01-004/005`), closure-loop naming (`CAP-NAV04-004`), prompt-index
reconciliation (`CAP-NAV05-001`), and project-coupled review/run instances.
`NEEDS_MODEL_CHANGE` items are blocked from extraction: project-specific
kernel/role content (`CAP-NAV02-001`, `CAP-NAV04-005/006/007`) remains L3;
the project-hardcoded state validator (`CAP-NAV06-004`/`CAP-NAV13-008`)
requires the later declarative model packet; query/index, DOA, second adapter,
identity, and program-state work require their named prerequisite packets.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md §3:B-01 ---
- packet_id: B-01
  objective: Establish an immutable, semantic baseline and exact candidate boundary inventory for Option B; perform no extraction.
  source_scope: Current HugePlanning governance L0-L7 realizations named by G3 plus their direct imports.
  target_scope: A generated G6 evidence projection only; no runtime target.
  logical_layers: [L0, L1, L2, L3, L4, L5, L6, L7]
  capabilities: [boundary inventory, provenance map, semantic baseline]
  requirements_or_pressures: [AP-1, AP-2, AP-3, AP-4, AP-5, AP-6]
  preconditions: [Owner-authorized packet execution, clean scoped worktree, frozen source revision, B-01 input projection <=20k tokens]
  allowed_mutations: [packet-local inventory, dependency graph, hashes, baseline test/report]
  forbidden_mutations: [all implementation artifacts, AGENTS.md, CLAUDE.md, L3, L5, target directories]
  bounded_inputs: [G3 R2 §§4,6-8,10, G4 R1 §§4, G4 base §9, G5 R1 §4.2/§7/§8, GR §§3-5, direct source files named by inventory]
  validation: [source hashes, direct-import closure, baseline deterministic checks, explicit L3/L5 exclusion, no implementation diff]
  independent_review_required: true
  rollback_or_recovery: Delete only packet-local generated evidence; source tree remains unchanged.
  completion_state: B-01_BOUNDARY_BASELINE_REVIEW_READY
  depends_on: []


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md §4 ---
## 4. Instruction, proof, and decision gates

Active instruction surfaces may change only after B-02 proves the core/local
adopter boundary and a separately authorized adoption packet demonstrates
semantic equivalence. `AGENTS.md` changes must additionally wait for B-03's
configuration seam; `CLAUDE.md` remains outside this governance plan unless a
separate methodology-runtime authority is granted. B-08 may propose, never
self-apply, instruction changes after its two-adapter conformance evidence.

Option B is empirically proven only when B-02's boundary and local adoption
pass independent review, B-03 proves no HugePlanning values are embedded in
the reusable mechanism, B-04 proves an actual READY L6 move retains semantics,
and B-08 proves the same core semantics through a second adapter. This proves
the Option B boundary/adopter hypothesis, not external reuse, L0 distribution,
Option C readiness, or AP-1–AP-6 completion. Option C remains deferred until
that proof, a real second consumer, and designed resolution paths for all six
pressures; Option D remains separately authorized only.


--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1.md all ---
---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1
title: HugePlanning Governance Generalization — G6 Bounded Extraction Plan — Clarification R1
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
base_deliverable_sha256: 86aba6ab024c92f4c5e0c8cc0b241a6e26db8f29c0a69687a9e489be4dd0152f
contract: GOV-GEN-G6-CONTRACT-001/0.1.0
correction_index: 1
version: 0.1.0
status: G6_R1_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
authority: BOUNDED_PLAN_CLARIFICATION_ONLY_NOT_EXTRACTION_EXECUTION_OR_OWNER_ACCEPTANCE
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
source_authority: Project Owner direct task “GOV-GEN G6 — Bounded Plan Clarification”
---

# GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1 — Bounded Plan Clarification

## 0. Scope and historical integrity

This is the minimum prospective clarification of
`GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0`. The base deliverable and its
manifest remain unmodified historical planning evidence. This R1 is read
together with the base and corrects only the ambiguity between its displayed
packet sequence and the per-packet `depends_on` fields.

It does not redesign, add, remove, merge, split, or reorder B-01 through
B-08; change a packet's objective, scope, preconditions, allowed or forbidden
mutations, validation, context budget, authority gate, review requirement, or
rollback/recovery condition; execute a packet; authorize extraction,
migration, AP-1–AP-6 implementation, Option D, or instruction-surface change;
or accept this corrected plan on the Project Owner's behalf.

## 1. Corrected execution semantics

The displayed sequence

```text
B-01 → B-02 → B-03 → B-04 → B-05 → B-06 → B-07 → B-08
```

is the **recommended default serial execution order**. It remains the plan's
unchanged, safest default presentation order; it is not a replacement hard
dependency chain.

Each packet's `depends_on` field in the base plan is the **authoritative hard
dependency graph**. A packet may not execute until all of its listed
dependencies have reached the packet's required prerequisite state. No
inference from the displayed serial order may add a hard dependency that is
absent from `depends_on`.

Satisfying the authoritative dependencies can make a schedule other than the
recommended default serial order technically available. Such a different
schedule may be used **only under explicit authorization**. This clarification
does not grant that authorization, authorize parallel execution, or alter any
existing packet authority gate.

## 2. Unchanged Option B empirical-proof gate

The Option B empirical-proof criteria in base plan §4 remain unchanged. The
proof gate consists exactly of:

- B-02: independently reviewed boundary and local-adoption pass;
- B-03: proof that HugePlanning values are not embedded in the reusable
  mechanism;
- B-04: proof that an actual READY L6 move retains semantics; and
- B-08: proof of the same core semantics through a second adapter.

B-05, B-06, and B-07 remain planned G6 work with their unchanged respective
scopes and `depends_on` fields. They are not prerequisites for the stated
Option B empirical-proof gate unless another accepted dependency requires
them. This does not remove, defer, or change those packets, and does not
change the base plan's statement that the proof demonstrates the Option B
boundary/adopter hypothesis only.

## 3. Correction disposition

```yaml
completion:
  status: G6_R1_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
  base_deliverable_modified: false
  base_manifest_modified: false
  packets_added_removed_merged_split_or_reordered: false
  packet_scopes_preconditions_mutation_boundaries_validation_context_budgets_and_authority_gates_changed: false
  packet_execution_authorized_or_performed: false
  authoritative_hard_dependency_graph: per_packet_depends_on_fields_in_base_plan
  displayed_sequence_semantics: recommended_default_serial_execution_order
  alternative_schedule_requires_explicit_authorization: true
  option_b_empirical_proof_packets: [B-02, B-03, B-04, B-08]
  b_05_b_06_b_07_required_for_stated_option_b_empirical_proof_gate: false
  extraction_executed: false
  ap_1_through_ap_6_implemented: false
  active_instruction_surfaces_modified: false
  project_owner_acceptance: PENDING
  next_authority_required: PROJECT_OWNER_REVIEW_AND_ACCEPTANCE_OR_BOUNDED_REVISION_OF_G6_PLAN
```

--- seed governance/audits/GOV-GEN-AUD-001-governance-generalization/G6/GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2.md all ---
---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2
title: HugePlanning Governance Generalization — G6 Bounded Extraction Plan — B-01 Execution-Contract Correction R2
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
base_deliverable_sha256: 86aba6ab024c92f4c5e0c8cc0b241a6e26db8f29c0a69687a9e489be4dd0152f
prior_controlling_correction: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1/0.1.0
prior_controlling_correction_sha256: 9aa9ea026dc87ea50e02fd57150628fc1e51e60bf8f46aaba33c448b711f7f72
independent_review: GOV-GEN-G6-INDEPENDENT-BOUNDED-PLAN-REVIEW-001/0.1.0
correction_index: 2
version: 0.1.0
status: G6_R2_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
authority: BOUNDED_CORRECTION_OF_F_001_AND_F_002_ONLY_NOT_PACKET_EXECUTION_OR_OWNER_ACCEPTANCE
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
source_authority: Project Owner direct task “GOV-GEN G6 — Bounded Correction of B-01 Execution Contract”
---

# GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2 — B-01 Execution-Contract Correction

## 0. Scope and historical integrity

This is the minimum prospective correction of the accepted controlling G6
result, `GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0` read together with
`GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1/0.1.0`. It resolves only
`F-001` and `F-002` in
`GOV-GEN-G6-INDEPENDENT-BOUNDED-PLAN-REVIEW-001/0.1.0`.

The base plan, R1, their manifests, and the independent review remain
unmodified historical evidence. This R2 is a candidate correction, not
Project Owner acceptance. It does not execute or authorize B-01 or any other
packet.

Except for the B-01 input-construction, validation, and recovery/custody
clauses replaced below, every base/R1 packet field and plan invariant remains
unchanged: all eight packet identities; the per-packet `depends_on` DAG; the
recommended default serial order; the B-02/B-03/B-04/B-08 Option B
empirical-proof gate; B-05/B-06/B-07 planned status; L3/L5 project ownership;
instruction-surface gates; mutation boundaries; and the accepted architecture
decision. This correction does not address the known unrelated immutable
PASS-03 scaffold-validator condition.

## 1. F-001 — non-circular B-01 pre-execution input construction

The base-plan B-01 `bounded_inputs` and relevant `preconditions` are replaced
by this construction contract. The B-01 inventory is an output only; it is
never an input selector.

### 1.1 Fixed seed set

Before B-01 starts, a future authorized executor must freeze one clean
repository revision and assemble the following **fixed seed source set** from
that revision. A reference to a corrected G3 result means the named physical
artifact(s), not an inferred or reconstructed history.

```yaml
seed_fragments:
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md: ["§4", "§6", "§7", "§8", "§10"]
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md: ["all"]
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2.md: ["all"]
  - GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001.md: ["§9"]
  - GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md: ["§4", "§7", "§8"]
  - GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md: ["§4.2", "§7", "§8"]
  - GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md: ["§3", "§4", "§5"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md: ["§1", "§2", "§3:B-01", "§4"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1.md: ["all"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2.md: ["all"]
```

The fragment selector is deterministic: Markdown `§N` is the bytes from that
ATX heading through, but excluding, the next heading of equal-or-higher level;
`§3:B-01` is the B-01 YAML mapping only; and `all` is the complete UTF-8 file.
All selected files must exist, decode as UTF-8 without replacement, and match
the frozen revision. Otherwise construction fails before B-01 begins.

### 1.2 Deterministic source-root and import-closure discovery

From the rendered seed fragments only, extract every backticked or plain-text
repository-relative pathname matching `^[A-Za-z0-9][A-Za-z0-9._/-]*\.(md|py|yaml|yml|json)$`.
Normalize with POSIX separators; reject an absolute path, `..`, a missing
path, or a path outside the frozen Git tree. Retain only paths whose G3 §4
allocation is L0, L1, L2, or L6, or that are explicitly named by the G3
§6–§8 boundary/context sections. Deduplicate and sort bytewise. This ordered
list is the B-01 source-root set.

For each source root and each discovered Python file, parse UTF-8 Python with
the standard-library `ast` parser and resolve `import` and `from ... import`
targets only to repository-local `.py` files using Python's normal package
resolution from that importing file. Recurse breadth-first, processing paths
in bytewise order, until no new repository-local Python target remains.
Non-Python source roots contribute no imports. A parse error, ambiguous local
resolution, missing local target, symlink escaping the frozen tree, or an
unsupported source-root extension is a deterministic construction failure;
the executor must not silently omit it. The resulting ordered source roots
plus closure are the source-file portion of the projection. This procedure
does not read any path named by a B-01 inventory because no B-01 inventory
exists yet.

### 1.3 Projection, provenance, measurement, and refusal

The executor renders the projection in this exact order: (1) a YAML header
recording frozen revision; (2) seed fragments in the order above; (3) source
roots plus closure in bytewise pathname order. Each member must carry its
repository-relative canonical path, selection rule, SHA-256 of the exact
source bytes, and, for closure members, its importing parent path. A
content-addressed `B-01-input-projection-manifest.yaml` records the ordered
members, their byte counts and SHA-256 values, the rendered-projection
SHA-256, and the measurement below. It is provisional packet-local evidence
until B-01 completion/review custody applies under §2.

Token measurement is over the complete rendered UTF-8 projection, including
the header and provenance fields, using `tiktoken` **0.12.0**,
`cl100k_base`, and `encoding.encode(rendered_text, disallowed_special=())`.
The manifest records the package version, encoding name, token count, and
the limit `20000`. B-01 may begin only when the count is `<= 20000`.

If any construction check fails or the measured count is greater than 20,000,
the executor must record `B-01_INPUT_PROJECTION_REFUSED` with the failing
rule, ordered candidate paths, hashes available before failure, and measured
count where applicable; discard only provisional construction output; make no
source or implementation mutation; do not start B-01; and return to the
Project Owner for a separately authorized bounded-plan correction or changed
execution authority. It must not trim, summarize, substitute, or load the
full GOV-GEN history to force compliance.

Accordingly, B-01 validation additionally requires successful verification of
the manifest's member hashes, selection/provenance chain, rendered hash,
tokenizer/version, and `<=20000` count before any B-01 semantic work begins.

## 2. F-002 — B-01 recovery and immutable custody

The base-plan B-01 `rollback_or_recovery` is replaced with the following:

> During a failed, refused, or rolled-back B-01 execution, only provisional,
> unaccepted packet-local construction and draft outputs may be discarded.
> Source-tree bytes remain unchanged. Once a B-01 semantic baseline, its
> input-projection manifest, source/provenance map, and required independent
> review record have been completed and accepted, they are immutable
> historical custody and may not be deleted or rewritten. A later correction
> or replacement requires explicit authorization and a new prospective,
> versioned/superseding artifact that preserves the earlier baseline, its
> manifest, review record, and provenance.

This lifecycle makes the B-02 prerequisite retrievable: only an accepted,
custodied B-01 baseline and its approved immutable-history map can support
B-02. A provisional B-01 draft is not a baseline, cannot satisfy B-02, and
may be discarded without altering historical custody.

## 3. Correction disposition

```yaml
completion:
  status: G6_R2_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
  findings_resolved: [F-001, F-002]
  f_001_resolution: non_circular_fixed_seed_deterministic_closure_content_addressed_manifest_pinned_token_measurement_pre_execution_cap_and_refusal
  f_002_resolution: provisional_outputs_discardable_accepted_baseline_manifest_provenance_and_review_immutable_prospective_supersession_only
  base_deliverable_modified: false
  r1_modified: false
  independent_review_modified: false
  packets_added_removed_merged_split_or_reordered: false
  b_02_through_b_08_materially_changed: false
  authoritative_hard_dependency_graph: per_packet_depends_on_fields_in_base_plan
  displayed_sequence_semantics: recommended_default_serial_execution_order
  option_b_empirical_proof_packets: [B-02, B-03, B-04, B-08]
  b_05_b_06_b_07_status: planned_unchanged
  b_01_status: NOT_STARTED_NOT_AUTHORIZED
  packet_execution_authorized_or_performed: false
  extraction_executed: false
  active_instruction_surfaces_modified: false
  project_owner_acceptance: PENDING
  next_authority_required: PROJECT_OWNER_REVIEW_AND_ACCEPTANCE_OR_BOUNDED_REVISION_OF_G6_PLAN
```

--- source governance/AGENTS.md ---
# HugePlanning Governance Workspace Instructions

These instructions apply only to `governance/` and descendants. Apply root `../AGENTS.md` first. This file narrows governance work; it does not enlarge authority.

## Grounding

Before material governance work read `README.md`, `CURRENT_STATE.md`, `GOVERNANCE_MASTER_PLAN.md`, the applicable methodology/role contract, and the exact run, review, decision, or task inputs required for the current result.

Treat current durable governance state, accepted decisions, immutable run evidence, ratified Kernel artifacts, and applicable contracts as controlling over chat summaries or generated views. Verify raw-source custody against `SOURCE_CHECKSUMS.sha256` when those sources are in scope.

The canonical stable operating semantics are in `methodology/project-operating-contract.md`. Apply them by reference rather than duplicating them into prompts or local instruction files.

## Governance-specific authority

Keep formal governance roles and authority distinct. Designer, Adversary, reviewer, future Controller, implementer, validator, and Owner responsibilities are not interchangeable. A role's output, a validation PASS, or independent review never grants another role's authority.

The Project Owner retains material authorization, risk acceptance, governance adoption, acceptance, constitutional/Kernel ratification, phase transitions, and other decisions reserved by the controlling contract.

Formal run authority is stricter than ordinary repository-maintenance authority when the applicable contract says so. A formal GOV/KGR run must satisfy its exact prospective authorization, role/mode/run identity, immutable input package, execution-count, output contract, custody, validation, independence, and forbidden-action requirements before it is represented as validly executed.

Do not reuse formal-run authority outside its bound identity or scope. Do not infer execution authority from readiness, prepared prompts, packages, access, or previous Owner decisions.

At the same time, do not impose formal-run ceremony on a routine governance-document, tooling, validation, or repository-maintenance change unless the controlling task or canonical methodology requires it. Once a bounded material result is authorized, routine mechanics covered by that authority should continue to the next genuine material gate without manufacturing extra Owner approvals.

## Status and historical integrity

Preserve honest lifecycle distinctions:

```text
PROPOSED != PREPARED != EXECUTED != VALIDATED != ACCEPTED != RATIFIED != IMPLEMENTED != OPERATIONAL
```

Completed runs, bound prompts, inputs, outputs, imported raw sources, decisions, ratification evidence, validated learning bases, and other declared immutable evidence remain immutable. Correct prospectively through the applicable version/event/correction mechanism.

The Kernel's exact ratification, enforceability, implementation, and operational states are determined only by durable governance evidence. Never infer enforceability or operation from ratification.

## Prompt, evidence, and learning custody

Use `methodology/project-operating-contract.md` and `prompts/README.md` for material-prompt classification, IDs, versioning, custody, execution status, historical recovery, and formal-run prompt snapshots. Do not create a second prompt registry or duplicate exact prompt bytes when an authoritative run snapshot already exists.

Use `learning/README.md` for material failures, near misses, Owner corrections, ambiguity, defects, tooling gaps, and cost waste. Route incidents, decisions, formal-run evidence, methodology proposals, and transient operational logs to their own record classes.

A methodology backlog item is prospective and non-authoritative. A learning record is evidence of an observed causal chain. Neither is an Owner decision, active requirement, ratified rule, or implementation authority.

Do not silently promote ideas, lessons, audit findings, tooling comparisons, research results, or accepted future-review candidates into active GOV scope or methodology.

## Formal execution and review

For a formal run, use the exact applicable manifest, authorization, input package, prompt snapshot, role protocol, output specification, validation plan, and independent-review requirement. Do not substitute a reconstructed prompt, partial package, or chat summary.

Independent review is required when the controlling formal contract or material semantic/authority/constitutional risk requires it. It is not a default ritual for every deterministic correction or low-risk repository mutation.

A session that authored or materially corrected a candidate must not represent its own review as independent where independence is required.

Stop when a required package is missing, identity or provenance drifts, an authorization boundary is ambiguous, validation fails, a forbidden path changes, evidence conflicts materially, or remediation requires an Owner-reserved decision.

## State reconciliation

Update `CURRENT_STATE.md`, `ARTIFACT_REGISTRY.yaml`, decision/run/plan records, learning surfaces, or generated views only when the authorized event materially changes the facts those surfaces own. Instruction wording or routine repository mechanics do not by themselves require a canonical governance-state transition.

When a material governance event does change status-bearing surfaces, reconcile every affected owner of that state and run the applicable cross-surface consistency validation. `CURRENT_STATE.md` follows evidence; it never leads or fabricates it.

## Validation and completion

Use deterministic governance tools for hashing, manifests, package checks, schema validation, state replay, ID/reference checks, path safety, registry generation, and other exact facts. Use model judgment only for semantic work that cannot be settled mechanically.

Validate the smallest affected surface first, then broader governance consistency where the risk or controlling contract requires it. Task-local PASS does not substitute for required formal-run or cross-surface evidence.

Do not change client-facing methodology runtime surfaces from governance authority unless an explicit integration/adoption task authorizes those exact paths.

Communicate with the Owner in Spanish. Write durable governance artifacts in English. End at the next genuine material Owner or formal-authority boundary.
--- source governance/methodology/project-operating-contract.md ---
---
document_id: GOV-METHOD-OPERATING-CONTRACT-001
version: 0.3.0
status: IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
constitutional_authority: NONE
---

# Project Operating Contract

## Purpose and precedence

This contract defines stable operating semantics for repository work. It does not authorize an action, execute a protocol, validate an artifact, accept risk, ratify the Kernel, or open Enforcement Engineering.

Applicable authority descends from platform constraints, the Project Owner's explicit current instruction, repository and closest path-scoped `AGENTS.md`, a formally bound run set, canonical methodology, role protocols, schemas, and finally generated views. A lower layer may specialize but must not silently contradict a higher layer. Historical run snapshots govern their runs even after canonical methodology changes.

## Authority boundaries and preview-first workflow

The Project Owner retains authorization, sequencing, acceptance, risk, publication, and ratification authority. Designer, Adversary, future Controller, implementer, and validator authority is bounded by their explicit contracts. No actor inherits another actor's authority, and no prior authorization is reusable outside its stated scope.

For a material change, first identify intended paths, effects, validation, exclusions, and each separately authorized publication step. Perform only the authorized scope. Modification, staging, commit, push, pull request, merge, tag, release, deployment, and publication are distinct actions.

## Durable truth and status vocabulary

Durable truth is ordered: immutable source and run evidence; explicit decisions and transition records; accepted registry and state records; versioned methodology and schemas; then generated indexes, summaries, reports, and conversational context. Derived views must reconcile with their sources.

- `PROPOSED`: offered for review, without approval or authority.
- `PREPARED`: inputs or contracts are assembled; execution has not occurred.
- `EXECUTED`: the contracted activity occurred; validity is not implied.
- `VALIDATED`: declared checks passed against identified requirements.
- `ACCEPTED`: a competent owner accepted a bounded result or risk.
- `RATIFIED`: competent human constitutional approval was explicitly recorded.
- `IMPLEMENTED`: artifacts or controls exist locally or in the identified system.
- `OPERATIONAL`: implementation is adopted, active, and supported by operational evidence.

A protocol, prompt, package, generated artifact, or output directory is not proof of execution.

## Formal execution, orchestration, and output contract

Formal execution is a role-bound analysis with exact identity, inputs, prompt, applicable controls, outputs, status, and provenance. Orchestration selects, transfers, schedules, or validates work but does not itself perform the role's substantive analysis. A future deterministic Controller may replay declared facts and route allowed transitions; it must not decide constitutional sufficiency.

Every formal analysis intended for review, reuse, implementation, comparison,
or versioning must declare before execution its output artifact path,
filename, format, status, required sections, and validation requirements.

Before any formal execution, an exact Project Owner authorization record must
enter repository custody and bind the run, role, mode, protocol, formal input
package hash, permitted execution count, and forbidden actions. A deterministic
pre-execution gate must reject a missing or mismatched record. Readiness,
package custody, a prepared prompt, or retrospective attestation cannot satisfy
this prospective gate.

The declared output artifact must be materialized at that path, use the declared filename and format, contain every required section, state its honest status, and pass the declared validation before any completion claim.

Formal architecture and implementation reports used as durable design,
review, validation, or implementation evidence must be imported into
repository custody before the associated change is committed.

## Versioned formal-run correction identity

A correction of an immutable completed formal run uses
`<BASE_RUN_ID>-R<N>`, where `BASE_RUN_ID` is the original run identity and
`N` is a positive sequential integer beginning at 1. The first correction of
`KGR-006` is therefore `KGR-006-R1`. A correction identity does not overwrite
or replace the base run, does not consume the next unrelated sequential run
identity, and grants no execution, acceptance, risk, ratification, or phase
authority.

Each correction contract must bind the immutable base input package, base
output package, independent-evaluation result and correction findings, and an
explicit Project Owner authorization. It must state the bounded correction
scope, preserve unaffected meaning and evidence, declare a new output
contract, pass deterministic preparation and completed-output validation, and
receive a new independent evaluation outside the corrected source role's
unilateral control. `R<N>` increments only for a later correction of that same
base run; historical artifacts remain immutable. A pre-execution preparation
failure or interrupted preparation is repaired within the same unexecuted run
identity and is not a correction run.

Review bundles are temporary transport and review artifacts unless an
explicit custody decision registers them for long-term preservation.

## Material prompt custody

A prompt is material when it authorizes material repository modification; defines implementation or review scope, affected files, or validation requirements; prepares or executes a formal run; corrects a material defect; authorizes pull request, merge, tag, release, deployment, or publication beyond the bounded exception below; changes governance methodology, tooling, or authority boundaries; or produces formal architecture, implementation, review, or other durable artifacts. Brief questions, minor clarifications, formatting-only requests, status checks, and messages without repository, execution, authority, or durable-artifact effect are not material.

`OWNER_PUBLICATION_AUTHORIZATION` is a distinct evidence type, not a material implementation prompt, only when it comes explicitly from the Project Owner; identifies an already reviewed immutable change set, bundle, inventory, or commit candidate; adds no implementation scope; authorizes only atomic publication actions such as stage, commit, or push; and does not authorize a pull request, merge, release, execution, ratification, risk acceptance, or additional modification. Failure of any condition keeps the instruction subject to ordinary material-prompt custody.

Qualifying `OWNER_PUBLICATION_AUTHORIZATION` may be preserved through publication evidence, commit metadata, operational records, or a subsequent append-only record. Its custody must not require a new pre-publication repository file that changes the authorized change set. The authorization remains bounded to the identified immutable candidate and named atomic actions; it does not imply authority for any other publication or governance step.

Every material prompt receives a stable `HP-PROMPT-###` identifier and a semantic version. The identifier remains stable across corrections to the same prompt lineage; a correction increments the version and records supersession. Categories identify the prompt function without granting authority. Lifecycle states are `DRAFT`, `APPROVED_NOT_EXECUTED`, `EXECUTED`, `SUPERSEDED`, `ABORTED`, `INVALID_EXECUTION`, and `NOT_PRESERVED`.

Preserve the exact prompt text with its authorization scope, forbidden actions, environment, execution status, and links to resulting artifacts, reports, validation evidence, and commit when available. A material prompt must enter repository custody before or as part of the commit containing the work it authorized or defined. Once executed, its file is immutable execution-contract evidence; correction requires a new semantic version and an explicit supersession link. Prompt existence does not establish execution: execution status and evidence remain separate facts.

After interruption, recover from the repository-custodied prompt and durable worktree or result evidence, verify identity and status, record the interruption and resumption, and do not silently substitute a revised prompt. If an exact historical prompt is unavailable, record `NOT_PRESERVED`, describe the evidence limitation, and never reconstruct a plausible text as original evidence.

Formal run prompt snapshots under `governance/runs/<run>/prompt/` retain authoritative custody for their runs. The prompt catalogue references those snapshots and their run evidence without unnecessary byte duplication. Prompt custody carries only the authority explicitly stated in the prompt and cannot expand, reuse, or transfer it.

Prompt custody does not itself prove that the prompt was executed correctly, that its outputs were validated, or that its authorized actions occurred.

## Record classes

Failure and lesson records capture causal learning. Formal run records capture an execution contract and evidence. Operational logs capture transient chronology. Decision records capture authoritative choices. Incident records govern material security or authority breaches. Methodology parking-lot proposals capture prospective improvements without asserting an observed failure. One class may link to another but never substitutes for it.

Material methodology proposals discovered during orchestration must be captured in the canonical methodology backlog before the current reviewed change is closed. They must not remain only in chat or an external working note.

## Deterministic and cost-aware routing

Use offline scripts for exact parsing, duplicate detection, hashing, path safety, member counts, schema checks, comparisons, indexing, serialization, packaging, and state replay. Reserve capable model reasoning for synthesis and judgment that cannot be represented deterministically. Use the least costly capable model or method, and record actual cost data only when preserved. A model may help design a deterministic check, but repeated application belongs to the check; do not recursively launch agents to settle exact machine facts.

## Failure, learning, and immutability

Material failures, near misses, ambiguities, owner corrections, defects, tooling gaps, and cost waste require triage under `../learning/README.md`. Never silently repair a material error. Preserve the observation, impact, cause, containment, correction, prevention, evidence limits, owner, and validation plan. Missing evidence, timestamps, tokens, and quotes remain explicitly unavailable.

Completed runs, bound artifacts, decisions, validated learning bases, and raw sources are historical evidence. Correct methodology prospectively through new versions and append-only events. Supersede; do not rewrite history to match a newer method.

## Traceability, handoffs, and anti-recursion

Lower-layer artifacts must identify the higher-layer source, applicable version, derived requirement, and validation evidence. A lower layer may add implementation detail but may not relax authority, safety, or evidence requirements without an explicit competent decision.

When context is overloaded, create a durable handoff containing scope and authority, verified facts, artifact identities, completed work, open risks and decisions, exact current status, validation state, and exact next action. The handoff is continuity evidence, not new authority.

Stop recursive review when deterministic validation settles the question or when the next step requires owner authority, independent role judgment, new evidence, or a versioned contract correction.

--- source governance/tools/_lib/strict_yaml.py ---
"""Strict UTF-8 YAML loading with duplicate mapping-key rejection."""

from pathlib import Path
from typing import Any

import yaml


class StrictYAMLError(ValueError):
    pass


class StrictLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: StrictLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    result: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as exc:
            raise StrictYAMLError(f"unhashable mapping key at line {key_node.start_mark.line + 1}") from exc
        if duplicate:
            raise StrictYAMLError(
                f"duplicate mapping key {key!r} at line {key_node.start_mark.line + 1}"
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def loads(text: str, source: str = "<string>") -> Any:
    try:
        return yaml.load(text, Loader=StrictLoader)
    except (yaml.YAMLError, StrictYAMLError) as exc:
        raise StrictYAMLError(f"{source}: {exc}") from exc


def load_bytes(data: bytes, source: str = "<bytes>") -> Any:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise StrictYAMLError(f"{source}: invalid UTF-8") from exc
    return loads(text, source)


def load(path: str | Path) -> Any:
    source = Path(path)
    try:
        data = source.read_bytes()
    except OSError as exc:
        raise StrictYAMLError(f"{source}: {exc}") from exc
    return load_bytes(data, str(source))

--- source governance/tools/validate_governance_state.py ---
#!/usr/bin/env python3
"""Validate the durable KGR-006-R1/GOV-7 direction state across governance surfaces."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib.strict_yaml import load


OUTPUT_SHA256 = "0f496b5b17feb724977f189413f485100b9a66d98b1f79dc05cf45fb60aee66b"
RUN_REL = Path("governance/runs/KGR-006-R1-enforcement-analysis-correction")
REVIEW_REL = Path("governance/reviews/kgr-006-r1-controlled-import-and-owner-review")
DECISION_RECORD_REL = REVIEW_REL / "project-owner-decision-record-v0.2.0.yaml"
EXECUTED_REVIEW_REL = REVIEW_REL / "gov-5-phase-closure-readiness-v0.2.0.yaml"
RATIFICATION_RECORD_REL = Path("governance/reviews/gov-6-ratification/kernel-ratification-decision-record-v0.1.0.yaml")
GOV_7_DIRECTION_RECORD_REL = Path("governance/reviews/gov-7-direction/od-005-gov-7-direction-decision-record-v0.1.0.yaml")
READY_REVIEW_STATUS = "EXECUTED_READY_FOR_PROJECT_OWNER_DECISION"
READY_REVIEW_RESULT = "READY_FOR_PROJECT_OWNER_GOV_5_CLOSURE_DECISION"
ALLOWED_REVIEW_RESULTS = {
    READY_REVIEW_RESULT,
    "RETURN_FOR_REMEDIATION",
    "OWNER_DECISION_REQUIRED_BEFORE_GOV_5_CLOSURE",
    "INVALID_REVIEW",
}


def markdown_state(path: Path, marker: str) -> dict:
    text = path.read_text()
    match = re.search(
        rf"<!-- {re.escape(marker)} -->\n```yaml\n(?P<body>.*?)\n```",
        text,
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"{path}: missing structured marker {marker}")
    from _lib.strict_yaml import loads

    return loads(match.group("body"), f"{path}:{marker}")


def markdown_yaml_section(path: Path, heading: str) -> dict:
    text = path.read_text()
    match = re.search(
        rf"^{re.escape(heading)}\n\n```yaml\n(?P<body>.*?)\n```",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise ValueError(f"{path}: missing structured section {heading}")
    from _lib.strict_yaml import loads

    return loads(match.group("body"), f"{path}:{heading}")


def markdown_table(path: Path, heading: str) -> dict[str, str]:
    text = path.read_text()
    start = text.find(heading)
    if start < 0:
        raise ValueError(f"{path}: missing table section {heading}")
    lines = text[start + len(heading):].splitlines()
    table_lines: list[str] = []
    started = False
    for line in lines:
        if line.startswith("|"):
            started = True
            table_lines.append(line)
        elif started:
            break
    if len(table_lines) < 3:
        raise ValueError(f"{path}: incomplete table section {heading}")
    result: dict[str, str] = {}
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2 or cells[0] in result:
            raise ValueError(f"{path}: invalid table row in {heading}")
        result[cells[0]] = cells[1]
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_executed_review(review: dict, errors: list[str]) -> None:
    expected_flags = {
        "status": READY_REVIEW_STATUS,
        "authority": "NONE",
        "authoritative_to_accept_run": False,
        "authoritative_to_close_phase": False,
        "phase_transition_requested": False,
        "creates_new_governance_layer": False,
        "accepts_risk": False,
        "ratifies_kernel": False,
        "activates_gov_6": False,
    }
    for key, value in expected_flags.items():
        if review.get(key) != value:
            errors.append(f"executed closure review {key} mismatch")
    if review.get("completion_gate", {}).get("overall_satisfied") is not True:
        errors.append("executed closure review GOV-5 completion gate mismatch")
    for gate in ("clause_feasibility_and_coverage", "unresolved_owner_decisions"):
        if review.get("completion_gate", {}).get(gate, {}).get("satisfied") is not True:
            errors.append(f"executed closure review gate {gate} mismatch")

    result_values: list[str] = []
    def collect(value):
        if isinstance(value, dict):
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)
        elif value in ALLOWED_REVIEW_RESULTS:
            result_values.append(value)
    collect(review)
    if result_values != [READY_REVIEW_RESULT] or review.get("review_result") != READY_REVIEW_RESULT:
        errors.append("executed closure review must emit exactly one allowed ready result")

    required_item_fields = set(review.get("item_field_contract", {}).get("required_fields", []))
    expected_item_fields = {
        "id", "category", "item", "current_status", "evidence", "closure_relevance",
        "blocks_gov_5_closure", "legitimate_deferral_destination",
        "future_action_trigger", "owner_decision_required",
    }
    if required_item_fields != expected_item_fields:
        errors.append("executed closure review item field contract mismatch")
    items = review.get("items", [])
    ids = [item.get("id") for item in items if isinstance(item, dict)]
    if len(ids) != len(set(ids)) or len(ids) != len(items):
        errors.append("executed closure review item IDs must be unique")
    for item in items:
        if set(item) != expected_item_fields:
            errors.append(f"executed closure review item field mismatch: {item.get('id')}")
        if not isinstance(item.get("evidence"), list) or not item.get("evidence"):
            errors.append(f"executed closure review item evidence missing: {item.get('id')}")
        if not isinstance(item.get("blocks_gov_5_closure"), bool):
            errors.append(f"executed closure review item blocking value invalid: {item.get('id')}")
    if {f"RR-{number:03d}" for number in range(1, 16)} - set(ids):
        errors.append("executed closure review must classify all fifteen residual risks")
    if {f"SD-{number:03d}" for number in range(1, 5)} - set(ids):
        errors.append("executed closure review must classify all four specialist dependencies")
    if {f"OD-{number:03d}" for number in range(1, 7)} - set(ids):
        errors.append("executed closure review must classify OD-001 through OD-006")
    for required in (
        "HP-FAIL-005", "HP-FAIL-020", "IE-MC-001", "IE-MC-002", "IE-MC-003",
        "MINIMUM-GOV-7-RECOMMENDATION", "PROJECT-OWNER-KGR-006-R1-ACCEPTANCE",
        "PROJECT-OWNER-GOV-5-CLOSURE", "PHASE-TRANSITION-BOUNDARY",
    ):
        if required not in ids:
            errors.append(f"executed closure review missing material item {required}")

    reassessments = review.get("explicit_reassessments", {})
    if reassessments.get("HP-FAIL-005", {}).get("blocks_gov_5") is not False or reassessments.get("HP-FAIL-005", {}).get("blocks_gov_6") is not False:
        errors.append("executed closure review HP-FAIL-005 reassessment mismatch")
    if reassessments.get("HP-FAIL-020_recurrence", {}).get("validated_before_review") is not True:
        errors.append("executed closure review HP-FAIL-020 recurrence validation mismatch")
    if reassessments.get("OD-002_and_OD-003", {}).get("fully_satisfy_decisions_required_before_gov_6") is not True:
        errors.append("executed closure review OD-002/OD-003 reassessment mismatch")
    if reassessments.get("OD-004", {}).get("disposition") != "CORRECTLY_ROUTED_TO_GOV_6":
        errors.append("executed closure review OD-004 disposition mismatch")
    if reassessments.get("OD-005", {}).get("disposition") != "CORRECTLY_ROUTED_AFTER_ANY_RATIFICATION_AND_BEFORE_AFFECTED_GOV_7_WORK":
        errors.append("executed closure review OD-005 disposition mismatch")
    if reassessments.get("OD-006", {}).get("disposition") != "MAY_REMAIN_DEFERRED_UNTIL_RELEVANT_PROVIDER_DATA_PILOT_OR_REAL_WORLD_BOUNDARY":
        errors.append("executed closure review OD-006 disposition mismatch")
    risks = reassessments.get("residual_risks", {})
    if risks.get("exact_count") != 15 or risks.get("accepted") is not False or risks.get("routed") is not True:
        errors.append("executed closure review residual-risk treatment mismatch")
    dependencies = reassessments.get("specialist_dependencies", {})
    if dependencies.get("exact_count") != 4 or dependencies.get("trigger_gated_correctly") is not True:
        errors.append("executed closure review specialist-dependency treatment mismatch")
    if reassessments.get("research_items", {}).get("blocks_constitutional_ratification") is not False:
        errors.append("executed closure review research-item reassessment mismatch")

    disposition = review.get("readiness_disposition", {})
    if disposition.get("gate_satisfied") is not True or disposition.get("remediation_required") != []:
        errors.append("executed closure review readiness disposition mismatch")
    if disposition.get("blocking_items") != [
        "PROJECT-OWNER-KGR-006-R1-ACCEPTANCE", "PROJECT-OWNER-GOV-5-CLOSURE"
    ]:
        errors.append("executed closure review blocking items mismatch")
    state = review.get("resulting_state", {})
    if state.get("KGR-006-R1", {}).get("project_owner_acceptance") != "PENDING":
        errors.append("executed closure review acceptance state mismatch")
    if state.get("GOV-5") != {
        "status": "IN_PROGRESS", "closure_review": READY_REVIEW_STATUS, "closed": False
    }:
        errors.append("executed closure review GOV-5 resulting state mismatch")
    if [state.get(f"GOV-{number}") for number in range(6, 10)] != ["INACTIVE"] * 4:
        errors.append("executed closure review later-phase state mismatch")
    if state.get("kernel") != "0.2.0-proposed/PROPOSED_NOT_RATIFIED":
        errors.append("executed closure review Kernel state mismatch")


def validate_markdown_links(root: Path, paths: list[Path], errors: list[str]) -> None:
    for relative in paths:
        path = root / relative
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = target.split("#", 1)[0]
            if not local:
                continue
            candidate = (path.parent / local).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(f"Markdown link escapes repository: {relative} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Markdown link target missing: {relative} -> {target}")


def validate(root: Path) -> dict:
    errors: list[str] = []
    run = load(root / RUN_REL / "run-manifest.yaml")
    authorization = load(root / RUN_REL / "authorization/execution-authorization.yaml")["execution_authorization"]
    decisions = load(root / DECISION_RECORD_REL)["project_owner_decision_record"]
    ratification = load(root / RATIFICATION_RECORD_REL)["kernel_ratification_decision_record"]
    gov_7_direction = load(root / GOV_7_DIRECTION_RECORD_REL)["gov_7_direction_decision_record"]
    executed_review = load(root / EXECUTED_REVIEW_REL)["phase_closure_readiness_review"]
    registry = load(root / "governance/ARTIFACT_REGISTRY.yaml")
    current_path = root / "governance/CURRENT_STATE.md"
    plan_path = root / "governance/GOVERNANCE_MASTER_PLAN.md"
    readme_path = root / "governance/README.md"
    current = markdown_state(current_path, "GOVERNANCE_STATE_V1")["governance_state"]
    current_durable = markdown_yaml_section(current_path, "## Durable state")
    current_table = markdown_table(current_path, "# Current Governance State")
    plan = markdown_state(plan_path, "GOVERNANCE_STATE_V1")["governance_state"]
    plan_table = markdown_table(plan_path, "## Status summary")
    readme = markdown_state(readme_path, "GOVERNANCE_STATE_V1")["governance_state"]
    log = (root / "governance/DECISION_LOG.md").read_text()

    validate_executed_review(executed_review, errors)

    expected_decisions = {
        "KGR-006-R1": ("ACCEPTED_BY_PROJECT_OWNER", None),
        "GOV-5": ("COMPLETED_CLOSED", None),
        "OD-002": ("RESOLVED", "CONFIRM_EXACT_SCOPE"),
        "OD-003": ("RESOLVED", "PACKET_SUFFICIENT"),
        "OD-004": ("UNRESOLVED", None),
        "OD-005": ("UNRESOLVED", None),
        "OD-006": ("UNRESOLVED", None),
    }
    actual_decisions = {
        item["id"]: (item["status"], item.get("selection"))
        for item in decisions.get("decisions", [])
    }
    if actual_decisions != expected_decisions:
        errors.append("Owner decision record state mismatch")
    decisions_by_id = {item["id"]: item for item in decisions.get("decisions", [])}
    if decisions_by_id.get("KGR-006-R1", {}).get("decision") != "ACCEPT_KGR_006_R1":
        errors.append("Owner decision record KGR-006-R1 acceptance mismatch")
    if decisions_by_id.get("GOV-5", {}).get("decision") != "CLOSE_GOV_5":
        errors.append("Owner decision record GOV-5 closure mismatch")
    if decisions.get("status") != "ACCEPTED_KGR_006_R1_AND_GOV_5_CLOSED":
        errors.append("Owner decision record status mismatch")
    if decisions.get("additional_owner_rationale") != "NOT_PROVIDED":
        errors.append("Owner decision rationale must remain NOT_PROVIDED")

    if ratification.get("document_id") != "GOV-DECISION-RECORD-002" or ratification.get("status") != "RATIFIED_EXACT_KERNEL_0_2_0_GOV_6_CLOSED":
        errors.append("GOV-6 ratification record identity or status mismatch")
    decision = ratification.get("decision", {})
    if decision != {
        "id": "OD-004",
        "selection": "RATIFY_EXACT_KERNEL_0_2_0",
        "status": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
    }:
        errors.append("GOV-6 ratification record OD-004 mismatch")
    kernel = ratification.get("ratified_kernel", {})
    if kernel.get("version") != "0.2.0" or kernel.get("scope") != "HugePlanning level 3 under the Kernel scope rules":
        errors.append("GOV-6 ratification record Kernel version or scope mismatch")
    conditions = ratification.get("ratification_conditions", {})
    if conditions != {
        "residual_risk_accepted": False,
        "enforceability_claimed": False,
        "implementation_status": "NOT_PERFORMED",
        "gov_7_authorized": False,
        "provider_or_real_data_authorized": False,
    }:
        errors.append("GOV-6 ratification conditions mismatch")
    resulting = ratification.get("resulting_state", {})
    expected_ratification_state = {
        "OD-004": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
        "kernel": "0.2.0/RATIFIED",
        "GOV-6": "COMPLETED_CLOSED",
        "GOV-7": "INACTIVE",
        "OD-005": "UNRESOLVED",
        "OD-006": "UNRESOLVED_TRIGGER_GATED",
        "residual-risk-accepted": False,
        "enforcement-implementation": "NOT_PERFORMED",
        "minimum-GOV-7-package": "RECOMMENDATION_ONLY",
    }
    if resulting != expected_ratification_state:
        errors.append("GOV-6 ratification resulting state mismatch")

    if gov_7_direction.get("document_id") != "GOV-DECISION-RECORD-003" or gov_7_direction.get("status") != "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION":
        errors.append("OD-005 direction record identity or status mismatch")
    if gov_7_direction.get("decision") != {
        "id": "OD-005",
        "selection": "ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "status": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
    }:
        errors.append("OD-005 direction record decision mismatch")
    if gov_7_direction.get("accepted") != [
        "seven-component capability direction",
        "one bounded governed transition as the initial target",
        "reuse of existing deterministic custody and validation primitives",
        "read-only tooling and methodology audit",
        "GOV-7 design preparation",
    ]:
        errors.append("OD-005 direction record accepted scope mismatch")
    if gov_7_direction.get("authority_exclusions") != [
        "GOV_7_IMPLEMENTATION",
        "GOV_7_REPOSITORY_MODIFICATIONS_BEYOND_THIS_DECISION_CUSTODY",
        "TECHNOLOGY_OR_FRAMEWORK_ADOPTION",
        "PROVIDER_USE",
        "REAL_DATA_PROCESSING",
        "PILOT_EXECUTION",
        "RESIDUAL_RISK_ACCEPTANCE",
        "OD_006_RESOLUTION",
    ]:
        errors.append("OD-005 direction record authority exclusions mismatch")
    expected_direction_state = {
        "OD-005": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "GOV-7": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "OD-006": "UNRESOLVED_TRIGGER_GATED",
        "minimum-GOV-7-package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
        "residual-risk-accepted": False,
        "enforcement-implementation": "NOT_PERFORMED",
    }
    if gov_7_direction.get("resulting_state") != expected_direction_state:
        errors.append("OD-005 direction record resulting state mismatch")
    if gov_7_direction.get("constitutional_authority") != "PROJECT_OWNER_DIRECTION_DECISION_ONLY":
        errors.append("OD-005 direction record authority mismatch")
    for fragment in (
        "## GOV-DEC-026 — OD-005 minimum GOV-7 direction",
        "Status: RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "Source: Project Owner instruction `HP-PROMPT-022/0.1.0` and `GOV-DECISION-RECORD-003/0.1.0`.",
        "GOV-7 remains `INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY`",
    ):
        if fragment not in log:
            errors.append("OD-005 decision log custody mismatch")

    expected_authorization = {
        "status": "CONSUMED",
        "execution_count_limit": 1,
        "execution_count_consumed": 1,
        "execution_available": False,
        "consumed_by_output_package_sha256": OUTPUT_SHA256,
    }
    for key, value in expected_authorization.items():
        if authorization.get(key) != value:
            errors.append(f"authorization {key} mismatch")
    terminal = authorization.get("terminal_reconciliation", {})
    if terminal.get("decision_log_entry") != "GOV-DEC-020" or terminal.get("creates_new_execution_authority") is not False:
        errors.append("authorization is missing terminal GOV-DEC-020 reconciliation")
    if f"consuming output SHA-256: `{OUTPUT_SHA256}`" not in log:
        errors.append("decision log terminal authorization hash mismatch or reconciliation missing")

    run_decisions = run.get("owner_decisions", {})
    if run.get("run", {}).get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("run manifest KGR-006-R1 state mismatch")
    if run_decisions.get("OD-002") != "RESOLVED_CONFIRM_EXACT_SCOPE" or run_decisions.get("OD-003") != "RESOLVED_PACKET_SUFFICIENT":
        errors.append("run manifest OD-002/OD-003 state mismatch")
    if [run_decisions.get(item) for item in ("OD-004", "OD-005", "OD-006")] != ["UNRESOLVED"] * 3:
        errors.append("run manifest must leave OD-004 through OD-006 unresolved")
    run_review = run.get("phase_closure_review", {})
    if run.get("run", {}).get("readiness") != "ACCEPTED_BY_PROJECT_OWNER_GOV_5_CLOSED_READY_FOR_SEPARATE_GOV_6_DECISION":
        errors.append("run manifest closure-review readiness mismatch")
    if run_review != {
        "path": EXECUTED_REVIEW_REL.as_posix(),
        "status": READY_REVIEW_STATUS,
        "result": READY_REVIEW_RESULT,
        "authoritative_to_accept_run": False,
        "authoritative_to_close_phase": False,
        "gov_5_closed": True,
        "gov_6_activated": False,
    }:
        errors.append("run manifest phase-closure review state mismatch")

    surfaces = {"CURRENT_STATE": current, "GOVERNANCE_MASTER_PLAN": plan, "README": readme}
    expected_surface = {
        "phase": "GOV-6_CLOSED",
        "gov_5_status": "COMPLETED_CLOSED",
        "gov_5_closure_review": READY_REVIEW_STATUS,
        "kgr_006_r1_status": "ACCEPTED_BY_PROJECT_OWNER",
        "authorization_status": "CONSUMED_1_OF_1_NONE_REMAINING",
        "od_002": "RESOLVED_CONFIRM_EXACT_SCOPE",
        "od_003": "RESOLVED_PACKET_SUFFICIENT",
        "od_004": "RESOLVED_RATIFY_EXACT_KERNEL_0_2_0",
        "od_005": "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION",
        "od_006": "UNRESOLVED_TRIGGER_GATED",
        "gov_6_status": "COMPLETED_CLOSED",
        "gov_7_status": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "gov_8_through_gov_9": "INACTIVE",
        "kernel": "0.2.0/RATIFIED",
        "minimum_gov_7_package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
        "risk_accepted": False,
        "enforcement_implementation": "NOT_PERFORMED",
    }
    for name, surface in surfaces.items():
        for key, value in expected_surface.items():
            if surface.get(key) != value:
                errors.append(f"{name} {key} mismatch")

    durable_run = current_durable.get("KGR-006-R1", {})
    if durable_run.get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("CURRENT_STATE Durable state KGR-006-R1 status mismatch")
    if durable_run.get("project_owner_acceptance") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("CURRENT_STATE Durable state Project Owner acceptance mismatch")
    if durable_run.get("owner_decisions") != {
        "OD-002": "RESOLVED_CONFIRM_EXACT_SCOPE",
        "OD-003": "RESOLVED_PACKET_SUFFICIENT",
        "OD-004": "UNRESOLVED",
        "OD-005": "UNRESOLVED",
        "OD-006": "UNRESOLVED",
    }:
        errors.append("CURRENT_STATE Durable state Owner decisions mismatch")
    durable_gov_5 = current_durable.get("GOV-5", {})
    if durable_gov_5.get("status") != "COMPLETED_CLOSED" or durable_gov_5.get("closed") is not True:
        errors.append("CURRENT_STATE Durable state GOV-5 closed status mismatch")
    if durable_gov_5.get("closure_review") != READY_REVIEW_STATUS:
        errors.append("CURRENT_STATE Durable state GOV-5 closure review mismatch")
    if current_durable.get("GOV-6", {}).get("status") != "COMPLETED_CLOSED" or current_durable.get("GOV-7") != {
        "status": "INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY",
        "decision": "OD-005",
        "direction_record": "GOV-DECISION-RECORD-003/0.1.0",
        "minimum_package": "DIRECTION_ACCEPTED_NOT_IMPLEMENTED",
    } or [current_durable.get(f"GOV-{number}", {}).get("status") for number in range(8, 10)] != ["INACTIVE"] * 2:
        errors.append("CURRENT_STATE Durable state GOV-6 closure or later-phase state mismatch")
    if current_durable.get("kernel") != {
        "version": "0.2.0",
        "status": "RATIFIED",
        "scope": "HugePlanning level 3 under the Kernel scope rules",
        "ratification_record": "GOV-DECISION-RECORD-002/0.1.0",
        "enforceability_claimed": False,
        "implementation_status": "NOT_PERFORMED",
        "operational": False,
    }:
        errors.append("CURRENT_STATE Durable state Kernel mismatch")

    current_table_expectations = {
        "Current governance phase": ("GOV-6", "COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "GOV-5 status": ("COMPLETED / CLOSED", "ACCEPTED_BY_PROJECT_OWNER", f"closure review remains `{READY_REVIEW_STATUS}`"),
        "Enforcement Engineering gate": ("CLOSED", "1 of 1"),
        "GOV-6 status": ("COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "Human ratification": ("RATIFIED", "0.2.0"),
        "Phase-transition boundary": ("GOV-6 is closed", "GOV-7 remains inactive pending audit and separate design or implementation authority"),
    }
    for row, fragments in current_table_expectations.items():
        value = current_table.get(row, "")
        if not all(fragment in value for fragment in fragments):
            errors.append(f"CURRENT_STATE table {row} mismatch")

    plan_table_expectations = {
        "GOV-5 Enforcement analysis and derived governance requirements": ("COMPLETED / CLOSED", "KGR-006-R1 accepted by the Project Owner"),
        "GOV-6 Human ratification": ("COMPLETED / CLOSED", "ratified exact Kernel `0.2.0`"),
        "GOV-7 Minimum executable governance bootstrap": ("INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY", "DIRECTION_ACCEPTED_NOT_IMPLEMENTED"),
        "GOV-8 Honest S0a–S1 adoption and regularization": ("PLANNED",),
        "GOV-9 S2 governed pilot": ("PLANNED",),
    }
    for row, fragments in plan_table_expectations.items():
        value = plan_table.get(row, "")
        if not all(fragment in value for fragment in fragments):
            errors.append(f"GOVERNANCE_MASTER_PLAN table {row} mismatch")

    artifacts = {item.get("id"): item for item in registry.get("artifacts", [])}
    if len(artifacts) != len(registry.get("artifacts", [])):
        errors.append("artifact registry IDs must be unique")
    for artifact_id, artifact in artifacts.items():
        value = artifact.get("path")
        if not isinstance(value, str):
            errors.append(f"artifact registry path missing for {artifact_id}")
            continue
        pure = PurePosixPath(value.rstrip("/"))
        if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
            errors.append(f"artifact registry path unsafe for {artifact_id}")
            continue
        if not (root / Path(*pure.parts)).exists():
            errors.append(f"artifact registry path missing for {artifact_id}")
    for required in (
        "KGR-006-R1", "GOV-AUTH-001", "GOV-DECISION-RECORD-001",
        "GOV-VAL-008", "GOV-REVIEW-014", "HP-PROMPT-018",
        "GOV-VAL-009", "GOV-REVIEW-015", "GOV-REVIEW-016", "HP-PROMPT-019", "HP-PROMPT-020",
        "GOV-DECISION-RECORD-002", "HP-PROMPT-021", "GOV-DECISION-RECORD-003", "HP-PROMPT-022",
    ):
        if required not in artifacts:
            errors.append(f"artifact registry missing {required}")
        elif not (root / artifacts[required]["path"]).exists():
            errors.append(f"artifact registry path missing for {required}")
    auth_entry = artifacts.get("GOV-AUTH-001", {})
    if auth_entry.get("status") != "CONSUMED" or OUTPUT_SHA256 not in " ".join(auth_entry.get("notes", [])):
        errors.append("artifact registry authorization terminal state mismatch")
    run_entry = artifacts.get("KGR-006-R1", {})
    if run_entry.get("status") != "ACCEPTED_BY_PROJECT_OWNER":
        errors.append("artifact registry KGR-006-R1 state mismatch")
    direction_entry = artifacts.get("GOV-DECISION-RECORD-003", {})
    if direction_entry.get("status") != "RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION" or direction_entry.get("source_path") != "governance/prompts/orchestration/HP-PROMPT-022-record-od-005-gov-7-direction-decision-v0.1.0.md":
        errors.append("artifact registry OD-005 direction decision custody mismatch")
    prompt_entry = artifacts.get("HP-PROMPT-022", {})
    if prompt_entry.get("status") != "EXECUTED" or prompt_entry.get("aliases") != ["GOV-DEC-026"]:
        errors.append("artifact registry HP-PROMPT-022 custody mismatch")

    immutable = load(root / REVIEW_REL / "kgr-006-r1-import-validation-v0.1.0.yaml")["subject"]
    for group, directory in (("source_package", "outputs"), ("evaluation_package", "evaluation")):
        for item in immutable[group]["inventory"]:
            path = root / RUN_REL / directory / item["member"]
            if sha256(path) != item["sha256"]:
                errors.append(f"immutable artifact hash mismatch: {path.relative_to(root)}")

    validate_markdown_links(root, [
        Path("governance/CURRENT_STATE.md"),
        Path("governance/GOVERNANCE_MASTER_PLAN.md"),
        Path("governance/README.md"),
        Path("governance/learning/FAILURE_AND_LESSONS_INDEX.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-019-gov-5-phase-closure-readiness-review-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-020-accept-kgr-006-r1-and-close-gov-5-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-021-ratify-kernel-0-2-0-and-close-gov-6-v0.1.0.md"),
        Path("governance/prompts/orchestration/HP-PROMPT-022-record-od-005-gov-7-direction-decision-v0.1.0.md"),
        REVIEW_REL / "gov-5-phase-closure-readiness-implementation-report-v0.1.0.md",
    ], errors)

    return {"result": "VALID" if not errors else "INVALID", "diagnostics": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["result"] == "VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())

--- source governance/tools/validate_prompts.py ---
#!/usr/bin/env python3
"""Validate durable material-prompt custody without proving execution."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

from _lib.strict_yaml import StrictYAMLError, loads


STATUSES = {
    "DRAFT", "APPROVED_NOT_EXECUTED", "EXECUTED", "SUPERSEDED",
    "ABORTED", "INVALID_EXECUTION", "NOT_PRESERVED",
}
CATEGORIES = {"ORCHESTRATION", "FORMAL_RUN", "REVIEW", "CORRECTION", "PUBLICATION", "ARCHITECTURE"}
MATERIAL_PROMPT = "MATERIAL_PROMPT"
OWNER_PUBLICATION_AUTHORIZATION = "OWNER_PUBLICATION_AUTHORIZATION"
PROMPT_RE = re.compile(r"^HP-PROMPT-(\d{3})$")
VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
EXACT_MARKER = "\n## Exact executed text\n\n"
REQUIRED = {
    "prompt_id", "version", "category", "status", "purpose", "target_environment",
    "repository_branch", "repository_base_head", "authorization_scope", "forbidden_actions",
    "exact_text_preserved", "execution_interrupted", "execution_resumed", "result_artifacts",
    "result_commit", "supersedes",
}


class PromptError(ValueError):
    pass


def parse_file(path: Path) -> tuple[dict, str, bytes]:
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise PromptError(f"{path}: unreadable UTF-8: {exc}") from exc
    if not text.startswith("---\n"):
        raise PromptError(f"{path}: YAML front matter is required")
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise PromptError(f"{path}: unterminated YAML front matter")
    try:
        metadata = loads(text[4:boundary], str(path))
    except StrictYAMLError as exc:
        raise PromptError(str(exc)) from exc
    if not isinstance(metadata, dict):
        raise PromptError(f"{path}: front matter must be a mapping")
    return metadata, text[boundary + 5 :], raw


def safe_repo_path(root: Path, value: str, label: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or "\\" in value or any(part in ("", ".", "..") for part in pure.parts):
        raise PromptError(f"{label}: unsafe repository path")
    candidate = (root / Path(*pure.parts)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise PromptError(f"{label}: repository path escapes root") from exc
    return candidate


def validate_metadata(root: Path, path: Path, metadata: dict, body: str) -> None:
    missing = sorted(REQUIRED - metadata.keys())
    if missing:
        raise PromptError(f"{path}: missing front matter fields: {', '.join(missing)}")
    prompt_id = metadata["prompt_id"]
    version = metadata["version"]
    if not isinstance(prompt_id, str) or not PROMPT_RE.fullmatch(prompt_id):
        raise PromptError(f"{path}: invalid prompt_id")
    if not isinstance(version, str) or not VERSION_RE.fullmatch(version):
        raise PromptError(f"{path}: invalid semantic version")
    if metadata["status"] not in STATUSES:
        raise PromptError(f"{path}: invalid lifecycle status")
    if metadata["category"] not in CATEGORIES:
        raise PromptError(f"{path}: invalid category")
    evidence_type = metadata.get("evidence_type", MATERIAL_PROMPT)
    if evidence_type == OWNER_PUBLICATION_AUTHORIZATION:
        raise PromptError(
            f"{path}: OWNER_PUBLICATION_AUTHORIZATION is publication evidence, not a material prompt custody record"
        )
    if evidence_type != MATERIAL_PROMPT:
        raise PromptError(f"{path}: invalid evidence_type")
    for field in ("authorization_scope", "forbidden_actions", "result_artifacts"):
        if not isinstance(metadata[field], list) or any(not isinstance(item, str) or not item for item in metadata[field]):
            raise PromptError(f"{path}: {field} must be a string list")
    for field in ("exact_text_preserved", "execution_interrupted", "execution_resumed"):
        if not isinstance(metadata[field], bool):
            raise PromptError(f"{path}: {field} must be boolean")
    if metadata["status"] == "EXECUTED" and not metadata["result_artifacts"]:
        raise PromptError(f"{path}: executed prompt requires result references")

    custody = metadata.get("custody", "EXACT_TEXT")
    if custody == "FORMAL_RUN_REFERENCE":
        authoritative = metadata.get("authoritative_prompt_path")
        if not isinstance(authoritative, str) or not authoritative.startswith("governance/runs/") or "/prompt/" not in authoritative:
            raise PromptError(f"{path}: formal run reference requires an authoritative run prompt path")
        if not safe_repo_path(root, authoritative, str(path)).is_file():
            raise PromptError(f"{path}: authoritative formal run prompt is unavailable")
        if metadata["exact_text_preserved"] or EXACT_MARKER in body:
            raise PromptError(f"{path}: formal run reference must not duplicate exact prompt text")
    elif custody != "EXACT_TEXT":
        raise PromptError(f"{path}: invalid custody mode")
    elif metadata["status"] == "NOT_PRESERVED":
        if metadata["exact_text_preserved"] or EXACT_MARKER in body:
            raise PromptError(f"{path}: NOT_PRESERVED cannot claim or contain exact text")
        if not isinstance(metadata.get("evidence_limitation"), str) or not metadata["evidence_limitation"].strip():
            raise PromptError(f"{path}: NOT_PRESERVED requires an evidence limitation")
    else:
        if not metadata["exact_text_preserved"]:
            raise PromptError(f"{path}: preserved prompt must declare exact_text_preserved")
        if EXACT_MARKER not in body:
            raise PromptError(f"{path}: missing exact prompt text")
        exact = body.split(EXACT_MARKER, 1)[1]
        if exact.endswith("\n"):
            exact = exact[:-1]
        if not exact:
            raise PromptError(f"{path}: missing exact prompt text")
        expected = metadata.get("exact_text_sha256")
        if not isinstance(expected, str) or not SHA_RE.fullmatch(expected):
            raise PromptError(f"{path}: exact_text_sha256 is required")
        actual = hashlib.sha256(exact.encode("utf-8")).hexdigest()
        if actual != expected:
            raise PromptError(f"{path}: exact prompt text hash mismatch")


def validate_immutability(root: Path, path: Path, raw: bytes) -> None:
    try:
        relative = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"HEAD:{relative}"],
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
    )
    if result.returncode != 0:
        return
    try:
        committed, _, _ = parse_bytes(result.stdout, relative)
    except PromptError:
        return
    if committed.get("status") == "EXECUTED" and result.stdout != raw:
        raise PromptError(f"{path}: executed prompt is immutable after commit")


def parse_bytes(raw: bytes, label: str) -> tuple[dict, str, bytes]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise PromptError(f"{label}: unreadable UTF-8") from exc
    if not text.startswith("---\n") or (boundary := text.find("\n---\n", 4)) < 0:
        raise PromptError(f"{label}: invalid front matter")
    try:
        metadata = loads(text[4:boundary], label)
    except StrictYAMLError as exc:
        raise PromptError(str(exc)) from exc
    return metadata, text[boundary + 5 :], raw


def validate(root: Path) -> dict:
    prompt_root = root / "governance/prompts"
    paths = sorted(path for path in prompt_root.rglob("*.md") if path.name != "README.md")
    registry = loads((root / "governance/ARTIFACT_REGISTRY.yaml").read_text(encoding="utf-8"), "governance/ARTIFACT_REGISTRY.yaml")
    artifacts = registry.get("artifacts", [])
    if not isinstance(artifacts, list):
        raise PromptError("governance/ARTIFACT_REGISTRY.yaml: artifacts must be a list")
    identities: dict[tuple[str, str], Path] = {}
    lineage_versions: dict[str, set[str]] = {}
    for path in paths:
        raw = path.read_bytes()
        if raw.startswith(b"---\n"):
            metadata, body, raw = parse_file(path)
            validate_metadata(root, path, metadata, body)
            identity = (metadata["prompt_id"], metadata["version"])
            validate_immutability(root, path, raw)
        else:
            relative = path.relative_to(root).as_posix()
            matches = [item for item in artifacts if item.get("path") == relative and item.get("artifact_type") == "exact_orchestration_prompt"]
            if len(matches) != 1:
                raise PromptError(f"{path}: verbatim prompt requires exactly one exact_orchestration_prompt registry entry")
            item = matches[0]
            prompt_id, version, expected = item.get("id"), item.get("version"), item.get("source_sha256")
            if not isinstance(prompt_id, str) or not PROMPT_RE.fullmatch(prompt_id) or not isinstance(version, str) or not VERSION_RE.fullmatch(version):
                raise PromptError(f"{path}: verbatim prompt registry identity is invalid")
            if not isinstance(expected, str) or not SHA_RE.fullmatch(expected) or hashlib.sha256(raw).hexdigest() != expected:
                raise PromptError(f"{path}: verbatim prompt registry hash mismatch")
            identity = (prompt_id, version)
        if identity in identities:
            raise PromptError(f"duplicate prompt identity {identity[0]} v{identity[1]}: {identities[identity]} and {path}")
        identities[identity] = path
        lineage_versions.setdefault(identity[0], set()).add(identity[1])
    if not paths:
        raise PromptError("no material prompt custody records found")
    return {"prompts": len(paths), "lineages": len(lineage_versions), "valid": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    try:
        result = validate(args.root.resolve())
    except PromptError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
