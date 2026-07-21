# 13 — MVP Scope and AI-First Implementation Roadmap

**Purpose:** the MVP boundary, the AI-first build sequence with per-stage effort decomposition and three delivery scenarios, the critical path, and the progressive-automation map.
**Baseline traceability:** B27 refined, B30 superseded (DEC-19). **V2:** AI-first effort model (R2-09), S0 split + stage-driven infrastructure (R2-02), profile-aware scope (R2-01), verified distribution (R2-16).

---

## 1. MVP definition

**The MVP is the capability to take one real client from first conversation to a monitored production website, with every lifecycle stage covered, using manual gates and manual glue where automation isn't built yet — at process weight matched to the project's profile (`21`).**

In scope: methodology repo (versioned, locked, schema-validated) · client template + `new-client.sh` · working `client-discovery` agent (both modes, profile-scaled, sanitizing evidence capture) · specification pipeline with audits, content inventory, and G1/G2 · working `technical-solution-architect` with ADRs, UX outlines + G3-V, delivery backlog · Jira export where the profile uses Jira · task loop with implementer + reviewers (merged pass on LITE) + risk triggers · layered testing with definitions-only matrix + release verification snapshots · GitHub protections + CI floors per profile · staging + production deploy via one provider adapter · release manifests + rehearsed rollback · monitoring floor · CR/BUG/incident workflows · retention + raw-evidence deletion.

Out of MVP (deferred): Jira REST automation & reconciliation · hooks-based methodology guard · parallel worktrees + parallel ID allocation · web UI / API runtime · orchestrated multi-agent chaining · additional provider adapters · transcript-replay scenario automation · encrypted evidence platform · domain packs.

**MVP acceptance = baseline §27's 15 validity criteria demonstrated on the pilot (S8), plus:** a production deploy, a rollback rehearsal, one CR end-to-end, **profile confirmation + one trigger-escalation exercised, and a sanitized-evidence interview**.

## 2. AI-first delivery model (R2-09)

Every stage follows the same loop — and its acceptance is always behavioural, never "the files look right":

```text
design contract (this plan, per 20's matrix)
→ AI generation (Claude Code/Fable writes files, multi-file patches)
→ integration (wire into repo, run scripts)
→ deterministic validation (schemas, script tests, CI)
→ behavioural scenario (fictitious-client runs, golden checklists)
→ human review (you judge behaviour + spot-check content)
→ bounded correction (findings back to generation; max 2 cycles per
   defect class, then re-examine the design contract, not the output)
→ release (methodology version tag)
```

The loop executes inside the **proportional assurance sequence of `22`** (S0a-verified): the design-contract step includes contract reconciliation (closed normative sets vs examples/schemas/templates/scripts — examples never silently shrink a closed set); tests are derived from material failure risks before generation; implementation is one principal implementer with bounded independent review only where risk justifies it; every failing check is classified (`CODE | TEST | CONTRACT | DATA | OPERATOR | PROCESS | ENVIRONMENT` — `22` §5, R2-39) before it is fixed, and runtime results distinguish fake-runtime, live-runtime, inconclusive-environment, and genuine failure; each release records the concise evidence set (`22` §7). Depth scales with the `22` §6 factors — a documentation-only change does not inherit the bootstrap-stage process.

**Where AI compresses effort (≈70–90% saving):** repo skeletons, schemas + fixtures, templates, scripts, rule/agent/skill file drafting, knowledge first drafts, test scenario scripts, boilerplate CI, multi-file consistency patches.
**Where it doesn't (≈0–30%):** behavioural scenario runs (you play the client — wall-clock human hours), interview-quality judgment, integration defects between generated parts, gate reviews, external research (18), real-client latency (content, approvals). **These dominate the critical path; plan around validation capacity, not generation capacity.**

Effort classes per stage below: **SP** spec/prompt prep · **G** AI generation · **I** integration · **DV** deterministic validation · **BV** behavioural validation · **C** correction cycles · **HA** human approval. Units = focused hours (fh) for you, the operator; generation wall-time is negligible at this scale.

## 3. Stage sequence

Stage fields kept from V1 (objective, deliverables, tests, acceptance, deps, risks, manual, must-not-defer, gate) with the AI-first effort row added.

---

