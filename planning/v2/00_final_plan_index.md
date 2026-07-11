# 00 — Final Plan Index (V2)

**System:** AI-assisted freelance web development operating system
**Baseline:** `planning/baseline/plan_director_sistema_freelance_web_asistido_por_ia.md` (v0.1, immutable — untouched)
**This plan:** V2 ("robustness"), 2026-07-11, 22 files, implementation-ready. V1 preserved at tag `plan-v1.0`; V1 decision log in `16` (frozen); V2 decision log in `19`.

---

## 1. Architecture summary

One versioned **methodology repository** (agents, skills, rules, knowledge, templates, schemas, scripts, tests) connected read-only via `--add-dir` — a **verified official mechanism** (`19` §0) — to one **independent repository per client** (evidence, canonical data, documents, code, releases). Git is canonical truth in four layers with explicit precedence (evidence → canonical data → human documents → operational views); raw sensitive evidence lives outside Git in `evidence-raw/` with sanitized, anchor-preserving evidence committed (R2-03). Two interviewer agents (client discovery; technical solution + UX) plus seven delivery-side agents work through ten human gates (G0–G9, records append-only in `docs/handoffs/`). Jira, where used, owns only in-flight workflow status (Model B). The methodology is versioned, locked per project, and tested like software.

## 2. Process profile model (V2 core change)

Every project = **archetype × profile** (`21`):

- **Archetype** (9: static-landing, corporate-content-site, cms-content-site, forms-or-lead-generation, booking-system, e-commerce, authenticated-web-app, integration-heavy-web-app, migration-or-replatforming) — *what* is being built → activates interview topics, knowledge packs, decision categories.
- **Profile** (`LITE | STANDARD | HIGH-RISK`) — *how much* assurance → activates gates, artifacts, reviewers, test layers, deployment/ops floors through the single requirement matrix (`21` §5).
- Interaction: archetype decides whether a concern exists; profile decides how much assurance it gets; conflicts resolve stricter. Profile derives from **risk triggers** (payments, auth, sensitive data, migration, availability…), is hypothesized at G0, **confirmed at G1**, re-verified at G3, auto-upgraded on any trigger, downgraded only by explicit human decision with recorded reasoning. Agents propose, never select; ambiguity defaults up.
- Result: a landing page carries ≈6–10 h of process overhead (`21` §7) while an e-commerce build gets full assurance — same repos, same evidence discipline, strict subset vs superset.

## 3. Reading order and file inventory

| Order | File | Contents |
|---|---|---|
| 1 | `19_revision_audit_and_change_log.md` | V2 decisions R2-01..25 + Claude Code verification — read first |
| 2 | `01_architecture_and_operating_model.md` | System architecture, layers, stages, gates, authority |
| 3 | `21_process_profiles_and_archetypes.md` | Archetypes, profiles, triggers, requirement matrix, LITE fast path |
| 4 | `02_methodology_repository_design.md` | Methodology repo, versioning/lock, verified distribution, scripts, tests |
| 5 | `03_client_repository_design.md` | Client repo, evidence split, project.yaml, privacy, G0 |
| 6 | `04_client_discovery_interviewer_system.md` | Discovery interviewer (38 dimensions; sanitizing capture; trigger & content duties) |
| 7 | `05_technical_solution_interviewer_system.md` | Technical/UX interviewer, decision backlog, ADRs, G3-V visual approval |
| 8 | `06_artifact_and_information_architecture.md` | Artifact inventory/ownership, IDs, statuses, schemas (requirements v2, NFR, DAT, content) |
| 9 | `07_requirements_and_specification_pipeline.md` | Normalization, audits, product backlog, content inventory, G1/G2 |
| 10 | `08_backlog_jira_and_traceability.md` | Two backlogs, slicing, story/task DoR/DoD, Jira Model B, traceability |
| 11 | `09_implementation_agent_workflow.md` | Task loop, context packages (retained), reviewers, worktree policy |
| 12 | `10_testing_and_quality_architecture.md` | Test layers, definitions-only matrix, verification snapshots |
| 13 | `11_git_github_ci_cd_and_deployment.md` | Branches, pipeline, adapters, releases, rollback |
| 14 | `12_operations_change_management_and_maintenance.md` | Monitoring, incidents, CRs, maintenance tiers, retention/deletion |
| 15 | `17_knowledge_architecture_and_authoring_standard.md` | Knowledge taxonomy, metadata, sourcing, retrieval, activation, per-file minimums |
| 16 | `18_knowledge_research_and_evidence_plan.md` | Research backlog RES-01..10 (provisional vs research-mandatory) |
| 17 | `13_mvp_scope_and_implementation_roadmap.md` | MVP, AI-first stages S0a–S9, scenarios, critical path, automation map |
| 18 | `14_agent_skill_rule_and_knowledge_catalog.md` | Contracts: 9 agents, 18 skills, 8 rules, 19 knowledge files |
| 19 | `20_specification_completeness_matrix.md` | Generation-readiness of every element; no S0a blockers |
| 20 | `15_risks_open_decisions_and_validation_plan.md` | Risk register, open decisions, deferred limitations |
| 21 | `16_baseline_audit_and_decision_log.md` | V1 audit of the original baseline (historical, frozen) |
| 22 | `22_implementation_assurance_and_adversarial_validation.md` | Stage-level assurance loop for building the methodology itself (S0a lessons; read with `13`) |

