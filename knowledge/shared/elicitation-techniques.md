---
id: kn-elicitation-techniques
title: Elicitation techniques for stuck or vague topics
type: catalog
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "a topic is stuck, an answer is vague, the client says they don't know, or a critical topic resists the standard funnel"
do_not_use_for: "question content per topic (see kn-question-bank) or process reconstruction specifics (see kn-process-elicitation)"
used_by: [client-discovery, adaptive-interview-control, nfr-elicitation, process-elicitation]
related: [kn-question-bank, kn-interview-strategies]
supersedes: null
---

# Elicitation techniques

## Purpose

Technique reference for extracting decision-grade information from
non-technical clients when the straightforward question doesn't work. Each
entry: when it applies, a script skeleton, a mini-dialogue, and its failure
signs. (RES-01 upgrades this file with externally sourced technique
literature before the first real paid interview.)

## The funnel (default per topic)

Open → specific → example → confirm. When: every topic's first pass.

> — ¿Cómo funcionan hoy las reservas? *(open)*
> — Nos llaman o escriben por WhatsApp.
> — ¿Quién las confirma y cómo? *(specific)*
> — Yo, contestando el mensaje.
> — Cuénteme las reservas del martes pasado, tal cual. *(example)*
> — Hubo cuatro; una la perdí porque no vi el mensaje…
> — Entonces hoy es usted confirmando cada una por WhatsApp, y a veces se
> pierde alguna — ¿es así? *(confirm)*

Failure signs: jumping to *confirm* without the *example* step produces
agreements about generalities that fall apart on details.

## Example anchoring

When: answers stay abstract ("depende", "lo normal"). Ask for the last
concrete instance: "la última vez que pasó, ¿qué hizo?" Recent-past specifics
beat hypotheticals — clients narrate what happened more accurately than what
"usually" happens.

> — ¿Cuántas reservas tienen por semana?
> — Uf, depende…
> — La semana pasada, ¿cuántas fueron, más o menos?
> — Unas quince, veinte en verano.

Failure sign: the client invents a "typical" case under pressure — if the
narration has no texture (names, times, hiccups), it's a hypothetical wearing
a past tense.

## Laddering (why beneath the ask)

When: a want arrives without its need ("quiero un chat en la web"). Ladder
down: what would that give you? and what would *that* give you? Two or three
rungs usually expose the requirement the want was standing on.

> — ¿Qué le daría el chat?
> — Que la gente pregunte sin llamar.
> — ¿Qué preguntan normalmente?
> — Si hay sitio para hoy, casi siempre.
> *(the need is availability visibility — a chat is one proposal for it)*

Failure sign: more than three "why" rungs reads as interrogation; stop at the
first rung that names an outcome the business recognizes.

## Contrast questions

When: the client can't articulate a preference or boundary in the abstract.
Offer two concrete poles: "¿más parecido a X o a Y?" Works for visual
direction, tone, depth of admin control, formality of process.

> — ¿La web debería sentirse más como la de [asador tradicional] o como la
> de [bistró moderno]?
> — Lo segundo, pero menos oscura.

Failure sign: offering poles the client doesn't know — anchor on sites or
businesses they mentioned themselves when possible.

## Consequence framing (for quality topics)

When: any NFR-shaped topic. Translate the technical dimension into a business
consequence and ask about the consequence: "si la web se cae una mañana, ¿qué
pasa con su negocio?" instead of availability targets. The measurable anchor
is then negotiated from the reaction (see [[kn-nfr-catalog]]).

## Exception hunting

When: any process description that sounds complete. Ask what happens when the
happy path breaks: "¿y cuando alguien cancela?", "¿y si llegan dos a la vez?"
A process is understood by its exceptions; details in
[[kn-process-elicitation]].

## Silence and minimal encouragers

When: the client trails off mid-thought or hesitates after a hard question.
Waiting two beats, or a neutral "ajá…", routinely completes the thought;
filling the silence with a new question loses it. Failure sign: chaining a
clarifying question onto an unfinished answer — the first thought dies.

## The "I don't know" protocol

Classify the cause before responding; each cause has a different move.

| Cause | Detect by | Move |
|---|---|---|
| needs to look it up | "tendría que mirarlo" | OQ, owner = client, with deadline |
| someone else knows | "eso lo lleva mi socia" | OQ, owner = that person, named |
| genuinely undecided | "no lo hemos pensado" | record decision-pending + a labeled default for confirmation |
| didn't understand | blank pause, off-topic reply | re-ask concretely with an example, once |

The move that isn't on the menu: pressing until the client invents an answer.
An invented answer is worse than a recorded gap — it looks like evidence.

## Vagueness gate (one attempt, then record)

When: an answer is too vague to become a requirement ("rápida", "moderna").
One concretization attempt with a scale anchor, example, or comparison; if it
stays vague, record `client_preference` with `precision: low` and move on.
Looping on the same vague topic burns rapport for no information.

## Anti-example (technique misuse)

> — ¿Verdad que querrán pagos online? *(leading — embeds the answer)*
> — Eh… supongo que sí.

The "yes" is manufactured. The non-leading form: "¿cómo le gustaría recibir
el dinero de las reservas?" — and its answer might have been "en el local,
como siempre".

## Failure modes

- Technique stacking: applying three techniques to one question; pick one.
- Interrogation drift: funnels without playback make clients defensive —
  module summaries are part of the pacing, not decoration.
- Anchoring bias: contrast poles chosen by the interviewer can steer the
  answer; prefer poles from the client's own references.

## Limitations

Model-generated and provisional. Technique inventory intentionally small;
RES-01 (high priority) sources the professional literature and expands this
file before any real paid discovery interview (R2-32).

## References

- Plan `04` §7.2 (question craft rules), `19` R2-32.
- Prototype material (secondary): `planning/history/claude-ai-prototypes/`
  — business-discovery-interviewer core behavior; PROJECT_INSTRUCTIONS §2/§8.

## Related

[[kn-question-bank]] (what to ask) · [[kn-interview-strategies]] (when and in
what order) · [[kn-process-elicitation]] · [[kn-nfr-catalog]].
