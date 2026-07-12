---
id: kn-question-bank
title: Question bank — seeds, sufficiency checks, risk keywords per topic
type: catalog
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "selecting seed questions for the current module, judging whether a topic is sufficient, or activating an archetype/trigger deep-dive"
do_not_use_for: "session-level trajectory (kn-interview-strategies) or technique choice (kn-elicitation-techniques)"
used_by: [client-discovery, adaptive-interview-control, nfr-elicitation, process-elicitation]
related: [kn-interview-strategies, kn-elicitation-techniques, kn-nfr-catalog, kn-scope-and-mvp, kn-technical-operational-context]
supersedes: null
---

# Question bank

## Purpose

Per topic of the `04` §5 module tree: three-plus seed questions (funnel
forms, ES), the sufficiency check, and the risk keywords whose appearance
feeds `risk_triggers[]`. Deep-dive sections at the end activate by archetype
or trigger. Grows from every real interview — the highest-maintenance file.

Seeds are starting forms, not scripts: adapt wording to the client's own
vocabulary. Anti-pattern per module = a leading form seen in the wild, kept
here so it isn't reinvented.

## M1 — Business context & problem

**business.identity** · seeds: "Cuénteme su negocio: ¿qué hacen y para
quién?" · "¿Qué les diferencia de los demás [sector] de la zona?" · "¿Cómo
llegan hoy los clientes nuevos?" · sufficient when: what they sell, to whom,
and the acquisition channel are stated. · risk keywords: franquicia, varios
locales, regulado.

**problem.trigger** · seeds: "¿Qué le ha hecho buscar una web ahora?" ·
"¿Qué es lo que peor funciona hoy?" · "Si esto sale bien, ¿qué habrá
cambiado dentro de un año?" · sufficient when: the pain and the "why now"
are explicit. · risk keywords: multas, inspección, "nos lo exige".

*Anti-pattern (M1):* "¿Su problema es que pierden reservas, no?" — diagnosis
embedded in the question.

## M2 — Objectives & success

**objectives.outcomes** · seeds: "¿Qué debería conseguir la web, en sus
palabras?" · "De todo eso, ¿qué es lo más importante?" · "¿Qué sería un
fracaso, aunque la web quedara bonita?" · sufficient when: ≥1 outcome is
stated as a business result (not a feature) and ranked.

**objectives.metrics** · seeds: "¿Cómo sabrá que está funcionando?" · "¿Qué
número le gustaría ver cambiar?" · "Hoy, ¿cuántas [reservas/consultas]
tienen por semana?" · sufficient when: a signal and its current rough
baseline exist, or "no metric" is explicitly accepted.

*Anti-pattern (M2):* "¿El objetivo es vender más, verdad?" — objective
supplied, not elicited.

## M3 — Stakeholders & users

**stakeholders.decision** · seeds: "¿Quién más opina sobre este proyecto?" ·
"Si hay dos opiniones, ¿quién decide?" · "¿Quién aprobará la web al final?"
· sufficient when: the decision-maker is named. · risk keywords: socios en
desacuerdo, "el del marketing".

**users.groups** · seeds: "¿Quiénes usarán la web — qué tipos de cliente
tiene?" · "¿Cambia mucho lo que necesita cada tipo?" · "¿Desde dónde le
escriben: móvil, ordenador?" · sufficient when: primary group, meaningful
secondary groups, and device reality are known.

*Anti-pattern (M3):* asking "¿quién es su buyer persona?" — jargon.

## M4 — Current processes & pain

**process.current** · seeds: "¿Cómo funciona hoy [el proceso central]?" ·
"Míreme el martes pasado: ¿qué pasó, paso a paso?" · "¿Dónde se pierde más
tiempo o dinero?" · sufficient when: the process-elicitation frame is filled
(see [[kn-process-elicitation]]). · risk keywords: "lo llevo yo todo", doble
registro, papel.

**process.tools** · seeds: "¿Qué usan hoy — cuadernos, Excel, algún
programa?" · "¿Qué hace bien esa herramienta que no quiera perder?" · "¿Qué
le obliga a hacer dos veces?" · sufficient when: tool inventory + what they'd
keep is recorded (feeds `existing_systems`). · risk keywords: programa de
gestión, TPV, "lo tiene la gestoría".

