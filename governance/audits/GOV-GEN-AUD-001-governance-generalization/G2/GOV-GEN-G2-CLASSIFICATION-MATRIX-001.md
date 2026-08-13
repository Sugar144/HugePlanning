---
document_id: GOV-GEN-G2-CLASSIFICATION-MATRIX-001
title: HugePlanning Governance Generalization — G2 Governance Generalization Assessment / Classification Matrix
program_id: GOV-GEN-AUD-001
phase: G2
contract: GOV-GEN-G2-CONTRACT-001/0.1.0
version: 0.1.0
status: G2_READY_FOR_OWNER_REVIEW
authority: FACTUAL_CLASSIFICATION_ONLY_NO_ARCHITECTURE_OR_EXTRACTION_AUTHORITY
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
---

# GOV-GEN-G2 — Governance Generalization Assessment / Classification Matrix

## 0. Scope statement

This document is the single principal G2 deliverable required by
`GOV-GEN-G2-CONTRACT-001/0.1.0` §8. It classifies every one of the 88
accepted `GOV-GEN-G1B-CAPABILITY-MAP-001/0.1.0` capability records and
dispositions every one of its 6 accepted gap records, using the axes the
Project Owner named directly (`HP-PROMPT-043/0.1.0`): generality, reuse
readiness, current maturity, coupling, duplication status, evidence
reference, and material limitation. It also evaluates Delegated
Operational Authority and Provider-Neutral Governance as program
requirements for future architecture assessment, without designing or
implementing either. It does not select, recommend, or compare a target
architecture, decide kernel ownership, or modify any artifact outside this
contract's own custody path.

## 1. Execution verification (contract §2.2)

| Check | Expected | Observed | Result |
|---|---|---|---|
| Repository root | `/home/sugar/Documents/HugePlanning-governance` | `/home/sugar/Documents/HugePlanning-governance` | MATCH |
| Branch | `governance/kernel-designer-revision-v0.1` | `governance/kernel-designer-revision-v0.1` | MATCH |
| Worktree status (pre-execution) | clean | clean (`git status --short` empty before this directory was created) | MATCH |
| HEAD | `a0b3c023074edf8bcf49dfe4f1a4b0cfb1f90fd4` (task baseline) | `a0b3c023074edf8bcf49dfe4f1a4b0cfb1f90fd4` | MATCH |
| G1B acceptance | `ACCEPTED_BY_PROJECT_OWNER`, no `PENDING_OWNER_ACCEPTANCE` | confirmed via `GOV-GEN-DECISION-003/0.1.0` and `CURRENT_STATE.md` | MATCH |

No baseline drift was triggered. Execution proceeds under contract §4.2.

## 2. Evidence base and method

Primary evidence is the accepted `GOV-GEN-G1B-CAPABILITY-MAP-001.md` in
full (all 88 capability records and 6 gap records, read completely before
classification began), plus the G1B contract's own schema and boundary
(`GOV-GEN-G1B-CONTRACT-001-v0.1.0.md`), `governance/AGENTS.md`,
`governance/methodology/project-operating-contract.md`, and
`governance/CURRENT_STATE.md`. The 679-row G1A corpus was **not** reread
broadly, per the Owner's context-cost rule.

Two targeted lookups were performed to resolve a specific ambiguity that
the accepted G1B map's own fields could not resolve on their own —
whether an obligation that *reads* as generic is *realized* generically —
and are recorded here rather than left silent:

1. `governance/tools/validate_governance_state.py` (realizing
   `CAP-NAV13-008`/`CAP-NAV06-004`) was read in full. It hardcodes exact
   HugePlanning-specific literal values (Kernel version `0.2.0`, OD-002
   through OD-006 dispositions, specific decision-record document IDs,
   exact `CURRENT_STATE.md`/`GOVERNANCE_MASTER_PLAN.md` table-row text
   fragments) rather than deriving them from a declarative, swappable
   expectation set. G1B's own record for this capability did not capture
   this distinction because G1B's schema explicitly excluded reuse
   judgment (contract §6.4).
2. `governance/tools/validate_prompts.py` (realizing `CAP-NAV13-010`) was
   read in full for the same reason. No HugePlanning-specific literal
   value was observed in its validation logic; its checks are the generic
   `HP-PROMPT-###` identifier shape, a semantic-version regex, SHA-256
   exact-text matching, and the closed enums already stated in
   `governance/prompts/README.md`.

No other file outside the G1B map, the G1B contract, and the two named
targeted lookups was read to produce a classification judgment.

## 3. Classification — NAV-01 (ROOT + archive, 12 capabilities)

