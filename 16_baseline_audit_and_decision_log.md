# 16 — Baseline Audit and Decision Log

**Baseline audited:** `plan_director_sistema_freelance_web_asistido_por_ia.md` (v0.1, 2026-07-10, Spanish). The baseline is immutable; this file records what the new plan retains, refines, removes, defers, and adds, with reasons. Every material deviation in files `01`–`15` traces back to a decision ID here (`DEC-xx`).

---

## 1. Baseline assumptions and decisions extracted

| # | Baseline decision | Location (§) | Verdict |
|---|---|---|---|
| B1 | Manual-first; automation responds to repeated friction | §2.1, §22, §29 | **Retain** |
| B2 | One single formal client interview + targeted clarifications | §2.2 | **Retain**, formalize clarification workflow (DEC-08) |
| B3 | Two main agents: Client Discovery / Technical Solution | §2.3 | **Retain**, add support agents (DEC-12) |
| B4 | Git is the source of truth | §2.4, §8 | **Retain** |
| B5 | Jira is an operational view; Git → Jira only | §2.5, §15 | **Retain** |
| B6 | Multi-level verification with adversarial review | §2.6, §16 | **Retain**, detail in `10` |
| B7 | Web app / API postponed | §2.7, §23 | **Retain** |
| B8 | Methodology repo + independent client repo, `--add-dir` | §3–6 | **Retain**, add verification spike + fallback (DEC-01) |
| B9 | Methodology read-only during client work (soft enforcement) | §6.4 | **Retain**, harden in MVP (DEC-02) |
| B10 | Semantic versioning + per-client `methodology.lock.yaml` | §7 | **Retain**, add schema_version in artifacts (DEC-03) |
| B11 | Four information layers with precedence order | §8 | **Retain** verbatim |
| B12 | Discovery artifact set (transcript, PRD, requirements, solution-context, backlog, open-questions, handoff) | §9 | **Retain**, extend schemas (DEC-04) |
| B13 | Requirement/US/UC/BDD are complementary, not rivals | §10 | **Retain** |
| B14 | Six artifact statuses; agents produce `draft` only | §11.1 | **Retain**, extend requirement lifecycle (DEC-05) |
| B15 | Four gates (business, technical, task, release) | §11.2 | **Refine** into ten explicit gates G0–G9 (DEC-06) |
| B16 | 14-step manual process | §12 | **Retain** as skeleton, detail per subsystem |
| B17 | DoR / DoD for tasks | §13 | **Retain**, add DoR/DoD for interview & stages (DEC-07) |
| B18 | Branch model, doc PRs, worktrees deferred, commit conventions | §14 | **Retain**, detail in `11` |
| B19 | Canonical IDs independent of Jira keys | §15.1 | **Retain**, normalize grammar (DEC-09) |
| B20 | Risk-based review matrix | §16.4 | **Retain** verbatim in `09`/`10` |
| B21 | Systemic learning loop (error → regression test → methodology change) | §16.5 | **Retain** |
| B22 | Change management flow | §17 | **Retain**, add CR IDs, classification, impact analysis (`12`) |
| B23 | Privacy rules (private repos, secrets out of Git, no client data in methodology) | §18 | **Retain**, add retention/anonymization (DEC-10) |
| B24 | Launch scripts select client + methodology + agent | §19 | **Retain** |
| B25 | `project.yaml` tracks state and artifact statuses | §20 | **Refine** — remove duplicated per-artifact statuses (DEC-11) |
| B26 | Agent design method + fictitious scenarios + golden artifacts | §21 | **Retain**, detail in `02`/`10` |
| B27 | Roadmap stages 0–10 | §22 | **Refine** into roadmap with gates and effort (`13`) |
| B28 | Hybrid future: API for interview, Claude Code for processing | §23 | **Retain** as future direction |
| B29 | "What not to build yet" list | §25 | **Retain** verbatim |
| B30 | First methodology backlog METH-01..06 | §26 | **Superseded** by roadmap in `13` (absorbed, not contradicted) |

