# 13 — MVP Scope and Implementation Roadmap

**Purpose:** the MVP boundary, the ordered build sequence with gates/effort/risks per stage, the critical path, and the progressive-automation map.
**Baseline traceability:** B27 (roadmap refined), B30 superseded (DEC-19); absorbs baseline §22, §26, §27.

---

## 1. MVP definition

**The MVP is the capability to take one real client from first conversation to a monitored production website, with every lifecycle stage covered, using manual gates and manual glue where automation isn't built yet.**

In scope: methodology repo (versioned, locked, schema-validated) · client template + `new-client.sh` · working `client-discovery` agent (both modes) · specification pipeline with audits and G1/G2 · working `technical-solution-architect` with ADRs and delivery backlog · Jira export (CSV-level) · task loop with implementer + 2 reviewers + risk triggers · layered testing with test matrix · GitHub protections + CI (lint/type/test/build) · staging + production deploy via one provider adapter · release manifests + rehearsed rollback · monitoring minimal set · CR/BUG/incident workflows · retention policy.

Out of MVP (deferred, baseline §25 + DEC list): Jira REST automation & reconciliation · hooks-based methodology guard · parallel worktrees · web UI / API runtime · orchestrated multi-agent chaining · additional provider adapters · transcript-replay scenario automation.

**MVP acceptance = baseline §27's 15 validity criteria, all demonstrated on the pilot (S8), plus:** a production deploy + rollback rehearsal + one CR handled end-to-end.

## 2. Stage sequence

Per-stage fields: Objective · Why now · Inputs · Deliverables · Files · Tests · Acceptance · Deps · Risks · Effort (XS–XL) · Stays manual · Must not defer · Gate.

---

### S0 — Foundations (Effort: M)
- **Objective:** methodology repo skeleton + client template + launch/validation tooling + the load-bearing spike.
- **Why now:** everything else writes into these structures; SPK-01 de-risks the whole operating model first.
- **Inputs:** this plan; empty repos.
- **Deliverables:** `freelance-methodology` on private GitHub: `CLAUDE.md`, 5 always-on rules, `VERSION/CHANGELOG`, 13 schemas + fixtures, `templates/client-repo/` (03 §2 incl. settings deny rules, workflow shells), scripts (`new-client`, `start-agent`, `validate`, `status`, `check-methodology-clean`), methodology CI (schema/script tests), SPK-01 result recorded.
- **Files:** per `02` §2 tree (agents/skills as empty stubs only).
- **Tests:** schema fixtures valid+invalid; script smoke on scratch repo; SPK-01 checklist (a–d in `02` §5).
- **Acceptance:** `new-client.sh` → G0-passable repo in <10 min; `validate.sh` green on template; SPK-01 verdict documented (fallback A activated if failed).
- **Deps:** none. **Risks:** SPK-01 failure (mitigated: fallback designed); schema over-engineering (mitigate: only fields used by `04`–`08`).
- **Manual:** GitHub repo creation, branch protection clicks. **Must not defer:** deny rules, lock mechanism, ID counters, SPK-01.
- **Gate:** methodology v0.1.0 tagged; a fictitious client repo passes G0.

### S1 — Discovery interviewer (Effort: L) **[critical path]**
- **Objective:** working `client-discovery` per `04`.
- **Why now:** the baseline's stated differential value; hardest agent; everything downstream consumes its output.
- **Inputs:** S0; `04` in full.
- **Deliverables:** agent file; skills `adaptive-interview-control`, `interview-evidence-capture`, `nfr-elicitation`, `process-elicitation`; knowledge: `question-bank`, `interview-strategies`, `requirements-taxonomy`, `nfr-catalog`, `elicitation-techniques`, `evidence-and-uncertainty`, `glossary`; `interview-state` schema live; 3 interview scenarios (clear / contradictory / non-technical) + golden artifacts.
- **Tests:** scenario runs scored against golden checklists (coverage, classification, non-invention, contradiction catch, pause/resume mid-M7).
- **Acceptance:** contradictory-client scenario → CTR registered and confronted; pause/resume works from state file; DoD refuses premature close; evidence anchors on every candidate.
- **Deps:** S0. **Risks:** context bloat (keep skills lean, knowledge on-demand); scoring rubric subjectivity (fixed checklist per golden).
- **Manual:** you play the fictitious client. **Must not defer:** state persistence contract; completion criteria enforcement.
- **Gate:** all 3 scenarios pass; methodology v0.2.0.

