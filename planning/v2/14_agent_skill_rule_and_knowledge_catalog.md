# 14 — Agent, Skill, Rule, and Knowledge Catalog

**Purpose:** the complete inventory with contracts: for every agent and major skill — responsibility, trigger, inputs/outputs, read/write scopes, tools, prohibitions, completion, failure states, and result hand-off. Rules and knowledge files with their loading policy.
**Baseline traceability:** B3, DEC-12; information architecture per baseline Appendix C (retained).

---

## 1. Placement rule (what belongs where — baseline Appendix C, operationalized)

`CLAUDE.md`: durable identity, invariants, critical boundaries, source-of-truth rules — things that must never be missed. **Rules:** modular policies (evidence, traceability, privacy, change control), always-on or path-scoped. **Agents:** role identity, authority, tool scope, model, required skills, completion conditions — no procedures. **Skills:** reusable procedures with steps and checks. **Knowledge:** consultable reference, loaded on demand via `INDEX.md`. **Templates/schemas:** expected shape / structural validation.

Litmus: *must never be violated* → CLAUDE.md/rule · *who does this class of work* → agent · *how exactly is it done* → skill · *what does an expert know* → knowledge · *what does the output look like* → template+schema.

## 2. Agents (9 — DEC-12)

Common to all: write only inside the client repo; methodology read-only; produce `draft` statuses; stop at completion criteria or escalate; report results by writing artifacts + a short session summary appended to the relevant state/handoff file (file-based hand-off — the next agent reads files, never chat history).

