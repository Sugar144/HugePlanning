# 21 — Process Profiles and Project Archetypes

**Purpose:** the two-dimensional classification model (R2-01) that scales process weight to project complexity, and the single requirement matrix every other subsystem reads.
**Principle:** archetype = *what is being built* (capabilities, domain concerns → activates interview modules, knowledge packs, decision categories). Profile = *how much assurance is required* (→ activates gates, artifacts, reviews, test layers, operations). Profile derives from **risk triggers**, never from archetype alone.

---

## 1. Dimension A — Archetypes (9)

| Archetype | Definition | Typical concerns activated | Common profile range |
|---|---|---|---|
| `static-landing` | Single page / few pages, no CMS, no accounts | content, SEO basics, form (maybe) | LITE |
| `corporate-content-site` | Multi-page brochure site, dev-maintained content | content inventory, IA/navigation, SEO | LITE–STANDARD |
| `cms-content-site` | Client edits content via CMS | CMS choice, editor training, roles-lite, backups | STANDARD |
| `forms-or-lead-generation` | Business forms, lead capture, quotes | validation, spam, personal data, notifications | STANDARD |
| `booking-system` | Availability, reservations, scheduling | business rules, concurrency, notifications, calendars | STANDARD–HIGH-RISK |
| `e-commerce` | Catalog, cart, payments, orders | payments, tax/invoicing, inventory, consumer law | HIGH-RISK |
| `authenticated-web-app` | User accounts, per-user data, workflows | authN/Z, data model, sessions, privacy | HIGH-RISK |
| `integration-heavy-web-app` | Behaviour dominated by external systems | contracts, failure modes, sandboxes, data sync | STANDARD–HIGH-RISK |
| `migration-or-replatforming` | Existing system/data must survive the move | data migration, parity, cutover, rollback of data | STANDARD–HIGH-RISK |

A project may combine archetypes (corporate site + booking module): each archetype's concerns activate; the profile is computed once from all triggers. Archetype hypothesis set at G0/discovery, confirmed at G3 (unchanged from V1).

## 2. Dimension B — Profiles: entry criteria

| | LITE | STANDARD | HIGH-RISK |
|---|---|---|---|
| Entry criteria (all must hold) | No auth (beyond a single protected admin page with no personal data), no payments, no sensitive/special-category data, ≤1 trivial integration (e.g., embedded map/form service), low operational impact (site down ≠ business stopped), no legal exposure beyond baseline web law | Normal personal-data handling (contact/booking data), common small-business systems, moderate integrations, moderate operational impact — and **no HIGH-RISK trigger** | Any HIGH-RISK trigger fires (§3) |

## 3. Risk triggers (any one ⇒ HIGH-RISK; italic ones ⇒ at least STANDARD)

Payments or money movement · authentication with per-user data · special-category or regulated personal data (health, minors, finance…) · regulated sector or specific compliance regime · migration with data-loss potential · high availability genuinely required (downtime = immediate material loss) · ≥2 non-trivial integrations or one business-critical integration · high-value business process (errors cost real money/legal exposure) · client contractually requires formal assurance. *Any personal-data collection beyond an email link · client-editable content (CMS) · any business workflow the client depends on daily.*

Triggers are recorded as `risk_triggers[]` in `solution-context.yaml` (`06` §7.2) with evidence refs — the machine-readable input to profile confirmation.

## 4. Profile lifecycle

```text
G0: profile hypothesized (engagement facts) → project.yaml.profile + rationale
Discovery: agent records risk_triggers as evidence arrives; if a trigger
           exceeds the hypothesis, it flags PROPOSED UPGRADE immediately
G1: profile CONFIRMED by you against the trigger list (checklist item)
G3: profile re-verified (design may reveal triggers, e.g. an integration
    turns out business-critical)
Any time: new trigger ⇒ automatic upgrade proposal; work paused on affected
          areas until you confirm (accept upgrade or refute the trigger
          with evidence). Upgrades are logged in project.yaml.profile_history.
Downgrade: ONLY you, with written reasoning in profile_history and a check
           that no recorded trigger contradicts it. Agents can never downgrade.
Anti-gaming: agents propose with trigger evidence, never select; when
           classification is ambiguous, default to the stricter profile.
```

## 5. Requirement matrix (the single lookup for all subsystems)

