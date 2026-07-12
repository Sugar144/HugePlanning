---
name: adaptive-interview-control
description: The client-discovery interviewer's per-turn control loop (plan 04 §7) — statement classification, coverage updates, next-question selection, module playback, fatigue handling, completion checking. Invoke on every interview turn of a client-discovery session; the agent contract (04 §1) requires it. Not for use outside a discovery interview.
---

# adaptive-interview-control

**Purpose.** Run each interview turn so that coverage, honesty, and rapport
advance together: classify what was said, update state, pick exactly one next
question, and close modules with confirmed playback — per the behavioural
architecture of plan `04` §4–§7.

**Trigger.** Every turn of a `client-discovery` interview, from M0 framing to
the closure proposal. In import mode (`04` §2), the same loop runs over the
ingested material to produce the gap-analysis question set.

**Preconditions.** `interview-state.json` exists for this session (created at
setup); `knowledge/INDEX.md` consulted; question-bank and
interview-strategies sections for the project's profile/archetype loaded;
`project.yaml` read for profile, archetype hypothesis, and language.

**Inputs.** The client's latest answer (or imported material); current
`interview-state.json`; the registers; the sitting budget.

**Procedure (per turn — 04 §7.3).**
1. Hand the answer to `interview-evidence-capture` (transcript append with
   anchor id) before doing anything with its content.
2. Classify every statement in the answer per the taxonomy
   (`knowledge/shared/requirements-taxonomy.md`): exactly one primary type
   each; decompose proposed solutions into need + preference; register
   assumptions and inferences as themselves, not as facts.
3. Update coverage for **every** topic the answer touched (not only the one
   asked about); update registers (CTR/ASM/OQ/scope flags) and, on any risk
   keyword from the question bank, append to `risk_triggers[]` in
   solution-context with the evidence anchor.
4. Detect specials, in priority order: (a) contradiction with anchored
   evidence → register CTR; if severity critical, schedule the neutral
   confrontation within ~2 turns (interrupt); (b) risk keyword on a critical
   trigger (payments, health/minor data, legal deadline) → probe immediately
   and flag the proposed profile upgrade at the next module boundary;
   (c) emotionally significant material → follow it (rapport preserves data
   quality); (d) vague answer → apply the vagueness gate once (example,
   scale anchor, or comparison), then record `precision: low` and move on;
   (e) "no lo sé" → classify the cause and apply the protocol
   (`knowledge/shared/elicitation-techniques.md`).
5. If all topics of the current module are at their target state → module
   close: playback summary (2–4 sentences, client language), obtain explicit
   yes/no/correction (corrections are new evidence turns), state honest
   progress at the boundary ("hemos cubierto X; nos quedan Y") — no fixed
   block-count mechanics — then pick the next module by trajectory and
   energy (`knowledge/client-discovery/interview-strategies.md`).
6. Run the completion check when in or near M11, and every ~15 turns after
   M8; record the result and failing criteria in `completion_check`.
7. Select the next question: pending interrupts first; otherwise best
   candidate by the ordered decision list — critical-topic gaps with low
   confidence, then follow-ups that unlock other topics, then register
   items, then question-bank seeds for the module; prefer thread continuity;
   under fatigue prefer critical topics only; avoid a topic just probed
   twice.
8. If the budget or fatigue threshold is reached, follow the fatigue ladder
   (reduce → options → labeled defaults → propose pause at the module
   boundary with a resume plan, `04` §10). Any default offered under fatigue
   is recorded as ASM / proposed-default material and verbally marked as a
   proposal.
9. Ask **exactly one question**, in the client's language, jargon-free,
   never leading, never multi-part unless trivially paired.
10. Checkpoint: have `interview-evidence-capture` persist state per its
    contract before ending the turn.

**Outputs.** Updated `interview-state.json` (via the capture skill); the
single next question; at module boundaries, the confirmed playback; at
completion, the closure proposal citing the DoD evaluation.

**Self-checks (each turn).** One primary classification per statement; every
new record carries a resolving anchor; coverage touched-topic sweep done; no
question asked while an unregistered critical contradiction is pending; the
turn ends with one question (or a pause/closure proposal), never zero or two.

**Failure modes.** Client refuses a critical topic → record refusal, mark the
topic `blocked`, escalate to the operator. Client answers only in solutions →
keep decomposing; if the underlying need stays inaccessible, escalate.
Context pressure → trust the registers and coverage over conversational
memory (the state file is the compaction). Session crash → resume path per
`interview-evidence-capture`.

**Must not:** ask more than one question per turn; use leading forms ("¿verdad
que…?"); propose implementations during elicitation; convert inference to
fact without a confirming turn; close a module without confirmed playback;
propose interview closure while the DoD (`04` §12) fails; continue under a
revealed trigger without flagging the upgrade proposal; expose block-count
progress mechanics (modules are adaptive, not a numbered form).
