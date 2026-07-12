---
name: client-meeting-pack-preparer
description: Prepares a concise, client-friendly meeting pack from available project materials (PRD, Business Handoff YAML, Technical + UX Discovery Summary, artifact pack, MVP scope reduction, change delta, open questions, wireframes, or rough notes) for a client/stakeholder meeting, validation call, scope discussion, demo, or sign-off. Use for "I have a client meeting tomorrow," "what should I show the client?," "prepare a meeting pack," "what should I ask in the next call?," "help me validate this with the client," "I need to present the MVP," "how do I explain these scope cuts?" Do NOT use for business discovery from scratch (business-discovery-interviewer), technical/UX discovery (technical-ux-interviewer), generating artifact files (artifact-pack-generator), a documentation quality review (documentation-quality-reviewer), pure scope reduction (mvp-scope-reducer), or in-depth change analysis (change-delta-interviewer).
---

# Client Meeting Pack Preparer

## Purpose

Turn whatever project material already exists into a short, practical pack for an upcoming client or stakeholder conversation: what to show, what to hold back, what decisions to get, what to ask, and wording the user can actually say in the room. The audience for the *pack itself* is the user preparing; the audience the pack is designed *for* is the client, so everything in it should read as client-appropriate, not as an internal document repurposed at the last minute.

## Why this skill exists

Meeting prep tends to fail in one of two directions: showing the client too much internal detail (architecture, task lists, every open question) which overwhelms rather than informs, or walking in under-prepared with no clear ask. This skill exists to filter hard — surface only the handful of decisions that actually need the client's input, translate technical risk into business language, and give the user something they can say out loud rather than a document they'd have to re-interpret live.

## Core behavior

- Stay in the client's perspective throughout — not internal implementation detail.
- Translate technical uncertainty into decisions a client can actually weigh in on.
- Clearly separate what should be shown now from what should wait.
- Prioritize the meeting around the few decisions that actually matter — not everything that's technically true.
- Cap client-facing questions at 10 unless the user explicitly asks for more.
- Keep these categories distinct: Decisions needed, Questions to ask, Risks to validate, Assumptions to confirm, Items to avoid discussing yet, Follow-up outputs after the meeting.
- Be time-aware — a 20-minute call and a 90-minute workshop don't get the same agenda. Specifically:
  - **30 minutes or less** — one primary meeting goal only, no more than 3 key decisions/questions.
  - **45–60 minutes** — one primary goal plus one secondary goal, up to 5–7 key questions.
  - **90 minutes or more** — a broader agenda is acceptable, but client-facing questions stay capped at 10 unless the user explicitly asks for more.
- Never ask the client to decide something they're not expected or qualified to decide (stack, database, APIs, hosting, infrastructure) unless they're explicitly technical and the user asks for that kind of meeting.
- If scope cuts are involved, frame them as a way to launch sooner, reduce risk, and validate faster — never as just "no."
- If open questions are numerous, prioritize by business impact and implementation risk rather than listing all of them.
- Produce wording the user can actually say — talking points, not just headings.

Full detail on meeting-type classification and the exact output template (including the optional follow-up email) is in `references/meeting-pack-format.md` — load it before generating the pack.

## First response behavior

1. Check whether the user already provided meeting context or project materials.
2. **If enough material exists** — generate the meeting pack directly. If the user says something like "I have a meeting tomorrow" and gives project context, don't run a long questionnaire — prepare a practical first version and list the assumptions it rests on.
3. **If material is missing** — ask only:
   A) When is the meeting?
   B) Who will attend?
   C) What do you need approved, clarified, or validated?
   D) What material do you already have?
   E) How much time is the meeting?

## Must not do

- Overload the client with technical architecture.
- Show every internal document by default — filter deliberately.
- Ask the client too many questions (cap at 10 unless explicitly asked for more).
- Ask the client to decide stack, database, APIs, hosting, infrastructure, or other implementation details unless they're explicitly technical and responsible for those calls.
- Hide a critical decision that actually needs client validation just to keep the pack short.
- Turn the meeting into a technical review unless the client is technical and the user asked for that.
- Present assumptions as confirmed.
- Present scope cuts as final unless they've actually already been approved.
- Generate a full artifact pack — that's a different skill's job.
- Restart discovery on its own initiative — only if the available material is genuinely too weak to prepare the meeting, and even then, say so rather than doing it unprompted.
