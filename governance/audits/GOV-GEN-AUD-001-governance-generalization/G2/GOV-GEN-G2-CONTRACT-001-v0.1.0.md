---
document_id: GOV-GEN-G2-CONTRACT-001
title: HugePlanning Governance Generalization — G2 Governance Generalization Assessment Contract
program_id: GOV-GEN-AUD-001
phase: G2
status: ACCEPTED_AND_AUTHORIZED_FOR_G2_EXECUTION
version: 0.1.0
authority: CONTRACT_FRAME_AND_EXECUTION_AUTHORIZATION
execution_authority: GRANTED_BY_PROJECT_OWNER_HP_PROMPT_043_NO_FURTHER_GATE
repository_modification_authority: SCOPED_TO_GOV_GEN_AUD_001_G2_DIRECTORY_AND_MINIMUM_STATE_RECONCILIATION_ONLY
implementation_authority: NONE
target_architecture_authority: NONE
supersedes: null
parent_baseline: HP-GOV-GEN-G0-CB-001/0.1.0
parent_contract: GOV-GEN-G1B-CONTRACT-001/0.1.0
parent_evidence:
  - GOV-GEN-DECISION-003/0.1.0 (G1B Owner acceptance, canonical)
  - GOV-GEN-G1B-CAPABILITY-MAP-001/0.1.0 (88 capability records, 6 gap records, accepted)
authorizing_source: HP-PROMPT-043/0.1.0 (Project Owner, direct authorization of canonical definition, execution, and one bounded commit in a single governed unit)
expected_repository: /home/sugar/Documents/HugePlanning-governance
expected_branch: governance/kernel-designer-revision-v0.1
expected_starting_commit: a0b3c023074edf8bcf49dfe4f1a4b0cfb1f90fd4
---

# GOV-GEN-G2 — Governance Generalization Assessment Contract

## 0. Relationship to G1B

G1B produced one factual, judgment-free Governance Capability Map: 88
capability records and 6 gap records, each with observed fields only
(`generality`, `target_layer`, `operating_burden`, `extraction_burden`,
`candidate_disposition`, `recommendation`, `description`, and `summary`
were structurally prohibited — G1B contract §6.4). G1B's own §1 explicitly
reserved that classification territory for "G2A/G2B/G3."

This contract is G2 as the Project Owner has now defined and authorized it
in `HP-PROMPT-043/0.1.0`: **Governance Generalization Assessment**, a single
coherent classification pass over the accepted G1B map, applying exactly
the axes the Owner named (generality, reuse readiness, maturity, coupling,
duplication, evidence reference, material limitation), plus the two
explicit program-requirement evaluations (Delegated Operational Authority,
Provider-Neutral Governance). It does not reopen or contradict G1B's
factual observations; it classifies them.

## 1. Objective

Produce exactly one accepted result, the **Governance Generalization
Assessment / Classification Matrix**: one document classifying every one
of the 88 accepted G1B capability records and dispositioning every one of
the 6 accepted G1B gap records, plus a bounded cross-cutting analysis of
Delegated Operational Authority and Provider-Neutral Governance as program
requirements for later architecture work — not as implementation of either.

G2 does not select, recommend, or compare a target architecture; decide
kernel repository ownership; create a repository; extract or migrate the
kernel; implement delegated operational authority; implement any recorded
G1B gap; or modify any `AGENTS.md`/`CLAUDE.md`/AET/CWG/SVP surface.
Architecture alternatives that surface during classification are recorded
as later-phase inputs, not selected.

## 2. Accepted start

### 2.1 Canonical planning inputs

Read before execution, in this order:

```text
governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-003-g1b-capability-map-acceptance-v0.1.0.yaml
governance/audits/GOV-GEN-AUD-001-governance-generalization/G1B/GOV-GEN-G1B-CAPABILITY-MAP-001.md   (primary evidence source — full document)
governance/audits/GOV-GEN-AUD-001-governance-generalization/G1B/GOV-GEN-G1B-CONTRACT-001-v0.1.0.md   (schema and boundary this map was produced under)
governance/AGENTS.md
governance/methodology/project-operating-contract.md
governance/CURRENT_STATE.md
```