## 4. MVP definition (full: `13` §1)

Take one real client from first conversation to a monitored production website with every lifecycle stage covered, at profile-appropriate weight, with manual gates and glue where automation isn't built. Acceptance = baseline §27's 15 criteria on the S8 pilot **plus** production deploy, rollback rehearsal, one CR end-to-end, profile confirmation + one trigger escalation, and a sanitized-evidence interview. Out: Jira REST sync, web UI/API runtime, agent orchestration, worktree parallelism, encrypted evidence platform.

## 5. Implementation sequence, critical path, AI-first scenarios

```text
S0a bootstrap → S0b discovery infra → S1 interviewer → S2 specification
→ S3 technical design → S4 pilot(front half) → S6 implementation loop
→ S7 CI/CD+ops → S8 full pilot = MVP        [critical path]
S5 Jira (profile-conditional, before S8) · RES-06/07/08 legal research
(during S2–S4, before first real client) · S9 automation (post-MVP)
```

Every stage runs the AI-first loop (`13` §2), executed under the proportional assurance sequence of `22`: contract reconciliation → risk-based test design → implementation → bounded independent review (risk-justified) → deterministic validation → real-runtime validation where relevant → failure classification → release evidence. Generation is cheap; **behavioural validation is the bottleneck and the planning basis** (R2-09).

| Scenario | Focused hours | Calendar (~8 fh/wk) |
|---|---|---|
| Optimistic | ≈ 90 | ~6–7 weeks |
| **Realistic (planning basis)** | ≈ 135 | **~9–11 weeks** |
| Contingency | ≈ 225 | ~5–6 months |

Earliest revenue point: a real LITE client after S4 + S6 + S7-floor.

## 6. Differences from V1 (summary — full log in `19`)

