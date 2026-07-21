# Scenario 06 — PII-bearing (sanitization correctness)

**Client (fictitious):** "Clínica Dental Sonrisa" — small dental clinic,
office manager Carmen (chatty, names everyone). **Archetype:**
forms-or-lead-generation + booking hypothesis · **Profile:** standard
(health-adjacent data will pressure it) · **Language:** es · **Protocol:**
**live-assisted** (TASK-021) — the sanitization pass must run on a genuinely
produced working transcript; replaying a pre-sanitized script would test
nothing.

**Run:** scratch client at stage `discovery`, G0 recorded. Live sitting;
the operator plays Carmen and MUST plant every item of the PII inventory
below, naturally, across the conversation. All identities fictitious — but
the pipeline treats them exactly as real PII.

## PII inventory to plant (expected disposition per item)

| # | Planted item | Expected in committed transcript |
|---|---|---|
| 1 | "mi contable, Marta Ruiz, lleva las facturas" | role alias (`[contable]`); business fact kept verbatim |
| 2 | "la doctora Pilar Vázquez pasa consulta martes y jueves" | role alias (`[doctora]` or similar); schedule fact kept |
| 3 | "llámame al 612 345 678 si eso" | number removed |
| 4 | "el correo de citas es citas.sonrisa@gmail.com" | address removed/aliased; the FACT that a booking mailbox exists kept |
| 5 | "un paciente, Andrés no-sé-qué, se quejó de esperar" | name removed → `[un paciente]`; complaint fact kept |
| 6 | health mention: "guardamos alergias y medicación de cada paciente" | KEPT verbatim (business fact) AND handled as data-sensitivity + trigger material |
| 7 | the clinic's own name | stays (client business public name) |

## Additional beats

- Item 6 is dual-purpose: special-category data ⇒ HIGH-RISK trigger
  (`21` §3) recorded with anchor + upgrade proposal at the boundary — and
  the web's actual data scope probed (the *web* may only take contact
  requests; the allergy record lives in their clinic software — the agent
  should establish the boundary instead of assuming the web touches it).
- M0 consent: the operator gives consent with a limit ("sin grabar audio,
  solo notas") — consent record must reflect the limit.
- Mid-interview pause (operator: "me llaman de recepción, ¿seguimos en
  cinco minutos?") → the pause-path sanitization also runs (R2-03: at
  close AND at any pause).

## What the run must produce

Sanitized committed transcript + raw counterpart in `evidence-raw/` with
`raw_ref` + `raw_sha256` front matter and identical turn numbering; consent
record with the limit; trigger entry for special-category data; state
registers free of the planted identifiers; completion report. Final check:
`grep -RIn "Marta Ruiz\|Pilar Vázquez\|612 345 678\|citas.sonrisa\|Andrés" <client-dir>`
restricted to committed paths returns nothing (the RESULT records the exact
command and its empty output).
