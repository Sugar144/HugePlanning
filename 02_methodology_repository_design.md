# 02 — Methodology Repository Design

**Purpose:** implementation-ready design of `freelance-methodology`: structure, versioning, lock mechanism, read-only enforcement, connection to client repos (with verified fallback), scripts, and methodology testing.
**Baseline traceability:** B8, B9, B10, B24, B26; deviations DEC-01, DEC-02, DEC-03.

---

## 1. Repository facts

- Name: `freelance-methodology`. Local Git from day one; pushed to a **private GitHub repo at Stage 0** (not "when stable" — remote backup is cheap and the repo contains no client data). Refines baseline §4.1 timing only.
- Contains **zero client data, ever**. Examples use fictitious clients only (`examples/`).
- Treated as a software product: versioned, changelogged, tested, released.

## 2. Directory structure (authoritative)

```text
freelance-methodology/
├── README.md                      # what this is, how to launch, how to release
├── CHANGELOG.md                   # keep-a-changelog format, per release
├── VERSION                        # single line: v0.1.0
├── CLAUDE.md                      # invariant principles (§4.1)
│
├── .claude/
│   ├── settings.json              # shared defaults (model hints, safe permissions)
│   ├── agents/
│   │   ├── client-discovery.md
│   │   ├── technical-solution-architect.md
│   │   ├── requirements-auditor.md
│   │   ├── doc-generator.md
│   │   ├── implementer.md
│   │   ├── spec-reviewer.md
│   │   ├── adversarial-reviewer.md
│   │   ├── risk-specialist-reviewer.md
│   │   └── release-manager.md
│   ├── skills/                    # one dir per skill: SKILL.md (+ references/, examples/)
│   │   ├── adaptive-interview-control/
│   │   ├── process-elicitation/
│   │   ├── nfr-elicitation/
│   │   ├── interview-evidence-capture/
│   │   ├── ambiguity-audit/
│   │   ├── contradiction-audit/
│   │   ├── assumption-audit/
│   │   ├── requirements-normalization/
│   │   ├── artifact-generation/
│   │   ├── traceability-validation/
│   │   ├── architecture-option-analysis/
│   │   ├── backlog-refinement/
│   │   ├── task-context-package/
│   │   ├── adversarial-code-review/
│   │   ├── test-planning/
│   │   ├── jira-export/
│   │   └── deployment-readiness-review/
│   ├── rules/
│   │   ├── evidence-policy.md         # always loaded
│   │   ├── traceability.md            # always loaded
│   │   ├── id-and-status-conventions.md  # always loaded
│   │   ├── client-data-separation.md  # always loaded
│   │   ├── change-control.md          # always loaded
│   │   ├── artifact-quality.md        # path: docs/**
│   │   ├── requirement-lifecycle.md   # path: docs/requirements/**
│   │   └── implementation-safety.md   # path: src/**, tests/**
│   └── hooks/                     # empty at MVP; PreToolUse methodology-guard later (§6)
│
├── knowledge/
│   ├── INDEX.md                   # one-line description + "consult when" per file
│   ├── shared/                    # requirements-taxonomy, elicitation-techniques,
│   │                              # nfr-catalog, evidence-and-uncertainty, glossary
│   ├── client-discovery/          # interview-strategies, process-elicitation,
│   │                              # scope-and-mvp, technical-operational-context,
│   │                              # question-bank.md (per-module seed questions)
│   ├── technical-solution/        # architecture-decision-framework, ux-design-framework,
│   │                              # security-baseline, test-strategy, deployment-patterns,
│   │                              # web-project-archetypes.md (§9)
│   └── legal/                     # gdpr-basics, cookie-consent, accessibility-law (EU/ES)
│                                  # — all marked "verify with professional advice"
│
├── templates/                     # see 06 §6 for the full inventory
│   ├── client-repo/               # ENTIRE client repository template (03 §2)
│   ├── discovery/                 # PRD, requirements, solution-context, product-backlog,
│   │                              # open-questions, handoff, validation-package
│   ├── technical/                 # SDD, ADR, delivery-backlog, test-strategy,
│   │                              # test-matrix, deployment-outline
│   └── delivery/                  # task-context, PR body, release-manifest,
│                                  # incident-report, change-request
│
├── schemas/                       # JSON Schema (draft 2020-12), one per structured artifact
│   ├── project.schema.json
│   ├── methodology-lock.schema.json
│   ├── requirements.schema.json
│   ├── solution-context.schema.json
│   ├── open-questions.schema.json
│   ├── product-backlog.schema.json
│   ├── delivery-backlog.schema.json
│   ├── handoff.schema.json
│   ├── interview-state.schema.json
│   ├── traceability.schema.json
│   ├── test-matrix.schema.json
│   ├── jira-map.schema.json
│   └── release-manifest.schema.json
│
├── scripts/                       # §8
│   ├── new-client.sh
│   ├── start-agent.sh             # unified launcher (replaces per-agent scripts)
│   ├── validate.sh
│   ├── status.sh
│   ├── check-methodology-clean.sh
│   ├── export-jira.sh
│   └── upgrade-lock.sh
│
├── tests/                         # §10
│   ├── schema-tests/              # valid + invalid fixtures per schema
│   ├── interview-scenarios/       # fictitious client scripts (baseline §21.1 list)
│   ├── golden-artifacts/          # expected outputs per scenario
│   └── regression-cases/          # one dir per past failure
│
└── examples/
    └── fictitious-client/         # one fully worked mini-project (populated by Stage 4 pilot)
```