### S2 — Specification pipeline (Effort: M) **[critical path]**
- **Objective:** interview evidence → audited, client-approvable baseline (`07`).
- **Inputs:** S1 scenario outputs as fixtures.
- **Deliverables:** `requirements-normalization` skill; `requirements-auditor` agent (5 audits); `doc-generator` agent; ambiguity/contradiction/assumption audit skills; PRD + validation-package + clarification templates; G1/G2 checklists operational.
- **Tests:** golden: planted ambiguities/contradictions/inventions in fixture evidence must be caught; schema round-trip; generated PRD cites only existing IDs.
- **Acceptance:** from a scenario transcript to G2-ready validation package with ≤2 fix cycles, no invention.
- **Deps:** S1. **Risks:** audit noise (severity thresholds tuned on fixtures). **Manual:** estimation, G1/G2 themselves. **Must not defer:** non-invention golden test.
- **Gate:** full discovery→validation-package run on fictitious client; v0.3.0.

### S3 — Technical design pipeline (Effort: L) **[critical path]**
- **Objective:** working `technical-solution-architect` per `05` + backlog generation.
- **Deliverables:** agent; skills `architecture-option-analysis`, `backlog-refinement`, `test-planning`, `artifact-generation` (SDD/ADR assembly); knowledge: `architecture-decision-framework`, `web-project-archetypes`, `security-baseline`, `test-strategy`, `deployment-patterns`, `ux-design-framework`; SDD/ADR/delivery-backlog/test-matrix templates+schemas; design-session state file; 2 design scenarios (hidden infeasibility; missing-client-fact→CLAR).
- **Tests:** scenario goldens (infeasibility caught at P1; CLAR generated, nothing invented; every approved REQ lands in coverage matrix).
- **Acceptance:** G3-ready package from S2's fixture baseline; delivery backlog passes DoR sampling.
- **Deps:** S2. **Risks:** decision-backlog sprawl (fixed category list caps it). **Manual:** all decisions (by design). **Must not defer:** requirement-coverage consolidation check.
- **Gate:** v0.4.0.

### S4 — Pilot: discovery → technical baseline (Effort: M) **[critical path]**
- **Objective:** run S1–S3 for real on a serious fictitious client or own project (baseline §22 E4).
- **Deliverables:** complete client repo through G3; friction log; methodology fixes (patch releases); `examples/fictitious-client/` populated (anonymized).
- **Acceptance:** end-to-end without editing methodology mid-flight (fixes queue for release); metrics captured: duration, question count, fix cycles, artifact usefulness verdicts.
- **Deps:** S3. **Risks:** self-leniency — use the gate checklists literally. **Gate:** G3 reached; friction log triaged; v0.5.0.

### S5 — Backlog → Jira (Effort: S)
- **Objective:** `08` operational: export, jira-map, G4 batch flow.
- **Deliverables:** `export-jira.sh` (CSV), `jira-map` schema, Jira project conventions doc, `jira-export` skill (formatting).
- **Acceptance:** pilot backlog visible in Jira with canonical IDs; re-export idempotent.
- **Deps:** S4 backlog. **Risks:** CSV import field quirks (timebox; fall back to manual creation with map file — still MVP-valid). **Manual:** import click, key capture. **Gate:** pilot board live.

### S6 — Implementation loop (Effort: L) **[critical path]**
- **Objective:** `09` operational: context packages, implementer, spec+adversarial reviewers, risk triggers, PR/DoD flow.
- **Deliverables:** 4 agents (implementer, spec-reviewer, adversarial-reviewer, risk-specialist-reviewer); skills `task-context-package`, `adversarial-code-review`; PR/task-context templates; `traceability-validation` skill live; branch/commit conventions enforced by convention doc + PR template.
- **Tests:** run 3–5 pilot tasks end-to-end incl. one high-risk (forms/auth) triggering specialist review; one seeded-defect task (adversarial reviewer must catch a planted bug).
- **Acceptance:** a story goes requirement→merged PR with all DoD boxes real; bounded fix cycles observed.
- **Deps:** S5 (or S4 backlog directly if Jira lags). **Risks:** reviewer rubber-stamping (seeded-defect test guards). **Manual:** launching each session; G5. **Must not defer:** reviewer role separation; traceability update in DoD.
- **Gate:** walking skeleton + first real story merged; v0.6.0.

