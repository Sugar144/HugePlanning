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
│   │   ├── ux-design-outline/          # V2 (R2-17)
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
│   │                              # open-questions, content-inventory, handoff,
│   │                              # validation-package (+ LITE combined variant)
│   ├── technical/                 # SDD, ADR, delivery-backlog, test-strategy,
│   │                              # test-matrix, deployment-outline, ux-outline
│   └── delivery/                  # task-context, PR body, release-manifest,
│                                  # verification-snapshot, incident-report, change-request
│
├── schemas/                       # JSON Schema (draft 2020-12), one per structured artifact
│   │                              # created stage-by-stage at first consumer (R2-02);
│   │                              # conventions (ID grammar, enums, schema_version) fixed at S0a
│   ├── project.schema.json                # S0a
│   ├── methodology-lock.schema.json       # S0a
│   ├── interview-state.schema.json        # S0b
│   ├── requirements.schema.json           # S0b
│   ├── solution-context.schema.json       # S0b
│   ├── open-questions.schema.json         # S0b
│   ├── handoff.schema.json                # S0b
│   ├── content-inventory.schema.json      # S2  (V2, R2-18)
│   ├── product-backlog.schema.json        # S2
│   ├── delivery-backlog.schema.json       # S3
│   ├── test-matrix.schema.json            # S3  (definitions only, R2-07)
│   ├── jira-map.schema.json               # S5
│   ├── traceability.schema.json           # S6
│   ├── release-manifest.schema.json       # S7
│   └── verification-snapshot.schema.json  # S7  (V2, R2-07)
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

- Agents: 4 → 9 (DEC-12). Skills: 7 → 18 (V2 adds `ux-design-outline`, R2-17), all with named contracts in `14`.
- Added `knowledge/legal/`, `templates/client-repo/` (the client template lives *inside* the methodology so it is versioned with it), `templates/delivery/`, 15 schemas (was 5; V2 adds content-inventory and verification-snapshot), unified launcher script, `upgrade-lock.sh`.
- Renamed: `requirements-pack-generator` → `artifact-generation` (it generates all document packages, not only requirements).
- V2: knowledge governed by the authoring standard (`17`); schemas created stage-by-stage (R2-02); scripts are profile-aware (R2-21).

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

Reference material only — no policies, no procedures. Authoring, metadata, sourcing, retrieval, activation, lifecycle, and testing are governed by the knowledge standard (`17`); the research backlog for content requiring external verification is `18`. `knowledge/legal/` files carry a mandatory header (*informational only, verify with a qualified professional*) and remain `provisional` until primary-sourced.

## 5. Connection mechanism — VERIFIED (R2-16; evidence in `19` §0)

**Primary mechanism, confirmed against official Claude Code docs (2026-07-11):**

- `.claude/agents/` in `--add-dir` directories **is scanned** — methodology agents load alongside project subagents (verified).
- `.claude/skills/` in `--add-dir` directories **is loaded automatically, with live reload** (verified).
- Methodology `CLAUDE.md` and `.claude/rules/` load **only** with `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` (verified) — `start-agent.sh` always sets it.
- `claude --agent <name>` selects the agent for the main session (verified).

**Hard constraints propagated from verification:**
1. The methodology must be passed via the `--add-dir` **flag** (or `/add-dir`). The `permissions.additionalDirectories` setting grants file access only and loads **no** agents/skills — never rely on it for distribution.
2. Hooks and permission rules do **not** load from added directories; all enforcement config lives in the client repo's `.claude/settings.json` (already the design).
3. Knowledge/templates/schemas need no discovery at all — they are plain files read by path from the added directory.

**SPK-01 (downgraded to smoke check, S0a, ~1 h):** on the installed CLI version, from a scratch client repo confirm (a) agent resolution, (b) skill invocation, (c) CLAUDE.md/rules loading with the env var, (d) deny rules block methodology writes. Re-run on every Claude Code upgrade (CLI version recorded in the lock; RES-03 in `18`). Record results in methodology `README.md`.

