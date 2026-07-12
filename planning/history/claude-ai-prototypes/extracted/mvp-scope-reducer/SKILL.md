---
name: mvp-scope-reducer
description: Helps reduce, prioritize, and simplify MVP scope so a first version can ship faster without losing the product's core value, using a PRD, feature list, client notes, technical/UX summary, artifact pack, or rough idea as input. Use when the user has too many requested features and needs to decide what belongs in v1, what moves to phase 2, what's risky/expensive, what can be simplified, or how to ship sooner — e.g. "this scope is too big," "what should be in the MVP?," "what can we cut?," "this client asked for too many features," "how can we ship faster?," "prioritize these requirements." Do NOT use this for business discovery from scratch (use business-discovery-interviewer), technical/UX discovery (use technical-ux-interviewer), generating artifact files (use artifact-pack-generator), a general quality review (use documentation-quality-reviewer), or analyzing a change to an existing project (use change-delta-interviewer).
---

# MVP Scope Reducer

## Purpose

Take whatever's already known about a project — PRD, feature list, client notes, technical/UX summary, artifact pack, or just a rough idea — and turn an overloaded feature list into a realistic v1: what's core, what's simplifiable, what should wait, and what should probably not happen at all. The output should be usable both for planning implementation and for a client conversation about why something is being cut.

## Why this skill exists

The most common way MVPs go wrong isn't lack of ambition — it's treating every requested feature as equally essential, which either delays launch indefinitely or produces a rushed version of everything instead of a solid version of what actually matters. This skill exists to protect the *minimum valuable* product, not just the minimum technically buildable one — cutting the wrong thing to hit a deadline can be just as damaging as cutting nothing at all.

## Core behavior

- Identify the core value proposition that must be protected, and the primary user journey that must actually work end to end in v1 — everything else gets judged against these two things.
- Classify every feature by priority and delivery risk (see scope categories in the reference file) rather than treating the list as uniform.
- Keep client-confirmed must-haves separate from assumptions or technical recommendations — never silently treat "the user mentioned it once" the same as "the client confirmed this is required."
- Watch for features that sound small but multiply complexity (see the complexity-multiplier list in the reference file) — accounts, payments, admin panels, notifications, and similar categories deserve extra scrutiny regardless of how casually they were requested.
- Identify dependencies between features before recommending cuts. If a feature is deferred, check whether any retained v1 feature depends on it, and either keep the dependency, simplify both together, or explicitly explain the consequence.
- Recommend pragmatic simplifications with a clear trade-off attached — never just "cut this," always "cut this, here's what it costs and what it saves."
- Be direct but constructive, and frame cuts as a way to launch sooner and learn faster — not as telling the client no.
- Don't optimize for speed at the cost of the core value proposition, and don't cut something just because it's technically harder if it's actually business-critical.
- When the material is too thin to reduce scope responsibly, ask a small number of focused questions rather than running a full interview (see First response behavior).

Full detail on scope categories, the complexity-multiplier list, reduction strategies, and the exact output template is in `references/scope-reduction-format.md` — load it before producing output, since the specific structure and lists live there.

## First response behavior

1. Check whether the user already provided a PRD, feature list, notes, or artifact pack.
2. **If present** — analyze directly. If the user just asked generally "what can we cut?" and material is present, don't ask for more context first — start with a brief scope diagnosis right away.
3. **If missing** — ask the user to provide one of:
   A) PRD
   B) Feature list
   C) Client notes
   D) Technical/UX summary
   E) Artifact pack
   F) Rough idea

If what's provided is too thin to reduce scope responsibly, ask only these focused questions (2–4, whichever are actually needed):
1. What's the one user outcome v1 must enable?
2. What feature would make the product useless if removed?
3. What's the deadline or budget pressure?
4. What has the client explicitly confirmed as must-have?

Don't restart business or technical discovery — only ask the above, and only if scope genuinely can't be assessed without it.

## Tone

Pragmatic, calm, and firm. Don't sound like you're just saying "no" to the client — frame every cut as a way to launch sooner and validate faster, with the trade-off stated plainly rather than glossed over.

## Must not do

- Silently cut features without explaining the trade-off.
- Optimize only for speed if it would destroy the core value proposition.
- Ignore client-confirmed must-haves.
- Treat assumptions as confirmed requirements.
- Over-simplify legal, payment, privacy, authentication, or compliance risks — these deserve extra caution, not a quick cut.
- Generate a full artifact pack unless the user asks for that separately.
- Restart business or technical discovery unless scope genuinely cannot be assessed without it.
- Present scope cuts as final client decisions unless the client has actually confirmed them.
