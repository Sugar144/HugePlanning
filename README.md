# freelance-methodology (HugePlanning)

The versioned methodology repository for the AI-assisted freelance web
development operating system, **plus** the V2 plan that specifies it (the
numbered `NN_*.md` files at the root — start at `00_final_plan_index.md`).

Current methodology version: see `VERSION` · changes: `CHANGELOG.md` ·
implemented stage: **S0a — minimal runtime bootstrap** (plan `13` S0a).

## What is here (runtime)

| Path | Contents |
|---|---|
| `CLAUDE.md` | Methodology invariants (loaded into client sessions) |
| `.claude/rules/` | 5 always-on rules incl. the conventions rule (ID grammar, status enums, `schema_version` policy) |
| `.claude/agents/` | `client-discovery` (S0a stub; full contract at S1) |
| `.claude/skills/` | `methodology-smoke-check` (SPK-01 fixture) |
| `schemas/` | `project.schema.json`, `methodology-lock.schema.json` (draft 2020-12) |
| `templates/client-repo/` | Complete client repository template (`03` §2) |
| `scripts/` | `new-client.sh`, `start-agent.sh`, `validate.sh` (progressive — never replaced), `check-methodology-clean.sh`, `spk-01-smoke-check.sh` |
| `tests/` | `run-tests.sh` + schema fixtures |
| `knowledge/INDEX.md` | Knowledge index (files land at S1) |

## Prerequisites

- bash ≥ 4, git, Claude Code CLI (`claude`)
- python3 with `pyyaml` and `jsonschema`
  (Arch: `pacman -S python-yaml python-jsonschema`, or
  `python3 -m pip install --user --break-system-packages pyyaml jsonschema`)

## Create a client project

```bash
scripts/new-client.sh ~/Clients/acme-web ACME-WEB
```

Copies the template, substitutes placeholders (project id, methodology path,
date), writes `methodology.lock.yaml` from the current checkout, git-inits
with the initial commit, and prints the G0 checklist (`03` §7). It never
overwrites a non-empty directory. Then: create the private GitHub repo, push,
protect `main`, fill `engagement.md` and the `project.yaml` G0 fields.

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

**The single progressive validator (R2-26).** S0a scope: required structure,
`project.yaml`, `methodology.lock.yaml`, `.gitignore` covering
`evidence-raw/`, methodology deny rules. Extended in place at S0b+ (per-schema
checks, profile matrix); never replaced by a second validator. Exit 0 = pass.

## SPK-01 launch smoke check (`02` §5)

Run at S0a and after **every** Claude Code CLI upgrade:

```bash
scripts/spk-01-smoke-check.sh <client-dir>
```

Checks live: (a) methodology agent resolution, (b) skill invocation,
(c) CLAUDE.md + rules loading via the env var, (d) deny rules block
methodology writes while client writes stay allowed. Record the result below
and keep `claude_code_version` current in the client lock.

Manual fallback (no CLI): from the client dir run
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir <methodology> --agent client-discovery`,
then verify (a)–(d) by hand per `02` §5.

### SPK-01 results log

| Date | CLI version | a | b | c | d | Notes |
|---|---|---|---|---|---|---|
| 2026-07-11 | 2.1.207 (Claude Code) | PASS | PASS | PASS | PASS | S0a initial run, executed live (headless `claude -p`). Deny rule blocked the methodology write at the permission level ("directory denied by your permission settings") on a methodology path containing spaces; client control write succeeded; no methodology drift. Details: `EXPERIMENT_S0A_REPORT.md` |

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
