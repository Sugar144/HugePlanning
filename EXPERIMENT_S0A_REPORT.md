# Experiment report — S0a minimal runtime bootstrap (Claude)

**Evaluation-only document — not a canonical methodology artifact.**

## 1. Environment and model

- Environment: Claude Code (harness), Linux 7.0.14-zen1-1-zen, bash 5.3.15, git 2.x, python 3.14 (pyyaml 6.0.3, jsonschema 4.26.0 — installed during the session, see §10), Claude Code CLI 2.1.207.
- Model: Claude Fable 5 (`claude-fable-5`).
- Repository: `Sugar144/HugePlanning` · Branch: `experiment/claude-s0a` · Base commit: `51e0bf3fd1740a0c5e4f317bdc4cc5c7207b4c8c` (verified clean before work).
- The other experimental branch (`experiment/chatgpt-s0a`) was never inspected, fetched, compared, or referenced.

## 2. Implementation summary

Implemented S0a exactly per plan `13` (S0a deliverables), `02` (repo design, scripts, SPK-01), `03` (client template, G0), `14` §4 (rules), `06` §2/§4 + `01` §4.1 (conventions content), `20` (readiness), `19` (R2-02, R2-16, R2-26, R2-30). The existing planning repository **is** the methodology repository (experiment mandate); all planning documents preserved untouched; runtime files added alongside per the `02` §2 tree. All scripts derive the methodology location from their own path (env-overridable), so the plan's `~/Projects/freelance-methodology` path is not hardcoded.

Delivered: methodology `CLAUDE.md` (10 invariants, ≤60 lines) · 5 always-on rules including the conventions rule (full ID grammar incl. DAT/CNT, all status enums incl. `proposed_default`, `schema_version` policy, S0a namespace) · `VERSION` v0.1.0 + `CHANGELOG.md` · `project.schema.json` + `methodology-lock.schema.json` (draft 2020-12, versioned `$id`) with 5 valid + 16 invalid fixtures · progressive `validate.sh` (S0a scope; explicit in-file extension contract for S0b+) · complete minimal client template (client `CLAUDE.md`, deny-rule settings, `.gitignore` with `evidence-raw/`, `project.yaml`, lock, empty `open-questions.yaml` (R2-30), `engagement.md` skeleton, full `03` §2 directory tree, no later-stage artifact files) · `new-client.sh`, `start-agent.sh`, `check-methodology-clean.sh` · SPK-01 mechanism (`spk-01-smoke-check.sh` + manual fallback in README) with its two minimal fixtures (stub agent `client-discovery`, skill `methodology-smoke-check`) · test suite `tests/run-tests.sh` (87 assertions) · operational README.

## 3. Complete file list

**Modified:** `README.md` (was a 1-line stub; now operational documentation + SPK-01 results log).

**Added:**

```text
CLAUDE.md  VERSION  CHANGELOG.md  EXPERIMENT_S0A_REPORT.md
.claude/settings.json
.claude/agents/client-discovery.md            (S0a stub / SPK-01 fixture)
.claude/skills/methodology-smoke-check/SKILL.md
.claude/rules/evidence-policy.md
.claude/rules/traceability.md
.claude/rules/id-and-status-conventions.md    (the conventions rule)
.claude/rules/client-data-separation.md
.claude/rules/change-control.md
knowledge/INDEX.md
schemas/project.schema.json
schemas/methodology-lock.schema.json
scripts/new-client.sh  scripts/start-agent.sh  scripts/validate.sh
scripts/check-methodology-clean.sh  scripts/spk-01-smoke-check.sh
scripts/lib/schema-validate.py  scripts/lib/read-yaml-value.py
scripts/lib/check-deny-rules.py
templates/client-repo/{README.md, CLAUDE.md, project.yaml,
  methodology.lock.yaml, gitignore, .env.example,
  .claude/settings.json,
  docs/requirements/open-questions.yaml, docs/product/engagement.md}
templates/client-repo/<20 .gitkeep dirs per 03 §2 tree>
tests/run-tests.sh
tests/schema-tests/project/{valid-01..03, invalid-01..10}.yaml
tests/schema-tests/methodology-lock/{valid-01..02, invalid-01..06}.yaml
```