*Anti-pattern (M4):* "O sea, que su proceso es un desastre, ¿no?" —
judgment, kills candor.

## M5 — Future flows & capabilities

**flows.main** · seeds: "El cliente entra en la web: ¿qué debería poder
hacer?" · "Guíeme por su caso ideal, de principio a fin." · "¿Qué pasa
después, en su lado del mostrador?" · sufficient when: the main flow has
trigger, user action, and business-side outcome. · risk keywords: pagar,
cuenta de usuario, "que se apunte la gente".

**flows.exceptions** · seeds: "¿Y cuando alguien cancela o no aparece?" ·
"¿Qué pasa cuando dos piden lo mismo a la vez?" · "¿Cuál es el caso raro que
más rabia da?" · sufficient when: main exceptions have a current or desired
handling each.

**content.needs** · seeds: "¿Qué tendría que ver la gente en la web —
páginas, fotos, textos?" · "¿Qué tienen ya y qué habría que crear?" ·
"¿Quién puede preparar eso, y para cuándo?" · sufficient when: content
inventory seeded with owners (R2-18 duty). · risk keywords: "lo va tocando
mi sobrino", traducciones, fotos profesionales.

*Anti-pattern (M5):* "¿Quiere un formulario con desplegable de fechas?" —
solutioning during elicitation.

## M6 — Business rules

**rules.policies** · seeds: "¿Qué normas de la casa debería respetar la
web?" · "¿Cuándo dicen que no a un cliente?" · "¿Hay precios o condiciones
que cambian según el día/temporada?" · sufficient when: pricing,
availability, and refusal policies are stated with their edge conditions. ·
risk keywords: señal/anticipo, penalización, menores, aforo.

*Anti-pattern (M6):* accepting "lo normal" as a rule — "lo normal" has an
exception the web will hit in week one.

## M7 — Data & integrations

**data.entities** · seeds: "¿Qué necesita apuntar la web de cada
[reserva/pedido/cliente]?" · "¿Qué datos guardan hoy y dónde?" · "¿Algo de
eso habría que traérselo a la web nueva?" · sufficient when: entities,
today's store, and any import wish are recorded (import → DAT candidate). ·
risk keywords: histórico, migrar, exportar, "está todo en el Excel".

**data.sensitivity** · seeds: "¿Qué datos personales manejaría la web?" ·
"¿Algo delicado — salud, menores, pagos?" · "¿Cuánto tiempo los necesita de
verdad?" · sufficient when: personal-data types + sensitivity + retention
expectation recorded. · risk keywords: salud, alergias, menores, DNI,
tarjeta — each is trigger material (`21` §3).

**integrations.systems** · seeds: "¿La web debería hablar con algo que ya
usan?" · "¿Qué pasaría si eso falla un día?" · "¿Quién tiene las claves de
ese sistema?" · sufficient when: each candidate system has purpose,
criticality, and access status. · risk keywords: sincronizar, API, TPV,
contabilidad.

*Anti-pattern (M7):* "¿Necesita GDPR?" — legal jargon as a yes/no.

## M8 — Quality expectations (NFR)

Topics and probes live per category in [[kn-nfr-catalog]] — usage, traffic
peaks, performance, accessibility, security worry, privacy, devices.
Sufficient when: each floor category for the profile has a client reaction
recorded (target, default-to-confirm, or explicit waiver). · risk keywords:
campañas (picos), "no puede caerse", clientes mayores (a11y).

*Anti-pattern (M8):* "¿Qué disponibilidad quiere, 99.9%?" — numbers before
consequences.

## M9 — Technical-operational context

Checklist and probes in [[kn-technical-operational-context]] (domain,
hosting, email, accounts, ownership, maintainer skill). Sufficient when:
each ownership item has value-or-unknown with an access status, and unknowns
have owners as OQs. · risk keywords: "eso lo llevaba la empresa anterior",
"no sé dónde está el dominio".

*Anti-pattern (M9):* skipping the module because "es una web pequeña" —
ownership surprises don't scale down.

## M10 — Scope, priorities, resources

