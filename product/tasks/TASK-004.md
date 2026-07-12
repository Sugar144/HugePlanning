# TASK-004 — interview-state.schema.json 1.0.0 + fixtures

Epic: EP-001 (S0b) · Implements: FR-004 · Depends on: —

## Goal
The interviewer's persistence contract (plan 04 §6) becomes a locked schema so
S1 state files validate from day one.

## Acceptance criteria (verbatim)
- FR-004-AC-01: The plan 04 §6 example state document passes validation.
- FR-004-AC-02: Phase, coverage status, importance, and confidence values
  outside their closed enums fail with the field named.
- FR-004-AC-03: A paused-state fixture (status paused, resume_hints filled)
  passes — the pause/resume contract shape is representable.

## Files
- `schemas/interview-state.schema.json` (new; instances are JSON —
  schema-validate.py reads YAML, a JSON superset, so fixtures may be .json
  or .yaml; keep the fixture group convention)
- `tests/schema-tests/interview-state/…` (new) · `tests/run-tests.sh` (T3 group)

## Contract sources
Plan `04` §6 (state model + example + phase enum) · `04` §4 (coverage node
fields/enums) · conventions rule (register ID grammar CTR/ASM/OQ).

## Validation
`tests/run-tests.sh` green.

## Out of scope
Any interviewer behavior (S1); transcript formats (evidence files are not
schema'd — they are markdown/jsonl evidence, `04` §8).
