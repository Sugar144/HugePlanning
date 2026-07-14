# freelance-methodology (HugePlanning)

The versioned methodology repository for the AI-assisted freelance web
development operating system, plus the planning corpus that specifies it.

Current methodology version: see `VERSION` · changes: `CHANGELOG.md` ·
implemented stage: **S0b — discovery infrastructure** (plan `13` S0b,
released as `v0.2.0`; S0a bootstrap was `v0.1.0`).

## Repository map

| Area | Path | What it is |
|---|---|---|
| **Released methodology runtime** | `CLAUDE.md`, `.claude/`, `schemas/`, `scripts/`, `templates/`, `tests/`, `knowledge/` | What client sessions actually load and run — versioned (`VERSION`), tagged, tested. Detailed below |
| **Product spec (this repo's own work)** | `product/` | Requirements, backlog, and task packets for the in-flight methodology stages (S0b/S1) — methodology-internal, suite-validated (R2-37) |
| **Current planning corpus** | `planning/v2/` | The V2 plan, 22 numbered files. Plan citations like `02 §6` resolve here — see `planning/README.md` |
| **Immutable baseline** | `planning/baseline/` | The original V1 plan document (frozen, audited in plan `16`) |
| **Historical prototypes** | `planning/history/` | Pre-V2 Claude.ai prototype skills — historical, not active runtime, not behaviorally validated (R2-36) |
| **Experiment reports** | `reports/experiments/` | Evaluation records (e.g. the S0a bootstrap experiment) — evidence, not canonical method |

**Where to start reading:** operating the runtime → stay in this README.
Understanding or changing the method → `planning/README.md`, then
`planning/v2/00_final_plan_index.md` for the reading order.

## What is here (runtime)

| Path | Contents |
|---|---|
| `CLAUDE.md` | Methodology invariants (loaded into client sessions) |
| `.claude/rules/` | 5 always-on rules incl. the conventions rule (ID grammar, status enums, `schema_version` policy) |
| `.claude/agents/` | `client-discovery` (S0a stub; full contract at S1) |
| `.claude/skills/` | `methodology-smoke-check` (SPK-01 fixture) |
| `schemas/` | S0a: `project`, `methodology-lock` · S0b: `open-questions`, `requirements` 2.0.0, `solution-context`, `interview-state`, `handoff` · internal: `product-*` (draft 2020-12, versioned `$id`s) |
| `templates/` | `client-repo/` — complete client repository template (`03` §2) · `discovery/` — schema-valid artifact skeletons (S0b) |
| `scripts/` | `new-client.sh`, `start-agent.sh`, `validate.sh` (progressive — never replaced), `status.sh` (derived dashboard, S0b), `check-methodology-clean.sh`, `spk-01-smoke-check.sh` |
| `tests/` | `run-tests.sh` + schema fixtures |
| `knowledge/INDEX.md` | Knowledge index (files land at S1) |

## Prerequisites

- bash ≥ 4, git, Claude Code CLI (`claude`)
- python3 with `pyyaml`, `jsonschema`, `pytest`, and `hypothesis`
  (Arch: `pacman -S python-yaml python-jsonschema python-pytest python-hypothesis`, or
  `python3 -m pip install --user --break-system-packages pyyaml jsonschema pytest hypothesis`)

## Create a client project

```bash
scripts/new-client.sh ~/Clients/acme-web ACME-WEB
```

Builds the client in a staging directory: copies the template, substitutes
placeholders (project id, methodology path, date), writes
`methodology.lock.yaml` from the current checkout (full 40-char commit SHA),
**validates the generated client before the initial commit**, then git-inits,
commits, and moves it into place — a failure at any step leaves no partial
target behind. It never overwrites a non-empty directory and **refuses a
dirty methodology checkout** (the lock must record what is actually on disk).
If no git identity is configured, the initial commit uses the command-local
fallback identity `Methodology Bootstrap <bootstrap@local.invalid>` (your git
config is never modified). Finally it prints the G0 checklist (`03` §7).
Then: create the private GitHub repo, push, protect `main`, fill
`engagement.md` and the `project.yaml` G0 fields.

## Launch a work session

```bash
scripts/start-agent.sh ~/Clients/acme-web client-discovery
```

Refuses to launch unless the client repo passes `validate.sh` and the
methodology checkout is clean; warns on lock/checkout mismatch; runs
`claude --add-dir <methodology> --agent <name>` from the client repo with
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`; alerts if the methodology
changed during the session. Append `--resume` to continue a session, or
`-- <extra claude args>` for non-interactive runs.

## Validate a client repository

```bash
scripts/validate.sh ~/Clients/acme-web
```

**The single progressive validator (R2-26).** S0b scope: the S0a checks
(required structure, `project.yaml`, `methodology.lock.yaml`, `.gitignore`
covering `evidence-raw/`, methodology deny rules) plus discovery artifact
schema validation (open-questions, requirements, solution-context,
interview-state files, handoff records), ID/reference integrity (`06` §4),
and the profile-aware matrix v0 (discovery registries required past the G1
boundary — R2-21). Extended in place at S2+; never replaced by a second
validator. Exit 0 = pass.

## SPK-01 launch smoke check (`02` §5)

Run at S0a and after **every** Claude Code CLI upgrade:

```bash
scripts/spk-01-smoke-check.sh <client-dir>
```

Checks live: (a) methodology agent resolution, (b) skill invocation,
(c) CLAUDE.md + rules loading via the env var, (d) deny rules block
methodology writes while client writes stay allowed. Check (a) passes on the
`SPK01-AGENT-OK` sentinel **or** on complete semantic evidence (the actual
client project id + the actual locked methodology version + the stub's exact
closing statement, verified against the client repo, never leaked into the
prompt); partial or unrelated output fails. Record the result below and keep
`claude_code_version` current in the client lock.

Manual fallback (no CLI): from the client dir run
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir <methodology> --agent client-discovery`,
then verify (a)–(d) by hand per `02` §5.

### SPK-01 results log

| Date | CLI version | a | b | c | d | Notes |
|---|---|---|---|---|---|---|
| 2026-07-11 | 2.1.207 (Claude Code) | PASS | PASS | PASS | PASS | S0a initial run, executed live (headless `claude -p`). Deny rule blocked the methodology write at the permission level ("directory denied by your permission settings") on a methodology path containing spaces; client control write succeeded; no methodology drift. Details: `reports/experiments/s0a/EXPERIMENT_S0A_REPORT.md` |
| 2026-07-11 | 2.1.207 (Claude Code) | PASS | PASS | PASS | PASS | S0a audited integration verification: deterministic suite passed twice (122/122 each run); live SPK-01 passed 5/5; methodology remained protected and clean. Commit tested: `09ae1adfa80abacdb0b57f757308aa72786f0e16`. |

## Test the methodology

```bash
tests/run-tests.sh
```

Deterministic suite (no live CLI needed): script syntax, schema meta-checks,
valid/invalid fixtures (each invalid fixture must fail for its declared
reason), scratch-client generation and validation red cases — all in paths
containing spaces, against a throwaway copy of this repo. Must be green before
any release.

## Release a methodology version (`02` §7)

1. `tests/run-tests.sh` green; re-run relevant scenarios (S1+).
2. Update `CHANGELOG.md` (migration notes if MAJOR).
3. Bump `VERSION` (SemVer: PATCH fixes · MINOR compatible additions · MAJOR breaking).
4. Annotated tag `vX.Y.Z` on the release commit; push with tags.

Client projects pin versions in `methodology.lock.yaml`; upgrades are always
intentional (`upgrade-lock.sh`, lands at S4).
