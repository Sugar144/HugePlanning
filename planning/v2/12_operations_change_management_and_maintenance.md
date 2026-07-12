# 12 — Operations, Change Management, and Maintenance

**Purpose:** post-release operating model: monitoring, incidents, production bugs, client change requests, dependency updates, retention/archival.
**Baseline traceability:** B22, B23, §17, §18; closes G-08, G-20; DEC-10.

---

## 1. Operating stance

`operation` is a stage, not an afterthought: the project stays governed by the same repo, gates, and traceability. Maintenance expectations were captured in discovery (M10), priced, and recorded in `engagement.md` as a **named billable tier** (R2-19) — e.g., `none` (handover only), `best-effort`, `committed` (response-time commitment, HIGH-RISK default). Incidents are handled against the purchased tier, not against anxiety; work beyond the tier is a CR. Operational floors (monitoring, maintenance window, retention) scale by profile (`21` §5).

## 2. Monitoring (MVP-minimal, per `ops/monitoring.md`)

| Signal | Tool class | Alert |
|---|---|---|
| Uptime | external ping monitor (free tier) | immediately, email/push |
| Errors | error tracker (Sentry-class) or provider logs | daily digest; spike → immediate |
| Domain/cert expiry | monitor or calendar automation | 30/7 days before |
| Backups | provider job + monthly restore spot-check | on failure |
| Form/booking flow | weekly synthetic check (smoke subset, can be manual at MVP) | on failure |

Setup is a Stage 7 task per project; tool choices recorded in `monitoring.md` with dashboards/credentials pointers (credentials in password manager, not repo).

## 3. Incident handling

Severities: **SEV-1** site down / data loss / security breach → act now, client informed proactively · **SEV-2** core flow broken (booking fails) → same business day · **SEV-3** degradation/cosmetic → becomes a BUG task in normal flow.

```text
Detect → classify SEV → stabilize (rollback 11 §9 / hotfix branch hotfix/INC-nnn)
→ verify (smoke) → communicate → INC-nnn report (timeline, cause, impact,
actions) → follow-up tasks (regression test mandatory, 10 §9) → close
```

Hotfixes still get a PR + your review (expedited: adversarial review may follow the merge for SEV-1, recorded as debt in the INC report — the *only* sanctioned review deferral in the system).

## 4. Production bugs vs change requests (classification, baseline §17 flow retained)

Every inbound item is classified first: **BUG** — behaviour violates an approved requirement/AC (fix within maintenance terms; repro test first) · **CR** — new/changed desired behaviour, including "small tweaks" (change control below) · **question/support** — answered, logged in engagement notes if recurrent.

## 5. Change control (CR workflow, G9)

```text
CR-nnn created (template): request text, source (client msg → evidence/),
requested_by, date
→ impact analysis: reverse traceability walk (08 §6) — affected REQ/US/tasks/
  tests/docs; effort class XS–XL; price/timeline effect
→ decision G9: you approve; client approves if scope/€/deadline change
  (recorded in evidence/confirmations/)
→ apply: requirement edits via docs PR (status changes, supersede old ids —
  never rewrite history); backlog + Jira updated; implement via normal task loop
→ release via normal G6–G8
```

Rules: no implementation before G9 (kills scope creep) · XS-class CRs may batch under one G9 email approval · agents may *propose* CRs (from `09` §8) but never enact them · a superseded requirement keeps its ID with `superseded_by:` · **client content delays are CRs too (R2-18): when a content-inventory deadline passes, the schedule/scope impact is put to the client as a G9 decision (wait / placeholder-launch / descope), per the engagement's content clause — never silent waiting** · a CR that introduces a risk trigger (e.g., "add online payment") forces a profile upgrade proposal before estimation (`21` §4).

## 6. Dependency & platform updates

Monthly maintenance window per active client: dependency audit (CI nightly output), patch/minor updates batched as `chore` task, full suite + staging smoke before prod. Security advisories on exposed components: treated as SEV-2. Major framework upgrades: CR to yourself with impact analysis (they're mini-projects).

## 7. Documentation upkeep

Docs update is part of task DoD (drift resistance is structural, not scheduled). Additionally at each release close: regenerate status report, check `generated_from` drift warnings (`06` §5), update runbook if ops changed. Quarterly per active client: 30-minute doc-truth spot-check (pick 3 requirements, verify site behaviour matches `verified` status).

## 8. Retention, archival, deletion (DEC-10, closes G-20)

Project close: final release manifest → client handover pack (credentials transfer, docs export if contracted) → `project.status: archived` → retention clock (`project.yaml`). At expiry: deletion runbook — remove repo (GitHub + local clones + backups inventory), **`evidence-raw/` and its encrypted backups (R2-03 — the raw store makes true deletion of sensitive material possible without rewriting Git history)**, provider data per contract, password-manager entries; record a deletion certificate note (kept, minimal, no client data). Early deletion on client request honored per GDPR: raw evidence deleted outright; for committed sanitized evidence the minimization design means erasure requests are normally satisfiable without history rewriting — residual identifiers found in Git are a sanitization defect handled per its severity (worst case: repo re-creation from filtered history, documented in the runbook).

## 9. Systemic feedback into the methodology

Monthly review (15 min): incidents, review findings, friction notes → candidate methodology changes → normal methodology release process (`02` §7, §10). This is the engine of progressive improvement — automation candidates come from *observed* repetition (`13` §5), honouring the baseline's automation-as-response-to-friction principle.