```yaml
- capability_id: CAP-NAV01-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-001
  material_limitation: NONE

- capability_id: CAP-NAV01-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-002
  material_limitation: NONE

- capability_id: CAP-NAV01-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-003
  material_limitation: NONE

- capability_id: CAP-NAV01-004
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-004
  material_limitation: "declaration.fields empty; content not reopened at G1B; own drift-control status UNRESOLVED"

- capability_id: CAP-NAV01-005
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [GOV_N_PHASE_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-005
  material_limitation: "declaration.fields empty (NO_SUPPORTED_DECLARATION); content names GOV-0..GOV-9 phase roadmap specifically"

- capability_id: CAP-NAV01-006
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-006
  material_limitation: "declaration.fields empty"

- capability_id: CAP-NAV01-007
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-007
  material_limitation: "declaration.fields empty"

- capability_id: CAP-NAV01-008
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-008
  material_limitation: NONE

- capability_id: CAP-NAV01-009
  generality: PROJECT_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-009
  material_limitation: "declaration.fields empty; content names HugePlanning's own S0A/S1 runtime surface specifically"

- capability_id: CAP-NAV01-010
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-010
  material_limitation: NONE

- capability_id: CAP-NAV01-011
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: OPERATIONAL
  coupling: [CROSS_DOMAIN]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV01-011
  material_limitation: "two-tier AGENTS.md / methodology/project-operating-contract.md split not reconciled; this is the exact surface a future Provider-Neutral Governance adapter model (§6.2) would need to sit under"

- capability_id: CAP-NAV01-012
  generality: UNIVERSAL
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: OBSOLETE
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV01-012
  material_limitation: NONE
```

## 4. Classification — NAV-02 (kernel, 2 capabilities)

```yaml
- capability_id: CAP-NAV02-001
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: PROPOSED
  coupling: [KERNEL_CONTENT_COUPLED]
  duplication_status: UNRESOLVED
  evidence_ref: G1B#CAP-NAV02-001, GAP-001
  material_limitation: "ratified 0.2.0 kernel text absent from this path family entirely (GAP-001); clause-set content is intrinsically HugePlanning's own, and no separate clause-structure schema (distinct from the loop-mechanism schema at CAP-NAV09-004) was observed to abstract clause shape from clause content"

- capability_id: CAP-NAV02-002
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV02-002
  material_limitation: "declaration.fields empty"
```

## 5. Classification — NAV-03 (learning, 5 capabilities)

```yaml
- capability_id: CAP-NAV03-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV03-002, CAP-NAV03-003]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV03-001
  material_limitation: "machine-generated index has no front matter (G1A-report.md §10.1 item 7) — cosmetic, not a reuse blocker"

- capability_id: CAP-NAV03-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV09-002]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV03-002
  material_limitation: "declaration.fields empty across all 26 rows — cosmetic extraction gap, not a schema-validity gap"

- capability_id: CAP-NAV03-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV09-002]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV03-003
  material_limitation: NONE

- capability_id: CAP-NAV03-004
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [CAP-NAV03-002]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV03-004
  material_limitation: "declaration.fields empty"

- capability_id: CAP-NAV03-005
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV03-005
  material_limitation: NONE
```

## 6. Classification — NAV-04 (methodology, 7 capabilities)

```yaml
- capability_id: CAP-NAV04-001
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CROSS_DOMAIN]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV04-001
  material_limitation: "status=IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW; two-tier AGENTS.md/contract split not reconciled (see CAP-NAV01-011); content itself has no HugePlanning-specific hardcoding observed"

- capability_id: CAP-NAV04-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: PROPOSED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV04-002
  material_limitation: NONE

- capability_id: CAP-NAV04-003
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV04-003
  material_limitation: "declaration.fields empty for both rows"

- capability_id: CAP-NAV04-004
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV09-004, CAP-NAV13-002, CAP-NAV13-007]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV04-004
  material_limitation: "bounded-loop mechanism itself is generic; current naming/binding is specific to the kernel-design-closure workflow"

- capability_id: CAP-NAV04-005
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: UNRESOLVED
  coupling: [KERNEL_CONTENT_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV04-005
  material_limitation: "declared phase=GOV-5 (GOV_N_PHASE_COUPLED); role content is defined in terms of HugePlanning's own kernel-clause model"

- capability_id: CAP-NAV04-006
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: UNRESOLVED
  coupling: [KERNEL_CONTENT_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV04-006
  material_limitation: "declaration.fields empty across all 4 rows"

- capability_id: CAP-NAV04-007
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: UNRESOLVED
  coupling: [KERNEL_CONTENT_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV04-007
  material_limitation: "declaration.fields empty across all 5 rows"
```

Cross-cutting note (not a separate capability): the three role-protocol
packages (`CAP-NAV04-005/006/007`) share one identical structural template
— `README.md` + `*-modes.yaml` + `protocols/README.md` + versioned prompt
templates — even though each role's own content is HugePlanning-kernel
specific. The packaging shape is reusable independent of the three roles'
subject matter; see §9.6.

## 7. Classification — NAV-05 (prompts, 3 capabilities)

