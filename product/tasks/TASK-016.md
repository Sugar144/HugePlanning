# TASK-016 — Scenario 01 clear: baseline coverage and classification

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **import mode** (pre-scripted transcript, repeatable)

## Scenario
Cooperative restaurant-booking client (STANDARD profile, booking-system
archetype). Fictitious material only. Answers are clear and complete; the
transcript includes one mid-M7 pause point so this scenario also exercises
pause/resume (FR-015-AC-01 evidence lands here).

## Deliverables
- `tests/interview-scenarios/01-clear/scenario.md` + scripted transcript
- `tests/golden-artifacts/01-clear/golden-checklist.md`
- One executed run, scored; evidence result recorded (see below)

## Golden checklist (distinct focus of this scenario)
- Coverage: every STANDARD module reaches its target state; all critical
  topics `sufficient` (04 §4)
- Classification: statement types assigned per 04 §3 across the transcript
- Non-invention: every state entry anchored to an existing turn
- Pause/resume: mid-M7 pause persists state; resume re-hydrates from
  `interview-state.json` + last transcript page only and continues with the
  queued question
- DoD discipline: one early-close request is refused with the failing
  criteria listed
- Module playback: summary + explicit confirmation at each module close

## Primary failure mode guarded
Shallow "checklist visiting" — modules touched but topics not actually
`sufficient`; state file diverging from the conversation.

## Evidence result
`tests/golden-artifacts/01-clear/RESULT.md`: run date, agent/methodology
commit, checklist outcomes, defects found (classified per 22 §5),
disposition. Referenced from TASK-015's release evidence.

## Out of scope
Contradiction handling depth (TASK-017), sanitization (TASK-021).
