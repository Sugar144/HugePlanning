# Experiment S0a Report

## Identity

- Environment: ChatGPT Work
- Model: Sol
- Reasoning effort: Extra High
- Repository: `Sugar144/HugePlanning`
- Branch: `experiment/chatgpt-s0a`
- Required/base commit: `51e0bf3fd1740a0c5e4f317bdc4cc5c7207b4c8c`
- Initial verification: branch matched; HEAD matched exactly; working tree was clean;
  `git diff 51e0bf3..HEAD` was empty.
- Scope: S0a minimal runtime bootstrap only
- External research/lookups: none

## Implementation summary

The existing planning repository now also hosts the minimal executable
methodology runtime. S0a fixes global invariants and namespaces, validates the
two core structured artifacts, creates a minimal G0-capable client repository,
guards methodology immutability, and supplies a reproducible SPK-01 fixture.
The progressive entrypoint is `scripts/validate.sh`; later stages must extend
that file and its adapter rather than introduce a replacement validator.

The client template intentionally contains only S0a/G0 files and tracked empty
directory markers. It does not pre-create absent/`missing` artifacts belonging
to S0b or later stages.

## Complete changed-file list

Modified:

- `.gitignore`
- `README.md`

Added:

- `CHANGELOG.md`
- `CLAUDE.md`
- `EXPERIMENT_S0A_REPORT.md`
- `VERSION`
- `.claude/agents/spk-01-fixture.md`
- `.claude/rules/change-control.md`
- `.claude/rules/client-data-separation.md`
- `.claude/rules/evidence-policy.md`
- `.claude/rules/id-and-status-conventions.md`
- `.claude/rules/traceability.md`
- `.claude/skills/spk-01-smoke/SKILL.md`
- `schemas/methodology-lock.schema.json`
- `schemas/project.schema.json`
- `scripts/check-methodology-clean.sh`
- `scripts/lib/render_template.py`
- `scripts/lib/schema_validate.py`
- `scripts/new-client.sh`
- `scripts/start-agent.sh`
- `scripts/validate.sh`
- `templates/client-repo/.claude/settings.json`
- `templates/client-repo/.env.example`
- `templates/client-repo/.gitignore`
- `templates/client-repo/CLAUDE.md`
- `templates/client-repo/README.md`
- `templates/client-repo/docs/handoffs/.gitkeep`
- `templates/client-repo/docs/product/engagement.md`
- `templates/client-repo/docs/requirements/open-questions.yaml`
- `templates/client-repo/evidence/clarifications/.gitkeep`
- `templates/client-repo/evidence/client-materials/.gitkeep`
- `templates/client-repo/evidence/confirmations/.gitkeep`
- `templates/client-repo/evidence/interviews/.gitkeep`
- `templates/client-repo/methodology.lock.yaml`
- `templates/client-repo/project.yaml`
- `templates/client-repo/src/.gitkeep`
- `templates/client-repo/tests/.gitkeep`
- `tests/run-s0a-tests.sh`
- `tests/schema-tests/methodology-lock/invalid/bad-commit.yaml`
- `tests/schema-tests/methodology-lock/invalid/missing-cli-version.yaml`
- `tests/schema-tests/methodology-lock/valid/minimal.yaml`
- `tests/schema-tests/project/invalid/bad-profile.yaml`
- `tests/schema-tests/project/invalid/bad-project-id.yaml`
- `tests/schema-tests/project/valid/minimal.yaml`
- `tests/spk-01/run.sh`

No V2 planning document was modified.

## Plan requirement mapping

| Plan requirement | Implementation |
|---|---|
| Methodology invariants | Root `CLAUDE.md` (19 lines) |
| Five always-on rules | `.claude/rules/{evidence-policy,traceability,id-and-status-conventions,client-data-separation,change-control}.md` |
| ID/status/schema conventions | `id-and-status-conventions.md`; complete S0a namespace and enum set |
| Methodology version | `VERSION` = `v0.1.0`; Keep-a-Changelog `CHANGELOG.md` |
| Two S0a schemas | Draft 2020-12 project and methodology-lock schemas with versioned `$id` |
| Valid/invalid fixtures | Three project fixtures and three methodology-lock fixtures |
| Single progressive validator | `scripts/validate.sh` plus the dependency-light schema adapter in `scripts/lib/` |
| Minimal client template | `templates/client-repo/`; settings deny rules, lock, project, engagement, empty OQ registry, raw/sanitized evidence split, required directories |
| Bootstrap | `scripts/new-client.sh`; guarded substitution, validation, `main`, initial commit, no overwrite |
| Launcher | `scripts/start-agent.sh`; validate/clean/lock checks before `claude --add-dir ... --agent ...`, env var, post-session drift check |
| Cleanliness guard | `scripts/check-methodology-clean.sh` |
| SPK-01 | S0a-only fixture agent + skill and `tests/spk-01/run.sh` |
| Automated/reproducible tests | `tests/run-s0a-tests.sh` |
| Operations documentation | Root and client `README.md` files |

## Tests and exact results

Final deterministic command:

```bash
./tests/run-s0a-tests.sh
```

Result: **PASS — 24 test groups**. Coverage included:

- Bash syntax for every shell script.
- Both valid schema fixtures pass.
- Every invalid fixture fails for its named field/reason.
- Generated client passes `validate.sh`.
- Missing/invalid project, missing/invalid lock, and missing required path all
  fail with actionable errors.