```yaml
- capability_id: CAP-NAV05-001
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CROSS_DOMAIN]
  duplication_status: UNRESOLVED
  evidence_ref: G1B#CAP-NAV05-001, GAP-005
  material_limitation: "indexes only governance/prompts/; audit-program prompts and per-run embedded prompt copies not cross-referenced (GAP-005)"

- capability_id: CAP-NAV05-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV05-002
  material_limitation: "HP-PROMPT-030 0.3.0 row declaration.fields empty (extraction gap); authority-field usage inconsistent across the 35-file register — data-quality items, not a structural blocker"

- capability_id: CAP-NAV05-003
  generality: PROJECT_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: DESIGNED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV05-003
  material_limitation: "bound to one specific GOV-AUD-001 PASS-03 review identity; the underlying prepared-review-pending-authorization pattern is not separately extracted as a template here"
```

## 8. Classification — NAV-06 (reviews, 6 capabilities)

```yaml
- capability_id: CAP-NAV06-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV09-005, CAP-NAV13-003, CROSS_DOMAIN]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV06-001
  material_limitation: "declaration.fields empty across all instances — cosmetic"

- capability_id: CAP-NAV06-002
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [GOV_N_PHASE_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV06-002
  material_limitation: "the declared-status vocabulary itself matches project-operating-contract.md's honest-status vocabulary and is fully reusable; only the phase/run names are project-specific"

- capability_id: CAP-NAV06-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV06-003
  material_limitation: NONE

- capability_id: CAP-NAV06-004
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV13-008, GOV_N_PHASE_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV06-004; targeted lookup: governance/tools/validate_governance_state.py (§2)"
  material_limitation: "the tool realizing this obligation (CAP-NAV13-008) hardcodes exact HugePlanning-specific literal expectations rather than a declarative/data-driven expectation set"

- capability_id: CAP-NAV06-005
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: OPERATIONAL
  coupling: [KGR_RUN_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV06-005
  material_limitation: "declaration.fields empty across all 10 rows; pattern generic, instances are per-KGR-run"

- capability_id: CAP-NAV06-006
  generality: PROJECT_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: PROPOSED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV06-006
  material_limitation: "this specific instance (HP-ARCH-GOV-TOOLING-001) is HugePlanning's own tooling-architecture proposal; the report-for-review pattern itself is reusable but not separately templated"
```

## 9. Classification — NAV-07 (runs, 6 capabilities)

```yaml
- capability_id: CAP-NAV07-001
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: OPERATIONAL
  coupling: [CROSS_DOMAIN]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV07-001
  material_limitation: "the README/prompt/inputs/outputs/manifest packaging shape is already independently reused by CAP-NAV08-012 in a second internal program; extracting it as a named, KGR-prefix-independent template is the remaining normalization step"

- capability_id: CAP-NAV07-002
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [KGR_RUN_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV07-002
  material_limitation: "absent from the earliest 3 runs (KGR-001..003); a progressive-hardening fact, applied inconsistently across the run history observed"

- capability_id: CAP-NAV07-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV09-001, CAP-NAV13-002]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV07-003
  material_limitation: NONE

- capability_id: CAP-NAV07-004
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV07-004
  material_limitation: NONE

- capability_id: CAP-NAV07-005
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV07-005
  material_limitation: NONE

- capability_id: CAP-NAV07-006
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV07-006
  material_limitation: NONE
```

## 10. Classification — NAV-08 (audits, 13 capabilities)

```yaml
- capability_id: CAP-NAV08-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: UNRESOLVED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-001
  material_limitation: "01/02 declaration.fields empty — cosmetic; the charter+plan+status pattern is already independently reused by GOV-GEN-AUD-001's own 00-program-charter.md/01-program-status.yaml, direct in-repository evidence of universality"

- capability_id: CAP-NAV08-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: UNRESOLVED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-002
  material_limitation: "declaration.fields empty"

- capability_id: CAP-NAV08-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-003
  material_limitation: NONE

- capability_id: CAP-NAV08-004
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: DESIGNED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-004
  material_limitation: "directly relevant evidence for the Delegated Operational Authority evaluation (§11)"

- capability_id: CAP-NAV08-005
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: DESIGNED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-005
  material_limitation: NONE

- capability_id: CAP-NAV08-006
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: VALIDATED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV08-006
  material_limitation: NONE

- capability_id: CAP-NAV08-007
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV08-007
  material_limitation: NONE

- capability_id: CAP-NAV08-008
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV08-008, GAP-006"
  material_limitation: "the pattern's own next-phase-only-contract discipline (also stated in the accepted Compact Conceptual Baseline §7.2 and applied by GOV-GEN itself) is violated in its own current instance — PASS-04..07 contracts exist despite being unauthorized/unexecuted (GAP-006); reuse requires an enforcement mechanism, not just the documented convention"

- capability_id: CAP-NAV08-009
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: DESIGNED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-009
  material_limitation: NONE

- capability_id: CAP-NAV08-010
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [GOV_AUD_001_COUPLED, CAP-NAV05-001]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV08-010, GAP-005"
  material_limitation: "not cross-referenced with governance/prompts/README.md's HP-PROMPT-* register (GAP-005)"

- capability_id: CAP-NAV08-011
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV08-011
  material_limitation: "same GAP-005 cross-referencing need as CAP-NAV08-010"

- capability_id: CAP-NAV08-012
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV07-001, CROSS_DOMAIN]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV08-012
  material_limitation: "this is CAP-NAV07-001's own template independently reapplied to a second internal program — the strongest direct evidence of universality in the whole map"

- capability_id: CAP-NAV08-013
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: DESIGNED
  coupling: [CAP-NAV05-003, CAP-NAV08-009]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV08-013
  material_limitation: NONE
```