| Dimension | LITE | STANDARD | HIGH-RISK |
|---|---|---|---|
| Discovery modules (`04` §5) | M0, M1–M3 (compressed), M5, M7 (content focus), M8 (floor confirm only), M9, M10, M12; M4/M6/M11 folded into M5/M12 | All modules; depth per coverage model | All modules, full depth + trigger-specific deep dives (payments, data, compliance) |
| Interview depth | Single sitting target (60–90 min); critical topics only | Standard coverage model | Full coverage + follow-up sittings expected |
| Canonical artifacts required | project.yaml, lock, sanitized transcript+state, requirements.yaml (compact), solution-context.yaml, **open-questions.yaml (always present; may be empty)**, content-inventory, **SDD.md in design-note variant**, delivery-backlog (task list), handoffs | + full open-questions depth, product-backlog.yaml, full SDD, test-matrix, traceability, ADRs (key decisions), release manifests | + api-contract/data-model as applicable, security-checklist, verification snapshots, full ADR discipline, incident/CR records |
| Human documents | 1-page brief (mini-PRD, generated via artifact-generation skill) + validation email | PRD, validation package, SDD | + formal design baseline, acceptance script, release notes per release |
| Gates | **G0 · compact validation workflow** = G1 (internal check, your record) **then** G2 (client email approval, client record) — one workflow, **two decisions, two append-only records** **· G3-lite** (short internal technical session → design note; no client-facing meeting) **· task DoR per task (no G4 batch ceremony) · G5 per PR · compact release workflow** = G6 (readiness, you) + G7 (client acceptance) + G8 (production authorization, you) — one workflow, **three decisions, three records · G9** | All gates G0–G9 separate; G3 includes the G3-V visual checkpoint (`01` §4.2b) | All gates, none combinable; G3-V formal design baseline; G8 requires rehearsed rollback + monitoring armed before go |
| Agents | client-discovery (lite modules) + artifact-generation skill for the brief; technical-solution-architect (**one short internal session** → design note); implementer; **one merged reviewer pass** (spec+adversarial contracts in one session); **no separate auditor session — G1 uses `validate.sh` + a compact audit checklist run by you**; you | All 9 agents as designed | All 9; risk-specialist-reviewer mandatory on trigger areas |
| Reviewers per task | 1 merged review | spec + adversarial; specialist per trigger table | spec + adversarial + specialist on all trigger-area tasks; human review mandatory on payment/auth/migration diffs |
| Requirements floor | Page/feature-level FRs with plain ACs; NFR floor confirmed as defaults; no UC/BDD | Full model (`06` §7.1): typed, sourced, prioritized ACs; UC/BDD for complex flows | + measurable NFRs mandatory (no waived-by-silence), data requirements (DAT), compliance requirements explicit |
| Backlog floor | Single-phase task list in delivery-backlog.yaml | Product backlog (epics/stories, phases) → delivery backlog | + release_target per story, dependency graph validated, migration/cutover plan tasks |
| UX deliverables (R2-17) | Sitemap + page outlines + visual direction (reference sites/moodboard-lite) + responsive acceptance criteria | + user flows, low-fi wireframes, component & state inventory, client visual approval (G3-V) | + detailed flows incl. role/error/empty states, interactive prototype where useful, accessibility design review, formal approved design baseline |
| Accessibility floor | Automated scan + keyboard walkthrough of all pages (WCAG 2.2 AA basics) | + manual checks per flow (matrix rows), form error patterns | + assistive-tech pass on critical flows, a11y sign-off at G6, design-stage a11y review |
| Security floor | HTTPS/HSTS, headers, form spam/rate protection, dependency audit, no secrets in Git | + security-checklist instantiated, authZ review where any auth exists, backup/restore check | + full checklist at G6 and G8, payment/auth specialist review, threat-model pass in SDD, restore rehearsal |
| Testing floor (`10`) | Build + link check + smoke + a11y scan + scripted manual walkthrough; no unit suite mandated | Layered per test matrix; unit/integration/E2E on core flows; regression on bugs | + contract tests per integration, performance budget, migration rehearsal tests, full regression before every release |
| CI/CD floor | One workflow: build → deploy staging → smoke; prod deploy manual-approved | Full `11` §3 pipeline | + required checks strictly enforced, nightly lane, migration rehearsal job |
| Deployment/rollback | Static-class adapter; rollback = redeploy previous (verified once) | Adapter per archetype; rollback rehearsed at S7-equivalent setup | + documented rollback runbook incl. data restore, rehearsed before first prod deploy and re-verified per release with migrations |
| Monitoring | Uptime + cert/domain expiry | + error tracking, weekly synthetic check of key flow | + alert routing with severities, backup monitoring, availability target watch |
| Jira (R2-06) | **None** — delivery-backlog.yaml is the board | Default yes; waivable for tiny backlogs (recorded) | Yes |
| Maintenance | Named tier in engagement (e.g., best-effort); monthly dependency batch optional | Tier + monthly maintenance window | Tier with response-time commitment; monthly window mandatory; security advisories = SEV-2 |
| Evidence retention | Standard (`03` §6); raw evidence minimal | Standard | + retention per compliance regime; deletion runbook verified |
| Escalation | Any trigger appearance ⇒ upgrade proposal; client dispute ⇒ move to STANDARD evidence discipline | Trigger ⇒ HIGH-RISK proposal | Incident SEV-1 ⇒ post-incident review mandatory |

