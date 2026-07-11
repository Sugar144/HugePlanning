# Changelog

All notable changes to the `freelance-methodology` repository are documented
here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: SemVer per `02_methodology_repository_design.md` §7 —
PATCH: fixes, no contract change · MINOR: new skills/agents/knowledge,
compatible schema additions · MAJOR: schema-breaking changes, artifact renames,
behavioral contract changes.

## [0.1.0] - 2026-07-11

S0a — minimal runtime bootstrap (plan `13` S0a, decisions in `19`).

### Added

- Methodology `CLAUDE.md` (invariants only, `02` §4.1).
- Five always-on rules in `.claude/rules/`: `evidence-policy`, `traceability`,
  `id-and-status-conventions` (the conventions rule: ID grammar, status enums,
  `schema_version` policy, S0a namespace — R2-02), `client-data-separation`,
  `change-control`.
- Schemas (JSON Schema draft 2020-12): `project.schema.json` 1.0.0,
  `methodology-lock.schema.json` 1.0.0, with valid + invalid fixtures in
  `tests/schema-tests/`.
- **Progressive `validate.sh`** (R2-26): S0a scope = `project.yaml`,
  `methodology.lock.yaml`, required client-repository structure. The same
  script is extended at every later stage, never replaced.
- Client repository template `templates/client-repo/` (`03` §2): client
  `CLAUDE.md`, `.claude/settings.json` with methodology write-deny rules,
  `.gitignore` incl. `evidence-raw/`, initial `project.yaml`,
  `methodology.lock.yaml`, always-present empty `open-questions.yaml`,
  `engagement.md` skeleton, full directory tree.
- Scripts: `new-client.sh`, `start-agent.sh`, `check-methodology-clean.sh`,
  `spk-01-smoke-check.sh` (SPK-01 launch smoke check, `02` §5).
- S0a fixtures for SPK-01/G0: stub agent `client-discovery` (full contract
  lands at S1) and skill `methodology-smoke-check`.
- `knowledge/INDEX.md` placeholder (knowledge files land at S1 per `17`).
- Reproducible test suite `tests/run-tests.sh` (schema fixtures, script
  contracts, scratch-client generation, paths with spaces).

### Notes

- Release tag `v0.1.0` intentionally not created in this working copy
  (experiment git discipline); `new-client.sh` records the exact commit in the
  lock and warns when HEAD is not at the tag matching `VERSION`.
