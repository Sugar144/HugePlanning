# 00 — Final Plan Index

**System:** AI-assisted freelance web development operating system
**Baseline:** `plan_director_sistema_freelance_web_asistido_por_ia.md` (v0.1, immutable — untouched)
**This plan:** v1.0, 2026-07-10, 17 files, implementation-ready
**Status:** complete; consistency review passed (1 correction pass applied)

---

## 1. Executive summary

This plan turns the baseline's high-level architecture into a definitive, implementation-ready design. The baseline's core is **retained**: one versioned methodology repository + one independent repository per client, connected via `--add-dir`; Git as the source of truth; Jira as an exported operational view; two specialist interviewer agents; human gates everywhere; manual-first with a designed automation path for every manual step.

What this plan **adds** (full audit in `16`): complete behavioural architectures for both interviewers (state machines, coverage models, question-selection logic, completion criteria); a normalized artifact/ID/status system with schemas; ten explicit gates G0–G9; a bounded implementation loop with separated implementer/reviewer agents; a layered testing architecture including tests for the methodology itself; a provider-agnostic CI/CD and deployment design; operations, incident, change-control, and retention procedures; and a 9-stage roadmap (S0–S8 + S9 automation) reaching a lifecycle-complete MVP in roughly 3.5–4 months of part-time work. Twenty material decisions/deviations are logged with rationale (`16` §6, DEC-01…DEC-20).

## 2. System map

```text
Methodology repo (how) ──--add-dir──▶ Client repo (what) ──▶ GitHub (truth, CI)
   agents · skills · rules ·             evidence · requirements ·   ├─▶ Jira (view)
   knowledge · templates ·               docs · backlog · code ·     ├─▶ Staging
   schemas · scripts · tests             tests · releases · ops      └─▶ Production
                        YOU: orchestrator + gates G0–G9
Lifecycle: onboarding → discovery → specification → technical_design → planning
           → implementation → validation → release → operation (→ change loop)
```

## 3. Files and reading path

Read in this order (each file states purpose + baseline traceability at top):

| File | Contents |
|---|---|
| `16_baseline_audit_and_decision_log.md` | Audit of the baseline; gaps; decision log DEC-01…20 — read first to understand every deviation |
| `01_architecture_and_operating_model.md` | System architecture, authority model, information layers & precedence, stages, gates G0–G9, agent roster, session/cost model |
| `02_methodology_repository_design.md` | Methodology repo structure, versioning + lock, read-only enforcement, `--add-dir` spike + fallback, scripts, methodology testing |
| `03_client_repository_design.md` | Client repo structure, creation process, `project.yaml`, client `CLAUDE.md`, privacy/secrets, G0 checklist |
| `04_client_discovery_interviewer_system.md` | **Priority subsystem.** Full behavioural architecture of the client interviewer (38 design dimensions, cross-indexed in its §15) |
| `05_technical_solution_interviewer_system.md` | The developer-facing design interviewer: decision backlog, option analysis, ADRs, spikes, CLAR requests |
| `06_artifact_and_information_architecture.md` | Artifact inventory, status models, ID grammar, schemas, templates, anti-duplication rules |
| `07_requirements_and_specification_pipeline.md` | Evidence → normalized requirements → audits → PRD → estimation → client validation (G1/G2) |
| `08_backlog_jira_and_traceability.md` | Decomposition rules, task DoR/DoD, Jira mapping/export, traceability model |
| `09_implementation_agent_workflow.md` | Task loop: context packages, implementer + reviewers, bounded corrections, PRs, worktree policy |
| `10_testing_and_quality_architecture.md` | Layered test strategy, test matrix, timing, adversarial-review relationship, security/a11y baselines |
| `11_git_github_ci_cd_and_deployment.md` | Branches, protections, pipeline, environments, provider adapters, release manifests, rollback |
| `12_operations_change_management_and_maintenance.md` | Monitoring, incidents, CR workflow (G9), dependency updates, retention/deletion |
| `13_mvp_scope_and_implementation_roadmap.md` | MVP boundary, stages S0–S9 (objective/deliverables/tests/gates/effort each), critical path, automation map |
| `14_agent_skill_rule_and_knowledge_catalog.md` | Contracts for all 9 agents, 17 skills, 8 rules, knowledge files; placement rules; coverage check |
| `15_risks_open_decisions_and_validation_plan.md` | Risk register, the 5 genuinely open decisions, plan validation approach |

## 4. Critical decisions (top 8 of 20 — full log in `16` §6)

