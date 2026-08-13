---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R4
title: HugePlanning Governance Generalization — G6 B-01 Path Resolution Correction R4
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
prior_controlling_corrections: [GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2/0.1.0, GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R3/0.1.0]
correction_index: 4
version: 0.1.0
status: G6_R4_B01_PATH_RESOLUTION_EXECUTION_AUTHORIZED
authority: PROJECT_OWNER_DIRECT_G6_B01_PATH_RESOLUTION_CORRECTION_AND_PHASE_CONTINUATION
source_authority: Project Owner direct task “GOV-GEN G6 — Correct B-01 Path Resolution and Continue”
---

# GOV-GEN-G6-R4 — B-01 deterministic path resolution

## 1. Scope and preservation

This prospective correction replaces only R2 §1.2's defective requirement that
each extracted textual pathname already exist literally from repository root.
R3's fixed G5 R1 selector correction remains exactly `G5 R1 §4.2 → G5 R1
§3`; it is preserved and is not reopened. No semantic source family, packet
dependency, B-01 objective, L3/L5 ownership, or B-02–B-08 material contract
changes.

## 2. Classification and resolution

For every extracted path-like reference, retain the declaring artifact and
original textual value. Classify it deterministically in this order:

1. `DECLARED_GENERATED_OUTPUT` when the value names a B-01 packet-local
   output specified by B-01, including `B-01-input-projection-manifest.yaml`.
   It is not a pre-existing seed input.
2. `EXISTING_REPO_RELATIVE_INPUT` when the normalized value uniquely names a
   tracked canonical repository file from repository root.
3. `EXISTING_DECLARER_RELATIVE_INPUT` when, and only when, the normalized
   value uniquely names a tracked canonical repository file from the
   declaring artifact's directory.
4. `UNRESOLVED_OR_AMBIGUOUS` otherwise, including unsafe paths and values
   yielding distinct root and declarer candidates.

Each accepted input records its original value, declaring artifact, resolution
rule, canonical normalized path, and SHA-256 source provenance. A generated
output records its generated-output rule and has no pre-existing source hash.

The source-root filter is then applied only to exact, successfully classified
canonical inputs supported by G3 §4's L0/L1/L2/L6 allocation and G3 §§6–8's
explicit boundary/context material. An unresolved textual reference is never
silently repaired, substituted, or admitted as a source root. If a candidate
that survives this source-root filter is unresolved or ambiguous, construction
records deterministic refusal for that reference. No fuzzy search, basename
guessing, nearest-match substitution, or scope broadening is permitted.

## 3. Validation and continuation

Deterministic validation must prove the preserved R3 selector, the ordered
classification/provenance record, generated-output exclusion, exact root or
declarer resolution, import closure, rendered hash, and pinned token count.
The 32 paths in refusal record 002 are re-evaluated by the classifier rather
than manually patched. On construction PASS, B-01 semantic baseline work may
start; no extraction starts before that success. A non-semantic deterministic
construction defect satisfying the delegated-authority conditions may be
corrected, recorded in provenance, validated, committed, and retried.
