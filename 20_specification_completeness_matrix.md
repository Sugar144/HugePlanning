# 20 — Specification Completeness Matrix

**Purpose:** classify every implementation element of the V2 plan by generation-readiness, so AI-first implementation can start without hidden blockers. Statuses assess the plan as revised on `plan-v2-robustness` (decisions in `19`).
**Status legend:** `FS` fully specified (contract + fields + example exist in plan) · `SG` sufficient to generate (contract complete; AI can produce a first version needing only behavioural validation) · `PS` partially specified (contract exists; named details missing) · `US` underspecified (would need design before generation).
**Column legend:** T/S/E/F = required Template / Schema / Example / Fixture · DT/BT = deterministic / behavioural test required · Blk = blocks its target stage if not resolved · Stage = target roadmap stage (`13`).

Everything at `PS` lists its missing details; nothing is `US`. **No unexplained blockers exist for S0a** (consistency check #35): every S0a element is `SG` or better.

## 1. Agents (owning file: `14` §2 + subsystem files)

| Element | Spec | Missing details | T | S | E | F | DT | BT | Blk | Stage |
|---|---|---|---|---|---|---|---|---|---|---|
| client-discovery | FS (`04` full behavioural architecture) | — | agent-file template implicit in `02` §4.3 | — | control-loop + transitions in `04` | scenarios | — | Y (scenario suite) | Y→S1 | S1 |
| technical-solution-architect | FS (`05`) | — | same | — | decision-item walkthrough `05` §12 | 2 design scenarios | — | Y | Y→S3 | S3 |
| requirements-auditor | SG (`07` §4, `14`) | severity thresholds tuned on fixtures (planned, not a gap) | — | — | findings format named, example generated at S2 | planted-defect fixtures | — | Y | N | S2 |
| doc-generator | SG (`07` §7, `14`; scope narrowed R2-04) | — | — | — | — | non-invention fixture | Y (ID-citation check) | Y | N | S2 |
| implementer | SG (`09` §4) | — | — | — | — | seeded-defect task | — | Y | N | S6 |
| spec-reviewer / adversarial-reviewer | SG (`09` §5) | — | — | — | findings format `09` §5 | seeded-defect task | — | Y | N | S6 |
| risk-specialist-reviewer | SG (`09` §5, `10` §5) | checklist sources = knowledge files (see §4) | — | — | — | — | — | Y | N | S6 |
| release-manager | SG (`11` §7, `14`) | — | — | — | manifest example `11` §7 | — | Y (readiness checks scriptable) | — | N | S7 |

## 2. Skills (18 — `14` §3)

| Element | Spec | Missing details | E | F | DT | BT | Blk | Stage |
|---|---|---|---|---|---|---|---|---|
| adaptive-interview-control | FS (`04` §7) | — | Y (`04` §14) | scenarios | — | Y | Y→S1 | S1 |
| interview-evidence-capture (+ sanitization, R2-03) | FS (`04` §6, §8) | — | Y | PII fixture | Y (hash/anchor checks) | Y | Y→S1 | S1 |
| process-elicitation / nfr-elicitation | SG (`04` §4–5, `14`) | seed content comes from question-bank (§4) | — | scenarios | — | Y | N | S1 |
| ambiguity/contradiction/assumption-audit | SG (`07` §4) | — | — | planted defects | — | Y | N | S2 |
| requirements-normalization | FS (`07` §2 rules + `06` §7.1 target) | — | Y | scenario output | Y (schema) | Y | N | S2 |
| artifact-generation | SG (`07` §7, templates `06` §6) | — | — | — | Y (`generated_from` stamps) | Y | N | S2 |
| backlog-refinement (product + delivery modes, R2-04/11) | SG (`08` §1–2) | — | Y (`06` §7.4) | pilot backlog | Y (schema) | Y | N | S2(prod)/S3(del) |
| architecture-option-analysis | FS (`05` §5) | — | Y (`05` §12) | design scenarios | — | Y | N | S3 |
| test-planning | SG (`10` §1, §4) | — | Y (matrix def) | — | Y | — | N | S3 |
| ux-design-outline (new, R2-17) | SG (`05` §8, `21` UX floors) | wireframe-description format example → generate at S3 | N (gen) | — | — | Y | N | S3 |
| task-context-package | FS (`09` §3) | — | Y | — | — | — | N | S6 |
| adversarial-code-review | SG (`09` §5, `14`) | — | — | seeded defect | — | Y | N | S6 |
| traceability-validation | SG (`08` §6) | — | Y | — | Y | — | N | S6 |
| jira-export | SG (`08` §5) | Jira CSV field quirks → S5 timebox (known risk, not spec gap) | Y (map) | — | Y | — | N | S5 |
| deployment-readiness-review | SG (`11` §6–7, `10` §6) | — | — | — | Y | — | N | S7 |

## 3. Rules (8 — `14` §4): all **SG** — policy core + violation stated; full text generated at S0a/S0b. DT: rule presence checked by methodology CI. No blockers. Stage: S0a (5 always-on), S0b–S6 (path-scoped, with first consumer).

## 4. Knowledge files (19 — `17` §K per-file minimum specs)

All **SG** for provisional generation per `17` §K, with research-mandatory flags per `18`:

| Group | Files | Provisional gen OK? | Research before client use? | Blk | Stage |
|---|---|---|---|---|---|
| shared/ | requirements-taxonomy, elicitation-techniques, nfr-catalog, evidence-and-uncertainty, glossary | Yes | nfr-catalog: partially (perf/a11y targets) | N | S1 |
| client-discovery/ | interview-strategies, question-bank, process-elicitation, scope-and-mvp, technical-operational-context | Yes | question-bank: quality validated via scenarios, no external research | N | S1 |
| technical-solution/ | architecture-decision-framework, web-project-archetypes, ux-design-framework, security-baseline, test-strategy, deployment-patterns | Yes | security-baseline (RES-05), deployment-patterns (RES-09, provider docs) | N | S3 |
| legal/ | gdpr-basics, cookie-consent, accessibility-law | Draft skeleton only | **Yes — mandatory** (RES-06/07/08); marked `provisional`, blocked from client-facing use until verified | N (S1) / Y (first real client) | S1 draft, verified pre-first-client |

## 5. Schemas (14)

| Schema | Spec | Missing | F | DT | Blk | Stage |
|---|---|---|---|---|---|---|
| project (+profile fields) | FS (`03` §4) | — | Y | Y | Y→S0a | S0a |
| methodology-lock | FS (`02` §7) | — | Y | Y | Y→S0a | S0a |
| interview-state | FS (`04` §6) | — | Y | Y | Y→S0b | S0b |
| requirements (v2: origin, NFR fields, DAT) | FS (`06` §7.1) | — | Y | Y | Y→S0b | S0b |
| solution-context (+risk_triggers) | FS (`06` §7.2) | — | Y | Y | Y→S0b | S0b |
| open-questions | FS (`06` §7.3) | — | Y | Y | Y→S0b | S0b |
| content-inventory (new) | SG (`07` §9 fields) | — | Y | Y | N | S2 |
| product-backlog | SG (`08` §1) | — | Y | Y | N | S2 |
| delivery-backlog | FS (`06` §7.4) | — | Y | Y | N | S3 |
| test-matrix (definitions-only) | FS (`10` §4) | — | Y | Y | N | S3 |
| handoff (+gate, sequence) | SG (`06` §7.5) | — | Y | Y | N | S0b (G1 first consumer) |
| jira-map | FS (`08` §5) | — | Y | Y | N | S5 |
| release-manifest | FS (`11` §7) | — | Y | Y | N | S7 |
| verification-snapshot (new) | FS (`10` §4b) | — | Y | Y | N | S7 |
| traceability | FS (`08` §6) | — | Y | Y | N | S6 |

## 6. Templates (≈17, `06` §6): all **SG** (section lists specified; full prose generated with first consumer). Blockers: none. Stages: client-repo → S0a; discovery set → S1–S2; technical set → S3; delivery set → S6–S7.

## 7. Scripts (8 — `02` §8)

| Script | Spec | Missing | DT | Blk | Stage |
|---|---|---|---|---|---|
| new-client.sh / start-agent.sh / check-methodology-clean.sh | FS (contracts `02` §8, verified flags `19` §0) | — | Y (scratch-repo test) | Y→S0a | S0a |
| validate.sh (profile-aware, R2-21) | SG | grows per schema per stage (by design) | Y | Y→S0b | S0b+ |
| status.sh (profile-aware, handoff-reading) | SG | — | Y | N | S0b |
| export-jira.sh | SG | CSV quirks at S5 | Y | N | S5 |
| upgrade-lock.sh | SG | — | Y | N | S4 |

## 8. Artifacts, fixtures, gates

- **Artifacts (≈30):** every artifact in `06` §1 has producer + consumer + lifecycle after R2-04/05/07/18 fixes; examples exist in-plan for the expensive ones (project.yaml, lock, interview-state, requirement incl. NFR, CLAR/CTR, delivery task, handoff, ADR walkthrough, task context, test definition, verification snapshot, release manifest, statement classification). CR and incident records: **PS** — field lists in `12`, full example generated at S7 (non-blocking).
- **Fixtures/scenarios (10):** 3 interview scenarios + LITE case + trigger-escalation case + PII case (S1); planted-defect evidence fixtures (S2); 2 design scenarios (S3); seeded-defect task (S6). All SG via `02` §10 scenario format + golden checklist structure; BT by definition.
- **Gates (G0–G9 + G3-V):** FS — each has approver, entry criteria, checklist location, record location (`01` §4 + owning files); LITE combinations defined in `21` §5.

## 9. Readiness summary

- **S0a can start immediately:** all its elements (repo skeleton, conventions rule, 5 rules, 2 core schemas, 3 scripts, client template, smoke check) are SG or FS.
- **Only hard blockers by stage:** S1 ← interviewer skills/scenarios (specified); first real client ← legal knowledge verification (`18` RES-06/07/08).
- **Deliberately deferred specs (non-blocking, documented):** parallel ID allocation (`19` R2-10), Jira REST reconciliation (S9), hook-based methodology guard (S9), encrypted evidence platform (post-MVP).