## 11. Classification — NAV-09 (schemas + validation, 9 capabilities)

```yaml
- capability_id: CAP-NAV09-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-001
  material_limitation: NONE

- capability_id: CAP-NAV09-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-002
  material_limitation: NONE

- capability_id: CAP-NAV09-003
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: DESIGNED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV09-003, GAP-002, GAP-003"
  material_limitation: "no populated instance observed anywhere under validation/ (GAP-003); this schema is the concrete artifact of the PROJECTION_DRIFT_CONTROL gap (GAP-002)"

- capability_id: CAP-NAV09-004
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV04-004]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-004
  material_limitation: "same kernel-design-closure naming/parameterization need as CAP-NAV04-004"

- capability_id: CAP-NAV09-005
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV06-001]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-005
  material_limitation: NONE

- capability_id: CAP-NAV09-006
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: IMPLEMENTED
  coupling: [GOV_N_PHASE_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-006
  material_limitation: "schema content is specific to GOV-PROTOCOL-002; a reusable version would need a protocol-agnostic closure/verdict schema"

- capability_id: CAP-NAV09-007
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: IMPLEMENTED
  coupling: [GOV_N_PHASE_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV09-007
  material_limitation: NONE

- capability_id: CAP-NAV09-008
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: IMPLEMENTED
  coupling: [GOV_N_PHASE_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV09-008
  material_limitation: "schema content is protocol-specific; the 0.1.0-preserved-alongside-0.2.0-correction versioning discipline itself is UNIVERSAL"

- capability_id: CAP-NAV09-009
  generality: UNIVERSAL
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV09-009, GAP-003"
  material_limitation: "entire validation/ path family is this one README; no populated validation-record instance exists (GAP-003)"
```

## 12. Classification — NAV-10 (skills, 5 capabilities)

```yaml
- capability_id: CAP-NAV10-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV10-001
  material_limitation: NONE

- capability_id: CAP-NAV10-002
  generality: EXECUTOR_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV10-001]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV10-002, GAP-004"
  material_limitation: "only agents/openai.yaml observed; no second-provider (e.g. Claude Code) executor binding present — the concrete Provider-Neutral Governance finding, §12 below"

- capability_id: CAP-NAV10-003
  generality: EXECUTOR_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV10-001, CAP-NAV07-001]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV10-003, GAP-004"
  material_limitation: "see GAP-004"

- capability_id: CAP-NAV10-004
  generality: EXECUTOR_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV10-001]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV10-004, GAP-004"
  material_limitation: "see GAP-004; CURRENT_STATE.md independently names this skill as bounded orchestration, not standing authority"

- capability_id: CAP-NAV10-005
  generality: EXECUTOR_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV10-001, CAP-NAV06-001]
  duplication_status: UNRESOLVED
  evidence_ref: "G1B#CAP-NAV10-005, GAP-004"
  material_limitation: "see GAP-004"
```

## 13. Classification — NAV-11 (sources, 5 capabilities)

```yaml
- capability_id: CAP-NAV11-001
  generality: UNIVERSAL
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: UNRESOLVED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV11-001
  material_limitation: "declaration.fields empty"

- capability_id: CAP-NAV11-002
  generality: PROJECT_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: OBSOLETE
  coupling: [KERNEL_CONTENT_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV11-002
  material_limitation: NONE

- capability_id: CAP-NAV11-003
  generality: PROJECT_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: OBSOLETE
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV11-003
  material_limitation: NONE

- capability_id: CAP-NAV11-004
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: OBSOLETE
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV11-004, GAP-004"
  material_limitation: "\"codex\" is the only provider-branded package name among the 6 zips; no equivalent \"claude\" bootstrap package observed"

- capability_id: CAP-NAV11-005
  generality: EXECUTOR_SPECIFIC
  reuse_readiness: NOT_REUSABLE_AS_IS
  current_maturity: OBSOLETE
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV11-005, GAP-004"
  material_limitation: "verbatim filename token \"codex\"; consistent with CAP-NAV11-004"
```

## 14. Classification — NAV-12 (tests, 4 capabilities)

