---
id: kn-scope-and-mvp
title: Scope and MVP — phase cutting, complexity multipliers, budget conversations
type: framework
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "running M10 (scope, priorities, budget), dispositioning scope flags, or a feature request smells bigger than it sounds"
do_not_use_for: "estimation itself (operator act, DEC-16) or backlog phasing mechanics (08, S2)"
used_by: [client-discovery, adaptive-interview-control]
related: [kn-question-bank, kn-interview-strategies]
supersedes: null
---

# Scope and MVP

## Purpose

Judgment for the scope conversation: which requests multiply complexity,
which phase-cutting heuristics keep v1 valuable, how to phrase exclusions so
they stick, and how to have the budget conversation without flinching.

## Complexity multipliers

Features that sound small and aren't — each deserves an explicit cost flag
and often a simplification proposal (adapted from the prototype baseline,
R2-36; validated against the archetype/trigger model):

user accounts · customer history · saved preferences · online payments ·
refunds · subscriptions · coupons/offers/campaigns · admin panels · editable
CMS · real-time dashboards · notifications (SMS/WhatsApp/push) · multilingual
content · roles and permissions · analytics/reporting · third-party
integrations · data migrations · search/filtering · scheduling/availability ·
inventory · audit logs · data export · consent workflows.

Several of these are simultaneously **risk triggers** (`21` §3): payments,
accounts, sensitive data, migrations, business-critical integrations. When
one appears, the scope conversation and the trigger duty both fire — flag
the cost *and* record the trigger.

## Simplification patterns (keep the outcome, cut the machinery)

| Pattern | Instead of | v1 form |
|---|---|---|
| manual-first | automation | a person handles it, the web captures it |
| no-auth | user accounts | guest flow + contact details |
| payment-light | full payment flow | deposit link / pay-on-site |
| notification-light | multichannel push | email-only to the owner |
| content-light | CMS | developer-updated content, monthly batch |
| single-language | multilingual CMS | one language + translated legal texts |
| report-light | dashboards | a monthly export |
| integration-light | live sync | manual export/import at agreed cadence |
| operational fallback | hardening | a documented manual path when it breaks |

Every simplification is proposed with its trade-off stated ("cut this,
here's what it costs and what it saves") — silent scope cutting reads as
broken promises later.

## Phase-cutting heuristics

- Protect the **minimum valuable** product: the core outcome (M2) and the
  primary journey end-to-end. Everything else is judged against those two.
- Cut by dependency, not by wish: before deferring X, check whether a kept
  feature depends on it — defer both, simplify both, or keep both.
- The forcing question when everything is essential: "si el plazo obligara a
  elegir la mitad, ¿qué mitad?" — halving forces ranking where listing
  doesn't.
- Phase 2 is a promise with a trigger ("cuando el primer mes confirme que
  llegan reservas"), not a euphemism for never.
- Scope flags parked during M1–M9 all get an explicit in/out/later at M10 —
  the parking lot empties or it wasn't a parking lot.

## Exclusion phrasing (client-facing)

An exclusion sticks when it names the thing, the reason, and the path back:
"la versión 1 no tendrá pedidos online; primero validamos que las reservas
funcionan, y el pedido online entra en la fase 2 si el volumen lo pide."
Naked exclusion lists get renegotiated at G2; framed ones get signed.

## Budget and deadline conversation

- Ask directly, offer a range as the exit ramp: "¿qué horquilla tienen en
  mente — más cerca de mil, de tres mil…?" A range is an answer; silence is
  not (the DoD requires the topic addressed, `04` §12).
- Anchor deadlines to their driver: a fair date is a hard deadline, "cuanto
  antes" is a preference — record which.
- When budget and wishes visibly diverge, name it neutrally in-interview
  ("con esa horquilla, la parte de pedidos probablemente es fase 2") — the
  estimation checkpoint (`07` §8) does the numbers, but pretending not to
  notice wastes everyone's G2.

## Examples

1. Restaurant wants: web, reservas, pedidos a domicilio, cuenta de clientes,
   ofertas por email. M10 outcome: v1 = web + reservas (core journey);
   pedidos → phase 2 (payments trigger + kitchen process unknown — OQ);
   cuentas → no-auth pattern (bookings by phone number); ofertas →
   notification-light (owner sends a monthly email manually). Two scope
   flags dispositioned, one trigger recorded, trade-offs stated.
2. "Que los clientes puedan cambiar su reserva ellos mismos" — sounds small;
   multiplier check: implies lookup by identity (accounts or magic links) +
   edit flow + rule handling (¿hasta cuándo se puede cambiar?). Proposal:
   v1 = "responda al email de confirmación y lo cambiamos" (manual-first),
   self-service change parked to phase 2 with volume trigger.

## Failure modes

- Equal-cost illusion: treating every listed wish as the same size — the
  multiplier list exists to break it.
- Cutting the core to fit the budget: a cheap v1 that can't do the primary
  journey validates nothing.
- Recording cuts as client decisions before the client actually confirmed
  them (that confirmation is G2's job — at M10 they are agreed intentions).

## Limitations

Model-generated with prototype-derived content (secondary source); patterns
biased toward small Spanish-market web work. Estimation itself is out of
scope by design.

## References

- Plan `04` §5 (M10), `04` §9 (scope flags), `07` §8 (estimation), `21` §3.
- Prototype (secondary): mvp-scope-reducer SKILL.md + references/
  scope-reduction-format.md (multipliers, reduction strategies, dependency
  check); PROJECT_INSTRUCTIONS §9 — `planning/history/claude-ai-prototypes/`.

## Related

[[kn-question-bank]] (M10 seeds) · [[kn-interview-strategies]] (pacing the
scope conversation) · [[kn-requirements-taxonomy]] (preference vs need).