## 2. Strengths (kept as design anchors)

1. Evidence / canonical data / human documents / operational views separation with explicit conflict precedence (§8) — the single best idea in the baseline; the whole plan is built on it.
2. Methodology-as-software: versioning, lock, tests, golden artifacts, regression (§7, §21).
3. Clear boundary between the two interviewers and between requirement / context / technical decision (§9.4).
4. Realistic risk table (§24) and "do not build yet" list (§25).
5. Human gates everywhere an irreversible decision occurs.

## 3. Gaps found (each is closed by a numbered plan file)

| Gap | Severity | Closed in |
|---|---|---|
| G-01 Interview state model, coverage model, next-question logic, completion criteria only named, never designed (§28 admits this) | Critical | `04` |
| G-02 Technical interviewer has responsibilities but no decision-backlog mechanism, no spike protocol, no clarification contract | Critical | `05` |
| G-03 No schemas defined (only file names) | High | `06`, `02` |
| G-04 No ID grammar, allocation, or uniqueness enforcement | High | `06` |
| G-05 Implementation loop is a 9-word diagram; no context package, agent contracts, fix-loop bounds | Critical | `09` |
| G-06 Testing listed by level but no test matrix, no planned/written/executed timing, no methodology-test harness design | High | `10` |
| G-07 CI/CD is one roadmap line; no pipeline, environments, secrets, migrations, rollback, provider adapters | High | `11` |
| G-08 Operations: no incident model, severities, monitoring stack, maintenance cadence, retention | High | `12` |
| G-09 Jira: no field mapping, no `jira-map.yaml`, no import contract, no divergence reconciliation | Medium | `08` |
| G-10 Interview channel undefined (who types? how is transcript captured? live vs imported?) | Critical | `04` (DEC-13) |
| G-11 No client onboarding / commercial phase (proposal, estimate, engagement record) although mission lifecycle starts there | Medium | `07`, `03` |
| G-12 No estimation checkpoint anywhere (budget is collected but never confronted with scope) | Medium | `07` (gate G2 includes estimate) |
| G-13 Session interruption / context-window exhaustion during long interviews unaddressed | High | `04` |
| G-14 Traceability file named but never designed | High | `08` |
| G-15 No model/cost policy per agent | Medium | `14` |
| G-16 Language policy (Spanish/Catalan clients vs English artifacts) undefined | Medium | `06` (DEC-14) |
| G-17 `--add-dir` agent/skill discovery is load-bearing but only doc-cited, never verified; no fallback | High | `02` (DEC-01) |
| G-18 No schema migration tooling between methodology versions | Medium | `02` |
| G-19 No branch protection / required checks spec for client repos | Medium | `11` |
| G-20 No archival, data-retention, or deletion procedure | Medium | `12` |
| G-21 No DoR for the interview itself; completion criteria informal | High | `04` |
| G-22 Duplication risk between requirements.yaml / PRD / backlogs / Jira — no generation-direction rules | High | `06` |
| G-23 No release manifest, rollback runbook, or smoke-test spec | Medium | `11` |
| G-24 No security baseline checklist for delivered sites (only review triggers) | Medium | `10` |

## 4. Contradictions / weak points in the baseline

| ID | Issue | Resolution |
|---|---|---|
| W-01 | §20 `project.yaml` duplicates artifact statuses that also live in artifacts → drift | DEC-11: statuses live in artifacts; `project.yaml` keeps stage + approvals + pointers only; a script derives a status report |
| W-02 | §15.1 mixes `REQ-001` and `FR-001`/`NFR-001` prefixes | DEC-09: single typed grammar; no generic `REQ-` IDs |
| W-03 | §11.1 statuses end at `approved` but §13 DoD needs "implemented/verified" for requirements | DEC-05: extended requirement lifecycle |
| W-04 | §2.2 "single interview" vs mission's iterative clarifications | DEC-08: CLAR workflow — single *formal* interview retained, clarifications are first-class artifacts |
| W-05 | Baseline assumes client interacts with Claude Code terminal directly — unstated and unrealistic for non-technical clients | DEC-13: two explicit interview modes |
| W-06 | AC IDs global (`AC-001`) → registry churn and weak locality | DEC-09: ACs scoped to parent (`FR-012-AC-01`) |