1. **Adaptive process profiles** (`21`): V1 applied uniform weight; V2 scales everything by LITE/STANDARD/HIGH-RISK with trigger-based escalation. Jira becomes profile-scoped (LITE: none) — logged deviation from baseline B5.
2. **AI-first roadmap** (`13`): effort re-decomposed around validation, not authoring; S0 split (S0a/S0b) + build-when-consumed schemas; three delivery scenarios.
3. **Evidence privacy** (`03`/`04`): gitignored `evidence-raw/` + committed sanitized evidence with identical turn anchors and hash linkage; consent at M0; true-deletion path.
4. **Verified distribution** (`02` §5, `19` §0): `--add-dir` agent/skill/rules loading confirmed against official docs; SPK-01 now a smoke check; fallbacks dormant.
5. **Ownership & history fixes**: product backlog → backlog-refinement product mode (doc-generator is layer-3 only); append-only `docs/handoffs/`; task contexts retained permanently.
6. **Requirements model v2** (`06` §7): `origin` provenance (defaults can't impersonate the client), structured measurable NFRs, `DAT-` data requirements, `approved_in` = baseline merge commit, single-writer ID allocation documented.
7. **Backlog architecture** (`08`): two backlog contracts, vertical slicing (no 1-FR→1-story), separate story/task DoR/DoD, outcome-based task sizing, Git/Jira authority Model B by field class.
8. **Testing** (`10`): matrix holds definitions only; execution evidence in CI runs + per-release verification snapshots.
9. **UX & content** (`05` §8, `07` §9): profile-scaled UX deliverables with G3-V client visual approval; content-inventory artifact wired into story DoR, gates, and change control.
10. **Knowledge system** (`17`/`18`): authoring standard (taxonomy, metadata, sourcing, retrieval, activation, testing) + per-file minimum specs + actionable research backlog; legal knowledge blocked from client use until primary-sourced.

## 7. Open decisions (`15` §2)

OD-1 first deployment adapter (S7; default static) · OD-3 pilot subject (S4; default fictitious) · OD-4 test stack per archetype (per project G3) · OD-5 client status reporting (first real client) · OD-6 LITE pilot vs first-real-LITE-client proof (S8; default the latter). **None block S0a–S3.** Documented deferred limitations: parallel ID allocation, Jira reconciliation automation, hook guard, encrypted evidence platform.

---

## Implementation starts here

**First concrete task (S0a):** create the `freelance-methodology` repository skeleton with the conventions rule, and run the SPK-01 smoke check — per `02` §2/§5 and `13` S0a.

**First ordered actions:**

1. Create `~/Projects/freelance-methodology`, `git init`, tree per `02` §2 (agents/skills as stubs).
2. Write `VERSION` (v0.1.0), `CHANGELOG.md`, `README.md`.
3. Write methodology `CLAUDE.md` (invariants, `02` §4.1).
4. Write the 5 always-on rules + the **conventions rule** (ID grammar incl. DAT/CNT, status enums incl. `proposed_default`, `schema_version` policy) — fixes the namespace before any schema exists (R2-02).
5. Generate `project.schema.json` (with profile fields) + `methodology-lock.schema.json` + fixtures.
6. Implement **minimal `validate.sh`** (project.yaml, lock, repo structure — the single progressive validator, extended at each later stage; R2-26).
7. Build `templates/client-repo/` per `03` §2 (settings deny rules, client CLAUDE.md, `.gitignore` with `evidence-raw/`, empty `open-questions.yaml`).
8. Implement `new-client.sh`, `check-methodology-clean.sh`, `start-agent.sh` (env var + `--add-dir` flag + `--agent`).
9. **Run SPK-01 smoke check** (`02` §5 a–d); record results + CLI version in README and lock template.
10. Create private GitHub repo, push, add methodology CI (schema/script tests).
11. Scratch client via `new-client.sh` → walk the full G0 checklist (`03` §7, incl. minimal `validate.sh` green) → tag **v0.1.0** (S0a gate).
12. S0b: generate the four discovery schemas (interview-state, requirements v2, solution-context+triggers, open-questions) + handoff schema + valid/invalid fixtures.
13. **Extend the same `validate.sh`** with the new schemas + profile-aware requirement matrix; implement `status.sh` v0; CI green → **v0.1.x** (S0b gate).
14. S1: write the `client-discovery` agent from `04` §1.
15. Generate skills: adaptive-interview-control, interview-evidence-capture (+sanitization), nfr-elicitation, process-elicitation.
16. Generate provisional knowledge set per `17` §K (S1 files), with front matter + INDEX.
17. Author the 6 interview scenarios + golden checklists (`02` §10 list incl. LITE, trigger-escalation, PII).
18. Run scenarios; score; bounded corrections; verify pause/resume and sanitization.
19. Tag **v0.2.0** (S1 gate) → proceed to S2 per `13`; in parallel with S2–S4, execute the RES-06/07/08 legal research batch and start RES-01 (`18` §4).
20. Continue S2 → S3 → S4 per `13`.

**Unresolved decisions blocking implementation: none.** S0a can start now.
