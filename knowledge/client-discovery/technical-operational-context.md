---
id: kn-technical-operational-context
title: Technical-operational context — ownership checklist and access reality (M9)
type: catalog
status: provisional
version: 0.1.0
language: en
source_quality: model-generated
reviewed_at: null
review_due: null
consult_when: "running M9 (domain, hosting, accounts, ownership) or recording access_status facts in solution-context"
do_not_use_for: "choosing providers or architecture (S3 decisions)"
used_by: [client-discovery]
related: [kn-question-bank, kn-evidence-and-uncertainty]
supersedes: null
---

# Technical-operational context (M9)

## Purpose

The ownership checklist behind M9: what to establish about domain, hosting,
email, accounts, and the humans who will operate the result — recorded as
facts (`value | unknown` + anchors) in `solution-context.yaml`, never as
decisions. Ownership surprises are a top launch-blocker in small-business
work; this module exists so they surface in week one, not launch week.

## The ownership checklist

Per item: what to establish · the probe (ES) · what `access_status` records.

| Item | Establish | Probe | access_status |
|---|---|---|---|
| domain | registrar, whose account, who pays | "¿dónde está registrado el dominio y a nombre de quién?" | located / credentials-with-client / with-third-party / unknown |
| hosting | current host, whose account, what else lives there | "¿la web actual dónde está alojada? ¿de quién es esa cuenta?" | same enum |
| email | provider, addresses in use, coupling to hosting | "¿el correo del negocio va con el dominio? ¿quién lo montó?" | same |
| analytics/ads | GA/GBP/social accounts, ownership | "¿la ficha de Google del negocio la controla usted?" | same |
| existing systems | per system: purpose, criticality, access owner | "¿quién tiene las claves de [sistema]?" | same |
| payments accounts | (if trigger fired) processor account existence and ownership | "¿tienen ya cuenta en algún banco/pasarela para cobrar online?" | same |

Credentials themselves are never collected or recorded — only that access
exists and where (`03` §6); actual secrets go to the operator's password
manager at the moment they're needed, outside the repo.

**Third-party dependency pattern.** "Eso lo llevaba la empresa anterior /
mi sobrino / la gestoría" is an ownership gap with a person attached: record
the fact, open an OQ with owner = client and a concrete ask ("recuperar el
acceso al registrador"), and a deadline — unresolved access gaps become G3
blockers, better visible now.

## Maintainer-skill assessment

Establish who touches the delivered site and their real skill level —
observed, not claimed:

- "Después de la entrega, ¿quién actualizará contenidos — usted, alguien
  del equipo, nadie?"
- "¿Qué cosas parecidas hace ya sin ayuda?" (edits GBP posts? sends
  newsletters? — calibrates better than self-rating)
- "¿Cada cuánto cambiará algo de verdad?"

Recorded in `operational.*`; this fact later scales admin/CMS decisions and
the maintenance tier — at discovery it's a fact, not a solution.

## Filled example (solution-context fragment)

```yaml
domain:
  provider: { value: "IONOS", source_refs: ["interview:client-discovery-01#turn-61"] }
  ownership: { value: "client (personal account)", source_refs: ["interview:client-discovery-01#turn-61"] }
  access_status: { value: "client will locate credentials", source_refs: ["interview:client-discovery-01#turn-64"] }
operational:
  maintainer_after_delivery: { value: "owner, monthly menu update", source_refs: ["interview:client-discovery-01#turn-70"] }
  technical_skill_level: { value: "low — edits GBP posts unassisted", source_refs: ["interview:client-discovery-01#turn-71"] }
```

(An `unknown` with an OQ beats a guessed value in every one of these slots —
see [[kn-evidence-and-uncertainty]].)

## Failure modes

- Skipping M9 on small projects — precisely where domains live in a departed
  cousin's account.
- Recording aspirations as facts ("sí, tenemos acceso" without anyone having
  located credentials — probe "¿cuándo lo usó por última vez?").
- Collecting credentials into evidence — existence and location only.
- Turning M9 into tech support — locating access is homework (OQ), not an
  in-interview activity.

## Limitations

Model-generated, provisional; checklist reflects ES small-business
realities (IONOS/1&1-class bundles, gestorías, GBP centrality).

## References

- Plan `04` §5 (M9), `06` §7.2 (solution-context shape), `03` §6 (secrets),
  `17` §K.10.

## Related

[[kn-question-bank]] (M9 anti-pattern) · [[kn-evidence-and-uncertainty]]
(unknown-with-OQ discipline).