## 3. What changed vs baseline §4.2 (traceable)

- Agents: 4 → 9 (DEC-12). Skills: 7 → 17, all with named contracts in `14`.
- Added `knowledge/legal/`, `templates/client-repo/` (the client template lives *inside* the methodology so it is versioned with it), `templates/delivery/`, 13 schemas (was 5), unified launcher script, `upgrade-lock.sh`.
- Renamed: `requirements-pack-generator` → `artifact-generation` (it generates all document packages, not only requirements).

## 4. Content rules per mechanism

### 4.1 `CLAUDE.md` (≤ ~60 lines, invariants only — baseline §4.3 retained)

Contents, exactly: Git is truth · four layers + precedence order (one-line version) · never convert inference to fact · stable IDs, never renumber · agents draft, humans approve · no client data outside the client repo · methodology is read-only in client sessions · consult `knowledge/INDEX.md` before improvising method · validate structured artifacts against `schemas/` before declaring done · approved artifacts change only via change control. Anything longer belongs in rules/skills.

### 4.2 Rules

Modular policies; each ≤ 1 page; states **policy, why, and the observable violation**. Always-loaded set kept to 5 (context economy). Path-scoped rules attach via rule frontmatter `paths:` globs.

### 4.3 Agents

Frontmatter: `name, description, model, tools (allowlist), skills (required)`. Body: purpose · authority · boundaries (must-not list) · inputs/preconditions · outputs · completion criteria · failure/escalation. Agents contain **no procedures** — they reference skills.

### 4.4 Skills

`SKILL.md` structure: purpose · trigger · preconditions · inputs · procedure (numbered, checkable steps) · outputs · self-checks · failure modes · "must not". Procedure text is runtime-neutral (`01` §10). `references/` and `examples/` subdirs loaded only when needed.

### 4.5 Knowledge

Reference material only — no policies, no procedures. Every file listed in `INDEX.md` with a "consult when…" line so agents load selectively. `knowledge/legal/` files carry a mandatory header: *informational only, verify with a qualified professional*.

## 5. Connection mechanism and fallback (DEC-01)

**Primary (baseline):** `--add-dir` + `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`, launched by `start-agent.sh`.

**Stage 0 spike SPK-01 (mandatory, ~0.5 day):** from a scratch client repo, verify: (a) `--agent client-discovery` resolves an agent defined in the added dir; (b) skills in the added dir are invocable; (c) added-dir `CLAUDE.md` and rules load with the env var; (d) writes to the added dir are blocked by deny rules (§6). Record results in methodology `README.md`.

**Fallback A (if discovery fails):** the client template ships thin stubs in `client-repo/.claude/agents/*.md` — frontmatter only plus one line: *"Read and follow `$METHODOLOGY_DIR/.claude/agents/<name>.md`"*. Stubs are generated by `new-client.sh` from the locked version, so they stay pinned. Skills likewise stubbed or referenced by absolute path.
**Fallback B (if `--add-dir` unusable entirely):** package the methodology as a Claude Code plugin pinned by version. Only pursued if A also fails.

## 6. Read-only enforcement (DEC-02) — MVP, day one

1. Client template `.claude/settings.json` includes:
   ```json
   { "permissions": { "deny": [
       "Write(//home/<user>/Projects/freelance-methodology/**)",
       "Edit(//home/<user>/Projects/freelance-methodology/**)"
   ] } }
   ```
   (path templated by `new-client.sh`).
