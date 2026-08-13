# Scenario 01 — clear (baseline coverage and classification)

**Client (fictitious):** "La Vinoteca del Puerto" — wine bar with kitchen,
one location, owner Elena (cooperative, concrete, answers what is asked).
**Archetype:** booking-system (+ corporate content) · **Profile:** standard
· **Language:** es · **Protocol:** import mode (TASK-016; FR-019-AC-03) —
ingest `import-material.md` as `evidence/client-materials/`, run the gap
analysis, then answer the agent's follow-up set from the persona notes below.

**Run:** scratch client (new-client.sh), stage `discovery`, G0 recorded,
profile standard. Ingest → gap analysis → follow-up run. **Pause the
follow-up run mid-M7** (operator: interrupt after a data question) and
resume in a fresh session — FR-015-AC-01 evidence lands here.

## Persona facts (for answering follow-ups; do not volunteer unasked)

- Bookings today: phone + WhatsApp to Elena's personal number; paper book at
  the bar; ~40/week, double on Friday/Saturday; loses 2–3/week unseen.
- Confirmation: Elena or head waiter answer; only Elena says yes to groups
  >8 (BR material). No deposits, no payments online wanted for v1.
- Kitchen closes 23:00; last booking 21:30 (BR). Cancellations by message;
  no-shows ~2/week, annoying but tolerated.
- Web wishes: menu (changes monthly), wine list (changes often — she edits?
  no: "me lo cambiáis vosotros, con una vez al mes vale"), booking request
  form, photos (photographer session already done — files exist), map/hours.
- Data: name + phone per booking; nothing sensitive; keep bookings 1 year.
- Domain: owns lavinotecadelpuerto.es at IONOS, credentials located.
  Hosting: none (old web died). Email: IONOS, works. GBP: hers.
- Success: fewer lost bookings, fewer calls during service.
- Budget: "entre dos y tres mil". Deadline: "antes de la primavera",
  flexible. Maintenance: monthly menu update by the developer.

## Planted material inventory

- BR candidates: last booking 21:30 · groups >8 need Elena · monthly menu.
- DAT candidate: none (no import wanted — paper book stays paper).
- Content items: menu PDF, wine list, photo set (received), legal texts (missing, owner client).
- No risk triggers (no payments, no accounts, normal contact data).
- One mild vague answer for the gate: "que la web se vea elegante".

## What the run must produce

Interview-state with coverage per the STANDARD floor, registers, content
seeds, empty `risk_triggers[]`, completion report; DoD refusal exercise:
operator asks the agent to close right after M8 — it refuses citing the
failing criteria.