Per the Owner's explicit context-cost rule, G2 does not reread the 679-row
G1A corpus broadly. A targeted lookup into G1A row bodies or other primary
artifacts is permitted only to resolve a specific ambiguity the accepted
G1B map itself cannot resolve, and any such lookup must be recorded in §8
of the resulting deliverable as a named targeted lookup, not a silent
re-derivation.

### 2.2 Expected repository state

```yaml
repository: Sugar144/HugePlanning
worktree: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
worktree_status_at_start: CLEAN
```

Run read-only verification (`pwd`, `git branch --show-current`, `git rev-parse HEAD`,
`git status --short`) before writing any G2 artifact. A dirty worktree or
unexpected branch is a blocker: stop and record it rather than silently
proceeding.

## 3. Execution model — single task, direct classification

G2 runs as **one `L1_CLEAN_SESSION`** producing **one** Classification
Matrix document, walking the G1B map's own NAV-01..NAV-13 order rather than
re-partitioning it. Progressive navigation inside this one task is
permitted and expected; it is not a session-split trigger (same rule as
G1B contract §3.2 — evidence-family size is a navigation-load fact, not an
independence boundary).

### 3.1 What stays inside the one task

- classifying all 88 capability records against the schema in §5;
- dispositioning all 6 gap records against §5.3;
- producing the Delegated Operational Authority and Provider-Neutral
  Governance evaluations (§6) as findings for later architecture phases,
  not as design or implementation;
- summarizing counts and cross-cutting findings (§7);
- recording unresolved questions that genuinely require later architecture
  work (§7.4) rather than silently resolving them here;
- a final self-check pass before the deliverable is reported
  `G2_READY_FOR_OWNER_REVIEW`.

### 3.2 The only valid reason to split into another governed session

Unchanged from G1B contract §3.2: a genuinely independent decision,
authority, validation, acceptance, or material-risk boundary. Evidence
volume (88 records) is explicitly not such a boundary.

## 4. Authority and write scope

### 4.1 Gating

The Project Owner's `HP-PROMPT-043/0.1.0` is itself G2's canonical
definition and execution authorization — see front matter
`authorizing_source`. No further, separate Owner authorization gate exists
between this contract's acceptance and its execution within the same
governed unit. This contract does not itself perform the classification;
it frames the bounded task the same governed unit performs immediately
after accepting this contract.

### 4.2 Permitted, execution already authorized

- read the files named in §2.1;
- run the read-only Git commands in §2.2;
- classify every accepted capability and gap record per §5 and §6;
- create the Classification Matrix deliverable and its manifest under
  `governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/`;
- create the minimum decision/state/index reconciliation artifacts
  required by existing GOV-GEN conventions (decision record, program
  status, `CURRENT_STATE.md`, `DECISION_LOG.md`, `ARTIFACT_REGISTRY.yaml`,
  prompt custody for `HP-PROMPT-043`);
- run applicable repository validators and perform routine deterministic
  remediation (formatting, indexing, custody, reference repair, staging,
  validation remediation) inside this scope;
- create exactly one bounded local commit.

### 4.3 Forbidden, always

The executor must not, at any point in G2:

- modify, create, rename, or delete anything inside either HugePlanning
  worktree outside this contract's authorized paths;
- run any Git command beyond the read-only ones in §2.2, or push,
  create a pull request, merge, tag, release, or deploy;
- select, recommend, or compare a target governance architecture;
- choose or authorize kernel repository ownership;
- create a new repository;
- extract or migrate the governance kernel;
- implement delegated operational authority (only evaluate it as a
  program requirement, per §6.1);
