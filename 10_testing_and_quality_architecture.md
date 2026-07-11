# 10 — Testing and Quality Architecture

**Purpose:** the layered test strategy across product code and methodology, the test matrix (definitions), execution evidence (verification snapshots), timing, and how adversarial review complements automation.
**Baseline traceability:** B6, B20, B21, §16; closes G-06, G-24. **V2:** definitions/executions split (R2-07), profile testing floors (R2-01, `21` §5).

---

## 1. Layer map and timing

| Layer | Verifies | Planned | Written | Executed |
|---|---|---|---|---|
| Requirement verification (AC → TEST rows) | The right thing is being built | Specification stage (ACs at `07`) | Matrix rows at technical design (`05`) | Continuously via the layers below |
| Unit | Functions/rules in isolation (BR logic especially) | Task DoR (`tests_required`) | With each task (implementer) | Every commit (CI) |
| Component | UI components / modules with mocked edges | Task DoR | With each task | Every commit |
| Integration | Modules + real db/services (test env) | Technical design | With each task or dedicated task | Every PR (CI) |
| Contract | `api-contract.yaml` ↔ implementation; external API shapes | Technical design (per INT) | Dedicated tasks | Every PR + before release |
| E2E | Critical user flows end-to-end (browser) | Technical design: flows list = must-FR flows | Walking-skeleton task, then per flow | Nightly/pre-release (slow lane) |
| Accessibility | WCAG target (NFR) | NFR floor (`07` §3) | Per UI task: automated (axe-class) + matrix keyboard/screen-reader checks | Automated every PR; manual checklist at G6 |
| Security | security-checklist + auth/input/session tests | Technical design | Per trigger table (`09` §5) + dependency audit in CI | Every PR (scans) + G6 review |
| Performance | NFR budgets (page weight, LCP-class metrics) | NFR floor | Budget config once (walking skeleton) | Pre-release + staging check |
| Regression | Past bugs stay dead | On every bug fix (mandatory test-first repro) | With the fix (BUG task DoD) | Every PR |
| Smoke | Deploy sanity: key pages 200, forms submit, auth works | Deployment outline (`05`) | Stage 7 pipeline task | After every deploy (staging & prod) |
| Production health | Uptime, error rate, cert/domain expiry | Deployment outline | Monitoring setup task | Continuous (`12` §3) |

## 2. Policy

- **Depth follows risk and profile**, not uniformity: `risk: high` requirements get all applicable layers; `low` may stop at unit+E2E-flow coverage; the **profile floor** (`21` §5) sets the minimum lane per project (LITE: build + link check + smoke + a11y scan + scripted walkthrough; HIGH-RISK adds contract/performance/migration-rehearsal lanes). The trigger table (`09` §5) binds review depth to the same risk signal.
- Every AC must be demonstrable: automated test **or** a scripted manual check defined in the matrix (`automation: manual` + `manual_procedure`), with its execution evidence landing in the release verification snapshot (§4b). Not everything is automated at MVP; everything is *demonstrable* (baseline §16.1 retained).
- Test-first for: business rules, bug fixes, payment/auth logic. Test-with for: UI composition, content.
- Coverage metric: no numeric target; the matrix (every AC mapped) is the coverage instrument. Line-coverage is advisory only.

## 3. Adversarial review vs automated tests (explicit relationship)

Automated tests verify *anticipated* behaviour; adversarial review hunts *unanticipated* failure modes and weak tests (tautological asserts, mocked-away reality). Adversarial findings that matter must land as new automated tests (regression ratchet) — a finding fixed without a test is not resolved unless explicitly waived by you. Review never substitutes for a missing declared test layer; a task with `tests_required: integration` and no integration test fails spec review regardless of review quality.

## 4. `test-matrix.yaml` — **stable definitions only (V2, R2-07)**

