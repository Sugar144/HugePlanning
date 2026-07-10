# 15 — Risks, Open Decisions, and Validation Plan

**Purpose:** consolidated risk register (baseline §24 retained + additions), genuinely open decisions with owners and deadlines, and how the plan itself gets validated.
**Baseline traceability:** B29 retained; audit findings from `16`.

---

## 1. Risk register

Baseline §24's sixteen risks are **retained in full** with their mitigations, now anchored to concrete mechanisms: manual-first (`13`), evidence+states+approvals (`04`/`07`), canonical artifacts + generation direction (`06` §5), version+lock (`02` §7), repo-per-client (`03`), read-only enforcement (`02` §6), Git-canonical Jira export (`08`), on-demand skills/knowledge (`14` §5), separated agents (`14` §2), gate records (`01` §4), independent reviewers (`09` §2), baselines+change control (`12` §5), change workflow (`12` §4–5), model tiers (`01` §8), file-based state (`01` §7), PII minimization+secrets (`03` §6).

**Additional risks identified by this plan:**

| ID | Risk | Impact | Mitigation | Residual |
|---|---|---|---|---|
| RSK-A1 | SPK-01 fails: `--add-dir` doesn't discover agents/skills | Operating model rework at S0 | Fallback A (stubs) fully designed, Fallback B (plugin) | Low — fallbacks preserve architecture |
| RSK-A2 | Interview quality plateaus below "senior architect" bar | Core value proposition weakens | Scenario+golden testing S1; question-bank iteration; the behavioural spec (`04`) is testable, not vibes | Medium — accept iteration |
| RSK-A3 | Solo-operator bottleneck: every gate is you | Throughput ceiling; gate fatigue → rubber-stamping | Checklists split mechanical (scriptable) vs judgment; automation map `13` §5 | Medium — inherent to model |
| RSK-A4 | Claude Code product changes break launch/discovery mechanics | Sessions fail after CLI update | Lock records CLI version; re-run SPK-01 on upgrade; runtime-neutral content (`01` §10) | Low |
| RSK-A5 | Long interview exceeds one session's context | Lost adherence mid-interview | Persistence contract + module checkpoints + state re-hydration (`04` §6) | Low |
| RSK-A6 | Client never approves G2 (drift, silence) | Stalled engagement | `paused` status + engagement terms; validation package designed for easy yes | Business risk, not system |
| RSK-A7 | Fictitious-pilot blind spots vs real clients | Method gaps surface with paying client | First real client scoped small/low-risk; discovery-only start allowed after S4 | Medium — accepted |
| RSK-A8 | Estimation error on fixed budgets | Margin loss | DEC-16 checkpoint; T-shirt ranges not promises; CR discipline for scope moves | Medium — improves with history |
| RSK-A9 | Reviewer agents rubber-stamp | False quality signal | Seeded-defect tests (S6); separate sessions; your G5 reviews the reviews | Medium |
| RSK-A10 | GitHub Actions minutes/cost on private repos | CI throttling | Verify quota S7; nightly lane trims PR load; self-hosted runner as fallback | Low |

## 2. Open decisions (genuinely unresolved — with owner and resolve-by)

| ID | Decision | Why open | Owner | Resolve by | Default if unresolved |
|---|---|---|---|---|---|
| OD-1 | First deployment provider adapter | Depends on first pilot/client archetype | You | S7 start | `static` adapter (cheapest to build/test) |
| OD-2 | Jira vs lighter tracker (GitHub Projects) for solo MVP | Baseline mandates Jira; solo overhead is real; mission requires Jira publication | You | S5 start | Keep Jira (baseline); map/export design is tracker-agnostic either way |
| OD-3 | Pilot subject for S4/S8: serious fictitious client vs own project | Availability/opportunity | You | S4 start | Fictitious (fully controllable, reusable as example) |
| OD-4 | Test stack per archetype (runner, E2E tool) | Stack chosen per project at technical design | You | Per project G3 | Vitest/Playwright-class defaults noted in test-strategy knowledge |
| OD-5 | Client-facing status reporting (none / periodic email / generated page) | Depends on client expectations; not MVP-blocking | You | First real client G0 | Manual email at milestones |

**None of these block S0–S3.** Everything else that looked "open" in the baseline (§28's fourteen design decisions) is now resolved in files `04`–`11`.

## 3. Validation plan for this plan

1. **Structural self-check (done as Pass 5):** cross-file consistency review — gates, stages, statuses, IDs, paths, agent/skill names identical everywhere; every artifact has producer+consumer (`06` §1, `14` §6); every stage has entry/exit gates; every loop bounded (DEC-20).
2. **SPK-01 (S0):** validates the load-bearing platform assumption before any content is written at volume.
3. **Scenario validation (S1–S3):** the interviewers are validated against fictitious-client scenarios with golden artifacts *before* touching anything real — the plan's quality claims become test results.
4. **Pilot validation (S4, S8):** the whole method demonstrated end-to-end; MVP acceptance = baseline §27 criteria + `13` §1 additions, evaluated literally against the checklists, with a friction log feeding v1.0.0.
5. **Review cadence:** after S4 and after S8, re-read files `04`/`05`/`09` against observed behaviour and patch via methodology releases — the plan is versioned with the methodology from S0 onward (copy these files into `freelance-methodology/docs/plan/` at S0 so plan and method version together; this directory here remains the frozen origin).