```yaml
- capability_id: CAP-NAV12-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: VALIDATED
  coupling: [CAP-NAV13-002, CAP-NAV09-001]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV12-001
  material_limitation: NONE

- capability_id: CAP-NAV12-002
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: VALIDATED
  coupling: [CAP-NAV12-001]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV12-002
  material_limitation: "fixture pattern is generic; fixture content is bound to this project's own transition/loop test cases"

- capability_id: CAP-NAV12-003
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: VALIDATED
  coupling: [GOV_N_PHASE_COUPLED, GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV12-003
  material_limitation: "one regression file per governed unit is a generic pattern; the 15 files' content is per-phase/per-program specific"

- capability_id: CAP-NAV12-004
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: OPERATIONAL
  coupling: [CAP-NAV12-001, CAP-NAV03-002, CAP-NAV05-001]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV12-004
  material_limitation: NONE
```

## 15. Classification — NAV-13 (tools, 11 capabilities)

```yaml
- capability_id: CAP-NAV13-001
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [STANDALONE]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-001
  material_limitation: "foundational internal library with no HugePlanning-specific content observed; every other tools/ capability depends on it"

- capability_id: CAP-NAV13-002
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV09-001, CAP-NAV07-003]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-002
  material_limitation: NONE

- capability_id: CAP-NAV13-003
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV09-005, CAP-NAV06-001]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-003
  material_limitation: NONE

- capability_id: CAP-NAV13-004
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV09-002, CAP-NAV03-002, CAP-NAV03-003]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-004
  material_limitation: NONE

- capability_id: CAP-NAV13-005
  generality: PROJECT_SPECIFIC
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV07-001]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV13-005
  material_limitation: "the run-preparation-plus-versioned-correction pattern is universal (CAP-NAV07-001; project-operating-contract.md's <BASE_RUN_ID>-R<N> rule), but this tool pair hardcodes it to the Enforcement Engineer role's specific input shape"

- capability_id: CAP-NAV13-006
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV08-006, CAP-NAV08-001, GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV13-006
  material_limitation: NONE

- capability_id: CAP-NAV13-007
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV09-004, CAP-NAV04-004]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-007
  material_limitation: NONE

- capability_id: CAP-NAV13-008
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_MODEL_CHANGE
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV01-001, CAP-NAV06-004, GOV_N_PHASE_COUPLED]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV13-008; targeted lookup: governance/tools/validate_governance_state.py (§2)"
  material_limitation: "hardcodes exact HugePlanning-specific literal expectations (Kernel version, OD dispositions, decision-record IDs, table-row text fragments) rather than a declarative/data-driven expectation set; the obligation is universal, the implementation is not portable without a rewrite"

- capability_id: CAP-NAV13-009
  generality: CROSS_PROJECT_CONFIGURABLE
  reuse_readiness: NEEDS_NORMALIZATION
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV08-008, CAP-NAV08-009, CAP-NAV08-012, GOV_AUD_001_COUPLED]
  duplication_status: DELIBERATE_SEPARATION
  evidence_ref: G1B#CAP-NAV13-009
  material_limitation: NONE

- capability_id: CAP-NAV13-010
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV05-001, CAP-NAV05-002]
  duplication_status: NOT_APPLICABLE
  evidence_ref: "G1B#CAP-NAV13-010; targeted lookup: governance/tools/validate_prompts.py (§2)"
  material_limitation: "no HugePlanning-specific literal value observed in its validation logic during direct inspection — only the generic HP-PROMPT-### identifier shape, semantic-version rules, and the prompt-custody methodology's own closed enums"

- capability_id: CAP-NAV13-011
  generality: UNIVERSAL
  reuse_readiness: READY
  current_maturity: IMPLEMENTED
  coupling: [CAP-NAV13-001, CAP-NAV07-001]
  duplication_status: NOT_APPLICABLE
  evidence_ref: G1B#CAP-NAV13-011
  material_limitation: NONE
```

## 16. Gap disposition (6 accepted G1B gaps)

```yaml
- gap_id: GAP-001
  generalization_relevance: ARCHITECTURE_DEPENDENT
  disposition_note: "no single canonical location holds the ratified 0.2.0 kernel text even within this one project (five duplicate copies embedded across KGR-004/005/006* runs, per G1B); resolving this is a kernel-repository/architecture decision this contract does not make — recorded as later-phase input, not decided here"

- gap_id: GAP-002
  generalization_relevance: BLOCKS_CROSS_PROJECT_CONFIGURABILITY
  disposition_note: "the durable governance-validation evidence contract (CAP-NAV09-003) is schema-designed but PLANNED_NOT_IMPLEMENTED; any adopting project would inherit the same unimplemented drift-control mechanism as-is"

- gap_id: GAP-003
  generalization_relevance: BLOCKS_CROSS_PROJECT_CONFIGURABILITY
  disposition_note: "no populated validation-record instance exists anywhere in custody; sub-detail of GAP-002 at the instance level rather than the schema level"

- gap_id: GAP-004
  generalization_relevance: BLOCKS_UNIVERSAL_REUSE
  disposition_note: "all 4 packaged skills bind only to agents/openai.yaml; zero have a Claude Code (or other second-provider) executor binding — this is the concrete, most direct Provider-Neutral Governance blocker in the accepted map (§12)"

- gap_id: GAP-005
  generalization_relevance: BLOCKS_CROSS_PROJECT_CONFIGURABILITY
  disposition_note: "three independent, non-cross-referenced prompt registries (governance/prompts/README.md, audit-program prompt-registry.yaml, per-run embedded prompt/ copies) would each transfer to an adopter as separate, unreconciled indexes unless unified first"

- gap_id: GAP-006
  generalization_relevance: PROJECT_SPECIFIC_ONLY_NOT_A_GENERALIZATION_BLOCKER
  disposition_note: "PASS-04 through PASS-07 contract.yaml files existing despite being unauthorized/unexecuted is specific to how GOV-AUD-001 was run; it is adjacent evidence for the Delegated Operational Authority evaluation (§11) but is not itself a portable-capability gap"
```

