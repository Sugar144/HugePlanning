# Changelog

All notable changes to the `freelance-methodology` repository are documented
here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: SemVer per `planning/v2/02_methodology_repository_design.md` §7 —
PATCH: fixes, no contract change · MINOR: new skills/agents/knowledge,
compatible schema additions · MAJOR: schema-breaking changes, artifact renames,
behavioral contract changes.

## [0.2.0] - 2026-07-12

S0b — discovery infrastructure (plan `13` S0b; decisions R2-36..38 in `19`
§5). MINOR per `02` §7: new compatible schemas; version reconciliation
recorded as R2-38 (plan `13`'s "v0.1.x" label superseded by the SemVer
policy). Release evidence per `22` §7: deterministic suite **224 passed /
0 failed**, run twice on the release commit; clean tree after the runs; no
runtime-launch surface changed (no live SPK-01 required — `start-agent.sh`,
deny rules, and agent/skill loading untouched); CI (first workflow) must show
green on GitHub Actions for this commit — recorded as FR-011's verification.

### Added

- **Discovery schemas** (draft 2020-12, versioned `$id`s, valid+invalid
  fixtures each): `open-questions` 1.0.0 (empty registry valid, R2-30),
  `handoff` 2.0.0 (append-only gate records, G3-V nested block, R2-05),
  `solution-context` 1.0.0 (facts value-or-unknown + `risk_triggers[]`,
  R2-24), `interview-state` 1.0.0 (04 §6 persistence contract incl.
  pause/resume and deferral discipline), `requirements` 2.0.0 (V2 model:
  origin provenance, `proposed_default` restricted to methodology/legal
  origins, structured NFRs with waiver alternative, DAT type, type↔prefix
  enforcement — R2-10).
- **`validate.sh` extended in place** (same script, R2-26): discovery schema
  checks incl. per-interview state files and every handoff record;
  ID/reference integrity via `scripts/lib/check-ids.py` (duplicates, AC
  scoping, counter collisions, dangling refs, handoff filename identity);
  profile-aware matrix v0 (discovery registries required past the G1
  boundary, INFO before — R2-21).
- **`status.sh` v0** + `scripts/lib/derive-status.py`: derived read-only
  dashboard (stage, latest gate state per gate, requirement histogram, OQ/CTR
  counts, pending risk triggers) — nothing stored (DEC-11).
- **`templates/discovery/`**: schema-valid commented skeletons for
  requirements, solution-context, interview-state, handoff.
- **Client lock template** pins the five S0b schema versions.
- **Methodology CI**: `.github/workflows/methodology-ci.yml` runs the suite
  on every push/PR.
- Test suite grown 122 → 224 checks (new fixture groups; T15 validator
  red/green incl. 8 failure paths; T16 status dashboard incl. read-only
  assertion; T17 template validity; T2 `$id` oracle generalized to any
  SemVer — TEST-class fix).

### Documentation (pre-release, same 0.2.0)

- New plan file `22_implementation_assurance_and_adversarial_validation.md`:
  the proportional stage-level assurance loop distilled from S0a (R2-34).
- Planning corpus moved to `planning/` (`baseline/` + `v2/`); S0a experiment
  report moved to `reports/experiments/s0a/`; navigation READMEs added.
  Plan citations `NN §m` resolve per `planning/README.md` (R2-35).
- Historical Claude.ai prototype baseline preserved verbatim at
  `planning/history/claude-ai-prototypes/` with reuse assessment (R2-36) —
  historical prototype, not active runtime, not behaviorally validated.
- Product-spec foundation (R2-37): `product/` (requirements, backlog, task
  packets for in-flight stages S0b/S1) with methodology-internal schemas
  `product-requirements` 1.0.0 + `product-backlog` 1.0.0, fixtures, and suite
  block T14. Never client-facing: excluded from `validate.sh` and the lock.
  S1 scenario validation split one-task-per-scenario by operator refinement.

### Known limitations (carried)

- Parallel-branch ID allocation, Jira reconciliation automation, hook-based
  methodology guard, encrypted evidence platform: deferred as documented
  (`15` §2).
- Profile matrix v0 covers discovery-stage rows only; later stages extend it.
- `check-ids.py` skips references whose registries land at later stages
  (ADR, TASK, …) — they gain checks with their schemas (R2-02).

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
