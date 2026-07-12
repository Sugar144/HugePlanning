# TASK-005 — requirements.schema.json 2.0.0 (V2 model) + fixtures

Epic: EP-001 (S0b) · Implements: FR-005 · Depends on: —

## Goal
The client requirements registry gains the V2 requirements-model schema —
the largest and most consequential S0b contract (replicates into every future
client via the lock).

## Acceptance criteria (verbatim)
- FR-005-AC-01: The full plan 06 §7.1 example (FR-004 booking, NFR-002
  performance, DAT-001 migration, BR-002, ASM-002) passes validation.
- FR-005-AC-02: Origin values outside the closed R2-10 enum fail; a
  methodology_default item is representable with status proposed_default.
- FR-005-AC-03: Invalid fixtures cover at least missing source_refs, bad AC id
  scoping, bad status, and an NFR lacking metric/target.
- FR-005-AC-04: The schema version is 2.0.0 per R2-10, recorded in the R2-38
  reconciliation note alongside the 06 §7.1 example header discrepancy.

## Files
- `schemas/requirements.schema.json` (new)
- `tests/schema-tests/requirements/…` (new) · `tests/run-tests.sh` (T3 group)

## Contract sources
Plan `06` §7.1 (normative field set + example) · R2-10 (origins, structured
NFRs, DAT type, approved_in semantics, 2.0.0) · `07` §2 (normalization rules
the shape must support) · conventions rule (types, statuses incl.
proposed_default, ID grammar incl. DAT; migration = category, never a prefix).

## Validation
`tests/run-tests.sh` green.

## Out of scope
Normalization skill behavior (S1/S2); audit logic (S2); content-inventory
schema (S2, R2-18).