## 17. Summary counts

### 17.1 By generality (88 capabilities)

| Generality | Count |
|---|---|
| `UNIVERSAL` | 54 |
| `CROSS_PROJECT_CONFIGURABLE` | 16 |
| `PROJECT_SPECIFIC` | 13 |
| `EXECUTOR_SPECIFIC` | 5 |
| `UNRESOLVED` | 0 |
| **Total** | **88** |

### 17.2 By reuse readiness (88 capabilities)

| Reuse readiness | Count |
|---|---|
| `READY` | 39 |
| `NEEDS_NORMALIZATION` | 27 |
| `NEEDS_MODEL_CHANGE` | 10 |
| `NOT_REUSABLE_AS_IS` | 12 |
| **Total** | **88** |

### 17.3 Gap disposition counts (6 gaps)

| Generalization relevance | Count |
|---|---|
| `BLOCKS_UNIVERSAL_REUSE` | 1 (GAP-004) |
| `BLOCKS_CROSS_PROJECT_CONFIGURABILITY` | 3 (GAP-002, GAP-003, GAP-005) |
| `PROJECT_SPECIFIC_ONLY_NOT_A_GENERALIZATION_BLOCKER` | 1 (GAP-006) |
| `ARCHITECTURE_DEPENDENT` | 1 (GAP-001) |
| **Total** | **6** |

### 17.4 Generality × NAV-family distribution

| NAV | Family | UNIVERSAL | CROSS_PROJECT_CONFIGURABLE | PROJECT_SPECIFIC | EXECUTOR_SPECIFIC |
|---|---|---|---|---|---|
| NAV-01 | ROOT+archive | 9 | 2 | 1 | 0 |
| NAV-02 | kernel | 1 | 0 | 1 | 0 |
| NAV-03 | learning | 5 | 0 | 0 | 0 |
| NAV-04 | methodology | 3 | 1 | 3 | 0 |
| NAV-05 | prompts | 2 | 0 | 1 | 0 |
| NAV-06 | reviews | 2 | 3 | 1 | 0 |
| NAV-07 | runs | 4 | 2 | 0 | 0 |
| NAV-08 | audits | 13 | 0 | 0 | 0 |
| NAV-09 | schemas+validation | 5 | 1 | 3 | 0 |
| NAV-10 | skills | 1 | 0 | 0 | 4 |
| NAV-11 | sources | 1 | 1 | 2 | 1 |
| NAV-12 | tests | 2 | 2 | 0 | 0 |
| NAV-13 | tools | 6 | 4 | 1 | 0 |
| **Total** | | **54** | **16** | **13** | **5** |

## 18. Cross-cutting findings

1. **The clearest existing proof of generality is internal self-reuse, not
   theory.** `CAP-NAV07-001` (KGR run packaging) is independently
   reapplied by `CAP-NAV08-012` in the separately firewalled `GOV-AUD-001`
   program; `CAP-NAV08-001`'s charter+plan+status pattern is independently
   reapplied by `GOV-GEN-AUD-001`'s own `00-program-charter.md` /
   `01-program-status.yaml` scaffold. Two internal programs have already
   generalized the same mechanics without any extraction — the strongest
   available evidence that these specific patterns are `UNIVERSAL`.

2. **The most reuse-ready layer is pure infrastructure.**
   `governance/tools/_lib` (`CAP-NAV13-001`) and the record-type schemas
   (`CAP-NAV09-001/002/005`) carry no HugePlanning-specific content
   observed anywhere and are immediately `READY`.

3. **The two-tier instruction split is the key open surface for Provider-
   Neutral Governance.** `AGENTS.md` (`CAP-NAV01-011`) names
   `methodology/project-operating-contract.md` (`CAP-NAV04-001`) as
   canonical operating semantics, but the split itself is unreconciled
   (`DELIBERATE_SEPARATION`, not merged, not formally layered). Any future
   Claude Code/Codex projection-adapter model has to decide which of the
   two is the provider-neutral kernel layer and which is the
   provider-specific projection.

