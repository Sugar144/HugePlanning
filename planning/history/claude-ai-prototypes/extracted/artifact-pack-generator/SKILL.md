---
name: artifact-pack-generator
description: Generates an implementation-ready technical artifact pack (README, init, proposal, spec, design, tasks, and optionally validation/rollout Markdown files) from existing discovery outputs — a Functional PRD, Business Handoff YAML, Technical + UX Discovery Summary, technical UX handoff YAML, client/technical notes, or existing documentation. Use when the user has already completed enough discovery and wants it converted into structured implementation documents, e.g. "generate the artifact pack," "create the technical documentation," "turn this PRD into implementation docs," "create SDD-style artifacts," "prepare docs for an AI coding agent," "convert this discovery into build-ready files." Do NOT use this for business discovery from scratch (use business-discovery-interviewer), technical/UX discovery (use technical-ux-interviewer), a documentation quality review with no new artifacts (use documentation-quality-reviewer), or pure scope reduction (use mvp-scope-reducer).
---

# Artifact Pack Generator

## Purpose

Convert discovery outputs that already exist — a Functional PRD, Business Handoff YAML, Technical + UX Discovery Summary, technical UX handoff YAML, client/technical notes, or an existing partial doc set — into an implementation-ready Markdown artifact pack: README, init, proposal, spec, design, tasks, and (when warranted) validation and rollout documents. The primary audience is whoever builds next — a human implementer or an AI coding agent — so documents need to be consistent with each other and traceable, not just individually well-written.

## Why this skill exists

Generating documentation before discovery is actually done produces confident-looking artifacts built on gaps that surface later, usually mid-implementation when they're expensive to fix. And over-documenting a small change wastes as much time as under-documenting a risky one. This skill exists to check readiness honestly first, scale the artifact set to what the project actually needs, and keep the boundary between what's confirmed and what's assumed intact all the way through to the tasks file.

## Baseline handling

Treat whatever discovery material the user provides (PRD, handoff YAML, discovery summary, notes, existing docs) as the baseline. Don't restart business or technical discovery — that's a different skill's job — unless the baseline is genuinely insufficient to proceed, in which case ask a small number of focused questions rather than re-running a full interview.

## First response behavior

1. Check whether the user already provided baseline materials (uploaded, pasted, or referenced).
2. **If present** — summarize briefly what's available, then run the readiness check (below).
3. **If absent** — ask the user to provide one or more of:
   A) Functional PRD
   B) Business Handoff YAML
   C) Technical + UX Discovery Summary
   D) Technical UX Handoff YAML
   E) Client notes
   F) Existing docs
   G) Rough requirements

Don't generate artifacts immediately unless the user explicitly asks for it and the baseline is sufficient. If the user says "generate now" but the baseline is incomplete, briefly explain what's missing and offer: A) Generate with assumptions clearly labeled, B) Ask focused questions first, C) Generate a smaller artifact set.

## Readiness check

Before generating anything, assess whether the baseline covers: project context, business goal, primary users, MVP scope, out of scope, UX/user flow, functional requirements, core data objects, technical direction, integrations, risks, open questions, implementation constraints.

Output it briefly in this shape:

```markdown
# Artifact Generation Readiness

## Available Inputs
- ...

## Missing or Weak Areas
- ...

## Assumptions Required
- ...

## Recommended Artifact Set
- ...

## Can Generate Now?
A) Yes, generate now
B) Yes, with assumptions clearly labeled
C) Ask a few questions first
```

If the user picks (or the check recommends) C, ask only 2–5 focused questions — never a full re-interview.

## Labeling discipline

Throughout every artifact, keep these distinct and never blur them: **Confirmed**, **Assumed**, **Needs client validation**, **Technical recommendation**, **Open question**, **Deferred**, **Risk**. An assumption never silently becomes a confirmed requirement; an open question is never silently treated as resolved; a technical recommendation is never presented as a client decision.

## Scaling the artifact pack

Match the pack to project size rather than always generating everything:

- **Small project / small change** → README.md, 01-proposal.md, 02-spec.md, 03-design.md, 04-tasks.md
- **Medium project** → add 00-init.md and 05-validation.md to the above
- **Major project, risky system, migration, existing-system change, integration-heavy, payment-heavy, compliance-sensitive, or multi-phase project** → add 06-rollout.md on top of the medium set

Full detail on what each artifact must contain is in `references/artifact-contents.md` — load it before generating any artifact, since the specific required sections and formats (requirement/scenario syntax, task ID conventions, etc.) live there rather than being repeated here.

## Consistency rules across the pack

- Every major feature in 02-spec.md should appear in 03-design.md and 04-tasks.md.
- Every task in 04-tasks.md should trace back to a requirement, design decision, risk mitigation, or setup need — no orphan tasks.
- Out-of-scope items stay out of scope across every artifact, not just the proposal.
- Assumptions never appear as confirmed requirements anywhere in the pack.
- Open questions are never silently resolved between artifacts.
- Risks raised in proposal/spec/design should reappear in validation and/or rollout.
- Client validation questions and technical validation questions are grouped separately, not merged.
- If the project touches payments, privacy, authentication, migrations, or integrations, their risks and open questions must be explicitly addressed somewhere in the pack, not left implicit.

## Final output behavior

If the platform supports file generation, create each artifact as a separate Markdown file. If not, output them in chat clearly separated by heading, e.g.:

```
# README.md
...
# 00-init.md
...
# 01-proposal.md
...
```
(continuing through whichever files are in scope for this pack)

Use English for all technical artifacts unless the user explicitly requests another language. Keep business-facing facts faithful to the source material — don't silently improve, expand, or reinterpret what the baseline actually said.

## Must not do

- Invent missing critical information — flag it instead.
- Hide uncertainty anywhere in the pack.
- Generate generic filler content that isn't grounded in the baseline.
- Overproduce documents for a tiny change, or underproduce for a risky/complex one.
- Produce architecture or design unsupported by the actual requirements.
- Treat open questions as resolved.
- Convert assumptions into stated facts.
- Silently add features that were never requested.
- Create implementation tasks that don't trace to the spec/design.
- Restart business or technical interviews when the baseline is actually sufficient — only ask focused follow-ups when it isn't.
