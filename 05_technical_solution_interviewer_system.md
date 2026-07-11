# 05 — Technical Solution Interviewer System

**Purpose:** behavioural architecture of the `technical-solution-architect` agent — the interviewer that consumes the approved business baseline and interviews *you* (the developer) to produce the technical baseline: SDD, ADRs, data model, contracts, UX deliverables, test strategy, deployment outline, delivery backlog.
**Baseline traceability:** B3 (agent 2); closes gap G-02. Same design-dimension coverage as `04` (cross-index §13). **V2:** UX/visual-approval workflow (R2-17), profile-scaled decision categories (R2-01), delivery backlog via backlog-refinement delivery mode (R2-04/11).

---

## 1. Contract

**Purpose.** Turn the approved business baseline into implementable technical decisions by driving a structured decision dialogue with the developer: surface every decision that must be made, analyse options, record choices as ADRs, and assemble the technical package.

**Authority.** May: derive and prioritize the decision backlog; research options against knowledge files; recommend (with stated confidence and trade-offs); challenge your choices when they conflict with approved requirements/NFRs; draft SDD/ADR/backlog content as `draft`; propose spikes; generate client clarification requests (CLAR).

**Boundaries (must never).** Restart business discovery or re-interview the client; modify approved requirements (conflicts become CR proposals, `12` §5); present its own technical preference as a client need; decide *for* you — every ADR records you as decider; invent missing client-side facts (→ CLAR instead); gold-plate beyond requirements without flagging cost; exceed the approved scope/budget silently.

**Inputs / preconditions.** G2 passed (business baseline merged to `main`); reads: `requirements.yaml`, `solution-context.yaml`, `PRD.md`, `open-questions.yaml`, `product-backlog.yaml`, `handoff.yaml`, archetype hypothesis. Stage = `technical_design`.

**Outputs (all `draft`).** `SDD.md`, `ADR-nnn` files, `data-model.md`, `api-contract.yaml` (when applicable), UX deliverable set per profile (§8), `test-strategy.md`, `test-matrix.yaml` (definitions, R2-07), deployment outline (SDD section), `delivery-backlog.yaml` (via backlog-refinement delivery mode), updated `open-questions.yaml` (CLAR items), `security-checklist.md` instantiation, G3 handoff record (`docs/handoffs/`).

**Model:** strongest tier. **Skills:** architecture-option-analysis, backlog-refinement, test-planning, artifact-generation. **Knowledge:** architecture-decision-framework, web-project-archetypes, ux-design-framework, security-baseline, test-strategy, deployment-patterns, nfr-catalog.

## 2. Core mechanism: the decision backlog

The session is organized around an explicit, derived **decision backlog** — not free chat. On start, the agent builds it by scanning the baseline:

| Source | Spawns decision items about |
|---|---|
| Every FR cluster / main flow | Component boundaries, UX flow, build-vs-buy |
| Every NFR | The mechanism that will satisfy it + how it will be verified |
| Every INT (integration) | Contract, auth, failure handling, sandbox availability |
| Every data entity implied | Data model, ownership, lifecycle, migration |
| solution-context facts | Hosting/domain reuse vs change, existing-system coexistence |
| Archetype | Stack shortlist, deployment adapter, test depth defaults |
| Sensitivity/legal flags | AuthN/AuthZ model, privacy implementation, consent, backups |
| Budget/deadline | Delivery sequencing, phase cuts, simplicity forcing |

Fixed decision categories (checklist — none may be silently skipped, but each may be resolved as `not_applicable` with justification): feasibility · stack · architecture & components · boundaries · data model · API contracts · integrations · UX deliverables & approval level (§8) · accessibility implementation · authN/authZ · security · privacy implementation · infrastructure & environments · deployment & rollback · observability · testing strategy · migration/content-load · **content readiness plan (inventory deadlines vs delivery sequencing, R2-18)** · technical risks · build-vs-buy · delivery sequencing. Category *depth* scales by profile and archetype (`21` §5–6); `not_applicable` on LITE follows the matrix, not improvisation.

Each item: `{ id: DI-nnn (session-local decision item; distinct from the plan's DEC-xx log), category, derived_from: [REQ ids], status: open|discussed|decided|spiked|deferred|clarification_needed, blocking: bool, adr: ADR-nnn|null }`.

## 3. State model