(`templates/client-repo/gitignore` is stored without the leading dot so it does not act on the methodology repo; `new-client.sh` renames it to `.gitignore` on copy.)

## 4. Plan requirement → implementation mapping

| Plan requirement (source) | Implementation |
|---|---|
| Methodology `CLAUDE.md`, invariants only, ≤~60 lines (`02` §4.1) | `CLAUDE.md` — exactly the ten listed invariants |
| 5 always-on rules, ≤1 page, policy/why/violation (`14` §4, `02` §4.2) | `.claude/rules/` × 5; path-scoped rules deferred to S0b–S6 per `20` §3 |
| Conventions rule: ID grammar, status enums, `schema_version` policy, S0a namespace (R2-02, `13` S0a) | `.claude/rules/id-and-status-conventions.md` |
| `VERSION` v0.1.0, `CHANGELOG.md` keep-a-changelog (`02` §2, §7) | Present |
| `project.schema.json` incl. profile fields (`03` §4, `20` §5) | `schemas/project.schema.json` — profile, profile_history, archetypes ×9, stages, approvals (6 gate keys per `03` §4, R2-22), privacy, 21 counters, jira tri-state |
| `methodology-lock.schema.json` (`02` §7) | `schemas/methodology-lock.schema.json` incl. `claude_code_version` (R-CC3) |
| Valid + invalid fixtures per schema (`02` §10, `13` S0a) | `tests/schema-tests/` — 3+10 project, 2+6 lock; each invalid file declares its intended failure via `# expect-error:` and the runner asserts it |
| Minimal progressive `validate.sh`: project.yaml, lock, structure; extended forever, never replaced (R2-26, `02` §8, R2-21) | `scripts/validate.sh` — table-driven checks, in-file S0b+ extension contract, profile read + S0b matrix hook, exit non-zero on error, INFO for gitignored `evidence-raw/` |
| Client template: tree, deny rules, client CLAUDE.md, `.gitignore` incl. `evidence-raw/`, empty `open-questions.yaml` (`03` §2/§5, `02` §6, R2-30) | `templates/client-repo/` — full directory tree, S0a files only (later-stage artifacts signalled by absence per `03` §2) |
| `new-client.sh` contract (`02` §8, `03` §3) | Copy, substitute `{{PROJECT_ID}}/{{METHOD_DIR}}/{{DATE}}` + lock fields, `git init` (main) + initial commit `chore: initialize <ID> from methodology <version>`, lock from checkout (+tag warning), prints G0 checklist, refuses non-empty target |
| `start-agent.sh` contract (`02` §8, §5–6, `19` §0) | Validates client (validate.sh), refuses dirty methodology, agent existence check, lock/checkout mismatch warning, exports `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`, launches `claude --add-dir … --agent …` from client dir, before/after drift alert (mandatory guard) |
| `check-methodology-clean.sh` (`02` §6) | Dirty detection with actionable output; used as launch precondition |
| SPK-01 smoke mechanism, checks a–d (`02` §5, R2-16) | `scripts/spk-01-smoke-check.sh` (live, headless) + minimal fixtures (stub agent, smoke skill) + manual fallback + results log in README |
| Automated tests for S0a contracts (`02` §10, `13` S0a tests) | `tests/run-tests.sh`: syntax, schema meta-checks, fixtures, scratch-client generation, validator red cases, script refusals, launch contract, drift alert — all under paths with spaces, against a committed throwaway copy |
| Operational documentation (`02` §2 README) | `README.md`: prerequisites, create/launch/validate, SPK-01 procedure + results, release procedure, testing |
| Scripts: bash, `set -euo pipefail`, `--help`, no embedded methodology content (`02` §8) | All five scripts + three python helpers comply; G0 checklist printout is the one scripted text (see assumption A6) |

## 5. Exact test commands and results

