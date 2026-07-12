# 11 — Git, GitHub, CI/CD, and Deployment

**Purpose:** branch/PR/protection model, the provider-agnostic pipeline, environments and secrets, migrations, release manifests, and rollback.
**Baseline traceability:** B4, B18, §14, §12 steps 13–14; closes G-07, G-19, G-23; DEC-18.

---

## 1. Branch model

```text
main                    approved baselines + released/releasable code only
docs/discovery-01       discovery→specification work (merges at G2)
docs/technical-solution-01   technical design work (merges at G3)
feature/US-nnn-slug     one task branch per implementation task
fix/BUG-nnn-slug · chore/TASK-nnn-slug · docs/CR-nnn-slug
release/vX.Y.Z          only if stabilization needs isolation; small projects tag from main
hotfix/INC-nnn-slug     production incident fixes (12 §4)
```

Documentation PRs are real PRs (diff review of requirement changes — baseline §14.2 retained). Squash-merge everywhere; linear history; branch deleted on merge.

## 2. Protection & required checks (client repo, set at G0)

`main`: PRs only (no direct pushes, including yours — discipline is the point) · required checks: `ci/lint`, `ci/typecheck`, `ci/test`, `ci/validate-artifacts` (docs PRs run only the last) · conversation resolution required · force-push blocked. Tags `v*` protected.

## 3. CI pipeline (GitHub Actions, generic core)

```text
ci.yml (on: PR, push to main)
  lint → typecheck → unit+component tests → integration tests (services via
  docker-compose) → build → artifact upload (build output, hashed)
  [docs paths only → validate-artifacts job instead]
nightly.yml            E2E + performance budget + dependency audit (slow lane)
deploy-staging.yml     on: push to main → build → deploy(staging) → smoke → notify
deploy-prod.yml        on: tag v* + manual approval environment gate
                        → deploy(prod) → smoke → health watch (§7)
```

Stack-specific steps (lint/test commands) are parameterized per project by a small `ci-config` block scaffolded from the archetype at technical design; the workflow *shape* is methodology-templated (`templates/client-repo/.github/workflows/`). **Profile floors (`21` §5):** LITE collapses to one workflow (build → deploy staging → smoke, manual-approved prod deploy); HIGH-RISK adds the nightly lane and migration-rehearsal job as required.

## 4. Environments

| Env | Purpose | Data | URL |
|---|---|---|---|
| local | development | fixtures/synthetic | — |
| staging | integration, client validation (G7) | synthetic or anonymized sample — **never raw production PII** | `staging.<domain>` or provider preview, access-protected |
| production | live | real | client domain |

Config via env vars only; `.env.example` documents names; per-env values live in GitHub environments (staging/prod) and the provider's secret store.

## 5. Deployment adapters (DEC-18 — no single-provider assumption)

Contract every provider adapter implements (`scripts/deploy/<provider>.sh`):

```text
deploy   <env> <artifact-ref>   → deploys, prints deployment-id
rollback <env> <deployment-id|release-id>
health   <env>                  → exit 0/1 + summary
```

Adapter families (build the one the first client needs, at Stage 7): `static` (Netlify/Vercel/Cloudflare Pages — often replaces `deploy` with provider Git integration; adapter then just wraps their CLI for rollback/health) · `node-server` (VPS/docker compose + reverse proxy) · `php-hosting` (rsync/SSH to shared hosting, common for ES small businesses) · `wordpress` (managed WP + migration plugin/CLI). The pipeline calls only the contract; provider quirks stay in the adapter.

## 6. Staging flow (G6)

Merge to `main` auto-deploys staging → smoke suite (key routes 200, critical form roundtrip, auth touch, no console errors) → failures block the release train (fix-forward). G6 checklist: full suites green (nightly lane run manually if needed) · a11y + security sign-offs (`10` §5–6) · staging smoke green · content/data loaded for a meaningful client walkthrough.

## 7. Release to production (G8) + manifest

Procedure (release-manager agent assists; you execute approvals):

```text
1. Scope freeze: list merged tasks since last REL
2. Generate REL-nnn manifest (below), CHANGELOG entry, version tag vX.Y.Z
3. Pre-flight: migrations rehearsed on staging copy; backup taken & restore
   point verified; rollback plan written into manifest
4. G8 approval (you) → tag push → deploy-prod workflow (manual gate)
5. Post-deploy: smoke on prod → 24h heightened watch (error rate, uptime)
6. Close: manifest committed, Jira release marked, client notified
```

```yaml
# docs/releases/manifests/REL-001.yaml
schema_version: 1.0.0
release: {id: REL-001, version: v1.0.0, date: 2026-10-20, tag_commit: 9f1c2d3}
scope: {tasks: [TASK-029, TASK-031], stories: [US-014], requirements_verified: [FR-004]}
artifacts: {build: "gh-run-4412", providers: {production: php-hosting}}
migrations: {applied: [0003_bookings.sql], rehearsed_on_staging: true, reversible: true}
rollback:
  strategy: redeploy-previous     # + db restore point id
  previous_release: null
  restore_point: backup-2026-10-20T06
  max_acceptable_downtime_min: 30
approvals: {g6: 2026-10-18, g7: 2026-10-19, g8: 2026-10-20}
verification: docs/releases/verification/REL-001-verification.yaml   # R2-07 (10 §4b)
smoke: {staging: pass, production: pass}
```

**Execution evidence (V2, R2-07):** the manifest references the release's verification snapshot; test pass/fail state lives there and in CI runs — never in `test-matrix.yaml` (definitions only, `10` §4).

## 8. Migrations & secrets policy

Migrations: forward-only files, versioned in repo; every migration PR states rollback path (down-migration or restore point); destructive changes require staged two-release deprecation (add-new → migrate → remove-old). Secrets: `03` §6 + GitHub environment secrets; rotation noted in `ops/runbook.md`; any secret ever committed = rotate immediately, no exceptions.

## 9. Rollback runbook (summary — full text in `ops/runbook.md` template)

Trigger: failed prod smoke, SEV-1/2 incident post-deploy. Steps: announce → `scripts/deploy/<provider>.sh rollback prod <previous>` → if migrations irreversible, restore DB to manifest restore point (accepting data-loss window — client informed per `12` §4) → smoke → incident report INC-nnn → fix-forward plan. Rehearsed once per project during Stage 7 setup (a rollback never executed before it's needed is a hope, not a plan).
