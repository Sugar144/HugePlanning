# TASK-008 — templates/discovery/ skeletons + lock template schema listing

Epic: EP-001 (S0b) · Implements: FR-010, FR-012 · Depends on: TASK-001..005

## Goal
Every S0b-schema'd artifact gets a commented skeleton, and new clients pin the
five discovery schema versions in their lock.

## Acceptance criteria (verbatim)
- FR-010-AC-01: Each template, stripped of comments and filled with the
  minimal example values it documents, passes its schema.
- FR-010-AC-02: Templates carry no client data and no invented method — field
  comments cite the owning plan sections.
- FR-012-AC-01: new-client.sh produces a lock whose schemas map includes the
  five S0b entries with their released versions, and the lock passes its
  schema.

## Files
- `templates/discovery/requirements.template.yaml`,
  `solution-context.template.yaml`, `interview-state.template.json`,
  `handoff.template.yaml` (new; open-questions already ships empty in the
  client template)
- `templates/client-repo/methodology.lock.yaml` (add 5 schema entries)
- `tests/run-tests.sh` (template-passes-schema checks; lock fixture update if
  needed)

## Validation
`tests/run-tests.sh` green; `new-client.sh` scratch run shows the 5 entries.

## Out of scope
PRD/validation-package templates (S1/S2, `06` §6); content-inventory (S2).
