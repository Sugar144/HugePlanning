<!-- completion-report.md skeleton (04 §12) — written by client-discovery at
     interview close, alongside the sanitization pass. Save as
     evidence/interviews/<session-id>/completion-report.md.
     Human document (layer 3): it cites state/register content, it does not
     restate requirements in new normative words. -->
---
status: draft
generated_from: evidence/interviews/{{SESSION_ID}}/interview-state.json
language: {{PROJECT_LANGUAGE}}
---

# Discovery completion report — {{PROJECT_ID}} / {{SESSION_ID}}

## Session summary

Mode, sittings (dates + durations), total turns, modules visited, profile
and archetype hypothesis at close.

**Run metrics** (observability, not normative): total turns · sittings ·
resumptions · segments (bounded fresh-context invocations) · final
`interview-state.json` size (bytes) · transcript-window size at each
re-hydration · playbacks · operator relays. These make interview cost
measurable across scenarios; record what is observable (including per-segment
context footprint when the runtime exposes it), never an estimated token
figure.

## Coverage table

| Topic | Module | Importance | Status | Confidence | Notes |
|---|---|---|---|---|---|
<!-- one row per coverage node; deferred rows cite their operator-approved
     deferral (reason/owner); not_applicable rows cite their justification -->

## Registers summary

- **Contradictions:** open / resolved / accepted_as_tension — list critical
  ones with their anchors and resolution refs.
- **Assumptions:** confirmed / unconfirmed carried to validation — list
  unconfirmed with their basis anchors.
- **Open questions:** each with owner, impact, blocking flag, deadline.
- **Scope flags:** each with its M10 disposition (in / out / later).
- **Risk triggers:** each with evidence anchor, implication, and status —
  proposed upgrades highlighted for the G1 profile confirmation.

## DoR / DoD evaluation (04 §11–§12)

| Criterion | Held? | Waiver / note |
|---|---|---|
| All critical topics sufficient or dispositioned | | |
| Zero open critical contradictions | | |
| Assumptions reviewed in M11 | | |
| Scope flags dispositioned | | |
| Every candidate anchored | | |
| Module summaries confirmed (M12) | | |
| OQs have owner + impact + blocking flag | | |
| Budget & timeline explicitly addressed | | |
| Domain/hosting/accounts ownership established or OQ'd | | |
| Data sensitivity assessed | | |
| Content responsibility assessed, inventory seeded | | |
| Risk triggers reviewed vs profile hypothesis | | |

## Content inventory seeds

Items seeded (id, item, owner, deadline) — pointer to
`docs/product/content-inventory.yaml`.

## Recommended next actions

Normalization inputs ready; blocking OQs to chase before G1; proposed
profile decision for the G1 checklist; suggested follow-up sitting topics,
if any.

## Closure

Proposed by the agent on {{DATE}}; **accepted by the operator on ____**
(human approval point 1, `04` §13).
