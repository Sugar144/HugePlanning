# TASK-003 — solution-context.schema.json 1.0.0 + fixtures

Epic: EP-001 (S0b) · Implements: FR-003 · Depends on: —

## Goal
The technical-operational facts registry (incl. `risk_triggers[]`) gains its
locked schema.

## Acceptance criteria (verbatim)
- FR-003-AC-01: Leaves accept an explicit "unknown" everywhere a value is
  expected; a filled fixture with source_refs passes.
- FR-003-AC-02: risk_triggers entries require trigger, evidence_ref,
  profile_implication, and status; a trigger without evidence_ref fails.
- FR-003-AC-03: The schema stores facts only — no field exists for decisions
  or chosen technologies (reviewed against plan 06 §7.2).

## Files
- `schemas/solution-context.schema.json` (new)
- `tests/schema-tests/solution-context/…` (new) · `tests/run-tests.sh` (T3 group)

## Contract sources
Plan `06` §7.2 (sections; every leaf value|unknown + source_refs) · R2-24
(risk_triggers as machine-readable profile input) · `21` §3 (trigger list —
informative for fixture content, not an enum).

## Validation
`tests/run-tests.sh` green.

## Out of scope
Profile derivation logic (human at G1); trigger keyword scanning (S9 map).
