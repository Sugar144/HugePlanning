# 08 — Backlog, Jira, and Traceability

**Purpose:** the transformation `objectives → requirements → stories → ACs → tasks → tests → PRs → releases`, Jira publication with Git as authority, and the traceability model.
**Baseline traceability:** B5, B19, §15; closes G-09, G-14.

---

## 1. Decomposition rules (backlog-refinement skill)

```text
OBJ ──▶ EP (1..n epics per objective; every epic names its objective_refs)
FR  ──▶ US (usually 1:1; large FR → several US; each US implements ≥1 FR)
US  ──▶ TASK (implementation slices ≤ ~1 day of work each)
AC  ──▶ TEST rows (each AC → ≥1 test-matrix row; 10 §4)
CON/NFR ──▶ either global tasks (e.g., TASK "a11y audit pass") or
            constraints attached to every relevant task's context package
```

Granularity rules: a task has one clear outcome, one primary code area, bounded scope statement ("out of scope for this task: …"); spikes are tasks of `type: spike`; docs/config work is a task like any other. Dependencies explicit (`depends_on`), cycles rejected by `validate.sh`. Sequencing: walking skeleton first (deploy pipeline + one thin end-to-end slice), then risk-descending order (high-risk/high-uncertainty early), then value order.

## 2. Definition of Ready — task (G4; baseline §13 retained + tightened)

- [ ] Goal + linked US/FR/AC ids
- [ ] ACs concrete and locally verifiable (or explicitly integration-level)
- [ ] Dependencies merged or scheduled
- [ ] Relevant design refs exist (SDD section, ADR, contract)
- [ ] Constraints & out-of-scope stated
- [ ] `tests_required` declared (levels, from test matrix)
- [ ] No open blocking OQ/CLAR
- [ ] Estimate ≤ L (XL must be split)

## 3. Definition of Done — task (G5; baseline §13 retained)

Code implemented · declared tests written and green · full relevant suite green · spec review + adversarial review findings resolved · risk-triggered specialist review done (if triggered) · docs touched by the change updated · traceability updated (task → PR → tests) · PR approved by you · merged · Jira status updated. "The agent finished writing code" ≠ done (baseline, verbatim).

## 4. Jira model (Git → Jira only; baseline §15 retained)

| Canonical | Jira type | Jira fields carried |
|---|---|---|
| EP-nnn | Epic | summary = `EP-002 — Reservas online`; description: objective refs + Git link |
| US-nnn | Story | summary = `US-014 — <title>`; description: implements FR ids, AC list, Git permalink; labels: `risk-high`, `must` |
| TASK/BUG/CR-nnn | Task/Bug/Task | summary with canonical id; description: context-package link, DoR checklist state |

Rules: canonical ID always leads the summary; Jira description carries **links + snapshot**, never the editable truth; specification edits happen in Git and re-export. Jira workflow columns: `To Do / In Progress / In Review / Done` mapped from task statuses (`06` §2: backlog+ready→To Do; in_progress→In Progress; in_review..approved→In Review; merged..done→Done).

## 5. Export and reconciliation

`export-jira.sh` (MVP): reads `delivery-backlog.yaml` → emits Jira-importable CSV (REST-API mode arrives in roadmap stage S9) → after import you paste/auto-capture the created keys → script writes `jira-map.yaml`:

```yaml
schema_version: 1.0.0
project_key: WEB
mappings:
  - canonical: US-014
    jira: WEB-42
    exported_at: 2026-09-28
    exported_commit: 9f1c2d3
```

Re-export is **idempotent**: items already in the map are skipped or flagged as "changed since export" (diff of exported_commit), producing an update list you apply manually at MVP. Divergence check (roadmap stage S9): weekly script compares Jira status vs Git task status and lists mismatches — Git wins for content, Jira wins for *work-in-progress status* until the task file is updated at PR time (single defined direction per field class, closing the two-truths risk).

## 6. Traceability model

`traceability.yaml` stores ID→ID edges only (`06` §5). Most edges already live in the artifacts (requirements link OBJ/AC; tasks link US); the file materializes the *derived* full chains and the implementation-side facts:

```yaml
schema_version: 1.0.0
links:
  - task: TASK-031
    story: US-014
    implements: [FR-004]
    branch: feature/US-014-booking-endpoint
    pr: 17
    commits: [a1b2c3d]
    tests: [TEST-011, TEST-012]
    release: REL-001
```

`traceability-validation` skill (+ `validate.sh`): every `approved` FR reaches ≥1 task and ≥1 test · every merged PR maps to a task · every release manifest lists its tasks · dangling refs = error. Updated at each task merge (part of task DoD) and at release close. Impact analysis for CRs = reverse walk of these edges (`12` §5).

## 7. G4 batch gate

Before an implementation batch (weekly at MVP): pick next tasks by dependency+risk order → run DoR checklist per task → mark `ready` → export/update Jira. Record: commit touching backlog + jira-map.
