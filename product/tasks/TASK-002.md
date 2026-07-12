# TASK-002 — handoff.schema.json 2.0.0 + fixtures

Epic: EP-001 (S0b) · Implements: FR-002 · Depends on: —

## Goal
Gate handoff records (`docs/handoffs/G<n>-<slug>-<seq>.yaml`) gain their locked
schema.

## Acceptance criteria (verbatim)
- FR-002-AC-01: The plan 06 §7.5 example record (G2) passes validation.
- FR-002-AC-02: A G3 record with visual_approval passes; result outside
  approved|approved_with_observations|rejected fails.
- FR-002-AC-03: Invalid fixtures cover at least missing commit, bad gate
  value, and sequence below 1.

## Files
- `schemas/handoff.schema.json` (new; schema_version 2.0.0 per `06` §7.5)
- `tests/schema-tests/handoff/…` (new) · `tests/run-tests.sh` (T3 group)

## Contract sources
Plan `06` §7.5 · R2-05 (append-only, gate+sequence identity) · `01` §4.2
(G0–G9 gate list; G3-V nested checkpoint).

## Validation
`tests/run-tests.sh` green.

## Out of scope
Append-only enforcement across commits (change-control rule / review duty, not
schema); status.sh derivation (TASK-007).