### S7 — CI/CD, staging, release, ops (Effort: L) **[critical path]**
- **Objective:** `11` + `12` minimal set operational on the pilot.
- **Deliverables:** workflow templates finalized (ci/nightly/deploy-staging/deploy-prod); first provider adapter (chosen by pilot archetype); smoke suite; release-manager agent + `deployment-readiness-review` skill; REL manifest flow; rollback rehearsed; monitoring set up; runbook.
- **Tests:** pipeline green on pilot; staging deploy + smoke; prod-like deploy to a scratch target; rollback rehearsal executed.
- **Acceptance:** tag → approved prod deploy → smoke → monitored; rollback demonstrated.
- **Deps:** S6. **Risks:** provider quirks (adapter isolates); Actions minutes on private repo (verify quota). **Manual:** G6–G8 approvals, Jira release marking. **Must not defer:** rollback rehearsal, backup restore check.
- **Gate:** pilot live on staging+prod targets; v0.7.0.

### S8 — Full-cycle pilot & MVP acceptance (Effort: M) **[critical path]**
- **Objective:** one continuous run: new client repo → discovery → … → production → 1 CR + 1 simulated SEV-2 incident.
- **Acceptance:** baseline §27 criteria 1–15 all demonstrated + §1 additions; metrics + friction log; methodology v1.0.0 tagged.
- **Gate:** **MVP declared complete.** Ready for the first real client.

### S9 — Automation enhancements (Effort: ongoing, post-MVP)
Pulled from the automation map (§5) strictly by observed friction (baseline §2.1). First candidates: Jira REST + key capture; PreToolUse methodology guard; session chaining for the review pipeline; scenario replay harness; status report auto-publish.

---

## 3. Critical path & parallelism

```text
S0 → S1 → S2 → S3 → S4 → S6 → S7 → S8        (critical path)
                     S5 (Jira) off-path: needed before S8, parallel to S6
```

Rough calendar for one person at ~2 focused days/week: S0 1–1.5 wk · S1 2–3 wk · S2 1.5 wk · S3 2 wk · S4 1 wk · S5 0.5 wk · S6 2 wk · S7 2 wk · S8 1 wk ≈ **3.5–4 months to MVP**. First real client can start after S4 (discovery/spec are client-safe) while S6–S7 are finished — acceptable overlap if the client's timeline tolerates it.

## 4. Work-class legend per stage

Foundation work: S0 · Interviewer MVP: S1 · Documentation pipeline: S2 · Technical design pipeline: S3 · Delivery pipeline: S5–S6 · Deployment pipeline: S7 · Automation enhancements: S9. (Mission's required distinction, mapped.)

## 5. Progressive automation map (mission section M)

| Manual step (MVP) | Owner | In → Out | Automation candidate | Trigger to automate | Implementation option | Risk of automating | Preconditions |
|---|---|---|---|---|---|---|---|
| Launching each agent session | You | stage → session | Session chaining script | >3 sessions/day routinely | `start-agent.sh` pipeline mode / Agent SDK | Wrong-stage runs | Stable stage checks in `project.yaml` |
| Gate checklists (G0–G9) | You | artifacts → approval record | Checklist evaluators (mechanical items only) | Checklist fatigue / missed items | `validate.sh` extensions per gate | False confidence on judgment items | Split mechanical vs judgment items per checklist |
| Estimation (G2) | You | backlog → estimate | Historical calibration aid | ≥5 completed projects | metrics store + comparison script | Anchoring on bad history | Consistent effort logging |
| CLAR send/receive | You | OQ → evidence | Email templating + inbox capture | >2 clients concurrent | mail merge script / future app | Tone/PII errors | Client comms policy file |
| Jira import & key capture | You | CSV → board + map | REST API + auto map-back | After S8, first friction | `export-jira.sh --api` | Divergence bugs | Stable field mapping from S5 |
| Reviewer pipeline sequencing | You | merged code ← reviews | Scripted chain implementer→reviewers | Loop stable across ~10 tasks | headless `claude -p` per role | Rubber-stamp risk unobserved | Seeded-defect test in CI of methodology |
| Traceability updates at merge | You/implementer | PR → traceability.yaml | Post-merge Action | Missed updates observed | GH Action + script | Silent wrong links | `validate.sh` traceability checks solid |
| Status reporting | You | repo → report | `status.sh` output to client-friendly page | Client asks twice | scheduled Action → artifact | Leaking internals | Report template review |
| Staging smoke walkthrough | You | deploy → verdict | Full E2E in nightly | Flake rate <2% | Playwright suite growth | Flaky blocks releases | Quarantine policy working |
| Methodology upgrade per client | You | lock → new lock | `upgrade-lock.sh` batch mode | >3 active clients | script loop + report | Mass breakage | Migration notes discipline |
| Monitoring checks | You | signals → action | Alert routing + weekly digest | First missed alert | uptime/Sentry webhooks | Alert fatigue | Severity policy (12 §3) |

Every automated step keeps its manual fallback (the MVP procedure remains documented in the runbook/skill and stays executable).