All commands run from the repository root; all executed for real in this session.

| # | Command | Result |
|---|---|---|
| 1 | `tests/run-tests.sh` (first run, pre-correction) | 86 passed / **1 failed** — fixture `invalid-04-empty-schemas.yaml` declared the wrong expected-error token (fixture failed validation for the intended reason; the declared token didn't match jsonschema's wording) |
| 2 | `tests/run-tests.sh` (after token fix) | **87 passed / 0 failed** |
| 3 | `tests/run-tests.sh` (after self-review corrections) | **87 passed / 0 failed** |
| 4 | `scripts/new-client.sh "<scratchpad>/spk client A" SPK-TEST` | Created; dirty-tree + no-tag warnings emitted as designed; deny rules substituted with the real space-containing path |
| 5 | `SPK01_TIMEOUT=240 scripts/spk-01-smoke-check.sh "<scratchpad>/spk client A"` | **5/5 PASS** (see §6) |
| 6 | G0 walkthrough: `new-client.sh` from a **committed byte-identical copy** → fill G0 fields (fictitious LITE client) → `validate.sh` → `start-agent.sh … client-discovery -- -p …` | validate.sh PASS; live launch PASS: preconditions enforced, agent resolved, stub reported project state, "Methodology unchanged" drift check green |
| 7 | Post-commit re-verification (results in §12) | `tests/run-tests.sh` re-run + live `start-agent.sh` against the real (now clean) methodology path |

Test-suite coverage highlights (all asserted, not eyeballed): every valid fixture passes; every invalid fixture fails **and** its stderr contains the declared reason; `validate.sh` red cases: missing `project.yaml`, invalid `project.yaml` (bad stage enum), missing lock, invalid lock (version pattern), missing `docs/handoffs/`, `.gitignore` without `evidence-raw/`, missing `open-questions.yaml`, deny rules absent; missing `evidence-raw/` is INFO-only (clone case); `new-client.sh` refuses non-empty target / bad ID / missing args with no partial output; generated client: one commit on `main`, no `{{` leftovers, lock commit == methodology HEAD, `evidence-raw/` present but untracked; `start-agent.sh` blocks launch on unknown agent / missing client / invalid client / dirty methodology (proven: stub binary never invoked), correct argv + env + cwd on the positive path, ALERT + exit 1 on simulated post-session methodology drift. Fake methodology and clients live under paths containing spaces throughout.

## 6. SPK-01 results (executed live)

`scripts/spk-01-smoke-check.sh` against the **real methodology path** (`/home/sugar/Documents/Huge Planning` — contains a space) from scratch client `SPK-TEST`, CLI **2.1.207**, headless `claude -p` sessions:

