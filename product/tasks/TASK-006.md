# TASK-006 — Extend validate.sh: schema checks, ID/dangling checks, profile matrix v0

Epic: EP-001 (S0b) · Implements: FR-006, FR-007, FR-008
Depends on: TASK-001..005

## Goal
The single progressive validator grows its S0b scope exactly as its own header
documents — same script, never forked.

## Acceptance criteria (verbatim)
- FR-006-AC-01: A scratch client with valid planted discovery artifacts
  passes; each artifact broken per its invalid-fixture classes turns the run
  red with the artifact and field named.
- FR-006-AC-02: Absence of not-yet-produced artifacts stays non-fatal at S0b —
  presence requirements come from the profile matrix (FR-008), not the schema
  checks.
- FR-006-AC-03: The S0a checks all still run unchanged — nothing is removed or
  forked.
- FR-007-AC-01: A planted duplicate FR id and a dangling blocks reference each
  turn the run red with the offending id printed.
- FR-007-AC-02: An id numerically at or above its counter value is reported as
  a counter collision (06 §4 allocation contract).
- FR-008-AC-01: A LITE fixture missing requirements.yaml at the G1 boundary is
  an error; the same absence pre-interview is INFO only.
- FR-008-AC-02: Only discovery-stage matrix rows are encoded at S0b —
  later-stage artifacts produce no checks yet.

## Files
- `scripts/validate.sh` (extend §5 SCHEMA_CHECKS incl. handoff glob; replace §6
  parse-only with the real schema; new §8 ID/dangling checks, §9 profile
  matrix v0) — possibly a new `scripts/lib/check-ids.py` helper
- `tests/run-tests.sh` (extend T5-style red cases with planted discovery
  artifacts)

## Validation
`tests/run-tests.sh` green twice; red cases enumerated in FR ACs all exercised.

## Out of scope
Later-stage matrix rows (S2+); traceability.yaml checks (S6); any second
validator (CON-001).