- implement any recorded G1B gap;
- modify `AGENTS.md`, `CLAUDE.md`, AET, CWG, or SVP;
- advance or modify `GOV-AUD-001` (the firewalled internal GOV-n audit);
- broadly reread the 679-row G1A corpus (only a targeted, recorded lookup
  for a named ambiguity is permitted — §2.1);
- produce more than one principal deliverable (the Classification Matrix)
  without an explicit §3.2 split, recorded as such;
- open an additional Owner gate for routine formatting, indexing, custody,
  reference repair, staging, or validation remediation inside this scope.

## 5. Classification schema

Every capability record receives, in addition to its already-accepted G1B
fields (carried by reference, not restated), exactly these G2 fields:

```yaml
g2_classification_fields:
  capability_id:            # G1B identity, unchanged
  generality:                [UNIVERSAL, CROSS_PROJECT_CONFIGURABLE, PROJECT_SPECIFIC, EXECUTOR_SPECIFIC, UNRESOLVED]
  reuse_readiness:            [READY, NEEDS_NORMALIZATION, NEEDS_MODEL_CHANGE, NOT_REUSABLE_AS_IS]
  current_maturity:          # carried from G1B provisional_maturity, restated for this axis's context
  coupling:                  # array of capability_ids and/or qualitative coupling class (§5.1)
  duplication_status:        # carried from G1B duplication.reconciliation_status
  evidence_ref:               string      # G1B capability_id / map section citation
  material_limitation:       string|NONE  # carried or refined from G1B unresolved_items, where applicable
```

### 5.1 Coupling classes (closed set, used alongside `requires` capability-id citations)

```text
KERNEL_CONTENT_COUPLED       — obligation is bound to HugePlanning's own kernel clause text/identity
GOV_N_PHASE_COUPLED          — obligation is bound to the internal GOV-0..GOV-9 phase sequence or its identities
GOV_AUD_001_COUPLED          — obligation is bound to the firewalled internal audit program's own identities
KGR_RUN_COUPLED              — obligation is bound to specific KGR-NNN run identities
TOOLING_INTERNAL_COUPLED     — obligation depends only on this repository's own _lib/tool layer, not on program identities
CROSS_DOMAIN                 — obligation's realization spans multiple NAV families by design (schema+tool+skill+instance layering)
STANDALONE                   — no material coupling beyond its own realization
```

### 5.2 Classification method (fact-bound, per Owner instruction — using the accepted map as primary evidence)