```yaml
schema_version: 2.0.0
tests:
  - id: TEST-011
    verifies: [FR-004-AC-01]
    level: integration
    automation: automated        # automated | manual
    location: tests/integration/booking-request.spec.ts
    required_for_profile: [lite, standard, high-risk]   # 21 §5 floor tag
    risk: high
    environment: "docker-compose test services"
  - id: TEST-034
    verifies: [NFR-002]
    level: accessibility
    automation: manual
    manual_procedure: "keyboard-only booking flow; NVDA pass on form errors"
    required_for_profile: [standard, high-risk]
    risk: medium
    environment: staging
```

No `status`, no `last_run` — pass/fail state lives in CI runs and verification snapshots (§4b). The only lifecycle exception: `quarantined: true` may be set on a definition per the flake policy (§7), because quarantine changes what CI *requires*, not what happened. `validate.sh`: every AC of an `approved` requirement appears in ≥1 definition row (per the profile floor).

## 4b. Execution evidence — verification snapshots (V2, R2-07)

Produced at release readiness (G6) by `deployment-readiness-review`; referenced by the release manifest; immutable per release:

```yaml
# docs/releases/verification/REL-001-verification.yaml
schema_version: 1.0.0
release: REL-001
commit: 9f1c2d3
results:
  - test: TEST-011
    result: pass                 # pass | fail | waived {by, reason}
    workflow_run: gh-run-4412
    environment: staging
    timestamp: 2026-10-18T09:12:00Z
  - test: TEST-034
    result: pass
    evidence: "manual walkthrough note + screenshot, evidence/confirmations/2026-10-18-a11y.md"
    executed_by: developer
    timestamp: 2026-10-18T10:00:00Z
```

**Requirement `verified` derivation (`06` §2):** a requirement becomes `verified` when the latest snapshot shows `pass` for all its definition rows required by the profile. Day-to-day pass/fail lives only in CI (linked by run id) — Git carries one auditable record per release, not per run (low noise, full audit).

## 5. Security & accessibility baselines (closes G-24)

`security-checklist.md` instantiated per project from methodology knowledge: HTTPS/HSTS · input validation & output encoding · authN/session config · authz per role matrix · secrets handling · dependency audit · headers (CSP, frame, referrer) · backups & restore test · rate limiting on public forms · GDPR: consent, privacy page, data export/delete path. Checked at G6, re-checked at G8. Accessibility: WCAG 2.2 AA default target; automated scans per PR + manual matrix rows per flow; a11y sign-off is part of G6.

## 6. Integration, staging, and client acceptance (validation stage)

After the last task of a release scope: full regression + E2E + a11y + security pass on integrated build → deploy to staging (`11` §6) → **staging smoke** → your walkthrough → **G7 client acceptance**: guided walkthrough against the AC list of the release scope (script generated from the matrix: "try booking a table for tonight — it should refuse (BR-002)"). Client confirmation recorded in `evidence/confirmations/`. Client-found issues → BUG or CR, never hot-edited.

## 7. Flaky/quarantine policy

A test failing intermittently: quarantined (`quarantined: true` on its definition, excluded from required checks) + BUG task opened; quarantine >2 weeks → escalate (delete-or-fix decision). Required CI checks never include known-flaky tests (protects merge signal integrity).

## 8. Methodology testing (product = the method; baseline §21 retained)

Covered in `02` §10 (schema/script tests, interview scenarios, golden artifacts, regression cases); the stage-level assurance process that builds and releases the methodology itself is `22` (this file governs client-product testing only). Additional golden checks tied to this file: scenario runs must produce matrix-mappable ACs (testability golden), and the "no invention" check (`07` §7). Design-session scenarios for `05`: a baseline with a hidden infeasibility (agent must catch at P1), a missing-client-fact case (must produce CLAR, not an invented answer).

## 9. Systemic learning loop (baseline §16.5 retained verbatim)

Repeated error → fix code → add regression test → inspect whether a skill/rule/template allowed it → patch methodology → release methodology version. `tests/regression-cases/` entry mandatory for any error that recurs twice.
