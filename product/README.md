# product/ — the methodology's own requirements and backlog

The methodology repository is itself a product. This directory versions **what
that product must do next** — requirements, backlog, and task packets for the
stages currently in flight — so implementation work traces to an agreed,
reviewable contract instead of ad-hoc session prompts. Decision: R2-37
(`planning/v2/19_revision_audit_and_change_log.md` §5).

**Scope rule (hard):** only the stages currently in flight — today **S0b and
S1**. Later stages (S2–S9) are specified here when they start, not before.
This directory must never grow into a parallel roadmap; the roadmap is plan
`13`.

**Methodology-internal:** nothing here is client-facing. These files and their
schemas (`schemas/product-requirements.schema.json`,
`schemas/product-backlog.schema.json`) are never listed in
`methodology.lock.yaml`, never checked by `validate.sh`, and never replicated
into client repositories. They are validated by the deterministic test suite
(`tests/run-tests.sh`, block T14).

## Files

| File | Contents |
|---|---|
| `requirements.yaml` | `FR`/`NFR`/`CON` items for the in-flight stages, with acceptance criteria and `source_refs` |
| `backlog.yaml` | `EP` epics and `TASK` items (`implements` → requirement IDs), plus the ID counters |
| `tasks/TASK-nnn.md` | Task packets: goal, ACs (verbatim from `requirements.yaml`), files touched, validation commands, out-of-scope |

## Conventions (reused from the conventions rule — no parallel conventions)

- **ID grammar:** `<TYPE>-<NNN>`, zero-padded, never reused or renumbered;
  child ACs `<PARENT>-AC-<nn>`. Counters live in `backlog.yaml` (`counters:`,
  next free number per prefix, single writer).
- **Statuses:** requirement and task enums exactly as defined in
  `.claude/rules/id-and-status-conventions.md`.
- **`schema_version`** on both YAML files; schemas carry versioned `$id`s.
- **`source_refs`** cite where a requirement comes from, using these prefixes:
  `plan:` a planning document section (`plan:06 §7.1`) · `prototype:` a
  preserved historical prototype
  (`prototype:business-discovery-interviewer#final-outputs`) · `report:` an
  experiment/verification report · `decision:` a decision-log entry
  (`decision:R2-26`).
- **Verification evidence is pointers, never a store** (`22` §7):
  `verified_by:` on a task references the CHANGELOG entry, report, commit, or
  CI run that proves it — logs are never duplicated here.

## What this deliberately is NOT

Not client requirements (those use `requirements.schema.json` with evidence
anchors, `origin`, and gate-bound approval — semantics this product context
cannot honestly populate). Not a second traceability system. Not workflow
tooling. Not a place for S2–S9 speculation.