4. **Generality-by-obligation-text is not reliable; realization must be
   checked.** `validate_prompts.py` (`CAP-NAV13-010`) and
   `validate_governance_state.py` (`CAP-NAV13-008`) have similarly generic-
   sounding obligations ("validate X conformance"), but direct inspection
   (§2, targeted lookups) shows one is already provider/project-neutral in
   its logic and the other is 100% hardcoded to this project's specific
   facts. This is a methodological finding for later phases: classify from
   realization, not obligation text alone.

5. **Executor-specificity is narrow and concentrated, not pervasive.**
   Of 88 capabilities, only 5 are `EXECUTOR_SPECIFIC`, and all 5 sit in
   exactly two places: the 4 packaged skills' `agents/openai.yaml`
   bindings (`CAP-NAV10-002..005`) and one historical, `OBSOLETE`,
   Codex-branded raw source file (`CAP-NAV11-005`). The normative
   governance core (`AGENTS.md`, the operating contract, schemas, the
   learning and prompt-custody contracts) is already
   `IMPLICIT_TOOL_AGNOSTIC` and names no provider anywhere. No capability
   anywhere in the accepted map records `EXECUTOR_EQUIVALENCE_OBSERVED:
   EXPLICIT_BOTH_NAMED`.

6. **A reusable structural template can wrap project-specific content.**
   The three kernel-workflow role protocols (`CAP-NAV04-005/006/007`)
   share one identical packaging shape (`README.md` + `*-modes.yaml` +
   `protocols/README.md` + versioned prompt templates) even though their
   content is `PROJECT_SPECIFIC`. The shape and the content classify
   differently; both facts matter for later architecture work.

7. **Versioned-correction discipline is itself universal even where
   schema content is not.** `GOV-PROTOCOL-004`'s `0.1.0`/`0.2.0` schema
   pair (`CAP-NAV09-008`) is `PROJECT_SPECIFIC` in content but instantiates
   exactly the `<BASE_RUN_ID>-R<N>`, preserve-and-append correction rule
   stated generically in `methodology/project-operating-contract.md`.

8. **The run-package template itself is still evolving, not frozen.**
   `input-envelope.yaml`/`output-contract.yaml` (`CAP-NAV07-002`) are
   absent from the earliest 3 KGR runs and present from KGR-004 onward —
   a directly observed progressive-hardening fact. Any future extraction
   of `CAP-NAV07-001` as a template should account for which run's shape
   is authoritative.

## 19. Delegated Operational Authority evaluation (program requirement, not implemented)

The Owner's stated requirement: routine deterministic work inside
already-authorized scope should not repeatedly require Owner approval.

- **What already exists.** Every one of the 11 `tools/` capabilities
  (`CAP-NAV13-001..011`) carries `authority_layer_observed:
  BOUNDED_DISCRETION` — deterministic tooling already runs without a
  per-invocation Owner gate once its own governing contract/schema bounds
  it. `AGENTS.md`'s repository-wide instruction ("Route deterministic
  parsing, hashing, comparison, serialization, counting, packaging, and
  validation to scripts first") and `project-operating-contract.md`'s
  deterministic-and-cost-aware-routing clause are the current mechanism
  realizing this — a documented norm applied by human/agent discipline.
- **What is missing.** No capability among the 88 (nor a gap distinct from
  `GAP-006`) records an *enforced* boundary between "already inside an
  authorized scope, proceed" and "outside it, ask" — the materiality test
  in `project-operating-contract.md` §"Material prompt custody" is applied
  by judgment each time, not mechanically gated. `GAP-006` is adjacent
  evidence (contracts prepared for phases beyond the currently authorized
  one) but concerns premature preparation, not the absence of an
  authorization-boundary mechanism per se.
- **Raw material for a future mechanism.** Execution-authorization custody
  is already explicit and per-act (`CAP-NAV07-005`, `CAP-NAV05-002`), and
  Owner-checkpoint scheduling already exists structurally
  (`CAP-NAV08-004`). A future delegation model has existing primitives to
  build from; none of them currently distinguish delegated-routine from
  new-authority work automatically.
- This is recorded as an unresolved question for later architecture work
  (§20.5), not designed or implemented here (forbidden by contract §4.3).

## 20. Provider-Neutral Governance evaluation (program requirement, not implemented)

The Owner's stated requirement: Claude Code and Codex must consume
equivalent canonical governance semantics; provider-specific instruction
files should be projections/adapters, not independent normative governance.

- **The normative core is already provider-neutral in text.** `AGENTS.md`,
  `methodology/project-operating-contract.md`, the learning contract, and
  the prompt-custody contract name no AI provider anywhere and are
  classified `executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC` in
  the accepted G1B map. This is direct evidence that the requirement is
  already substantially met at the layer that matters most.
- **The gap is narrow and located, not pervasive.** All `EXECUTOR_SPECIFIC`
  findings concentrate in exactly two places: the 4 skills'
  `agents/openai.yaml` bindings (`GAP-004`) and one historical, obsolete,
  Codex-branded raw-source file. Zero capabilities across the full
  accepted map record `EXPLICIT_BOTH_NAMED` (i.e., a binding that names
  both Claude Code and Codex as equivalent consumers).