## 5. Risks of the chosen platform (Claude Code) — acknowledged in plan

- **R-CC1** Long interviews exhaust context → adherence degrades. Mitigation: incremental persistence + state-file re-hydration, module checkpoints (`04` §7).
- **R-CC2** `CLAUDE.md` is guidance, not a barrier → methodology writes possible. Mitigation: permission deny rules + launch-script git check + future hook (`02` §6).
- **R-CC3** Claude Code feature drift between versions. Mitigation: record Claude Code version in `methodology.lock.yaml`; Stage 0 spike re-run on upgrade.
- **R-CC4** Future API migration: skills/rules written as Claude-Code-native prose must stay runtime-agnostic in content. Mitigation: skills separate *procedure* (portable) from *invocation* (runtime); schemas/templates are runtime-neutral by construction (`06`).

## 6. Decision log (material deviations and additions)

| ID | Decision | Type | Rationale | Reverts if… |
|---|---|---|---|---|
| DEC-01 | Keep `--add-dir` as the methodology-connection mechanism, but Stage 0 includes a mandatory verification spike; documented fallback: thin agent/skill stubs in the client template that reference methodology paths; secondary fallback: package methodology as a Claude Code plugin | Addition | Load-bearing capability was cited but unverified | Spike proves `--add-dir` discovery works → fallback stays dormant |
| DEC-02 | Enforce methodology read-only from MVP day one via `permissions.deny` rules in client `.claude/settings.json` (deny Write/Edit on the methodology path), plus the baseline's git-status check in launch scripts | Refinement of B9 | Cheap, deterministic, available now; prose-only protection is the baseline's own admitted weakness | Never |
| DEC-03 | Every structured artifact carries `schema_version`; schemas versioned with the methodology; migration notes required in CHANGELOG for MAJOR bumps | Addition | Enables lock upgrades without archaeology | Never |
| DEC-04 | Full JSON-Schema definitions for the 8 core artifacts (see `06`); validation script is a Stage 0 deliverable | Addition | "Schemas exist" was asserted, never designed | Never |
| DEC-05 | Requirement status lifecycle extended: `draft → under_review → changes_requested → approved → implemented → verified` plus terminal `rejected / superseded / deprecated`. Document-level statuses stay as the baseline's six | Refinement of B14 | DoD requires demonstrating ACs; needs machine-readable verification state | Never |
| DEC-06 | Ten explicit gates G0–G9 replace the four implicit ones; each has entry criteria, checklist, approver, and record location | Refinement of B15 | Mission requires explicit criteria per gate; baseline gates conflated internal review with client approval | Never |
| DEC-07 | DoR/DoD defined for: interview, discovery package, technical baseline, task, release, change request | Addition | Only tasks had them | Never |
| DEC-08 | Clarification requests are first-class artifacts (`CLAR-nnn` in `open-questions.yaml` with channel, deadline, blocked items); answers become evidence in `evidence/confirmations/` | Formalization of B2 | Keeps "single interview" honest instead of aspirational | Never |
| DEC-09 | Unified ID grammar (see `06` §4): typed prefixes, zero-padded, project-scoped; ACs scoped to parent; generic `REQ-` dropped | Refinement of B19 | W-02, W-06 | Never |
| DEC-10 | Privacy additions: per-project retention policy in `project.yaml`, transcript PII-minimization rule, archival/deletion runbook | Addition | GDPR reality for EU freelance work | Never |
| DEC-11 | `project.yaml` no longer stores per-artifact statuses; it stores stage, approvals, lock pointer, retention, language; artifact status lives in each artifact's front-matter/field; `scripts/status.sh` derives the dashboard | Refinement of B25 | W-01: two sources of truth for status | Never |
| DEC-12 | Agent roster fixed at 9 (2 interviewers + requirements auditor + doc generator + implementer + spec reviewer + adversarial reviewer + risk specialist reviewer + release manager); all others are skills, not agents | Addition | Baseline named 4 agents but the lifecycle needs implementation-side roles; capped to avoid the "twenty agents" anti-pattern (§25) | An agent proves unused in pilot → demote to skill |
| DEC-13 | Two interview modes: **live-assisted** (client present; developer hosts the session; client speaks/types, developer relays or supervises) and **import** (existing call transcript/notes imported; agent produces gap analysis + follow-up question set). Both produce the same evidence package | Addition | G-10/W-05: the baseline never says how a non-technical client meets a terminal | A web UI ships (Stage 9+) → live-assisted moves there |
| DEC-14 | Language policy: IDs, keys, statuses, file names, code = English. `statement`, PRD prose, client validation package = client language (per-project `language` field). Methodology content = English | Addition | Operator works with Spanish/Catalan clients; artifacts must be client-readable and machine-stable simultaneously | Never |
| DEC-15 | Lightweight onboarding stage precedes discovery: engagement record (`docs/product/engagement.md`), G0 readiness gate | Addition | G-11: mission lifecycle starts at onboarding | Never |
| DEC-16 | Estimation checkpoint: G2 (business baseline) requires an effort/price estimate confronted with the client's stated budget before technical design begins | Addition | G-12: collecting budget without ever using it is waste | Never |
| DEC-17 | Project lifecycle stages fixed at 9: `onboarding, discovery, specification, technical_design, planning, implementation, validation, release, operation` | Formalization | `project.yaml` needs an enum, baseline never enumerated stages | Never |
| DEC-18 | Deployment provider adapters: generic pipeline + `scripts/deploy/<provider>.sh` contract (`deploy/rollback/health`); first adapters chosen per first real client | Addition | Mission forbids assuming one host | Never |
| DEC-19 | Baseline's METH-01..06 backlog absorbed into the Stage 0–9 roadmap (`13`); no separate methodology backlog file | Supersession of B30 | Two overlapping roadmaps would violate the baseline's own anti-duplication principle | Never |
| DEC-20 | Bounded fix loops everywhere an agent can iterate: max 2 corrective cycles per review stage, then mandatory human escalation | Addition | Mission's "no infinite refinement loops"; baseline had no bound | Never |

