# TASK-001 — open-questions.schema.json 1.0.0 + fixtures

Epic: EP-001 (S0b) · Implements: FR-001 · Depends on: —

## Goal
The open-questions registry gains its locked schema, replacing the S0a
parse-only check as the artifact's contract.

## Acceptance criteria (verbatim from product/requirements.yaml)
- FR-001-AC-01: The template's empty registry (questions/contradictions absent
  or empty) is VALID — the always-present rule R2-30 must hold.
- FR-001-AC-02: A populated fixture with CLAR (owner, impact, blocks, status)
  and a resolved CTR (between anchors, severity, resolution_ref) is valid.
- FR-001-AC-03: Invalid fixtures fail for their declared reasons at least for:
  bad ID prefix, status outside the enum, CTR without "between" anchors.

## Files
- `schemas/open-questions.schema.json` (new)
- `tests/schema-tests/open-questions/valid-*.yaml`, `invalid-*.yaml` (new)
- `tests/run-tests.sh` (add group to T3)

## Contract sources
Plan `06` §7.3 (field set + example) · conventions rule (OQ/CLAR/CTR grammar,
status enums `open→answered→incorporated` +expired/withdrawn;
CTR `open→resolved|accepted_as_tension`) · R2-30 (always present, may be empty).

## Validation
`tests/run-tests.sh` green; template `open-questions.yaml` passes the schema.

## Out of scope
validate.sh wiring (TASK-006); gate-blocking logic (profile matrix, FR-008).
