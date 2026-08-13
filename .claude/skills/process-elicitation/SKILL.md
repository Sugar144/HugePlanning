---
name: process-elicitation
description: Business-process reconstruction for discovery interviews (M4/M5, plan 04 §4–§5) — the trigger/actors/steps/exceptions/outcome frame with explicit exception hunting; a process topic reaches sufficient only when the frame is filled. Invoke when a current or future business process is the topic. Not for UX flow design or screen mapping (S3).
---

# process-elicitation

**Purpose.** Reconstruct how the business actually works (M4) and how it
should work (M5) as five-slot frames complete enough to derive requirements
from the delta — with the exceptions found before they become week-one bugs.

**Trigger.** Any process topic in M4 (current) or M5 (future flows); also
mid-module whenever an answer reveals an undocumented process ("bueno, eso lo
apunto en otra libreta…").

**Preconditions.** `knowledge/client-discovery/process-elicitation.md`
loaded (the frame, prompts, worked example);
`knowledge/shared/elicitation-techniques.md` available for example anchoring.

**Inputs.** The client's process narration; existing coverage for the
process's topics; the archetype's process emphases (e.g. booking-system
activates capacity/confirmation processes).

**Procedure.**
1. Open with the narration ("cuénteme cómo funciona hoy…"), then anchor to a
   concrete recent instance ("míreme el martes pasado, paso a paso") — the
   narration gives the shape, the instance gives the truth.
2. Fill the frame slot by slot, probing only for what the narration left
   empty: **trigger** (all entry channels — ask "¿solo por WhatsApp?"),
   **actors** (roles; hunt the invisible actor: "¿quién más toca esto?"),
   **steps** (unpack tool mentions into the actions around the tool),
   **exceptions** (below), **outcome** (what state the world ends in —
   where is the money, where is the record).
3. Hunt exceptions explicitly with the knowledge file's prompts:
   cancellation, simultaneity, absence of the usual person, the last time it
   went wrong, the infuriating rare case. For each: how it is handled today,
   or record `decision-pending` if it has no handling — the interviewer's
   common sense does not fill that slot.
4. For M5 (future), run the same frame in the desired tense, then read the
   delta against the M4 frame — each difference is candidate requirement or
   business-rule material, anchored to its turns.
5. Capture business rules met along the way (pricing, refusal, timing
   policies) as BR candidates with their edge conditions — rules
   parameterize the process; they are not steps.
6. Mark the process topic `sufficient` only when all five slots hold
   confirmed material and at least the main exceptions have a handling or an
   explicit decision-pending; otherwise `partial` with the missing slots
   noted.
7. Close the topic with a playback of the reconstructed frame in the
   client's words and get the yes/no/correction.

**Outputs.** Frame records in the interview state (per process: the five
slots with anchors), BR candidates, decision-pending items, candidate
requirements from the M4→M5 delta.

**Self-checks.** Every slot filled or explicitly open; every exception has
handling or decision-pending; no step describes a tool without its action;
no solution proposals recorded as steps; frame playback confirmed.

**Failure modes.** Narration stays abstract after two anchoring attempts →
record the frame as `partial`, queue the topic for a follow-up with
materials ("¿me enseñaría la libreta en la próxima llamada?"). The process
owner isn't in the room → record what this client knows, open an OQ owned by
the actual operator of the process.

**Must not:** accept a tool name as a process description; mark a frame
sufficient with an empty exceptions slot; resolve a missing handling by
inventing one; design the future process before the current one is
understood; drift into screen or flow design (that is S3's conversation).