## 7. Removed / deferred (explicitly)

- **Removed:** nothing from the baseline is contradicted without a DEC entry above.
- **Deferred (unchanged from baseline §25):** autonomous orchestrator, bidirectional Jira sync, SaaS, automatic client detection, automatic worktrees, unattended deployment, large agent/skill inventories, complex RAG, multi-tenant infra. Additionally deferred by this plan: MCP-based Jira integration (script import first), plugin packaging of the methodology (unless DEC-01 spike fails), parallel implementation worktrees (introduced only when two independent tasks are truly concurrent — criteria in `09` §9).

## 8. Verified capability vs assumption (research policy)

- **Verified (baseline-cited official docs, 2026-07-10):** `CLAUDE.md` memory, `.claude/agents/`, `.claude/skills/`, `.claude/rules/`, `--add-dir`, `--agent`, Agent SDK existence.
- **Assumption pending Stage 0 spike (SPK-01):** agents/skills defined in an `--add-dir` directory are discoverable and selectable with `--agent` from the client root, and `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` loads that directory's `CLAUDE.md`/rules. Fallback designed in `02` §5.
- **Assumption:** GitHub Actions free tier suffices for MVP CI on private repos (verify minutes quota at Stage 7).
- **Future possibility (not designed in detail):** Messages API interview runtime, Agent SDK platform (baseline §23 retained as direction only).