**Dormant fallbacks (unchanged in design, unneeded per verification):**
- **A — materialized copies:** `new-client.sh` copies the locked version's agents/skills into the client `.claude/`; refreshed by `upgrade-lock.sh`.
- **B — dynamic injection:** `start-agent.sh` builds a `--agents '<json>'` payload from methodology files (flag verified to exist).
- **C — plugin packaging:** methodology as a version-pinned Claude Code plugin.

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

**Verified limitation (R2-16):** Edit/Write deny rules bind Claude's file tools and recognized Bash file commands, but **not arbitrary subprocesses** (a generated script that writes files itself). Consequently: the before/after `git status` check (item 2) is mandatory, never optional, and no client-session script may take the methodology path as a write target. OS-level sandboxing remains the eventual hard boundary.

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
| `validate.sh [client-dir]` | Validates every structured artifact against its locked schema version; checks ID uniqueness and dangling references; **profile-aware (R2-21): missing artifacts required by `21` §5 for the project's profile are errors, optional ones info**; exit non-zero on failure. Also runs in client CI |
| `status.sh [client-dir]` | Derives dashboard (DEC-11): stage, gate states (from latest `docs/handoffs/` per gate), artifact statuses read from artifacts, open questions/contradictions counts, requirement status histogram, profile + pending triggers; on LITE it renders the delivery-backlog task board (no Jira) |
| `export-jira.sh <client-dir>` | delivery-backlog.yaml → Jira CSV/JSON + updates `jira-map.yaml` (`08` §5) |
| `upgrade-lock.sh <client-dir> <version>` | §7 |
| `check-methodology-clean.sh` | §6 |

All scripts: bash, `set -euo pipefail`, no methodology content inside (baseline §19 retained), each with `--help`.

## 9. Web-project archetypes and process profiles (V2: governed by `21`)

The classification model lives in `21`: eight archetypes (what is being built → topics, knowledge packs, decision categories) × three process profiles (`LITE | STANDARD | HIGH-RISK` → assurance floors via the `21` §5 requirement matrix). `knowledge/technical-solution/web-project-archetypes.md` is the knowledge-pack expression of the archetype dimension (per `17` §K.12) and holds no floors — floors live once, in the matrix. The discovery agent tags an archetype hypothesis and records risk triggers; profile confirmation happens at G1 (`21` §4). Critical interview topics remain archetype-independent (unchanged from V1).

## 10. Methodology testing (baseline §21 retained, concretized)

| Layer | What | How run | When |
|---|---|---|---|
| Schema tests | Each schema accepts valid fixtures, rejects invalid ones | `validate.sh` against `tests/schema-tests/` | Every methodology commit (CI) |
| Script tests | Launcher/validators behave on a scratch repo | bats or plain bash asserts | Every methodology commit |
| Interview scenarios | Fictitious clients (clear, contradictory, solution-proposing, non-technical, exception-omitting, scope-inflating, sensitive-data, mind-changing, "I don't know" — baseline §21.1 list verbatim; **V2 adds: a LITE client, a trigger-escalation client (starts LITE, reveals payments), and a PII-bearing transcript for sanitization checks — R2-23, R2-03**) played against `client-discovery`; manual at MVP, scripted transcript-replay later | Human-driven session + checklist scoring | Before each MINOR/MAJOR release |
| Golden artifacts | Expected requirements/questions/contradictions per scenario; diff actual vs golden — judged on **coverage and non-invention**, not wording | Manual diff at MVP | Before each MINOR/MAJOR release |
| Regression cases | One dir per past failure: trigger input + expected safe behavior | Re-run relevant scenario | Before release touching the failed area |
| Knowledge tests (V2) | Consultation relevance, no gratuitous loading, evidence-over-knowledge precedence, defaults surfaced for confirmation, stale/provisional flags honored (`17` §J) | Scenario scoring + grep-level policy scan | Before each MINOR/MAJOR release |

**Release gate for the methodology itself:** all schema/script tests green + relevant scenarios re-run + CHANGELOG written. The methodology repo gets its own tiny GitHub Actions workflow for schema/script tests at Stage 0.
