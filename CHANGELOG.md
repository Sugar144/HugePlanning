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

### Fixed (S0a integration audit — pre-release, same 0.1.0)

- `project.schema.json`: counters completed to the full `06` §4 namespace
  (added `ASM`, `CTR`, `RSK`); approvals completed to the ten lifecycle gates
  G0–G9 (`01` §4.2, DEC-06: added `g4_task_ready`, `g5_task_merge`,
  `g6_staging_release`, `g9_change_approval`); `pii_in_evidence` constrained
  to `minimized`; approval `record` constrained to the canonical
  `docs/handoffs/G<n>-<slug>-<seq>.yaml` path. Template and fixtures aligned.
- `new-client.sh`: refuses a dirty methodology (was a warning); builds the
  client in a staging directory and validates it **before** the initial
  commit; a failure at any step leaves no partial target; the lock records
  the full 40-char commit SHA; command-local git identity fallback
  (`Methodology Bootstrap <bootstrap@local.invalid>`) when none is configured.
- `start-agent.sh`: lock/checkout comparison accepts an abbreviated (≥7 hex)
  or full lock commit as a prefix of HEAD.
- `spk-01-smoke-check.sh`: check (a) accepts the sentinel or complete
  semantic evidence (client project id + locked methodology version + exact
  stub statement, read from the client repo); partial/unrelated output fails.
- Test suite: closed-set contract checks (counters/gates), dirty-bootstrap
  refusal, validate-before-commit, no-partial-target, no-identity fallback,
  deterministic fake-runtime SPK oracle cases, and an end-of-suite
  methodology-unchanged assertion.

### Notes

- Release tag `v0.1.0` intentionally not created in this working copy
  (experiment git discipline); `new-client.sh` records the exact commit in the
  lock and warns when HEAD is not at the tag matching `VERSION`.
