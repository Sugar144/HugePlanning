---
document_id: GOV-GEN-G1B-CONTRACT-001
title: HugePlanning Governance Generalization — G1B Governance Capability Map Contract
program_id: GOV-GEN-AUD-001
phase: G1B
status: ACCEPTED_AND_AUTHORIZED_FOR_G1B_EXECUTION
version: 0.1.0
authority: CONTRACT_FRAME_AND_EXECUTION_AUTHORIZATION
execution_authority: GRANTED_BY_GOV_GEN_DECISION_002_NO_FURTHER_GATE
repository_modification_authority: SCOPED_TO_GOV_GEN_AUD_001_G1B_DIRECTORY_ONLY
implementation_authority: NONE
target_architecture_authority: NONE
supersedes: GOV-GEN-G1B-P-CONTRACT-001/0.1.0
parent_baseline: HP-GOV-GEN-G0-CB-001/0.1.0
parent_contract: GOV-GEN-G1A-CONTRACT-001/0.1.0
parent_evidence:
  - GOV-GEN-DECISION-001/0.1.0 (G1A Owner acceptance, canonical)
  - GOV-GEN-G1A-REPORT-001
  - G1A-artifact-authority-index.jsonl (679 rows, accepted)
authorizing_decision: GOV-GEN-DECISION-002/0.1.0
expected_repository: /home/sugar/Documents/HugePlanning-governance
expected_branch: governance/kernel-designer-revision-v0.1
expected_starting_commit: 1899a3e7b41e9b4930a5d0f7f0b7e9d542fcb8dc
---

# GOV-GEN-G1B — Governance Capability Map Contract

## 0. Supersession

This contract replaces the proposed `GOV-GEN-G1B-P-CONTRACT-001/0.1.0`
(`~/Downloads/HugePlanning-Governance-Generalization-G1B-P-Contract-PROPOSED.md`).
That proposal defined a preparation-only packet (`G1B-P`) whose accepted
output would then gate a separate, automatically multiplying execution
topology: `G1B-X1...Xn` (one contract per evidence family) followed by
`G1B-R` (reconciliation) and `G1B-V` (independent review) — up to sixteen or
more separately governed sessions for one 679-row index.

Per `GOV-GEN-DECISION-002/0.1.0`, that topology is replaced here with **one**
coherent G1B task. `context decomposition != task decomposition`: the G1A
index may still be partitioned into evidence families for progressive
retrieval inside that one task, but those families are navigation steps, not
separate governed execution packets. The G1B-P frame's substantive content —
the capability/gap record schema, the domain-coverage checklist, and the
evidence-family partition — is preserved below, restated as internal
navigation structures of this single contract rather than as inputs to a
follow-on contract-drafting packet.

## 1. Objective

Produce exactly one accepted result, the **Governance Capability Map**: a
single reconciled document enumerating the capabilities and capability gaps
realized (or absent) across the accepted 679-row G1A index, checked against
every cross-cutting capability domain named in §5, with every capability and
gap record conforming to the schema in §6.

G1B does not itself select, recommend, or compare a target architecture,
decide kernel repository ownership, create a repository, extract or migrate
the kernel, implement delegated operational authority, or modify any
`AGENTS.md`/`CLAUDE.md` surface. It remains factual, generalization-relevant
analysis only. Classification of generality, coupling, operating burden, and
extraction burden remain G2A/G2B/G3 territory, per
`HP-GOV-GEN-G0-CB-001/0.1.0` §6.2–§6.4 and §7.

## 2. Accepted start

### 2.1 Canonical planning inputs

Read before execution, in this order:

```text
governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-001-g1a-acceptance-v0.1.0.yaml
~/Downloads/GOV-GEN-G1A-001/G1A-report.md
~/Downloads/HugePlanning-Governance-Generalization-Compact-Conceptual-Baseline-ACCEPTED.md
  (§6 capability-model dimensions, §7 topology, §8 phase-vs-packet, §11
  decomposition controls — sections only; do not reread the full document
  if already internalized from a prior session)
governance/AGENTS.md
```

