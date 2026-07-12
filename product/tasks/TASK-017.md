# TASK-017 — Scenario 02 contradictory: CTR catch and resolution

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **live-assisted** (operator plays the client — contradiction timing
must react to the agent's actual questions, so a script would rig the test)

## Scenario
Client changes scope mid-interview (04 §14 pattern: "everything must be live
before the fair on Oct 3, and I also want the online shop from day one" after
turn-12 said the shop could wait). A second, minor contradiction about
pricing is planted for deferral handling.

## Deliverables
- `tests/interview-scenarios/02-contradictory/scenario.md` (operator brief:
  planted contradictions, when to introduce them, persona notes)
- `tests/golden-artifacts/02-contradictory/golden-checklist.md`
- One executed live sitting (~1–1.5 h + scoring); evidence result recorded

## Golden checklist (distinct focus)
- Critical CTR registered with BOTH evidence anchors within ~2 turns
  (interrupt override, 04 §7.1)
- Neutral confrontation form used — no leading resolution
- Resolution recorded as a new confirmed turn; CTR closed with pointer
- Minor CTR deferred to OQ with owner — not silently dropped, not blocking
- Coverage state updated after resolution (scope.mvp → sufficient)
- DoD: interview cannot close while a critical CTR is open

## Primary failure mode guarded
Silent side-picking: the agent adopting the latest statement without
registering the conflict — the exact behavior invariant 2 forbids.

## Evidence result
`tests/golden-artifacts/02-contradictory/RESULT.md` (same structure as
TASK-016's; live-sitting duration noted).

## Out of scope
Multi-stakeholder arbitration (covered by 04 §9 design, exercised at S4 pilot).
