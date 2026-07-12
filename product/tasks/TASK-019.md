# TASK-019 — Scenario 04 LITE: module floor and single sitting

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **import mode** (pre-scripted transcript)

## Scenario
Restaurant landing page (static-landing archetype, LITE profile, no
triggers) — the 21 §7 dry-run client at interview stage. Cooperative, time-
constrained; transcript sized to the single-sitting budget (60–90 min).

## Deliverables
- `tests/interview-scenarios/04-lite/scenario.md` + transcript
- `tests/golden-artifacts/04-lite/golden-checklist.md`
- One executed run; evidence result recorded

## Golden checklist (distinct focus)
- Module floor respected: M0, M1–M3 compressed, M5, M7 (content focus), M8
  (floor confirmation only), M9, M10, M12; M4/M6/M11 folded — not skipped
  silently (21 §5 row 1)
- Critical topics remain profile-independent and covered: objectives, users,
  scope boundary, budget, timeline, ownership, data sensitivity, legal flags,
  maintenance (04 §4)
- Content-inventory seeding happens despite the compressed flow (R2-18:
  cannot close with content ownership unassessed)
- Budget discipline: fatigue/soft-limit handling keeps the sitting inside
  target without dropping critical topics
- Output floor: compact registers sufficient for the 1-page brief pipeline

## Primary failure mode guarded
Profile bleed in either direction: running the full STANDARD interview on a
LITE client (commercial failure, R2-19) or dropping critical topics to save
time (assurance failure, RSK-A12).

## Evidence result
`tests/golden-artifacts/04-lite/RESULT.md`.

## Out of scope
Escalation behavior (TASK-020 owns the LITE→trigger path).