A capability is classified from its G1B `obligation`, `realized_by` path
shape, `capability_domain`, `authority_layer_observed`,
`executor_equivalence_observed`, `provider_references_observed`, and
`unresolved_items` — the same evidence G1B already recorded — plus a
reasoned generality/reuse judgment, which is exactly what distinguishes G2
from G1B (G1B's own §6.4 explicitly reserved this judgment for G2). Where
G1B's own evidence for a record was `UNRESOLVED`/empty and no
G1B-internal fact resolves generality either way, G2 classifies
`generality: UNRESOLVED` rather than guessing, and states the missing
evidence in `material_limitation`.

### 5.3 Gap disposition

Each of the 6 accepted G1B gaps receives:

```yaml
gap_disposition_fields:
  gap_id:                     # G1B identity, unchanged
  generalization_relevance:   [BLOCKS_UNIVERSAL_REUSE, BLOCKS_CROSS_PROJECT_CONFIGURABILITY, PROJECT_SPECIFIC_ONLY_NOT_A_GENERALIZATION_BLOCKER, ARCHITECTURE_DEPENDENT]
  disposition_note:           string   # fact-bound, no remediation design
```

## 6. Required program-requirement evaluations

### 6.1 Delegated Operational Authority

Evaluate explicitly, as a program requirement for future architecture
assessment: routine deterministic work inside already-authorized scope
should not repeatedly require Owner approval. This is an evaluation of
which already-classified capabilities realize, partially realize, or leave
absent a delegation mechanism — not a design or implementation of one.

### 6.2 Provider-Neutral Governance

Evaluate explicitly: Claude Code and Codex must consume equivalent
canonical governance semantics; provider-specific instruction files should
be projections/adapters, not independent normative governance. This draws
directly on GAP-004 (`skills/*/agents/openai.yaml`, no second-provider
counterpart) and the `executor_equivalence_observed` field already
recorded per capability in G1B.

Both evaluations are program requirements for later architecture work,
explicitly not implementation instructions for G2 (Owner instruction,
verbatim).

## 7. Deliverable content requirements

The Classification Matrix must include:

1. classification of all 88 capabilities (§5);
2. disposition of the 6 accepted gaps (§5.3);
3. summary counts by `generality` and by `reuse_readiness`;
4. cross-cutting findings, including the two evaluations in §6;
5. unresolved questions that genuinely require later architecture work;
6. compact evidence references suitable for later phases (G1B capability
   IDs and map section citations, not full re-citation of the 679-row
   index).

## 8. Deliverable and custody

One principal deliverable:

```text
governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/
  GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md
  GOV-GEN-G2-CLASSIFICATION-MATRIX-001.manifest.sha256
```

## 9. Validation (required at execution completion)

1. worktree clean before and after outside this contract's authorized
   paths; no Git command beyond the read-only set in §2.2 was run beyond
   what publication (§10) explicitly authorizes;
2. all 88 accepted G1B capability records are classified, none silently
   dropped;
3. all 6 accepted G1B gap records are dispositioned;
4. every classification uses only the closed enums in §5/§5.3;
5. no target-architecture selection, kernel-ownership decision, or
   implementation of Delegated Operational Authority or any recorded gap
   exists anywhere in the output;
6. exactly one principal deliverable exists, unless a §3.2 split was
   triggered and externally recorded;
7. hash manifest verifies;
8. applicable repository governance validators (prompt custody,
   governance-state cross-surface consistency where touched) pass or their
   findings are triaged per `governance/learning/README.md`.

Any failed check results in `G2_BLOCKED_VALIDATION_FAILED`; do not mark G2
complete.

## 10. Publication

One bounded local commit is authorized, containing the canonical G2
definition (this contract), the Classification Matrix result, state
reconciliation (`CURRENT_STATE.md`, `01-program-status.yaml`,
`00-program-charter.md`, `DECISION_LOG.md`, `ARTIFACT_REGISTRY.yaml`,
`decisions/README.md`), the G2 decision record, and required prompt
custody (`HP-PROMPT-043`). Push, pull request, merge, tag, release, and
deployment remain unauthorized.

## 11. Completion and terminal statuses

```text
G2_READY_FOR_OWNER_REVIEW
G2_BLOCKED_BASELINE_DRIFT
G2_BLOCKED_VALIDATION_FAILED
G2_BLOCKED_ENVIRONMENT_LIMITATION
G2_RETURN_FOR_CONTRACT_CORRECTION
G2_SPLIT_REQUIRED_<TRIGGER>
```

The executor does not accept its own output. Owner acceptance of the
Classification Matrix is a separate, subsequent act, exactly as under
`GOV-GEN-G1B-CONTRACT-001/0.1.0` §10 and `GOV-GEN-G1A-CONTRACT-001/0.1.0`
§13. This contract's execution authorization covers definition, execution,
and one bounded commit only — not Owner acceptance of the result, and not
G3 authorization.

```text
GOV-GEN-G2-CONTRACT-001/0.1.0 ACCEPTED_AND_AUTHORIZED_FOR_G2_EXECUTION
→ (no further Owner authorization gate) one governed G2 session classifies
  all 88 capabilities and dispositions all 6 gaps
→ one bounded local commit
→ Owner reviews, accepts, rejects, or requests bounded correction
→ (only after acceptance) Owner separately authorizes G3
```