### S0a — Minimal runtime bootstrap **[critical path]**
- **Objective:** launchable methodology + client skeleton + verified-mechanism smoke check + conventions locked.
- **Deliverables:** methodology repo on private GitHub: `CLAUDE.md`, 5 always-on rules, `VERSION/CHANGELOG`, **conventions rule (ID grammar, status enums, `schema_version` policy — fixes the namespace so later schemas can't drift, R2-02)**, `project.schema.json` + `methodology-lock.schema.json`, **minimal `validate.sh` (validates project.yaml, methodology.lock.yaml, and required repository structure — the same script is extended at every later stage, never replaced; R2-26)**, minimal client template (tree, settings deny rules, client CLAUDE.md, `.gitignore` incl. `evidence-raw/`), `new-client.sh`, `start-agent.sh`, `check-methodology-clean.sh`, SPK-01 smoke check executed and recorded.
- **Tests:** script smoke on scratch repo; SPK-01 checklist (a–d, `02` §5); schema fixtures for the 2 schemas; minimal `validate.sh` green on template, red on broken fixtures.
- **Acceptance:** `new-client.sh` → repo that **passes the full G0 checklist incl. minimal `validate.sh`** in <10 min; launch loads methodology agents/rules; deny rules verified live.
- **Deps:** none. **Risks:** low (mechanism verified, R2-16). **Manual:** GitHub clicks. **Must not defer:** conventions rule; deny rules; lock.
- **Effort:** SP 2 · G 1 · I 1 · DV 1 · BV 1 · C 1 · HA 0.5 ≈ **7–8 fh** (opt 5 / real 8 / cont 14).
- **Gate:** methodology v0.1.0 tagged; scratch client passes G0.

### S0b — Discovery infrastructure **[critical path]**
- **Objective:** everything the interviewer writes into, validated.
- **Deliverables:** schemas: interview-state, requirements (v2 model: origin, NFR fields, DAT), solution-context (+risk_triggers), open-questions, handoff; valid+invalid fixtures; **`validate.sh` extended with these schemas + the profile-aware requirement matrix (same script from S0a — no second validator)**; `status.sh` v0; methodology CI (schema/script tests); discovery templates (YAML skeletons, incl. the always-present empty `open-questions.yaml`).
- **Acceptance:** extended `validate.sh` green on template + red on every invalid fixture; CI runs on push.
- **Deps:** S0a. **Effort:** SP 2 · G 1.5 · I 1 · DV 2 · BV — · C 1.5 · HA 0.5 ≈ **8–9 fh** (opt 5 / real 9 / cont 15).
- **Gate:** v0.1.x; fixtures locked as the schema contract.

### S1 — Discovery interviewer **[critical path — the validation-heavy stage]**
- **Objective:** working `client-discovery` per `04` (both modes, sanitization, profile scaling, trigger duty, content seeding).
- **Deliverables:** agent file; skills: adaptive-interview-control, interview-evidence-capture (+sanitization), nfr-elicitation, process-elicitation; knowledge (per `17` §K, provisional): question-bank, interview-strategies, requirements-taxonomy, nfr-catalog, elicitation-techniques, evidence-and-uncertainty, glossary, scope-and-mvp, technical-operational-context, process-elicitation; **6 scenarios** (clear / contradictory / non-technical / LITE / trigger-escalation / PII-bearing) + golden checklists.
- **Tests (all behavioural):** scenario runs scored: coverage, classification (incl. `04` §3 example class), non-invention, contradiction catch, pause/resume mid-M7, sanitization correctness (PII case), LITE module floor respected, escalation flagged.
- **Acceptance:** all 6 scenarios pass their goldens; DoD refuses premature close; state re-hydration works.
- **Deps:** S0b. **Risks:** RSK-A2/A14 — behavioural quality needs iterations; budget 2 full correction cycles.
- **Manual:** you play the client (~1–1.5 h per scenario run + scoring). **Must not defer:** persistence contract; sanitization pass; completion enforcement.
- **Effort:** SP 3 · G 3 · I 2 · DV 1 · **BV 10–14** · C 4 · HA 1 ≈ **24–28 fh** (opt 16 / real 26 / cont 44).
- **Gate:** v0.2.0.

### S2 — Specification pipeline **[critical path]**
- **Objective:** evidence → audited, client-approvable baseline (`07`), incl. product backlog (product mode) + content inventory + profile confirmation at G1.
- **Deliverables:** requirements-normalization; requirements-auditor (5 audits + origin-integrity check); doc-generator (layer 3/4); backlog-refinement product mode; content-inventory schema+template; PRD/validation-package (+LITE compact variant)/clarification templates; G1/G2 checklists (incl. the LITE compact-workflow variants with distinct gate records).
- **Tests:** planted ambiguities/contradictions/inventions caught on fixture evidence; generated PRD cites only existing IDs; product backlog slices vertically (golden: a booking FR set → outcome stories, not renamed FRs); LITE fixture produces the 1-page brief.
- **Acceptance:** scenario transcript → G2-ready package in ≤2 fix cycles, zero invention.
- **Deps:** S1 outputs as fixtures. **Effort:** SP 2 · G 2 · I 1.5 · DV 1.5 · BV 5 · C 3 · HA 1 ≈ **16 fh** (opt 10 / real 16 / cont 27).
- **Gate:** v0.3.0.

### S3 — Technical design pipeline **[critical path]**
- **Objective:** working `technical-solution-architect` per `05` + UX outlines + delivery backlog.
- **Deliverables:** agent; skills: architecture-option-analysis, ux-design-outline, backlog-refinement delivery mode, test-planning, artifact-generation (SDD/ADR assembly); technical knowledge set (provisional per `17` §K); schemas: delivery-backlog, test-matrix (definitions-only); SDD/ADR/ux-outline templates; design-session state; 2 design scenarios (hidden infeasibility; missing-client-fact→CLAR).
- **Tests:** infeasibility caught at P1; CLAR generated, nothing invented; every approved REQ lands in the coverage matrix; UX outline depth matches profile; G3-V package produced for the STANDARD fixture.
- **Acceptance:** G3-ready package from S2's fixture baseline; delivery backlog passes DoR sampling with outcome-sized tasks (`08` §3).
- **Deps:** S2. **Effort:** SP 2.5 · G 2.5 · I 1.5 · DV 1 · BV 6 · C 3 · HA 1 ≈ **17–18 fh** (opt 11 / real 18 / cont 30).
- **Gate:** v0.4.0.

### S4 — Pilot: discovery → technical baseline **[critical path]**
- **Objective:** run S1–S3 for real on a serious fictitious client (STANDARD profile) — first uninterrupted end-to-end of the front half.
- **Acceptance:** G3 reached without mid-flight methodology edits (fixes queue for release); metrics captured (duration, questions, fix cycles, artifact usefulness); friction log triaged; `examples/fictitious-client/` populated.
- **Deps:** S3. **Effort:** mostly BV/HA ≈ **10–12 fh** (opt 8 / real 11 / cont 18). **Gate:** v0.5.0.
- **Recommended parallel:** run the RES-06/07/08 research batch (`18` §4) during S2–S4 so legal knowledge is verified before any real client.

### S5 — Backlog → Jira (profile-conditional)
- **Objective:** `08` §4–5 operational for Jira-using profiles: export, jira-map, G4 batch flow.
- **Acceptance:** pilot backlog on a board with canonical IDs; re-export idempotent; authority table exercised (status reconciliation at a fake PR event). LITE path needs none of this — `status.sh` board demonstrated instead.
- **Deps:** S4. **Effort:** ≈ **5 fh** (opt 3 / real 5 / cont 9, incl. RES-04 quirks). Off critical path.

### S6 — Implementation loop **[critical path]**
- **Objective:** `09` operational: context packages, implementer, reviewers (incl. LITE merged pass), risk triggers, PR/DoD flow, traceability.
- **Deliverables:** 4 agents; skills task-context-package, adversarial-code-review, traceability-validation; traceability schema; PR/task-context templates.
- **Tests:** 3–5 pilot tasks end-to-end incl. one high-risk task triggering the specialist and **one seeded-defect task the adversarial reviewer must catch**; story DoD (E2E AC demonstration) exercised once.
- **Acceptance:** a story goes requirement→merged PRs→demonstrated outcome with every DoD box real; bounded fix cycles observed.
- **Deps:** S4 (S5 optional). **Effort:** SP 2 · G 2 · I 2 · DV 1.5 · BV 6 · C 3 · HA 1.5 ≈ **18 fh** (opt 11 / real 18 / cont 30).
- **Gate:** walking skeleton + first real story merged; v0.6.0.

### S7 — CI/CD, staging, release, ops **[critical path]**
- **Objective:** `11` + `12` floors operational on the pilot: pipeline, first provider adapter, smoke suite, release-manager agent, verification snapshot, manifest, rollback rehearsal, monitoring, runbook.
- **Deliverables:** + schemas: release-manifest, verification-snapshot, jira-map (if S5 done); deployment-readiness-review skill.
- **Tests:** pipeline green; staging deploy + smoke; scratch prod-like deploy; **rollback rehearsal executed**; backup restore spot-check.
- **Acceptance:** tag → approved prod deploy → smoke → monitored; verification snapshot generated for the release.
- **Deps:** S6. **Risks:** provider quirks (RES-09), Actions quota. **Effort:** SP 2 · G 2.5 · I 3 · DV 2 · BV 4 · C 3 · HA 1.5 ≈ **18 fh** (opt 11 / real 18 / cont 32).
- **Gate:** v0.7.0.

### S8 — Full-cycle pilot & MVP acceptance **[critical path]**
- **Objective:** one continuous run at STANDARD profile: new client repo → discovery → … → production → 1 CR + 1 simulated SEV-2 + 1 trigger-escalation exercise. (LITE proof per OD-6 default: first real LITE client.)
- **Acceptance:** §1 MVP acceptance list, evaluated literally against checklists; friction log; **v1.0.0 tagged — MVP complete, ready for a real client.**
- **Deps:** S7 (+S5 for the STANDARD pilot). **Effort:** ≈ **12–14 fh** (opt 9 / real 13 / cont 22).

### S9 — Automation enhancements (post-MVP, friction-driven)
First candidates unchanged from V1 (Jira REST + reconciliation, PreToolUse guard, review-pipeline chaining via `--agents`/headless, scenario replay harness, status publishing) — pulled strictly by the observed-friction rule via the automation map (§6).

---

## 4. Scenarios and critical path

```text
Critical path: S0a → S0b → S1 → S2 → S3 → S4 → S6 → S7 → S8
Off-path:      S5 (Jira) before S8's STANDARD pilot; RES-06/07/08 before first real client
```

| Scenario | Focused hours | Calendar at ~8 fh/week | Assumes |
|---|---|---|---|
| **Optimistic** | ≈ 90 fh | **~6–7 weeks** | Generation mostly right first pass; ≤1 correction cycle per stage; scenarios pass early |
| **Realistic** | ≈ 135 fh | **~9–11 weeks** | 2 correction cycles on interviewer/design stages; normal integration defects |
| **Contingency** | ≈ 225 fh | **~5–6 months** | Interview quality needs a redesign iteration (`04` revision); a fallback mechanism activates; provider/Jira quirks; personal availability dips |

Do not promise the optimistic case: it depends on first-generation output quality you cannot guarantee (RSK-A14). The realistic case is the planning basis. **A real LITE client becomes serviceable after S4 + S6 + S7-floor** (LITE needs no Jira and only the collapsed pipeline), which is the earliest revenue point.

## 5. Work-class legend

Foundation: S0a/S0b · Interviewer MVP: S1 · Documentation pipeline: S2 · Technical design pipeline: S3 · Delivery pipeline: S5–S6 · Deployment pipeline: S7 · Automation enhancements: S9.

## 6. Progressive automation map

Unchanged in structure from V1 (owner / in→out / candidate / trigger / option / risk / preconditions), with V2 deltas: Jira REST row is conditional on profiles that use Jira; add rows — **sanitization assist** (owner: you+skill; candidate: PII-pattern pre-scan script; trigger: >2 redaction misses; risk: false confidence; precondition: PII scenario suite), **profile trigger scan** (candidate: `validate.sh` rule flagging trigger keywords in solution-context vs profile; trigger: first missed escalation), **verification snapshot assembly** (candidate: script pulling CI run results into the snapshot; trigger: 2nd manual assembly). Every automated step keeps its manual fallback documented.
