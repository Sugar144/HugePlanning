---
id: kn-glossary
title: Glossary — methodology and project terms (ES/EN)
type: concept
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "a term is disputed, ambiguous between agent and operator, or needs a client-facing Spanish equivalent"
do_not_use_for: "normative definitions of enums or IDs (the conventions rule owns those)"
used_by: [client-discovery, requirements-auditor, doc-generator]
related: [kn-requirements-taxonomy]
supersedes: null
---

# Glossary

## Purpose

One place for terms whose loose use causes drift, with the client-facing
Spanish pairing where one exists. Definitions here are explanatory; where a
term is normatively defined elsewhere, the entry points there.

## Methodology terms

| Term | Meaning here | ES (client-facing) |
|---|---|---|
| evidence | layer-1 source material with resolvable anchors | evidencia / "lo que nos contó" |
| anchor | a `#turn-nnn`-class pointer into evidence | referencia |
| register | a running list inside interview state (CTR/ASM/OQ/flags) | registro |
| coverage | per-topic progress state, not a questionnaire score | cobertura |
| sufficient | enough confirmed material to write requirements without inventing (`04` §4) | suficiente |
| module | an interview phase M0–M12 — a default trajectory, not a script | bloque de la entrevista |
| profile | assurance weight: LITE / STANDARD / HIGH-RISK (`21`) | nivel de proceso |
| archetype | what kind of thing is being built (`21` §1) | tipo de proyecto |
| risk trigger | evidence that forces a profile-upgrade proposal (`21` §3) | señal de riesgo |
| gate | a human decision point G0–G9 with an append-only record | punto de aprobación |
| baseline | the approved content a gate froze; changes go through change control | versión aprobada |
| validation package | the plain-language G2 instrument the client confirms | resumen para su confirmación |
| scope flag | a mid-interview expansion parked for the M10 decision round | tema aparcado |
| parking (technical) | noting a technical topic for the design stage instead of deciding it now | "lo apuntamos para la fase técnica" |
| proposed default | a floor item awaiting the client's explicit confirmation | propuesta nuestra, pendiente de su visto bueno |
| sanitized transcript | committed transcript with identifiers aliased, numbering intact | transcripción anonimizada |

## Project-domain terms (seed — grows per engagement)

| Term | Meaning here | ES |
|---|---|---|
| booking / reservation | a customer's claim on capacity at a time | reserva |
| walk-in | customer without a booking | sin reserva |
| lead | a captured contact with intent | contacto interesado |
| content item (CNT) | a page/asset someone owes, with owner and deadline | contenido pendiente |
| placeholder | temporary stand-in content, only ever by explicit approval | contenido provisional |

## Usage notes

- Client-facing documents use the ES column; repository artifacts use the
  term as defined by the owning plan file (DEC-14: statements in the client's
  language, structure in the methodology's).
- A dispute about what a term means during an interview is itself a signal:
  record the client's usage in the project glossary section rather than
  correcting them mid-flow.

## Failure modes

- Synonym drift: "reserva confirmada" vs "reserva aceptada" treated as two
  states when the business has one — ask, then record one term.
- Translating structure: IDs, statuses, and field names stay untranslated
  everywhere; only human-facing prose localizes.

## Limitations

Seed list, model-generated; grows from every engagement. The project-domain
section is illustrative until real projects feed it.

## References

- Plan `01` §4 (gates), `04` (interview terms), `21` (profiles/archetypes);
  conventions rule (normative enums).

## Related

[[kn-requirements-taxonomy]].