1. **DEC-01** `--add-dir` connection kept but verified by mandatory spike SPK-01 at S0, with a fully designed fallback (agent stubs in the client template).
2. **DEC-02** Methodology read-only enforced from day one via permission deny rules, not just prose.
3. **DEC-06** Ten explicit gates G0–G9, each with checklist, approver, and written record.
4. **DEC-11** One source of truth per fact: artifact statuses live in artifacts; `project.yaml` holds only stage/approvals/config; dashboards are derived.
5. **DEC-13** Two interview modes (live-assisted, import) — resolving how a non-technical client actually meets the system.
6. **DEC-16** Estimation checkpoint at G2: scope is confronted with budget before technical design.
7. **DEC-19** Baseline's METH backlog superseded by the S0–S9 roadmap.
8. **DEC-20** Every agent loop is bounded (max 2 corrective cycles → human escalation).

## 5. MVP definition (full: `13` §1)

Take one real client from first conversation to a monitored production website with every lifecycle stage covered — manual gates and glue allowed, lifecycle gaps not. Acceptance = the baseline's 15 validity criteria (§27) demonstrated on a full pilot, plus a production deploy, a rehearsed rollback, and one change request handled end-to-end. Explicitly out: Jira REST sync, web UI/API runtime, orchestrated agent chaining, multi-tenancy.

## 6. Implementation order and critical path

```text
S0 Foundations → S1 Discovery interviewer → S2 Specification pipeline
→ S3 Technical design pipeline → S4 Pilot (discovery→G3)
→ S6 Implementation loop → S7 CI/CD + deployment + ops → S8 Full pilot = MVP
   (S5 Jira export runs in parallel before S8; S9 automation is post-MVP)
```

Estimated ~3.5–4 months at ~2 focused days/week. First real client may start after S4 (discovery/specification are client-safe before delivery tooling exists).

## 7. Open decisions (non-blocking — `15` §2)

OD-1 first deployment adapter (decide at S7; default `static`) · OD-2 Jira vs GitHub Projects for solo MVP (decide at S5; default Jira per baseline) · OD-3 pilot subject (decide at S4; default serious fictitious client) · OD-4 test stack per archetype (per project at G3) · OD-5 client status reporting (first real client). **None block S0–S3.**

---

## Implementation starts here

**First concrete task:** create the `freelance-methodology` repository skeleton and run spike SPK-01 (verify `--add-dir` agent/skill discovery) — S0, per `02` §2 and `02` §5.

**First ordered actions:**

1. Create `~/Projects/freelance-methodology`, `git init`, add the directory tree from `02` §2 (empty stubs for agents/skills).
2. Write `VERSION` (v0.1.0), `CHANGELOG.md`, `README.md` (launch + release instructions).
3. Write methodology `CLAUDE.md` from the invariant list in `02` §4.1.
4. Write the 5 always-on rules (`14` §4): evidence-policy, traceability, id-and-status-conventions, client-data-separation, change-control.
5. Write the 13 JSON Schemas from the normative field sets in `06` §7 + valid/invalid fixtures in `tests/schema-tests/`.
6. Implement `scripts/validate.sh` (schema validation + ID uniqueness + dangling refs) and make it pass on fixtures.
7. Build `templates/client-repo/` per `03` §2, including `.claude/settings.json` deny rules and client `CLAUDE.md` (`03` §5).
8. Implement `scripts/new-client.sh` and `scripts/check-methodology-clean.sh` (`02` §8).
9. Implement `scripts/start-agent.sh` (launch + lock check + before/after methodology drift check).
10. **Run SPK-01** (`02` §5): scratch client repo → verify agent/skill/CLAUDE.md discovery from `--add-dir` and write-deny enforcement; record verdict in README; activate Fallback A if needed.
11. Add methodology CI (GitHub Actions: schema + script tests); create private GitHub repo; push.
12. Implement `scripts/status.sh` (derived dashboard per DEC-11).
13. Create a scratch client with `new-client.sh`, walk the full G0 checklist (`03` §7), fix friction.
14. Tag methodology **v0.1.0** — S0 gate passed.
15. Begin S1: write the `client-discovery` agent file from `04` §1 contract.
16. Write skill `adaptive-interview-control` from `04` §7 (control loop, question rules) and `interview-evidence-capture` from `04` §6/§8 (persistence contract).
17. Write skills `nfr-elicitation` + `process-elicitation` and knowledge `question-bank.md` (module topics + sufficiency checks per `04` §4–5).
18. Write `interview-state.schema.json` usage into the agent (checkpoint/resume behaviour) and test pause/resume manually.
19. Author 3 interview scenarios + golden checklists (`02` §10): clear client, contradictory client, non-technical client.
20. Run and score the scenarios; iterate; tag v0.2.0 — S1 gate passed, proceed to S2 per `13`.

**Unresolved decisions blocking implementation: none.** OD-1…OD-5 are all scheduled at later stages with safe defaults; S0 can start now.
