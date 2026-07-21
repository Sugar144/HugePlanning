---
id: kn-requirements-taxonomy
title: Requirements taxonomy and statement classification
type: concept
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "classifying a client statement, choosing a requirement type, or deciding whether something may be promoted from inference to fact"
do_not_use_for: "elicitation technique (see kn-elicitation-techniques) or NFR target selection (see kn-nfr-catalog)"
used_by: [client-discovery, requirements-auditor, requirements-normalization]
related: [kn-evidence-and-uncertainty, kn-nfr-catalog, kn-glossary]
supersedes: null
---

# Requirements taxonomy and statement classification

## Purpose

The interpretation reference for turning client speech into typed, honest
records: the statement types of `04` §3, the requirement types of `06` §7.1,
the origin (provenance) semantics of R2-10, and the promotion rules between
them.

## Scope

Classification concepts and worked examples. The normative enums live in the
conventions rule and plan `06`; this file explains how to recognize each class
in the wild, not what the closed lists are.

## Statement types — detection cues

| Type | You hear the client… | Cue phrases (ES/EN) |
|---|---|---|
| `confirmed_fact` | stating something checkable about their world, directly | "tenemos", "ahora mismo es así" / "we currently…" |
| `client_preference` | expressing taste or inclination, not necessity | "me gustaría", "preferiría" / "I'd like", "ideally" |
| `business_requirement` (candidate) | naming an outcome the business needs | "necesito que", "tiene que" / "it has to" |
| `constraint` | naming a limit imposed from outside the design | budget figures, dates, "la ley nos obliga", vendor lock |
| `proposed_solution` | prescribing an implementation | product names, "hagámoslo con…", "con un desplegable" |
| `assumption` (agent-made) | — nothing; the interviewer bridged a gap itself | any silent "presumably…" in the interviewer's head |
| `inference` (agent-derived) | — a conclusion derived from other statements | "so they probably have no CRM" |
| `contradiction` | conflicting with an earlier anchored statement | any clash with the registers |
| `open_question` | not answering, or raising something unresolved | "no lo sé", "tendría que mirarlo" / "I'd have to check" |
| `out_of_scope` | asking for something outside the engagement | "y ya de paso…" / "while we're at it…" |

## Requirement types

| Type / prefix | Holds | Recognize by |
|---|---|---|
| functional `FR` | an observable capability or behaviour | a user or the system does something |
| nonfunctional `NFR` | a quality with a measurable target | how well, how fast, how accessible |
| integration `INT` | an obligation toward an external system | another system's name in the obligation itself |
| constraint `CON` | a fixed boundary on the solution space | non-negotiable, externally imposed |
| data `DAT` | data entities, quality, import/export, retention | data survives, moves, or is governed |

Business rules (`BR`) parameterize FRs — a policy like "no bookings under
12 h notice" is a rule an FR consults, not an FR itself. Content obligations
are `CNT` items in the content inventory, not requirements. Migration is a
`category` on FR/DAT/CON, not a type.

## Origin (provenance) semantics — R2-10

| Origin | Meaning | Typical entry status |
|---|---|---|
| `client_evidence` | the client said it; anchor resolves | `draft` |
| `stakeholder_preference` | a named non-deciding stakeholder wants it | `draft`, weight noted |
| `methodology_default` | the method's floor supplied it | `proposed_default` until G2 |
| `legal_or_regulatory` | law or regulation supplies it | `proposed_default` until G2 |
| `technical_derived` | the architect derived it from other needs (S3) | `draft` |

The pairing is the honesty mechanism: a floor NFR the client never mentioned
carries `methodology_default` + `proposed_default`, so the validation package
asks the client about it instead of quietly attributing it to them.

## Promotion rules

- `inference → confirmed_fact` only through an explicit client confirmation
  recorded as a transcript turn.
- `assumption` stays `unconfirmed` until evidence or explicit acceptance;
  surviving assumptions travel into the validation package for sign-off.
- `proposed_solution` decomposes into the underlying need (candidate
  requirement) plus the proposal (preference with its stakeholder and weight).
- `client_preference` becomes a requirement only when the need behind it is
  established; the preference itself stays advisory.
- `out_of_scope` is acknowledged and recorded as a scope flag for the M10
  disposition round — recording it is what keeps it from silently returning.

## Worked classification examples

1. "Mi cuñado dice que lo hagamos con Wix" → `proposed_solution` →
   need: low-maintenance affordable platform (candidate CON) + preference
   attributed to a non-deciding stakeholder, weight low.
2. "Las reservas me tienen que llegar al móvil" → `business_requirement`
   candidate (FR: booking notification to owner's phone); channel
   unspecified → `open_question`.
3. "Casi nadie cancela, eso da igual" → inference risk: recording
   "cancellations out of scope" would launder an inference into scope. The
   honest record is `assumption` (cancellations rare) + an exception probe.
4. "Queremos parecer modernos" → `client_preference`, `precision: low`
   after one concretization attempt (reference sites, examples).
5. "La web tiene que estar antes de la feria del 3 de octubre" →
   `constraint` (deadline) and `confirmed_fact` (the fair's date).
6. "Usamos un Excel para apuntar las reservas" → `confirmed_fact`; the wish
   to import its rows later becomes a `DAT` candidate.
7. "Supongo que querrán pagar online" (said by the interviewer to itself) →
   `assumption`, register it — and note the payments risk keyword it implies.
8. "Sería genial tener también una app en el futuro" → `out_of_scope` scope
   flag, parked for M10 — not silently dropped, not silently adopted.
9. **Anti-example.** Client: "el formulario debe ser sencillo". Recording
   "FR: simple form" fails twice — untestable wording and a preference posing
   as a requirement. The workable record: preference (`precision: low`) plus
   a probe for what "sencillo" protects (completion time? fields count?).

## Failure modes

- Solution laundering: a `proposed_solution` recorded as a requirement.
- Inference laundering: "they said X so Y" recorded as `client_evidence`.
- Preference inflation: taste recorded as necessity (breaks MoSCoW later).
- Type drift: business rules written as FRs, content items as requirements —
  both create duplicate authoring homes downstream.

## Limitations

Model-generated, provisional; the type cues are heuristics tuned for small
Spanish-market web projects. Validated only through the S1 scenario suite so
far.

## References

- Plan `04` §3 (statement classes, worked example R2-25), `06` §7.1 (field
  set), `07` §2 (normalization rules), `19` R2-10 (origin decisions).

## Related

[[kn-evidence-and-uncertainty]] for confidence and anchoring ·
[[kn-nfr-catalog]] for the NFR categories · [[kn-glossary]] for term pairs.