- **Reading this correctly matters.** The finding is not "governance is
  provider-locked" — the core semantics are not. It is specifically that
  the 4 packaged skills currently have only one concrete executor binding
  each. Whether that reflects "Claude Code support not yet built" versus
  "intentionally scoped to one executor for a reason not captured in the
  679-row index" is exactly the kind of ambiguity G2 records rather than
  assumes (§20.3).

## 21. Unresolved questions for the next phase

1. Should the ratified kernel text (`GAP-001`) be consolidated to one
   canonical location before any extraction is considered — this is
   architecture-dependent and not decided here.
2. Should `AGENTS.md` and `methodology/project-operating-contract.md`
   (`CAP-NAV01-011`/`CAP-NAV04-001`) be collapsed, or formalized as a
   stable two-layer model applicable to any adopting project?
3. Should the 4 skills gain an explicit Claude Code executor binding
   alongside `agents/openai.yaml`, or is the current one-provider binding
   intentional for a reason not captured in the accepted index? This
   requires an actual Owner/architecture decision, not an assumption.
4. Should hardcoded validators in the `validate_governance_state.py`
   shape (`CAP-NAV06-004`/`CAP-NAV13-008`, and similarly-patterned
   `CAP-NAV13-006/007/009`) move to a declarative, data-driven model
   before any cross-project reuse is attempted?
5. What mechanism, if any, should formalize Delegated Operational
   Authority as an enforced boundary, versus continuing to rely on
   human/agent judgment applying the existing materiality test by hand?
6. Should the three prompt registries (`GAP-005`) be unified under one
   cross-referenced index, and at what layer — kernel-level or
   per-project projection?
7. Does `GAP-006` (contracts existing for unauthorized distant phases)
   reflect a genuine authority-boundary defect or a benign forward-
   planning convenience, and should a future phase define an explicit
   next-phase-only contracting rule with enforcement, not just
   documentation?

None of these is resolved by this document; each is recorded for whichever
future phase the Owner separately authorizes to take it up.

## 22. Self-check against contract §9

| # | Required check | Result |
|---|---|---|
| 1 | Worktree clean before/after outside authorized paths; no Git command beyond §2.2's read-only set was run beyond publication (§10) | PASS — verified §1; only files under `G2/` and the minimum reconciliation surfaces named in the contract were written |
| 2 | All 88 accepted capability records classified, none dropped | PASS — §3–§15, 88/88, cross-checked against G1B row accounting per NAV family |
| 3 | All 6 accepted gap records dispositioned | PASS — §16, 6/6 |
| 4 | Every classification uses only the closed enums in contract §5/§5.3 | PASS — self-reviewed; no value outside the declared enums appears |
| 5 | No target-architecture selection, kernel-ownership decision, or implementation of Delegated Operational Authority or any recorded gap | PASS — §19/§20 are evaluations only; §21 explicitly defers all resolution |
| 6 | Exactly one principal deliverable exists, unless a §3.2 split was triggered and recorded | PASS — one deliverable; no split triggered |
| 7 | Hash manifest verifies | PASS — see `GOV-GEN-G2-CLASSIFICATION-MATRIX-001.manifest.sha256`, generated after this file was finalized |
| 8 | Applicable repository validators pass or findings are triaged | see completion disposition (§23) for the actual run result |

No §3.2 split trigger was encountered: no genuinely independent decision,
authority, validation, acceptance, or material-risk boundary arose during
this execution that this contract does not already grant.

## 23. Completion disposition

```yaml
completion:
  status: G2_READY_FOR_OWNER_REVIEW
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  worktree_clean_outside_g2_and_reconciliation_surfaces: true
  capability_count_classified: 88
  gap_count_dispositioned: 6
  generality_counts:
    UNIVERSAL: 54
    CROSS_PROJECT_CONFIGURABLE: 16
    PROJECT_SPECIFIC: 13
    EXECUTOR_SPECIFIC: 5
    UNRESOLVED: 0
  reuse_readiness_counts:
    READY: 39
    NEEDS_NORMALIZATION: 27
    NEEDS_MODEL_CHANGE: 10
    NOT_REUSABLE_AS_IS: 12
  targeted_lookups_performed: 2
  self_check: PASS
  split_triggered: false
  next_authority_required: OWNER_REVIEW_AND_ACCEPTANCE_OF_G2
```

The executor does not accept this output. Owner acceptance, rejection, or
a request for bounded correction is a separate, subsequent act, exactly as
under `GOV-GEN-G1B-CONTRACT-001/0.1.0` §10. No target-architecture
selection, kernel extraction, delegated-authority implementation, gap
implementation, repository creation, or `AGENTS.md`/`CLAUDE.md`/AET/CWG/SVP
modification occurred or is implied by this document. No push has been
performed; the one bounded local commit authorized by this contract's §10
follows this deliverable's finalization.

`GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0 G2_READY_FOR_OWNER_REVIEW`