Read from `G1A-artifact-authority-index.jsonl` progressively, one navigation
step (§7) at a time:

- structural counts for that step's `path_family`/`path_subfamily` first;
- row bodies for that step only, to name and record capabilities/gaps;
- do not open row bodies belonging to a later navigation step before the
  current step's records are written — this is what keeps the single task
  bounded, not a hard session split.

### 2.2 Expected repository state

```yaml
repository: Sugar144/HugePlanning
worktree: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
expected_HEAD_at_reconciliation: 1899a3e7b41e9b4930a5d0f7f0b7e9d542fcb8dc
worktree_status_at_reconciliation: CLEAN
```

At the start of any future G1B execution session, run read-only
verification (`pwd`, `git branch --show-current`, `git rev-parse HEAD`,
`git status --short`, `git rev-parse --show-toplevel`) and confirm the
accepted G1A index still sums to 679 rows across 14 path families before
proceeding. On any mismatch: do not generate capability/gap records; write
one external blocker report; stop for Owner disposition. A moved HEAD or a
changed G1A index is not silently adopted as a new baseline.

## 3. Execution model — single task, progressive evidence navigation

G1B runs as **one `L1_CLEAN_SESSION`** (may span multiple working turns of
the same governed task, not multiple separately authorized contracts). It
produces and incrementally extends **one** Governance Capability Map
document, walking the navigation order in §7 rather than branching into
per-family contracts.

```yaml
recommended_executor:
  class: STRUCTURED_ANALYSIS
  avoid: [multiple subagents as separately governed sessions, an
    architecture/research-grade model for identity extraction]
session_topology: L1_CLEAN_SESSION
subagents: NOT_REQUIRED_FOR_IDENTITY_EXTRACTION
goal_loop: NOT_REQUIRED
network_access: NOT_REQUIRED
```

### 3.1 What stays inside the one task

- walking the 13 navigation steps of §7 in order;
- extracting and recording capability/gap entries per §6 for each step;
- checking off §5 domain coverage as evidence for each domain is found or
  confirmed absent;
- reconciling duplicate or cross-cutting capabilities discovered across
  steps into the same growing document (the function `G1B-R` would have
  performed in the superseded topology is now continuous reconciliation
  inside this one task, not a separate follow-on contract);
- a final self-check pass over the completed map before it is reported
  `G1B_READY_FOR_OWNER_REVIEW` (the function `G1B-V` would have performed is
  now a same-session self-review; it does not require a separate governed
  session unless §3.2 triggers).

### 3.2 The only valid reason to split into another governed session

Split G1B into a new governed session **only** if execution discovers a
genuinely independent:

- **decision** boundary (a choice only the Owner can make, not implied by
  already-accepted evidence);
- **authority** boundary (work that requires authority this contract does
  not grant — e.g. touching a HugePlanning worktree file, AGENTS.md/
  CLAUDE.md, AET, CWG, or SVP);