**scope.mvp** · seeds: "De todo lo hablado, ¿qué tiene que estar sí o sí el
primer día?" · "Si el plazo obligara a elegir la mitad, ¿qué mitad?" · "¿Qué
puede esperar tranquilamente unos meses?" · sufficient when: in/first,
later, and out lists exist and every scope flag from earlier modules got a
disposition. Phase-cutting heuristics: [[kn-scope-and-mvp]].

**resources.budget_deadline** · seeds: "¿Qué presupuesto tienen en mente,
aunque sea una horquilla?" · "¿Hay una fecha que mande?" · "¿Qué pasa si no
llegamos a esa fecha?" · sufficient when: budget and deadline are each a
number, a range, or an explicit "flexible" — silence on either blocks the
interview DoD (`04` §12). · risk keywords: feria/evento (fecha dura),
"cuanto antes".

**maintenance.expectations** · seeds: "Cuando esté entregada, ¿quién la
mantiene?" · "¿Qué esperan de nosotros después — cambios, averías?" · "¿Cada
cuánto cambiará el contenido?" · sufficient when: maintainer + expectation
tier recorded.

*Anti-pattern (M10):* "El presupuesto da igual por ahora" — it never does;
silence here resurfaces at G2 as conflict.

## M11 — Consolidation

Not seed-driven: the queue empties registers — each unconfirmed ASM gets
confirmed/converted/accepted, each open critical CTR gets the neutral
confrontation, each scope flag a disposition. Sufficient when: registers
match the `04` §11 DoR lines.

## M12 — Summary & closure

Per-module playback summaries, explicit confirmation, next steps
(internal review → validation package → client approval). The closure
proposal cites the completion check, and the operator accepts it.

*Anti-pattern (M11–M12):* bundling ten confirmations into one "¿todo bien?"
— confirmations are per module, small enough to actually be checked.

## Deep-dive sections (activate by archetype/trigger)

**Payments (trigger → HIGH-RISK).** Money flow today; who charges and when;
deposits vs full payment; refunds policy and who decides them; invoicing/tax
touchpoints; what happens with a chargeback today. Sufficient when the money
flow has actors, timing, and failure handling.

**Sensitive/health data (trigger).** Which data, why needed, who may see
it, retention, what the client believes their obligations are (recorded as
belief, not legal fact — legal knowledge is research-gated).

**Migration (`migration-or-replatforming`).** What exists, what counts as
"nothing lost" (checkable), cutover tolerance (freeze acceptable?), fallback
expectation, who validates parity.

**CMS editors (`cms-content-site` / client-editable trigger).** Who edits,
how often, their skill reality (observed, not claimed), what breaks today
when someone edits, review-before-publish needs.

**Bookings (`booking-system`).** Capacity model (tables/slots/staff),
confirmation policy (auto vs manual), no-show handling, peak behavior,
double-booking today.

**Content-heavy (`corporate-content-site`).** Page inventory, who writes,
photography plan, languages, legal texts ownership.

## Failure modes

- Seed-reading: three seeds asked verbatim in a row is a form, not a funnel —
  seeds open a topic, the answer drives what's next.
- Sufficiency by mention: a topic touched once is `touched`, not
  `sufficient`; the check lines above are the bar.
- Keyword deafness: a risk keyword appearing in an aside ("bueno, y cobrar
  la señal") and not landing in `risk_triggers[]`.

## Limitations

Model-generated seed set for small Spanish-market web projects; validated
through scenarios, not external research (by design — `17` §K.7). Expect
per-engagement growth; prune duplicates on each addition.

## References

- Plan `04` §4–§5 (topics, sufficiency), `21` §1/§3 (archetypes, triggers),
  `07` §9 (content duty).
- Prototype material (secondary): business-discovery-interviewer blocks 1–5;
  technical-ux-interviewer block 5 (data-model probes, adapted to business
  language) — `planning/history/claude-ai-prototypes/`.

## Related

[[kn-interview-strategies]] · [[kn-elicitation-techniques]] ·
[[kn-nfr-catalog]] (M8) · [[kn-technical-operational-context]] (M9) ·
[[kn-scope-and-mvp]] (M10) · [[kn-process-elicitation]] (M4/M5).