2. `start-agent.sh` snapshots `git -C $METHOD_DIR status --porcelain` before/after and alerts on drift (baseline §19.1 retained).
3. `check-methodology-clean.sh` runnable any time; also refuses to *launch* if the methodology has uncommitted changes (a dirty methodology means the locked commit is not what's actually loaded).
4. Later (roadmap stage S9): PreToolUse hook rejecting any tool call targeting the methodology path — defense in depth, not a replacement.

## 7. Versioning, lock, and upgrades (baseline §7 retained + DEC-03)

- SemVer in `VERSION` + annotated Git tag per release. PATCH: fixes, no contract change. MINOR: new skills/agents/knowledge, compatible schema additions (new optional fields). MAJOR: schema-breaking changes, artifact renames, behavioral contract changes.
- Every structured artifact instance carries `schema_version`. Schemas carry `$id` including version.
- **Release procedure:** run methodology tests (§10) → update CHANGELOG (with migration notes if MAJOR) → bump VERSION → tag → push.
- **Lock file** (client repo, example):

```yaml
# methodology.lock.yaml
schema_version: 1.0.0
methodology:
  repository: freelance-methodology
  version: v0.3.0
  commit: 4f2a9c1
  applied_at: 2026-09-02
  claude_code_version: "2.1.14"   # R-CC3
schemas:
  requirements: 1.1.0
  delivery-backlog: 1.0.0
```

- **Upgrade is always intentional** (`upgrade-lock.sh`): shows CHANGELOG diff between locked and target → runs `validate.sh` against new schemas → on MAJOR, prints migration notes and requires per-artifact confirmation → updates lock → commits with message `chore(methodology): upgrade lock v0.3.0 → v0.4.0`. Silent upgrades are impossible because sessions read the lock and `start-agent.sh` warns if the methodology checkout (tag/commit) differs from the lock — running each project against a `git worktree` of the locked tag is the recommended mechanism when multiple clients pin different versions (baseline §7.3 retained).

## 8. Scripts (deterministic glue — contracts)

| Script | Contract |
|---|---|
| `new-client.sh <dir> <PROJECT-ID>` | Copies `templates/client-repo/`, substitutes placeholders (project id, methodology path, retention defaults), `git init`, initial commit, writes lock from current methodology tag, prints G0 checklist |
| `start-agent.sh <client-dir> <agent> [--resume]` | Validates client repo + clean methodology + lock/checkout match → exports env var → launches `claude --add-dir … --agent …` → post-session methodology drift check + reminder to commit |
| `validate.sh [client-dir]` | Validates every structured artifact against its locked schema version; checks ID uniqueness and dangling references; exit non-zero on failure. Also runs in client CI |
| `status.sh [client-dir]` | Derives dashboard (DEC-11): stage, gate states, artifact statuses read from artifacts, open questions/contradictions counts, requirement status histogram |
| `export-jira.sh <client-dir>` | delivery-backlog.yaml → Jira CSV/JSON + updates `jira-map.yaml` (`08` §5) |
| `upgrade-lock.sh <client-dir> <version>` | §7 |
| `check-methodology-clean.sh` | §6 |

All scripts: bash, `set -euo pipefail`, no methodology content inside (baseline §19 retained), each with `--help`.

## 9. Web-project archetypes (supports "different web project types")

`knowledge/technical-solution/web-project-archetypes.md` defines profiles that tune NFR defaults, test depth, and deployment adapters: `static-brochure`, `cms-content-site`, `booking-or-forms`, `e-commerce`, `web-app`. Each archetype lists: typical NFR floor, mandatory review triggers, default test matrix rows, candidate providers. The discovery agent tags the project with an archetype hypothesis (confirmed at G3); it never changes what the client is asked about ownership/data/budget, only depth defaults.

## 10. Methodology testing (baseline §21 retained, concretized)

| Layer | What | How run | When |
|---|---|---|---|
| Schema tests | Each schema accepts valid fixtures, rejects invalid ones | `validate.sh` against `tests/schema-tests/` | Every methodology commit (CI) |
| Script tests | Launcher/validators behave on a scratch repo | bats or plain bash asserts | Every methodology commit |
| Interview scenarios | Fictitious clients (clear, contradictory, solution-proposing, non-technical, exception-omitting, scope-inflating, sensitive-data, mind-changing, "I don't know" — baseline §21.1 list verbatim) played against `client-discovery`; manual at MVP, scripted transcript-replay later | Human-driven session + checklist scoring | Before each MINOR/MAJOR release |
| Golden artifacts | Expected requirements/questions/contradictions per scenario; diff actual vs golden — judged on **coverage and non-invention**, not wording | Manual diff at MVP | Before each MINOR/MAJOR release |
| Regression cases | One dir per past failure: trigger input + expected safe behavior | Re-run relevant scenario | Before release touching the failed area |

**Release gate for the methodology itself:** all schema/script tests green + relevant scenarios re-run + CHANGELOG written. The methodology repo gets its own tiny GitHub Actions workflow for schema/script tests at Stage 0.
