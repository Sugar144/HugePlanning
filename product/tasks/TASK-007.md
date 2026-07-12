# TASK-007 — status.sh v0 (derived read-only dashboard)

Epic: EP-001 (S0b) · Implements: FR-009 · Depends on: TASK-002

## Goal
One command shows where a client project stands, derived live from artifacts —
never stored (DEC-11: no competing source of truth).

## Acceptance criteria (verbatim)
- FR-009-AC-01: On a scratch client with planted artifacts the output shows
  the derived gate state (latest sequence wins) and correct OQ/CTR counts.
- FR-009-AC-02: The script writes nothing and exits 0 on a valid repository
  (read-only contract, DEC-11 derivation rule).

## Files
- `scripts/status.sh` (new; bash + python lib reuse, `set -euo pipefail`,
  `--help`, paths-with-spaces safe)
- `tests/run-tests.sh` (output assertions on a planted scratch client)

## Contract sources
Plan `02` §8 (status.sh row) · R2-05 (latest handoff per gate derives state) ·
`03` §4 (what project.yaml deliberately omits).

## Validation
`tests/run-tests.sh` green; manual run on a scratch client.

## Out of scope
LITE task board rendering (needs delivery-backlog, S3); `--methodology`
staleness flags (`17` §E, lands with knowledge at S1+).
