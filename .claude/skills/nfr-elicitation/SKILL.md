---
name: nfr-elicitation
description: Quality-expectation elicitation for discovery interviews (M8, plan 04 §5) — consequence-framed probes per NFR category, measurable anchors, and profile-floor items entered as labeled proposed defaults (R2-10). Invoke when the interview reaches M8 or a quality expectation surfaces in any module. Not for normalizing NFRs into requirements.yaml (S2) or choosing technical solutions.
---

# nfr-elicitation

**Purpose.** Turn quality expectations into recordable material with
measurable anchors — in the client's language, without jargon, and without
ever letting a methodology floor item impersonate a client statement.

**Trigger.** Module M8; or any module where a quality expectation surfaces
(performance worry, accessibility mention, availability concern, data
sensitivity) — quality material is captured where it lands.

**Preconditions.** `knowledge/shared/nfr-catalog.md` loaded (categories,
probes, target patterns); the project profile known (its floor categories
come from the `21` §5 matrix); coverage state available for M8 topics.

**Inputs.** The current answer; the profile's floor category list; anything
already captured on usage, devices, peaks, or data sensitivity in earlier
modules.

**Procedure.**
1. For each category the profile floors or the archetype activates, probe in
   **consequences**, never dimensions — use the catalog's probe forms ("si la
   web se cae una mañana, ¿qué pasa con su negocio?"), one category at a
   time, skipping any already covered by earlier answers.
2. Quantify from the reaction: offer scale anchors or comparisons from the
   catalog's target pattern ("¿rápida como — la página aparece antes de que
   piense en mirar el móvil?"). Record the agreed anchor as
   metric/target/conditions material with the turn's anchor.
3. When an answer stays qualitative after one concretization attempt, apply
   the vagueness gate: record it as `client_preference` with
   `precision: low` and move on — the ambiguity audit (S2) will force the
   choice between a concretized target and an explicit waiver.
4. For each floor category the client never addressed: record the catalog's
   default as candidate material labeled `origin: methodology_default`,
   destined for `status: proposed_default` — and say so to the client in
   plain terms ("le propondremos un objetivo razonable y usted lo confirma").
   Nothing is silently imposed and nothing silently omitted.
5. On quality answers that reveal risk material (regulated data, genuine
   availability dependence, payment security concern), hand the trigger to
   the control loop's trigger duty — quality topics are a common trigger
   source.
6. Update M8 coverage per topic: `sufficient` means every floor category has
   a recorded reaction — a target, a labeled default, or an explicit waiver
   candidate; not merely "we talked about speed".

**Outputs.** Anchored quality material in the interview state (candidate
NFRs with metric/target/conditions where obtained; labeled default
candidates; preference records with precision flags); trigger entries where
revealed.

**Self-checks.** No question used a technical dimension name the client
didn't introduce; every floor category is dispositioned; every default
candidate carries `methodology_default`, never a client anchor it doesn't
have; every quantitative anchor has a turn reference.

**Failure modes.** Client defers wholesale ("eso lo que usted vea") → record
the delegation as a confirmed fact, enter floors as labeled defaults, and
note that G2 will present them for confirmation. Client gives an
unrealistic target ("que cargue instantáneo") → anchor to a comparison and
record the realistic form plus the stated aspiration as preference.

**Must not:** use jargon (SLA, LCP, WCAG…) in questions; skip a floor
category because the client seems uninterested; record a default as if the
client stated it; loop more than once on the same vague quality statement;
decide compliance questions (legal knowledge is research-gated — record as
OQ/legal flag instead).
