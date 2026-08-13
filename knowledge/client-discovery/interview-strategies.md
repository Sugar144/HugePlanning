---
id: kn-interview-strategies
title: Interview strategies — trajectories, pacing, rapport, fatigue, modes
type: framework
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "planning the module trajectory for a session, choosing between live-assisted and import mode, or responding to pacing/rapport/fatigue signals"
do_not_use_for: "individual question technique (kn-elicitation-techniques) or question content (kn-question-bank)"
used_by: [client-discovery, adaptive-interview-control]
related: [kn-question-bank, kn-elicitation-techniques, kn-scope-and-mvp]
supersedes: null
---

# Interview strategies

## Purpose

Session-level judgment: how to shape a whole interview — trajectory per
profile, energy-following, pacing and playback rhythm, fatigue response,
multi-stakeholder rooms, and import-mode gap analysis.

## Trajectory planning

Modules M0–M12 are a default order, not a script (`04` §5). Plan the
trajectory at M0 from three inputs: profile (module floor, `21` §5),
archetype hypothesis (which deep-dives may activate), and the sitting budget.
Then follow conversation energy: when a client explaining pain points drifts
into business rules, follow — coverage is updated wherever material lands,
and the queue brings skipped topics back later.

**Example — LITE trajectory (restaurant landing page, 75 min):**
M0 framing (5') → M1–M3 compressed as one conversation about the business
and its customers (15') → M5 capabilities with content focus (15') → M7
content responsibility + data touchpoints (10') → M8 floor confirmation only
(5') → M9 ownership checklist (10') → M10 scope/budget/deadline (10') → M12
summaries + closure (5'). M4/M6/M11 fold into M5/M12; critical topics stay
in even if minutes run short — the cut is depth, not criticals.

**Example — HIGH-RISK trajectory (bookings + payments, 2 sittings):**
Sitting 1: M0–M5 full depth, payment deep-dive activated the moment the
trigger fires, M6 business rules as their own block. Sitting 2 (after the
client gathers homework from OQs): M7–M9 with data-sensitivity and
integration deep-dives, M10, M11 consolidation (assumption review has real
material by now), M12. Between sittings: state persisted, OQs assigned with
owners and deadlines.

## Pacing and playback rhythm

One question per turn; playback at every module close (2–4 sentences, client
language, explicit yes/no/correction). The playback is load-bearing: it
catches misunderstandings while cheap, and it is the client's experience of
being heard. Progress statements ride on module boundaries ("hemos cubierto
el negocio y sus clientes; nos quedan el contenido y los plazos") — honest
and approximate, no fixed block-count mechanics, because trajectories adapt.

## Rapport mechanics

- Open with the client's world, not the project's paperwork (M1 before M2).
- Mirror their vocabulary; correct nothing mid-flow (glossary records usage).
- When something emotionally important surfaces, follow it even off-topic —
  rapport is data quality (`04` §7.1 interrupt class).
- Thank concreteness specifically ("ese ejemplo del martes ayuda mucho") —
  it trains the interview toward examples.

## Fatigue handling

Signals: very short replies, repeated "no sé", vagueness creep, "¿queda
mucho?", answer latency. The response ladder, in order:

| Rung | Move |
|---|---|
| 1 | drop to critical topics only (queue re-scores with fatigue penalty) |
| 2 | switch open questions to concrete options ("¿A o B?") |
| 3 | offer labeled defaults ("puedo proponer algo razonable y usted lo confirma luego") — recorded as ASM/proposed-default material, with an explicit verbal marker that it is a proposal |
| 4 | propose a pause at the module boundary with the resume plan (`04` §10) |

A shorter interview with honest assumptions beats a complete one with
resentful answers. Fatigue signals increment the budget counter either way —
the completion check sees them.

## Multi-stakeholder rooms

Attribute every statement by speaker from the first turn. When two people
disagree, record both positions (attributed), then ask the decision-maker
identified in M3 to arbitrate; unresolved disagreement is a CTR with
`owner: client-side decision`, not a coin flip. Watch for the quiet operator:
the person who runs the process day-to-day often isn't the one talking —
invite them into process topics explicitly.

## Import mode (gap analysis)

When a transcript/notes file already exists (`04` §2): ingest into evidence,
run the same coverage model over it marking topics from the material, then
the interview becomes the prioritized remainder — a follow-up set ordered by
importance × uncertainty, delivered live or as an async CLAR batch. The
classification discipline is identical; the only difference is that coverage
starts pre-populated. Trap: imported notes are usually someone's summary —
treat summarized claims as lower confidence than quoted speech, and confirm
load-bearing ones.

## Failure modes

- Script-following: marching M0→M12 in order against the conversation's
  energy produces thin answers and burned rapport.
- Coverage theater: many topics `touched`, few `sufficient` — depth beats
  breadth for whatever the profile marks critical.
- Playback skipping under time pressure — the cheapest error detector is the
  first thing dropped and the most expensive to skip.
- Fatigue denial: pushing to "finish" past rung 3 produces data that has to
  be re-elicited anyway.

## Limitations

Model-generated, provisional; trajectory timings are planning heuristics for
small Spanish-market engagements, to be recalibrated from real sittings
(question-bank and this file are the highest-maintenance pair).

## References

- Plan `04` §2/§5/§7/§10, `21` §5 (module floors).
- Prototype material (secondary): business-discovery-interviewer (block
  pacing, playback, fatigue) — `planning/history/claude-ai-prototypes/`.

## Related

[[kn-question-bank]] · [[kn-elicitation-techniques]] · [[kn-scope-and-mvp]]
(M10) · [[kn-technical-operational-context]] (M9).