- **validation** boundary (a check that cannot be performed deterministically
  or within this task's own review);
- **acceptance** boundary (output that is not itself part of the one
  Governance Capability Map, e.g. an architecture recommendation); or
- **material-risk** boundary (a finding whose consequence exceeds bounded
  factual/generalization analysis, e.g. discovery of a defect requiring its
  own correction cycle).

Evidence-family size or count is explicitly **not** such a boundary. Finding
that `runs` has 202 rows is a navigation-load fact, not an independence
trigger — it is handled by sub-stepping within §7, not by opening a new
contract. If a split does trigger, stop at the boundary, write one external
note naming the specific trigger, and return to the Owner; do not silently
keep going past it and do not retroactively rename the split step "G1B-X".

## 4. Authority and write scope

### 4.1 Gating

Contract acceptance (this document, via `GOV-GEN-DECISION-002/0.1.0`) **is**
G1B's execution authorization. `GOV-GEN-DECISION-002/0.1.0` records G1B as
the next authorized governance-generalization phase; no further, separate
Owner authorization gate exists before a future session may act under §4.2.
A future G1B session begins directly at §2's read-only verification and
proceeds into §3–§8 without requesting or waiting on a new
`GOV-GEN-DECISION-NNN`. This does not mean G1B has executed — no session has
yet walked §7 or produced a capability/gap record — only that no additional
Owner gate stands between an accepted contract and that execution.

### 4.2 Permitted, execution already authorized

- read the files named in §2.1, progressively per §3.1;
- run the read-only Git commands in §2.2;
- extract, name, and record capability and capability-gap entries
  conforming exactly to §6;
- check off and record §5 domain coverage;
- reconcile duplicate/cross-cutting entries within the same map;
- create or extend the Governance Capability Map deliverable under
  `governance/audits/GOV-GEN-AUD-001-governance-generalization/G1B/`
  (continuing this reconciliation's custody direction; a future Owner
  decision may relocate it, but it is not left external-only by default).

### 4.3 Forbidden, always

The executor must not, at any point in G1B:

- modify, create, rename, or delete anything inside either HugePlanning
  worktree outside `governance/audits/GOV-GEN-AUD-001-governance-generalization/`;
- run any Git command beyond the read-only ones in §2.2, or commit/push
  without separate authorization;
- classify generality, coupling, maturity, operating burden, extraction
  burden, or candidate disposition (G0-CB §6.4 `synthesis_fields`; G2A/G2B/G3
  territory);
- select, recommend, or compare a target architecture;
- choose or authorize kernel repository ownership;
- create a new repository;
- extract or migrate the governance kernel;
- implement, projectize, or modify any `AGENTS.md`/`CLAUDE.md` surface
  anywhere;
- modify AET, CWG, or SVP;
- advance or modify `GOV-AUD-001` or consume `GOV-AUD-AUTH-004`;
- produce more than one principal deliverable (the Governance Capability
  Map) without an explicit §3.2 split, recorded as such.

## 5. Cross-cutting capability-domain coverage checklist

Twelve domains cut across directory structure and must each resolve to at
least one navigation step (§7) responsible for finding realizing
capabilities or recording an explicit gap. `UNASSIGNED` blocks completion.

| # | Domain | Candidate evidence locations | Assigned navigation step(s) | Status |
|---|---|---|---|---|
| 1 | `OWNER_RESERVED_AUTHORITY` | `DECISION_LOG.md` (ROOT), `audits/*/decisions` | NAV-01, NAV-08 | ASSIGNED |
| 2 | `DELEGATED_OPERATIONAL_AUTHORITY` | `methodology/`, `skills/` | NAV-04, NAV-10 | ASSIGNED |
| 3 | `BOUNDED_TECHNICAL_DISCRETION` | `tools/`, `tests/` | NAV-13, NAV-12 | ASSIGNED |
| 4 | `PROVIDER_NEUTRAL_SEMANTICS` | `kernel/`, `schemas/` | NAV-02, NAV-09 | ASSIGNED |
| 5 | `EXECUTOR_EQUIVALENCE` | `prompts/`, `methodology/` | NAV-05, NAV-04 | ASSIGNED |
| 6 | `PROJECTION_SURFACE_GOVERNANCE` | `RUNTIME_PROJECTION_MAP.yaml` (ROOT), `kernel/` | NAV-01, NAV-02 | ASSIGNED |
| 7 | `PROJECTION_DRIFT_CONTROL` | `kernel/`, `reviews/` | NAV-02, NAV-06 | ASSIGNED |
| 8 | `CLEAN_SESSION_EXECUTION` | `runs/`, `prompts/` | NAV-07, NAV-05 | ASSIGNED |
| 9 | `TASK_CONTEXT_DECOMPOSITION` | `methodology/`, `runs/` | NAV-04, NAV-07 | ASSIGNED |
| 10 | `EVIDENCE_NAVIGATION` | `sources/`, `learning/` | NAV-11, NAV-03 | ASSIGNED |
| 11 | `VALIDATION_PUBLICATION_STOP_BOUNDARY` | `tests/`, `schemas/` (validation merged) | NAV-12, NAV-09 | ASSIGNED |
| 12 | `GOVERNANCE_LEVEL_OR_PROFILE` | `DECISION_LOG.md` (ROOT), `methodology/` | NAV-01, NAV-04 | ASSIGNED |

Candidate locations are starting hypotheses for where a domain is *most
likely* realized, drawn from directory naming only; they do not pre-judge
what execution actually finds. If a navigation step's evidence does not
realize a domain assigned to it, execution records an explicit gap (§6.3),
it does not leave the domain silently unassigned.

## 6. Capability and gap record schema

Every capability and gap record produced during G1B execution must conform
to this schema. This contract itself emits **zero** populated instances.

### 6.1 Baseline fields (accepted, `HP-GOV-GEN-G0-CB-001/0.1.0` §6.1)

```yaml
g1b_fields:
  - capability_id
  - obligation
  - realized_by
  - requires
  - cross_cutting
  - duplication
  - provisional_maturity
  - unresolved_items
```

### 6.2 Required extension — fact-only observation fields

Every value must be an observed fact (a verbatim citation, an explicit enum
state, or `NOT_OBSERVED`/`UNRESOLVED`) — never a judgment, recommendation, or
inferred intent.

```yaml
g1b_extended_fields:
  capability_domain:            # array, one or more, closed set — the 12 in §5
  authority_layer_observed:     [OWNER_RESERVED, DELEGATED_OPERATIONAL, BOUNDED_DISCRETION, NOT_APPLICABLE, UNRESOLVED]
  provider_references_observed: {type: array of verbatim tokens, example: ["Claude Code", "Codex"], empty_array_means: no provider/tool token found}
  executor_equivalence_observed: [EXPLICIT_BOTH_NAMED, EXPLICIT_ONE_NAMED_ONLY, IMPLICIT_TOOL_AGNOSTIC, NOT_APPLICABLE, UNRESOLVED]
  projection_relationship_observed: [GOVERNANCE_SOURCE, PROJECTION_SURFACE, BOTH_OBSERVED, NOT_APPLICABLE, UNRESOLVED]
  drift_control_observed:       [MECHANISM_PRESENT, MECHANISM_PLANNED_NOT_IMPLEMENTED, MECHANISM_ABSENT, NOT_APPLICABLE, UNRESOLVED]
  session_topology_observed:    [L0, L1, L2, L3, NOT_SPECIFIED, NOT_APPLICABLE]
  decomposition_mechanism_observed: {present: true|false, citation: string|NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true|false, citation: string|NONE_OBSERVED}
  boundary_type_observed:       {type: array, values: [VALIDATION, PUBLICATION, STOP, NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {type: string, value: verbatim citation or NONE_OBSERVED}
```

### 6.3 Gap record (missing capability)

```yaml
missing_capability_fields:
  - gap_id
  - capability_domain     # same closed set as §6.2
  - expected_basis        # citation implying this capability should exist
  - evidence_searched     # path_family/subfamily searched
  - status                # ABSENT | PLANNED_NOT_IMPLEMENTED | PARTIALLY_REALIZED
  - source_refs
```

### 6.4 Prohibited fields

Structurally rejected — reserved for G2A/G2B/G3:

```yaml
prohibited:
  - generality
  - target_layer
  - operating_burden
  - extraction_burden
  - candidate_disposition
  - recommendation
  - description
  - summary
```

## 7. Evidence-family navigation order

Base unit: the accepted G1A `path_family` breakdown (`G1A-report.md` §5),
already deterministically counted, accepted, and summing to 679. Grouped
into thirteen bounded navigation steps for the one G1B task — every row
belongs to exactly one step, small families are merged rather than left
unassigned, and the two disproportionately large families are marked for
subfamily-bounded sub-stepping at execution time rather than assigned whole.

| Step | Evidence family (rows) | Rows | Notes |
|---|---|---|---|
| NAV-01 | ROOT + archive | 12 | merged: archive (1) too small to justify its own step |
| NAV-02 | kernel | 3 | |
| NAV-03 | learning | 62 | |
| NAV-04 | methodology | 20 | |
| NAV-05 | prompts | 37 | |
| NAV-06 | reviews | 37 | |
| NAV-07 | runs | 202 | split into subfamily-bounded sub-steps at execution time (G0-CB §11); subfamily counts to be read from the accepted index, not fixed here |
| NAV-08 | audits | 112 | split into subfamily-bounded sub-steps at execution time (G0-CB §11); subfamily counts to be read from the accepted index, not fixed here |
| NAV-09 | schemas + validation | 14 | merged: validation (1) too small to justify its own step |
| NAV-10 | skills | 9 | |
| NAV-11 | sources | 53 | |
| NAV-12 | tests | 76 | |
| NAV-13 | tools | 42 | |

Row-count parity: `12+3+62+20+37+37+202+112+14+9+53+76+42 = 679`, matching
the accepted G1A index exactly.

Sub-stepping NAV-07 and NAV-08 by `path_subfamily` remains **navigation**,
not a new governed session boundary (§3.2): it changes how many turns the
one G1B task takes to walk those two families, not how many contracts or
Owner authorizations exist.

## 8. Deliverable and custody

One principal deliverable:

```text
governance/audits/GOV-GEN-AUD-001-governance-generalization/G1B/
  GOV-GEN-G1B-CAPABILITY-MAP-001.md (or .yaml)   the Governance Capability Map
  GOV-GEN-G1B-CAPABILITY-MAP-001.manifest.sha256
```

created only once a G1B session actually begins walking §7 (execution is
already authorized per §4.1; this deliverable simply does not exist until
that session runs). No interim
per-navigation-step deliverable is required or permitted to stand alone as
if it were a separate packet output; progressive navigation writes into the
one growing map.

## 9. Validation (required at future execution completion)

1. repository identity matches §2.2 before and after; worktree clean before
   and after outside `G1B/`, HEAD unchanged;
2. every one of the 14 accepted `path_family` entries is represented,
   directly or via its NAV step, with no family silently dropped;
3. every one of the 12 `capability_domain` values in §5 has confirmed
   coverage (a realizing capability or an explicit gap record), not merely
   an assigned candidate location;
4. every capability and gap record conforms to §6, rejects every §6.4
   prohibited field, and uses only the closed enums listed;
5. exactly one principal deliverable exists, unless a §3.2 split was
   triggered and externally recorded;
6. no capability judgment, architecture recommendation, or target-layer
   classification exists anywhere in the output;
7. hash manifest verifies.

Any failed check results in `G1B_BLOCKED_VALIDATION_FAILED`; do not mark G1B
complete.

## 10. Completion and terminal statuses

```text
G1B_READY_FOR_OWNER_REVIEW
G1B_BLOCKED_BASELINE_DRIFT
G1B_BLOCKED_VALIDATION_FAILED
G1B_BLOCKED_ENVIRONMENT_LIMITATION
G1B_RETURN_FOR_CONTRACT_CORRECTION
G1B_SPLIT_REQUIRED_<TRIGGER>          # only if §3.2 fires; names the exact trigger
```

The executor does not accept its own outputs. Owner acceptance is a separate
act, exactly as under `GOV-GEN-G1A-CONTRACT-001/0.1.0` §13.

## 11. Mandatory stop

This contract's own acceptance (via `GOV-GEN-DECISION-002/0.1.0`) already
authorizes execution of §3–§8 by a future G1B session — see §4.1. It does
not itself perform that execution, and it does not authorize:

- extraction, naming, or recording of a single capability or gap **within
  this reconciliation** (a future G1B session performs that under the
  authorization already granted here, not this document's own drafting);
- selection or recommendation of a target architecture;
- modification or integration of any HugePlanning artifact outside this
  contract's own custody path;
- commit, push, pull request, merge, or release of G1B outputs;
- modification of AET, CWG, or SVP.

```text
GOV-GEN-G1B-CONTRACT-001/0.1.0 ACCEPTED_AND_AUTHORIZED_FOR_G1B_EXECUTION
→ (no further Owner authorization gate) one governed G1B session walks §7,
  producing one Governance Capability Map
→ Owner accepts, rejects, or requests bounded correction
→ (only after acceptance) Owner separately authorizes G2A/G2B
```