| # | Agent | Model | Trigger | Reads | Writes | Tools | Must not | Done when | Failure states |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `client-discovery` | strongest | Stage `discovery`, G0 passed | project.yaml (incl. profile), lock, client-materials, question-bank & knowledge (profile/archetype-filtered, `17` §H) | evidence/interviews/** (sanitized), content-inventory seed, risk_triggers, requirements/context/OQ drafts | Read, Write, Edit (repo-scoped) | Full contract `04` §1; never write evidence-raw content into generated artifacts; never downgrade profile | DoD `04` §12 + your acceptance | paused, aborted, blocked-on-client, upgrade-proposed |
| 2 | `technical-solution-architect` | strongest | Stage `technical_design`, G2 passed | approved baseline, archetypes, tech knowledge | SDD, ADRs, data-model, api-contract, delivery-backlog, test-strategy/matrix, OQ(CLAR), design state | Read, Write, Edit, Bash (spike runs) | Full contract `05` §1 | DoD `05` §9 → G3 | paused, blocked-on-CLAR, infeasibility→CR |
| 3 | `requirements-auditor` | strong | Post-normalization; pre-G1; post-fix re-audit | evidence + draft artifacts + schemas | audit report (docs/quality/), CTR/OQ entries | Read, Write, Bash (validate.sh) | Fix findings itself; approve anything | 5 audits run, findings filed | inputs-unreadable → return to producer |
| 4 | `doc-generator` | strong | G1 passed; artifacts change post-approval | layer-2 artifacts | **Layer 3/4 only (R2-04):** PRD, validation-package, status report | Read, Write | Introduce un-ID'd statements; **write any layer-2 artifact (product-backlog.yaml is produced by `backlog-refinement`, product mode)** | docs generated + `generated_from` stamped | source-invalid → abort with report |
| 5 | `implementer` | strong | Task `ready` + context package | task-context, code, contracts | src/**, tests/**, task notes | Read, Write, Edit, Bash (build/test) | Contract `09` §4 | self-check green + summary | blocked, needs-CR, 2-attempts-failed |
| 6 | `spec-reviewer` | strong | Implementer done | context package, diff, test output | findings file in task dir | Read, Bash (run tests) | Rewrite code; expand scope of review | verdict + findings filed | diff-unreviewable → escalate |
| 7 | `adversarial-reviewer` | strongest | Spec review passed | same as 6 | findings + proposed regression tests | Read, Bash | Rewrite code; approve | verdict filed | same |
| 8 | `risk-specialist-reviewer` | strongest | Trigger table `09` §5 fires | diff + security/a11y checklists | findings + checklist evidence | Read, Bash | Waive its own findings | checklist complete | same |
| 9 | `release-manager` | strong | Release scope frozen (pre-G6) | merged tasks, matrix, manifests | REL manifest, CHANGELOG, runbook updates, G6/G8 checklists | Read, Write, Bash (status/validate) | Deploy or approve gates | manifest + checklists ready for your G8 | readiness-fail → blocking list |

## 3. Skills (18 — V2 adds `ux-design-outline`)

Format: **Trigger → In → Out → Key checks / must-not.** Users: agents listed; all invocable directly by you.

1. **adaptive-interview-control** (agent 1) — every interview turn → state+answer → next action per control loop `04` §7.3 → must-not: multi-questions, leading forms, close before DoD.
2. **process-elicitation** (1) — process topics in M4/M5 → narrative answers → structured process (trigger, actors, steps, exceptions, outcome) → sufficiency check `04` §4.
2b. **ux-design-outline** (2; V2, R2-17) — technical design, UX deliverables per profile (`21` §5) → approved baseline + visual preferences + ux-design-framework knowledge → sitemap/IA, flows, wireframe descriptions, component & state inventory, visual direction, responsive acceptance criteria (depth per profile); prepares the G3-V client visual-approval package → must-not: produce final visual design, skip error/empty states at HIGH-RISK, present visual choices as client needs.
3. **nfr-elicitation** (1) — M8 + archetype floor → client-language probes → NFR candidates with measurable anchors → must-not: jargon, skipping floor items.
4. **interview-evidence-capture** (1) — every turn → dialogue → transcript.md/.jsonl appends, anchors, state persistence per `04` §6 contract; **at close/pause: sanitization pass (R2-03): identifiers aliased/removed (never paraphrased), raw originals to evidence-raw/, `raw_ref` + sha256 stamped** → checks: no candidate without source_ref; turn numbering identical raw↔sanitized.
5. **ambiguity-audit** (3) — audit phase → draft requirements → findings with rewrites → vague-term lexicon + glossary check.
6. **contradiction-audit** (3) — audit phase → requirements+context+evidence → CTR entries → pairwise checks incl. budget/deadline vs scope.
7. **assumption-audit** (3) — audit phase → ASM register + spot-check source_refs against transcript → unconfirmed-load-bearing list → must-not: confirm assumptions itself.
8. **requirements-normalization** (1→2 pipeline) — post-interview / post-audit fixes → registers+transcript → requirements.yaml per rules `07` §2 → atomicity, dedup, typing, sourcing.
9. **artifact-generation** (2, 4) — G1/G3 packaging → layer 2 → PRD/SDD/validation-package per templates → no un-ID'd statements; `generated_from` stamp.
10. **traceability-validation** (3, 9, DoD step) — merge/release/audit → all artifacts → validation report + traceability.yaml updates → chain rules `08` §6.
11. **architecture-option-analysis** (2) — each decision item → item + driving REQs + knowledge → 2–4 options + recommendation + ADR draft → loop `05` §5; must-not: >4 options, no-recommendation lists.
12. **backlog-refinement** (2; two modes, R2-04/R2-11) — **product mode:** specification stage, post-normalization → approved-candidate REQs + scope phases → `product-backlog.yaml` (epics, vertically sliced stories, phases, priorities — `08` §1a); **delivery mode:** post-SDD; post-CR → product backlog + technical baseline → `delivery-backlog.yaml` (tasks, dependencies, code areas, tests, release targets — `08` §1b) → transformation contract `08` §2; DoR fields complete; must-not: mechanical 1-FR→1-story copying.
13. **task-context-package** (pre-implementation) — task `ready` → backlog+REQs+SDD+code map → TASK-nnn.md per `09` §3 → verbatim ACs; out-of-scope stated.
14. **adversarial-code-review** (7) — review step → diff+package → findings by failure-mode checklist (edge/error/injection/race/state/misuse) → must-not: style nitpicks as blockers.
15. **test-planning** (2) — technical design; new REQs → ACs+NFRs+archetype → test-strategy.md + matrix rows → every AC mapped `10` §4.
16. **jira-export** (with export-jira.sh) — G4 batch → delivery-backlog → CSV/JSON + map updates → idempotency `08` §5.
17. **deployment-readiness-review** (9) — pre-G6/G8 → manifest, suites, checklists, monitoring → go/no-go report with blocking list → must-not: waive rollback rehearsal.

## 4. Rules (8)

| Rule | Load | Policy core |
|---|---|---|
| evidence-policy | always | Evidence append-only; every fact needs source_ref; PII minimization; corrections are new turns; **raw/sanitized split (R2-03): raw stays in gitignored evidence-raw/, agents consume sanitized only, sanitization aliases identifiers but never paraphrases** |
| traceability | always | ID grammar `06` §4; no dangling refs; links updated at defined moments |
| id-and-status-conventions | always | Counters in project.yaml; status enums `06` §2; never renumber/reuse |
| client-data-separation | always | No client data outside client repo; methodology read-only; examples fictitious |
| change-control | always | Nothing `approved` changes without CR/G-record; supersede, don't rewrite |
| artifact-quality | path `docs/**` | Templates+schemas mandatory; generation direction `06` §5; `generated_from` stamps |
| requirement-lifecycle | path `docs/requirements/**` | Lifecycle transitions + who may trigger them; approval semantics per gate |
| implementation-safety | path `src/**, tests/**` | Scope bounds, no secrets, failing tests never committed, migration reversibility note |

## 5. Knowledge files (with "consult when") — V2: authored, sourced, versioned, and activated per the knowledge standard (`17`); research-gated items per `18`; per-file minimum content specs in `17` §K

**shared/**: requirements-taxonomy (classifying statements) · elicitation-techniques (stuck topics) · nfr-catalog (M8, NFR floor) · evidence-and-uncertainty (classification doubts) · glossary (term disputes).
**client-discovery/**: interview-strategies (module planning) · question-bank (seed questions + sufficiency checks per topic) · process-elicitation (M4/M5) · scope-and-mvp (M10) · technical-operational-context (M9).
**technical-solution/**: architecture-decision-framework (every decision item) · web-project-archetypes (P0 + NFR floors) · ux-design-framework (flows) · security-baseline (checklist source) · test-strategy (planning) · deployment-patterns (adapters, environments).
**legal/**: gdpr-basics, cookie-consent, accessibility-law — flagged topics; all headed "verify with a qualified professional".

`INDEX.md` lists each with a one-line "consult when"; agents load only on trigger (context economy — baseline risk mitigation retained).

## 6. Coverage check (every lifecycle subsystem has an owner)

Onboarding: you+scripts · Discovery: agent 1 · Analysis/spec: agents 3,4 + skills 5–9, 12(product) · Technical design: agent 2 + skills 2b, 11, 15 · UX & visual approval: agent 2 + skill 2b (G3-V) · Content readiness: agent 1 seeds, you+client feed, story DoR consumes (`08`) · Backlog/Jira: skills 12(delivery), 16 · Implementation: agents 5–8 + skills 13,14 · Testing: skill 15 + `10` · Git/CI/deploy: `11` + agent 9 · Client validation: you + skill 9 outputs · Operations/change: `12` + agent 9 · Methodology evolution: you + `02` §10 · Profile classification: agent 1 proposes, you confirm (G1), matrix applies (`21`). No orphan stages; no agent without artifacts; no artifact without a consumer (`06` §1).
