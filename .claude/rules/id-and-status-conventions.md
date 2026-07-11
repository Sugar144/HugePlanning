# Rule: id-and-status-conventions (always loaded — the conventions rule, R2-02)

Fixes the namespace at S0a so every later schema slots in without drift.

## ID grammar (`06` §4, DEC-09)

```text
<TYPE>-<NNN>                 zero-padded 3 digits, per-project sequence,
                             never reused, never renumbered
Scoped children:  <PARENT>-AC-<nn>   acceptance criteria
                  <PARENT>-T-<nn>    micro-subtasks inside a task context
```

Prefixes: `OBJ` objective · `FR`/`NFR`/`INT`/`CON`/`DAT` functional /
non-functional / integration / constraint / data requirement · `CNT` content
item · `BR` business rule · `ASM` assumption · `OQ`/`CLAR` open question /
client clarification · `CTR` contradiction · `EP`/`US`/`UC` epic / story /
use case · `TASK`/`BUG`/`CR` task / defect / change request · `ADR`/`SPK`/`RSK`
decision / spike / risk · `TEST` test case · `REL`/`INC` release / incident.
Migration is `category: migration` on FR/DAT/CON — there is no `MIG-` prefix.
Jira keys are additive labels, never replacements.

**Allocation:** counters in `project.yaml` allocate the next number at item
creation; single writer (one session at a time); `validate.sh` detects
duplicates and collisions. Parallel-branch allocation is a documented deferred
limitation (`15`).

## Status enums (`06` §2 — closed lists; no other values exist)

- Documents/artifacts: `draft → under_review → changes_requested → approved`
  (+ terminal `superseded | deprecated`). Status lives **in the artifact**,
  never in `project.yaml`.
- Requirements: `draft → under_review → changes_requested → approved →
  implemented → verified` (+ `rejected | superseded | deprecated`); defaults
  and legal items enter as `proposed_default` until confirmed (R2-10).
- Tasks: `backlog → ready → in_progress → in_review → changes_requested →
  approved → merged → verified → done` (+ `blocked`, `cancelled`).
- Stories: `draft → ready → in_progress → done`.
- Content items: `missing → promised → received → approved`
  (+ `placeholder_approved`).
- Open questions: `open → answered → incorporated` (+ `expired`, `withdrawn`).
  Contradictions: `open → resolved | accepted_as_tension`.
- Stages: `onboarding → discovery → specification → technical_design →
  planning → implementation → validation → release → operation`; stage status:
  `not_started | in_progress | blocked | in_review | approved | done`.

## `schema_version` policy (`02` §7)

Every structured artifact instance carries a `schema_version` (SemVer).
Schemas carry an `$id` that includes their version. The client's
`methodology.lock.yaml` pins the schema versions in force; instances validate
against the locked version, not the newest. Version bumps: PATCH = fix, no
contract change · MINOR = compatible additions (new optional fields) ·
MAJOR = breaking (migration notes mandatory in `CHANGELOG.md`).

## Namespace at S0a

Schemas existing now: `project` 1.0.0, `methodology-lock` 1.0.0. Later schemas
(interview-state, requirements, solution-context, open-questions, handoff at
S0b; others at their first consumer, R2-02) MUST reuse this grammar, these
enums, and this `schema_version` policy — never introduce parallel conventions.

**Why.** Stage-driven schema creation would fragment conventions without one
fixed namespace (V2 risk #4, `19` §4).

**Observable violation.** A renumbered/reused ID; a status value outside the
enums above; a structured artifact without `schema_version`; a schema without a
versioned `$id`; a new schema defining its own ID or status convention.