- `new-client.sh` substitution, path-with-spaces handling, `main` creation,
  exactly one initial commit, expected commit subject, clean tree, Git ignore,
  non-empty-target refusal, invalid-ID refusal, and no later-stage artifacts.
- Clean/dirty methodology behavior and dirty-methodology bootstrap refusal.
- Launcher lock mismatch and dirty-methodology precondition failures.
- Launcher invocation through a fake runtime verifies the env var, `--add-dir`,
  methodology path, `--agent`, agent name, and `--resume`.
- JSON/YAML syntax for schemas and the generated client.

Additional checks/actions:

```bash
bash -n scripts/*.sh tests/run-s0a-tests.sh tests/spk-01/run.sh
python3 -m py_compile scripts/lib/*.py
git diff --check
```

Result: **PASS**. Python bytecode cache is ignored and not part of the change.

SPK-01 command:

```bash
./tests/spk-01/run.sh /tmp/nonexistent-spk-client
```

Result: **UNVERIFIED / exit 77** — `claude` is not installed in this
environment. The command explicitly printed that SPK-01 was not executed live.
The deterministic launcher wiring was tested with a fake executable, but this
is not reported as a live Claude Code pass.

Development failures retained for transparency:

1. The first suite run exposed PyYAML converting an ISO date to a Python date;
   the adapter was corrected to retain JSON-compatible date strings.
2. A lock-mismatch test initially used forty zeroes, which YAML parsed as an
   integer; the fixture mutation was changed to a distinct valid 40-hex string.
3. All tests passed after those integration corrections and after the formal
   self-review correction below.

## G0 checklist result

The test suite generated a scratch client from a clean temporary methodology
checkout whose path and client path both contained spaces.

| G0 item | Result |
|---|---|
| Created from template; local `main`; initial commit | PASS |
| Lock pins current methodology version and commit | PASS |
| Engagement file exists with all required fields | PASS structurally; human values remain TODO |
| Project language/privacy/retention/profile hypothesis fields | PASS structurally; human confirmation remains required |
| `evidence-raw/` ignored | PASS |
| Absolute methodology Write/Edit denies | PASS |
| Minimal `validate.sh` | PASS |
| Live `start-agent.sh` smoke | UNVERIFIED (Claude Code unavailable) |
| Private client remote pushed and `main` protected | NOT EXECUTED; creating a second repository/remote was forbidden by the experiment |

Conclusion: the generated client **passes every automatable local S0a/G0
contract and is capable of satisfying G0**, but the complete human/external G0
gate is not claimed as approved. Engagement facts, remote privacy/protection,
and the live Claude runtime check remain explicit.

## Assumptions and narrow interpretations

1. The current `HugePlanning` repository is the methodology repository, despite
   the plan's generic `freelance-methodology` name. The lock therefore records
   `Sugar144/HugePlanning`.
2. “Complete minimal template” means files plus tracked directories consumed by
   S0a/G0. The full future tree in `03` is stage-driven; pre-creating its
   artifacts would violate the user's strict non-goals and `06`'s “no files just
   in case” rule.
3. Approval keys include G0–G9. This follows R2-22's explicit “full gate list”
   over the shorter illustrative map in `03`.
4. Counters include `ASM`, `CTR`, and `RSK`. They are reserved namespaces in
   `06` and allocation is counter-based, even though the compact `03` example
   omits those three counters.
5. `open-questions.yaml` carries `schema_version: 1.0.0` plus empty arrays. No
   open-questions schema or lifecycle validation was implemented.
6. The methodology version is `v0.1.0` and the lock uses the exact commit. No
   tag is created because the experiment explicitly prohibits tags.

## Deliberate non-goals confirmed absent

No interview-state, requirements, solution-context, open-questions, handoff,
delivery, test-matrix, Jira, traceability, release, or verification schema was
added. No `status.sh`, CI architecture, discovery/production agent,
requirements/design/delivery pipeline, Jira integration, deployment adapter,
PRD, SDD, product backlog, or delivery backlog was implemented. The only agent
and skill are explicitly named S0a SPK-01 fixtures.

## Self-review and correction

One complete review compared all changed files with `13` S0a, `02` §§2/4/5/6/8/10,
`03` §§2–7, `06` §§2–7, `14` §4, `20` §§3/5/7/9, and `21` §7. It also checked
planning-file immutability, scope leakage, script headers, rule length, and diff
whitespace.

Findings and bounded correction:

- The no-argument test runner did not reject unexpected arguments or expose
  `--help`; argument validation was added.
- `new-client.sh` could copy an uncommitted template while locking only HEAD;
  it now refuses a dirty methodology, with a regression test.

Final suite after the correction: **PASS (24 groups)**.

Correction-cycle count: **1**.

## Final known limitations / unverified behavior

- SPK-01 agent resolution, skill loading, additional-directory CLAUDE/rule
  loading, and live deny enforcement await a real Claude Code runtime.
- The scratch client has no remote/private/protected GitHub configuration by
  explicit experiment constraint.
- The connected methodology repository's visibility was not changed.
- No `v0.1.0` tag was created by explicit experiment constraint.
- `schema_validate.py` implements the draft 2020-12 keyword subset used by the
  two S0a schemas, not arbitrary future schemas. Later stages must extend this
  adapter and the same `validate.sh` when they introduce new keywords.
- Human onboarding facts and G0 approval are never fabricated by the bootstrap.

## Git publication

The required primary commit and branch push are performed after this report is
finalized. The authoritative final SHA and remote confirmation are the branch
Git history and the completion response; no PR, merge, or tag is created.
