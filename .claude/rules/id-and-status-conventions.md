# ID, Status, and Schema Conventions

## Policy

Canonical IDs use `<TYPE>-<NNN>`: an uppercase namespace, hyphen, and a
zero-padded three-digit project-local sequence. Allocate from `project.yaml`
counters under a single-writer model; increment at creation; never renumber,
reuse, or allocate at/above the next counter. Children use
`<PARENT>-AC-<nn>` for acceptance criteria and `<PARENT>-T-<nn>` for task-local
micro-subtasks.

S0a reserves these namespaces:

`OBJ FR NFR INT CON DAT CNT BR ASM OQ CLAR CTR EP US UC TASK BUG CR ADR SPK RSK TEST REL INC`.

Status enums are fixed as follows:

- Artifacts: `draft | under_review | changes_requested | approved | superseded | deprecated`.
- Requirements: `proposed_default | draft | under_review | changes_requested | approved | implemented | verified | rejected | superseded | deprecated`.
- Tasks: `backlog | ready | in_progress | in_review | changes_requested | approved | merged | verified | done | blocked | cancelled`.
- Stories: `draft | ready | in_progress | done`.
- Content: `missing | promised | received | approved | placeholder_approved`.
- Open questions: `open | answered | incorporated | expired | withdrawn`.
- Contradictions: `open | resolved | accepted_as_tension`.
- Project stages: `onboarding | discovery | specification | technical_design | planning | implementation | validation | release | operation`.
- Stage status: `not_started | in_progress | blocked | in_review | approved | done`.
- Project status: `active | paused | archived`.

Every structured artifact carries `schema_version` as SemVer without a `v`.
Every JSON Schema uses draft 2020-12 and a versioned `$id`. The artifact version
selects its schema contract. PATCH fixes preserve the contract; MINOR changes
may add compatible optional fields; MAJOR changes require migration notes and an
intentional lock upgrade. Methodology releases use `v`-prefixed SemVer.

## Why

Locking this namespace at S0a prevents later schemas and artifacts from drifting
into incompatible identities or lifecycles.

## Observable violation

Malformed, reused, renumbered, duplicate, or counter-ahead IDs; unknown status;
missing/non-SemVer `schema_version`; an unversioned schema `$id`; or a breaking
schema change without a major version and migration note.
