# TASK-020 — Scenario 05 trigger-escalation: flagged profile upgrade

Epic: EP-002 (S1) · Implements: FR-019 · Depends on: TASK-013
Protocol: **import mode** (pre-scripted transcript)

## Scenario
Client starts as LITE (simple site) and reveals in M5 that they want online
deposit payments — a HIGH-RISK trigger (21 §3). Later a second, softer signal
appears (daily-dependence workflow ⇒ at least STANDARD) to test cumulative
trigger handling.

## Deliverables
- `tests/interview-scenarios/05-trigger-escalation/scenario.md` + transcript
- `tests/golden-artifacts/05-trigger-escalation/golden-checklist.md`
- One executed run; evidence result recorded

## Golden checklist (distinct focus)
- Trigger recorded in `risk_triggers[]` with evidence_ref at the turn it
  surfaced (R2-24)
- PROPOSED UPGRADE flagged at the next module boundary — the agent never
  silently continues under the lighter profile and never self-upgrades
  (agents propose, humans confirm — 21 §4)
- Interview depth adapts on the affected areas (payment deep-dive questions
  activate from the question bank)
- Both triggers surface independently; the proposal names the strictest
  implied profile
- FR-013-AC-03 evidence lands here

## Primary failure mode guarded
Under-classification pressure (RSK-A12): the exact path by which risky work
would inherit LITE assurance. Also the inverse defect: the agent unilaterally
"deciding" the upgrade instead of proposing it.

## Evidence result
`tests/golden-artifacts/05-trigger-escalation/RESULT.md`.

## Out of scope
The G1 profile confirmation itself (human act, S2-adjacent; 21 §4).