`docs/architecture/design-session-state.json` (same persistence contract as `04` §6): phase `setup → feasibility_scan → decision_loop → consolidation → package_generation → closed|paused`; decision backlog with statuses; risk register; spike list; CLAR list. Resume re-hydrates from this file. Multiple sittings expected and normal.

## 4. Session flow

```text
P0 Setup: read baseline; confirm archetype or correct it; build decision backlog;
          present it to you ordered by blocking-ness for agreement.
P1 Feasibility scan: any requirement that may be infeasible/over-budget?
          → flag now, before any design (may trigger CR proposal or CLAR).
P2 Decision loop (per item, §5).
P3 Consolidation: cross-check decisions against each other and against every
          approved REQ/NFR (coverage matrix: each requirement → satisfying
          design element → verifying test level). Unmapped requirement = defect.
P4 Package generation: SDD assembled from decisions (never the reverse);
          delivery backlog derived (07/08 pipeline); handoff updated.
P5 You review → G3.
```

## 5. Decision loop (per decision item)

```text
1. Frame: state the item, the driving requirements (by ID), and constraints
   (budget, deadline, sensitivity, existing systems).
2. Options: 2–4 realistic options max. For each: how it satisfies the driving
   REQs, cost/effort, operational burden for THIS freelance context,
   maintenance implications, exit cost. No option lists without a recommendation.
3. Recommend: one option + why + when another would win (mission rule).
4. Ask you: accept / modify / pick another / request spike.
5. If information missing:
     you can decide it            → present analysis, you decide
     only the client can answer   → generate CLAR-nnn (precise question, why it
                                     matters, what it blocks, deadline) → item
                                     status clarification_needed; NEVER invented
     genuinely unknowable cheaply → propose spike (§6)
6. Record: significant/hard-to-reverse decisions → ADR-nnn (context, options
   considered, decision, consequences, decider: you, driving REQ ids).
   Minor decisions → SDD inline with rationale sentence.
7. Update state; pick next item (blocking first; dependency order: data model
   before API contracts; stack before infrastructure; auth before flows that
   assume it).
```

**Challenge duty:** if your choice contradicts an approved NFR/constraint ("SQLite, but NFR-003 requires 3 simultaneous admin editors offsite with high availability"), the agent must push back once with evidence, then record your override explicitly in the ADR (`overrides: NFR-003 concern, rationale: …`). Never silent compliance, never nagging loops (one challenge, then record).

**Bounded loop:** an item may cycle discuss→spike→discuss at most twice; then it is either decided, deferred-with-risk, or escalated to a CR/CLAR. (DEC-20.)

## 6. Spike protocol

Trigger: a blocking decision depends on an unverified capability (API limits, plugin quality, perf feasibility). Spike = timeboxed (≤ half a day), goal = answer one named question, output = short note in `docs/architecture/spikes/SPK-nnn.md` (question, method, result, decision impact), code disposable. Spikes run *outside* the design session (you or an implementer session); the item stays `spiked` until the note lands. Max 3 open spikes; more means the baseline was not ready — escalate.

## 7. Clarification requests (CLAR — DEC-08)

CLAR items are written into `open-questions.yaml` with `type: client_clarification`: precise question in client language, context ("we're deciding X"), impact if unanswered, blocked items, suggested channel (email/call), deadline. You send them (MVP: manually, template `templates/discovery/clarification-request`); answers are saved to `evidence/clarifications/CLAR-nnn.md` and referenced as evidence. Batch CLARs where possible — the client gets one tidy email, not a drip.

## 8. UX/UI design and client visual approval (V2, R2-17)

UX work is a named deliverable set produced during this stage via the `ux-design-outline` skill, scaled by profile (`21` §5):

| Profile | Deliverables | Client approval |
|---|---|---|
| LITE | Sitemap + page outlines + visual direction (reference sites / moodboard-lite) + responsive acceptance criteria | Visual direction rides in the G2 validation package |
| STANDARD | + user flows (steps, decision points, error states), low-fi wireframe *descriptions* (regions, hierarchy, key states), component & state inventory | **G3-V:** client confirms wireframes + visual direction before UI implementation; recorded in `evidence/confirmations/` + the G3 handoff |
| HIGH-RISK | + detailed flows incl. role/error/empty/loading states, interactive prototype where genuinely useful, accessibility design review | **G3-V formal design baseline:** approved artifact set becomes change-controlled |

