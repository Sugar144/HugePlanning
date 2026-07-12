---
id: kn-process-elicitation
title: Process elicitation — reconstruction frame and exception hunting
type: framework
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "reconstructing a current or future business process in M4/M5, or judging whether a process topic is sufficient"
do_not_use_for: "flow design or screen mapping (technical design, S3)"
used_by: [client-discovery, process-elicitation]
related: [kn-question-bank, kn-elicitation-techniques]
supersedes: null
---

# Process elicitation

## Purpose

The reconstruction frame that turns a client's process narration into a
record complete enough to derive requirements: trigger, actors, steps,
exceptions, outcome — plus the exception-hunting prompts that find what the
narration left out.

## The frame

A process is sufficiently understood when all five slots hold confirmed
material (`04` §4):

| Slot | Question it answers | Watch for |
|---|---|---|
| trigger | what starts it, and from where | multiple entry channels counted as one |
| actors | who does each part (roles, not names) | the invisible actor ("bueno, eso lo hace mi mujer") |
| steps | the happy path, in order, with handoffs | steps that are really tools ("lo meto en el Excel" — what exactly?) |
| exceptions | what breaks it and what happens then | "casi nunca pasa" — the requirement generator |
| outcome | what state the world is in when it worked | implicit outcomes ("y ya está" — is money collected? recorded where?) |

Future processes (M5) use the same frame in the desired tense; the delta
between current and future frames is where requirements live.

## Exception-hunting prompts

- "¿Y cuando alguien cancela / no aparece / llega tarde?"
- "¿Qué pasa si dos piden lo mismo a la vez?"
- "¿Y si el que lo hace normalmente está de vacaciones?"
- "¿Cuándo fue la última vez que esto salió mal? ¿Qué pasó?"
- "¿Qué caso raro le da más rabia cuando ocurre?"

One confirmed exception with its handling beats three acknowledged-but-
unexplored ones. Exceptions with no current handling are decisions-pending,
recorded as such — not silently resolved by the interviewer's common sense.

## Worked reconstruction

Client narration: "Nos escriben por WhatsApp, miro la libreta, si hay hueco
les digo que sí y lo apunto."

Frame after probing:

- **trigger:** booking request via WhatsApp or phone call (two channels —
  the call channel surfaced only when asked "¿solo WhatsApp?").
- **actors:** owner (checks + confirms); weekend waiter answers the phone
  but *doesn't* confirm — relays to the owner (invisible-actor probe).
- **steps:** message arrives → owner checks paper notebook → replies
  yes/no → writes name, people, time in notebook.
- **exceptions:** cancellation = customer messages again, owner crosses it
  out ("cuando me acuerdo" — integrity gap, recorded); double request for
  the last table = first-answered wins, no record of the loser (lost-demand
  gap); notebook at home on Mondays (availability gap).
- **outcome:** confirmed booking exists only in the notebook; no reminder,
  no-shows ≈ 1–2/week (baseline number captured for M2 metrics).

Requirement candidates fall out of the gaps, each anchored: notification to
owner's phone (FR), single availability record (FR/DAT), cancellation
handling (FR + BR), no-show reduction as an objective metric.

## Failure modes

- Tool answers accepted as step answers: "lo gestiono con el Excel" hides
  five steps and two actors — ask what happens *around* the tool.
- Happy-path sufficiency: a frame with an empty exceptions slot marked
  `sufficient` — the slot is part of the bar.
- Premature future tense: designing the new process (M5) before the current
  one (M4) is understood loses the constraints that make designs real.
- Solutioning inside the frame: recording "usará un calendario compartido"
  as a step — that's a proposal; the step is the business action it serves.

## Limitations

Model-generated, provisional; frame validated through S1 scenarios. Deeper
technique sourcing arrives with RES-01.

## References

- Plan `04` §4 (sufficiency), `04` §5 (M4/M5), `17` §K.8.

## Related

[[kn-question-bank]] (M4/M5 seeds) · [[kn-elicitation-techniques]]
(example anchoring, exception hunting).
