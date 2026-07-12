# TASK-018 — Scenario 03 non-technical: solution decomposition

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **import mode** (pre-scripted transcript)

## Scenario
Non-technical client who answers mostly in proposed solutions ("mi cuñado
dice que lo hagamos con Wix", "necesito que las reservas me lleguen al
móvil", "casi nadie cancela, eso da igual") — the 04 §3 worked example
expanded to a full transcript. Spanish-language client (exercises DEC-14
language handling).

## Deliverables
- `tests/interview-scenarios/03-non-technical/scenario.md` + transcript
- `tests/golden-artifacts/03-non-technical/golden-checklist.md`
- One executed run; evidence result recorded

## Golden checklist (distinct focus)
- Every proposed_solution decomposed: underlying need recorded as candidate +
  the proposal as preference with stakeholder weight (04 §3)
- The "casi nadie cancela" class: recorded as ASM + exception probe asked —
  never converted to "cancellations out of scope"
- Client language throughout: zero jargon; technical concepts translated to
  consequences (04 §7.2)
- Vagueness gate: one concretization attempt then `precision: low` — no
  looping
- "I don't know" protocol: correct branch per cause (lookup/other-person/
  undecided/misunderstood)

## Primary failure mode guarded
Solution laundering: client-proposed implementations entering the state as
requirements; interview quality collapsing into jargon the client can't
answer (RSK-A2's most likely surface).

## Evidence result
`tests/golden-artifacts/03-non-technical/RESULT.md`.

## Out of scope
Technology evaluation of the proposals (S3; boundary CON-003).