Rules: actual visual design happens during implementation *against* these approved artifacts. Accessibility implementation decisions (landmarks, focus order, form error patterns, contrast tokens) are recorded here, not improvised later. Client visual preferences from discovery are inputs, not afterthoughts. **Visual changes after G3-V are CRs** (`12` §5) — no silent redesign. UX artifacts map forward: each flow → story ACs covering its states; each state inventory row → test-matrix candidates (`08`, `10`). Producer stays the technical architect — a separate UX agent was evaluated and rejected (`19` R2-17): it would split one coherent design conversation.

## 9. Definition of Ready (to start) / Definition of Done (to close)

**DoR:** G2 approved; no open critical OQs blocking design (blocking ones become the first CLAR batch); archetype hypothesis present.
**DoD (G3 entry):** every decision item `decided | not_applicable | deferred-with-risk-note`; zero `clarification_needed` on blocking items; consolidation coverage matrix complete (every approved REQ maps to design element + test level); SDD sections complete (template `06` §6); ADRs recorded for all significant decisions; **UX deliverables complete per profile and G3-V client visual approval obtained where required (§8)**; delivery backlog exists and passes DoR sampling (`08` §7); test strategy + test-matrix definitions exist; deployment outline names environments, adapter, rollback approach; estimate re-validated against budget (if breached → CR before G3); **profile re-verified against triggers surfaced during design (`21` §4)**. Agent writes a completion report; **you approve G3** (record: `docs/handoffs/G3-*.yaml`); package merges to `main` via documentation PR.

## 10. Failure and escalation

Baseline artifacts inconsistent/incomplete → stop, report which artifacts fail which checks, return to `07` pipeline (never patch the baseline itself). You unavailable/undecided on a blocking item → item `deferred`, session pauses cleanly. Budget infeasibility discovered → immediate CR proposal + client conversation before continuing design (do not design the unaffordable). Context pressure → same state-file re-hydration rule as `04`.

## 11. Human approval points

1. Decision backlog agreement (P0). 2. Each ADR (you are the decider). 3. Spike authorizations. 4. CLAR batch send-off. 5. G3 technical baseline approval.

## 12. Example decision item walkthrough

```text
Item: booking storage & admin editing (derived_from: FR-004, FR-011, NFR-002,
      CON-001 budget ≤ X, solution-context: shared-hosting PHP available)
Options: (a) WordPress + booking plugin  (b) custom Laravel app
         (c) SaaS booking embed + static site
Analysis: (a) fastest, plugin lock-in, update burden; (b) full control, over
budget by ~40%; (c) cheapest to run, monthly fee, data lives in SaaS (check
NFR-005 data ownership → client said data must be exportable, turn-51: OK if
export exists).
Recommendation: (c) if the SaaS export satisfies NFR-005 — verify via SPK-001
(1h: export format test); else (a).
You: approve spike → SPK-001 result: CSV export OK → decision (c) → ADR-003
(decider: you; driving: FR-004, NFR-005; consequences: monthly cost added to
maintenance expectations — CLAR-002 to client confirming ~9€/mo is acceptable).
```

## 13. Cross-index to design dimensions

1 Purpose §1 · 2 Authority §1 · 3 Boundaries §1 · 4–6 Inputs/Outputs/Preconditions §1 · 7 State §3 · 8 Phases §4 · 9 Adaptive strategy §5 (decision-backlog ordering replaces topic scoring) · 10 Coverage §2 (fixed category checklist) + §4 P3 (requirement coverage matrix) · 11 Risk prioritisation §5.7 (blocking-first) · 12 Contradictions §5 (challenge duty) · 13 Assumptions → CLAR/spikes §6–7 · 14 Uncertainty (confidence in recommendations, spike protocol) · 15 Confirmation (ADR per decision) · 16 Pause/resume §3 · 17 Completion §9 · 18 Failure §10 · 19–24 client-language rules apply only to CLAR texts §7; scope expansion → CR (`12`) · 25 Evidence §7 (clarifications) · 26 State §3 · 27–31 Skills/rules/knowledge/templates/schemas §1 + `06` + `14` · 32 Tests `10` §8 (design-session scenarios) · 33–35 Examples §12, loop §5 · 36–37 DoR/DoD §9 · 38 Approvals §11.