| Check (`02` §5) | Result | Evidence |
|---|---|---|
| (a) agent resolution via `--add-dir` + `--agent` | **PASS** | stub printed `SPK01-AGENT-OK`, then correctly reported project id/stage/profile/lock from the client repo |
| (b) skill invocation from added dir | **PASS** | `SPK01-SKILL-OK v0.1.0` (read the real `VERSION`) |
| (c) CLAUDE.md + rules loading with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` | **PASS** | `SPK01-CLAUDEMD-OK` + `SPK01-RULES-OK` (see caveat §10-U4) |
| (d) deny rules block methodology writes | **PASS** | client control write succeeded under `--permission-mode acceptEdits`; methodology write blocked at permission level ("File is in a directory that is denied by your permission settings"); no file created; methodology `git status` unchanged |

Result and CLI version recorded in `README.md` (SPK-01 log) per `02` §5.

## 7. G0 checklist result (scratch client `G0-DEMO`, fictitious LITE client)

| Item (`03` §7) | Result |
|---|---|
| Repo created from template | **PASS** (via `new-client.sh`) |
| …private, pushed, `main` protected | **NOT EXECUTED** — the experiment forbids creating repositories/remotes; branch is `main` (verified); GitHub steps documented as manual follow-up |
| Lock matches an existing methodology tag | **PARTIAL** — lock correctly records version+commit; no `v0.1.0` tag exists because the experiment forbids tagging; `new-client.sh` emitted the designed warning |
| `engagement.md` filled (identity, scope, terms + tier, content-deadline clause, channel) | **PASS** (fictitious content) |
| `project.yaml`: language, sensitivity, retention set; archetype + profile hypothesis with rationale | **PASS** (`static-landing`, `lite`, rationale recorded in `profile_history`) |
| `.gitignore` covers `evidence-raw/` | **PASS** (validate.sh check + suite test) |
| Deny rules point at the real methodology path | **PASS** (validate.sh check; enforced live in SPK-01 d) |
| `validate.sh` passes on the fresh repo | **PASS** |
| Launch test: `start-agent.sh <dir> client-discovery` starts and loads methodology | **PASS** — executed live pre-commit against a committed byte-identical methodology copy (the real tree was necessarily dirty pre-commit and the launcher correctly refuses dirty trees); re-run live against the real methodology after the primary commit (§12) |

**Conclusion: a generated scratch client satisfies G0** for everything executable in this environment; the two environment-blocked items (GitHub push/protection, release tag) are procedure-documented manual steps.

## 8. Assumptions made (narrowest consistent interpretation)

- **A1 — Methodology location:** this repository is the methodology repository (experiment mandate); scripts resolve it from their own location (`METHODOLOGY_DIR` override for tests) instead of the plan's example path `~/Projects/freelance-methodology`.
- **A2 — Agent/skill stubs:** plan `00` action 1 says "agents/skills as stubs" (9 agents); the experiment forbids production agents beyond minimal SPK-01 fixtures. Implemented only the `client-discovery` stub (required by the G0 launch-test checklist item) and the `methodology-smoke-check` skill. The other 8 agents and 17 skills land at their owning stages.
- **A3 — Methodology CI:** `00` action 10 mentions CI at S0a, but `02` §10 and `13` S0b place it at S0b. Followed the roadmap (`13`): **no CI at S0a**; `tests/run-tests.sh` is the reproducible mechanism. Plan-internal inconsistency recorded here.
- **A4 — Template defaults:** `project.yaml` template ships `profile: standard` / `archetype: [corporate-content-site]` with explicit `SET AT G0` markers (schema requires valid values so `validate.sh` can pass on a fresh repo; `03` §4's example uses `standard`). The G0 checklist forces conscious re-selection with rationale.
- **A5 — `open-questions.yaml` carries `schema_version: 1.0.0`** at S0a ( `02` §7: every structured artifact carries one) even though its schema lands at S0b; S0a validation is parse-only.
- **A6 — G0 checklist text lives in `new-client.sh`** (its `02` §8 contract is "prints G0 checklist"); creating a separate checklist artifact would add a file outside the `06` §1 inventory.
- **A7 — `spk-01-smoke-check.sh`** added to `scripts/` as the "minimal smoke-test mechanism required by SPK-01" (deliverable 10); not in the `02` §2 script list, which predates SPK-01's downgrade to a recurring smoke check (R2-16 requires re-runs on CLI upgrades, so it must be executable, not a one-off).
- **A8 — `start-agent.sh` accepts `-- <extra claude args>`** so the launcher itself can run non-interactive smoke/launch tests; interactive behaviour unchanged.
- **A9 — Lock `schemas` map at S0a** pins `project` and `methodology-lock` (the only existing schemas).
- **A10 — `templates/client-repo/gitignore`** stored undotted and renamed on copy, so the template's ignore rules cannot act on the methodology repository itself.
- **A11 — Methodology `.claude/settings.json`** is a minimal valid stub (`{"permissions": {"deny": []}}`): `02` §2 lists the file, but no concrete S0a content is specified anywhere in the plan; inventing model hints would be speculation.

## 9. Deliberate non-goals (verified absent)

No S0b+ deliverables exist: no interview-state / requirements / solution-context / handoff schemas; no open-questions schema (registry file only); no `status.sh`, `export-jira.sh`, `upgrade-lock.sh`; no discovery agents beyond the stub; no production skills; no path-scoped rules (S0b–S6 per `20` §3); no knowledge files (INDEX placeholder only); no CI workflows; no backlog/PRD/SDD artifacts or templates; no Jira/deployment anything; no `examples/` content (S4); no `.claude/hooks/` (S9). No tag, no merge, no PR.

## 10. Unverified behavior (explicit)

- **U1 — GitHub-dependent G0 items** (private repo, push, `main` protection): not executed (forbidden). Reproduction: create private repo, `git push`, enable protection, tick checklist.
- **U2 — Lock-against-tag matching:** no tag exists (forbidden). Reproduction: `git tag -a v0.1.0 && scripts/new-client.sh <dir> <ID>` → warning disappears.
- **U3 — Interactive `start-agent.sh` session** (without `-p`): not exercisable in this harness; verified headless end-to-end plus argv/env/cwd assertions at the exec boundary. Reproduction: run `scripts/start-agent.sh <client> client-discovery` in a terminal; expect the stub's report and the post-session drift check.
- **U4 — SPK-01 check (c) is model-self-report** (asks the session whether CLAUDE.md/rules content is loaded, with an explicit `SPK01-NOT-LOADED` escape). Checks (a)/(b)/(d) are corroborated by deterministic side effects; (c) has no filesystem side effect to assert. Accepted as designed by `02` §5 (smoke check, not proof).
- **U5 — Deny rules do not bind arbitrary subprocesses** — known verified limitation from `19` §0, not a defect; the mandatory compensating control (before/after `git status` drift alert) is implemented and its firing is test-covered.

## 11. Self-review findings and corrections (one bounded pass)

Full-diff comparison against `13` S0a, `02`, `03`, `14` §4, `20` after implementation:

1. **Found (test run):** `invalid-04-empty-schemas.yaml` declared an expected-error token not matching jsonschema's actual `minProperties` message ("should be non-empty"). **Fixed** (fixture comment only; validation behaviour was already correct).
2. **Found (honesty check):** README SPK-01 results row was drafted as PASS before the live run. **Fixed** — blanked to *pending*, then filled with actual results after execution.
3. **Found (fragile assumption):** `check-deny-rules.py` compared only `realpath` of the methodology dir, while `new-client.sh` writes the logical path — a symlinked methodology location would false-fail validation. **Fixed** — accepts logical or physical path match.
4. **Checked, no action:** omissions (none against the deliverable list), scope creep (A7/A8 are the only additions beyond the literal `02` §2 list, both required by S0a contracts), duplicated sources of truth (checked: enums live in the conventions rule + schemas as the plan prescribes — rule=policy, schema=enforcement; G0 checklist exists once in a script, referenced by README), later-stage leakage (none, §9).

Tests re-run after corrections: 87/87 green. **Correction cycles used: 1** (≤2 allowed per DEC-20).

## 12. Post-commit verification

Executed after the primary commit (results appended here only if a fix commit was needed; otherwise reported in the final experiment response): re-run `tests/run-tests.sh`; live `start-agent.sh "<scratchpad>/spk client A" client-discovery -- -p …` against the real, now-clean methodology checkout.

## 13. Final known limitations

- Single-writer ID allocation only; parallel-branch allocation deferred (plan `15`, R2-10).
- Deny rules protect the Write/Edit tool path, not subprocesses (mitigated by the drift guard; OS sandboxing is the eventual hard boundary — `02` §6).
- `validate.sh` S0a scope is structural + two schemas; profile-matrix and per-artifact schema enforcement arrive at S0b by extending the same script.
- SPK-01 must be re-run on every Claude Code CLI upgrade (procedure + log in README; `claude_code_version` in each client lock).
- Python `jsonschema`/`pyyaml` are runtime prerequisites for validation (documented in README; installed here via `pip --user --break-system-packages` under PEP 668).
- The methodology repo currently hosts the planning corpus at its root; this is the experiment's mandated layout and does not affect the runtime contracts.
