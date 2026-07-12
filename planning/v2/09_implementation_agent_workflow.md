# 09 — Implementation Agent Workflow

**Purpose:** the task-level implementation loop: context packages, the implementer and reviewer agents, bounded correction cycles, PR flow, and worktree policy.
**Baseline traceability:** B6, B18, B20, §12 step 12, §16.3–16.4; closes G-05; DEC-20.

---

## 1. The loop (one task at a time)

```text
G4: task `ready`
 1. task-context-package skill → docs/task-context/TASK-nnn.md
 2. branch created: feature/US-014-booking-endpoint  (worktree only per §9)
 3. implementer agent: tests + code (TDD-leaning: ACs → failing tests → code)
 4. implementer self-check: suite green, lint/typecheck clean, scope respected
 5. spec-reviewer agent: diff vs REQ/AC/task scope
 6. adversarial-reviewer agent: diff vs failure modes
 7. risk-specialist-reviewer: only if trigger table fires (§5)
 8. correction: implementer fixes findings — max 2 cycles per reviewer stage,
    then human escalation (DEC-20)
 9. clean full run: relevant suites green from scratch
10. PR opened (template §6) → G5: your review → merge
11. post-merge: traceability + task status (+ Jira where used, `08` §4) updated;
    CHANGELOG entry if user-visible. The context package is retained permanently
    at docs/task-context/ (R2-08) — it is the auditable record of the scope the
    implementer was given; changes to it during implementation are ordinary
    commits on the task branch (scope-affecting ones also update the task per
    change control)
```

Each numbered step ends with a persisted status change on the task (session-crash recovery = read task status + branch state).

## 2. Roles are separate sessions

Implementer, spec-reviewer, and adversarial-reviewer run as separate agent sessions (fresh context) so reviews aren't contaminated by the implementer's rationalizations (baseline "tests solo del implementador" risk, retained). At MVP you launch them sequentially via `start-agent.sh`; later a script chains them.

## 3. Task context package (task-context-package skill)

Generated, not hand-written; the implementer reads **only this + the code**, not the whole docs tree (context economy). Retained permanently after merge (R2-08); the merged PR links it at its merge commit:

```markdown
# TASK-031 — Booking request endpoint + validation
Story: US-014 (implements FR-004) · Priority: must · Risk: high
## Goal
One-paragraph outcome.
## Requirements & acceptance criteria (verbatim from requirements.yaml)
FR-004: … / FR-004-AC-01: given/when/then … / BR-002: …
## Design constraints
SDD §4.2 excerpt or pointer · ADR-003 decision summary · api-contract.yaml path
· data-model entities touched
## Non-functional obligations for this task
NFR-002 (a11y: form labels/errors pattern), NFR-007 (validation, rate limit)
## Code context
Relevant paths, existing patterns to follow, fixtures available
## Tests required
unit (validation rules), integration (endpoint+db), a11y (form) → matrix rows TEST-011..013
## Out of scope
Admin confirmation UI (TASK-032); email notification (TASK-033)
## Done means
DoD checklist (08 §3) instantiated
```

## 4. Implementer agent contract

**May:** write code/tests on the task branch; add micro-subtasks (`TASK-031-T-01`) inside the package; run suites; refactor within touched files when needed for the task. **Must not:** expand scope; modify requirements/SDD/ADRs (mismatch found → stop, report, propose CR — never "fix the spec to match the code"); touch other tasks' areas; commit failing tests; commit secrets; merge. **Completion:** self-check passes + summary comment in the package (what changed, decisions made, doubts for reviewers). **Failure:** blocked by spec gap → status `blocked` + precise question; 2 failed attempts at an approach → stop and report options, don't thrash.

## 5. Reviewer contracts

| Reviewer | Question it answers | Verdict output |
|---|---|---|
| spec-reviewer | Does the diff implement exactly the ACs — nothing missing, nothing extra? Are the tests real verifications of the ACs (not tautologies)? | Findings: `blocking | should-fix | note`, each citing REQ/AC id |
| adversarial-reviewer | How does this break? Edge cases, error paths, injection, race/idempotency, state corruption, misuse; tests it would add | Same format + proposed regression tests |
| risk-specialist-reviewer | Domain-specific depth per trigger | Same + checklist evidence |

**Trigger table (baseline §16.4 retained verbatim, operationalized):** text/content → visual+a11y check only · forms → UX/validation/a11y · auth → security+authz+integration · payments → security+idempotency+regression+**mandatory human review** · migrations → backup/rollback/integrity · config/CI → build+env review. High `data_sensitivity` (`03` §4) upgrades any form/data task to security review. **Profile scaling (`21` §5):** LITE runs one merged reviewer session (spec+adversarial contracts in a single pass); HIGH-RISK makes the specialist mandatory on all trigger-area tasks.

Reviewers read: context package + diff + test run output. They do **not** rewrite code (findings only — corrections belong to the implementer, keeping accountability clean).

## 6. PR conventions

Branch names: `feature/US-014-booking-endpoint` · `fix/BUG-003-double-booking` · `chore/TASK-090-ci` · `docs/discovery-01` (baseline §14 retained). Commits: conventional style with canonical ids (`feat(US-014): implement booking creation endpoint`). PR body template: task id + story/FR links · what & why · AC checklist (ticked with evidence: test name or screenshot) · review findings summary & resolutions · test run proof · out-of-scope confirmations · rollback note if risky. One task = one PR (small, reviewable).

## 7. G5 — your review

You review: the diff (skim-level for low risk, careful for high), reviewer findings and their resolutions, AC evidence, CI green. You are reviewing *the reviews* as much as the code — that's what makes one human scale. Merge = squash (linear history, task-sized units). Post-merge steps are part of DoD (`08` §3), executed before the next task starts.

## 8. Escalation & failure paths

Reviewer/implementer deadlock after 2 cycles → you arbitrate in the PR. Spec found wrong mid-task → task `blocked`, CR proposed (`12` §5), never silent spec drift. Flaky test discovered → BUG task, quarantine policy (`10` §7). Build broken on `main` → fix-forward task is the immediate next task, nothing else proceeds.

## 9. Worktree policy (baseline §14.3 retained, made concrete)

Default: **no worktrees** — one task in flight. Worktrees become useful only when *all* hold: (a) two tasks with disjoint code areas and no dependency edge, (b) both `ready`, (c) you have review bandwidth for two PRs. Then: `git worktree add ../acme-web--TASK-032 feature/...`, one Claude session per worktree, never two sessions in one working dir. Never for: schema/migration tasks, refactors, anything touching shared core. Automation of worktree lifecycle is roadmap stage S9+ (baseline §25 respected).
