---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R3
title: HugePlanning Governance Generalization — G6 B-01 Selector Correction R3
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
prior_controlling_correction: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2/0.1.0
correction_index: 3
version: 0.1.0
status: G6_R3_B01_SELECTOR_CORRECTION_EXECUTION_AUTHORIZED
authority: PROJECT_OWNER_DIRECT_G6_B01_SELECTOR_CORRECTION
source_authority: Project Owner direct task “OWNER AUTHORIZATION — G6 B-01 SELECTOR CORRECTION”
---

# GOV-GEN-G6-R3 — B-01 selector correction

## 1. Scope

This prospective correction changes exactly one R2 B-01 fixed-seed selector.
Every other R2 selector, packet boundary, context limit, construction rule,
semantic requirement, custody rule, and the B-02–B-08 contract remains
unchanged. R2 and the B-01 refusal record remain immutable historical
evidence.

## 2. Deterministic substitution

```yaml
old_selector:
  path: governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md
  selector: §4.2
  status: INVALID
  evidence: The R1 artifact has top-level headings §§0–8 and no §4.2 heading.
new_selector:
  path: governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md
  selector: §3
  status: VALID
  evidence: >-
    R1 §3 is the unique top-level correction section that explicitly targets
    base §4.2 Option B's config_projection_boundary and gives its corrected
    controlling wording. Its content is therefore the R1 source intended by
    the B-01 input contract's G5-R1 §4.2 reference.
```

The substitution does not add a source artifact, a selector, or a layer of
content. It selects the bounded R1 correction that controls the base §4.2
Option B proposition; it does not select R1 `all` or the G5 base artifact.
The physical source's base §4.2 is already outside this corrected selector and
is not added by this correction.

## 3. Validation disposition

The correction is valid only when deterministic construction confirms all of
the following at the frozen B-01 revision:

- R1 §3 exists and R1 §4.2 does not;
- R1 §3 explicitly cites base §4.2, Option B, and
  `config_projection_boundary`;
- the seed path is unchanged and the selector count remains one for this
  member; and
- every other R2 seed member and selector is byte-for-byte unchanged.

On PASS, B-01 restarts from deterministic pre-execution construction. No
prior provisional B-01 output is a semantic baseline or a B-02 prerequisite.
