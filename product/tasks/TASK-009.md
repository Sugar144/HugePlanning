# TASK-009 — Methodology CI workflow

Epic: EP-001 (S0b) · Implements: FR-011 · Depends on: TASK-006

## Goal
Every push runs the deterministic suite on GitHub — the methodology gets the
CI floor plan `02` §10 schedules at S0b.

## Acceptance criteria (verbatim)
- FR-011-AC-01: The workflow installs the two python dependencies (pyyaml,
  jsonschema) and runs the suite; a green run is visible on GitHub for the S0b
  branch.
- FR-011-AC-02: The workflow needs no secrets and touches no client data.

## Files
- `.github/workflows/methodology-ci.yml` (new; ubuntu runner, checkout,
  `pip install pyyaml jsonschema`, `tests/run-tests.sh`)

## Validation
Local suite green, then a green Actions run on the pushed branch (this is the
one check that requires the remote — record the run id as the FR's
verification pointer).

## Out of scope
Client-project CI (per-project, `11`); release automation; scheduled lanes.