Scripts read this matrix: `validate.sh --profile` treats missing required artifacts as errors and missing optional ones as info (R2-21).

## 6. Interaction rules (no duplication between dimensions)

1. Archetype activates **topics** (interview deep-dives, decision categories, knowledge packs `17` §H, adapter family, matrix row seeds).
2. Profile activates **rigor** (matrix above).
3. Where both touch the same area, archetype decides *whether* a concern exists; profile decides *how much assurance* it gets. Example: `booking-system` activates business-rule elicitation and concurrency decisions regardless of profile; whether those get contract tests + specialist review is the profile's call.
4. Conflicts resolve to the stricter requirement.

## 7. LITE fast-path dry-run (commercial viability proof, R2-19; validated step-by-step in the V2 correction pass)

Landing page for a restaurant (static-landing, LITE, no triggers). Total process overhead beyond writing the site: ≈ 6–10 h.

| Step | Required files (in → out) | Session / actor | Gate / checkpoint | Approver | Output record | Next-stage precondition |
|---|---|---|---|---|---|---|
| 1. Onboarding | template → project.yaml (profile: lite + rationale), lock, engagement.md, settings deny rules, empty open-questions.yaml | `new-client.sh` + you (~30 min) | G0 (minimal `validate.sh` green: project.yaml, lock, repo structure) | You | `docs/handoffs/G0-readiness-01.yaml` | stage → discovery |
| 2. LITE discovery | client materials → sanitized transcript + state, requirements.yaml (compact), solution-context (+risk_triggers), open-questions (may stay empty), content-inventory seed, consent record | `client-discovery`, lite modules, one sitting ≈ 75 min + ~45 min normalization | Interview DoD (`04` §12, lite floor) | You accept closure | completion-report.md | interview DoD met |
| 3. Compact validation workflow — G1 | draft artifacts → checked artifacts | You (~20 min): `validate.sh` + compact audit checklist (no auditor session on LITE) + profile confirmation vs triggers | **G1** (own decision) | You | `docs/handoffs/G1-discovery-review-01.yaml` | G1 approved |
| 4. Compact validation workflow — G2 | layer 2 → 1-page brief (artifact-generation skill): scope, exclusions, price vs budget, content list + deadlines | Email to client; reply = approval | **G2** (own decision) | Client | `evidence/confirmations/` + `docs/handoffs/G2-business-baseline-01.yaml` | docs branch merged; `approved_in` set |
| 5. G3-lite | baseline → `SDD.md` (design-note variant: stack/hosting, sitemap/page structure, visual direction, applicable NFR/test/deploy floors) + delivery-backlog task list (4–8 tasks) | `technical-solution-architect`, **one short internal session ≈ 45–60 min** (no client-facing meeting; visual direction was already confirmed at G2) | **G3-lite** | You | `docs/handoffs/G3-technical-baseline-01.yaml` | task list DoR-ready |
| 6. Implementation (per task) | task-context (brief) → code + PR | `implementer`, then **one merged reviewer pass** (spec+adversarial contracts, one session) | task DoR before start; **G5** per PR | You (~10 min/PR) | merged PR; task status in delivery-backlog (no Jira) | all tasks merged; content per inventory |
| 7. Compact release workflow — G6 | integrated build → staging deploy + smoke + a11y scan + scripted walkthrough | LITE CI workflow + you | **G6 readiness** (own decision) | You | `docs/handoffs/G6-staging-readiness-01.yaml` | G6 pass |
| 8. Compact release workflow — G7 | staging URL → client walkthrough (~30 min) | You + client | **G7 acceptance** (own decision) | Client | `evidence/confirmations/` + `docs/handoffs/G7-client-acceptance-01.yaml` | G7 approved |
| 9. Compact release workflow — G8 | manifest (lite) → prod deploy + smoke + uptime/cert monitor | You + deploy adapter | **G8 production authorization** (own decision) | You | `docs/handoffs/G8-production-release-01.yaml` + REL manifest | stage → operation |

"Compact workflow" means the gates run back-to-back in one working session or email exchange — **each gate keeps its own decision, approver, and append-only record**; none is skipped or blended.

**HIGH-RISK contrast check (no weakening):** on HIGH-RISK, every row above expands rather than disappears — independent requirements-auditor session at G1; full validation package + estimation at G2; full technical package, G3-V formal design baseline, ADR discipline at G3; spec + adversarial + mandatory specialist reviewers per task; full test lanes, verification snapshot, rehearsed rollback, armed monitoring across G6–G8, all gates separate. The LITE reductions come only from this matrix; nothing in the LITE path relaxes any HIGH-RISK requirement.

The same system, same repos, same evidence discipline — a strict subset, not a different method. Upgrade path intact: if the restaurant later wants online ordering (payments trigger), the project upgrades to HIGH-RISK for that scope via G9 + profile_history entry.
