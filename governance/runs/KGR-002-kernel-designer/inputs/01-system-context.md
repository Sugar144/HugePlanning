---
artifact_id: KIP-01
title: HugePlanning System Context
version: 0.1.0
date: 2026-07-13
status: READY_WITH_NON_BLOCKING_QUESTIONS
artifact_type: kernel-design-input
language: English
---

# HugePlanning System Context

## 1. Current project state

### FACT

- Repository: `Sugar144/HugePlanning`.
- Owner-identified active production branch during intake: `feat/s1-discovery-interviewer`.
- S0a and S0b are considered completed.
- S1 is implemented and versioned but not accepted because manual behavioral testing remains.
- S2 is expected to follow S1 and focus on the technical interviewer/specification capability.
- Existing repository material includes runtime elements, agents, skills, schemas, validators, tests, reports, prompts, workflows, and architecture.
- Existing documentation may contain outdated summaries; repository artifacts must be checked by version and canonical status before use.

### EVIDENCE_GAP

The intake did not independently re-verify the current branch, HEAD, working tree, or every historical artifact. These facts must be rechecked before repository-changing work.

## 2. Reference lifecycle

### HUMAN_DECISION

HugePlanning uses the following complete reference lifecycle, with lighter routes for low-criticality work:

```text
need or problem
→ capability
→ hypothesis
→ research when needed
→ alternatives
→ decision
→ stage or increment contract
→ implementation
→ validation or experiment
→ acceptance or human review
→ release
→ learning and roadmap update
```

Inputs may include:

- vague ideas;
- detected defects;
- requested capabilities;
- research findings;
- technology or regulatory changes;
- self-evolution proposals;
- periodic reviews.

Inputs must be classified before execution.

## 3. Completion and state

### HUMAN_DECISION

An agent's statement that work is finished has no acceptance authority.

The normal distinction is:

```text
work produced
→ READY_FOR_EVALUATION
→ validation result
→ acceptance decision
```

Legitimate states include:

- `PLANNED`
- `AUTHORIZED`
- `IN_PROGRESS`
- `PAUSED`
- `BLOCKED`
- `READY_FOR_EVALUATION`
- `PASS`
- `FAIL`
- `INCONCLUSIVE`
- `ACCEPTED`
- `ACCEPTED_WITH_LIMITATIONS`
- `FAILED`
- `ABRUPT_TERMINATION`
- `SUPERSEDED`

Stages, tasks, decisions, evaluations, and releases may use related but distinct state models.

## 4. Canonical information model

### HUMAN_DECISION

- Each concept has one canonical source.
- Summaries and views may link to the canonical source but must not silently duplicate authority.
- Conversations are supporting evidence, not the sole durable project memory.
- Decisions, assumptions, evidence, hazards, defects, and state must be externalized into versioned artifacts.
- Facts, human decisions, proposals, assumptions, inferences, open questions, and evidence gaps must remain distinguishable.

## 5. Actor and function model

### HUMAN_DECISION

The initial system recognizes these abstract functions:

| Function | Primary responsibility |
|---|---|
| Human Project Owner / Ratification Owner | Purpose, constitutional authority, critical risk acceptance, ratification |
| Human Operator | Operate tools and authorize bounded execution |
| Kernel Intake Interviewer | Produce the structured input package |
| Kernel Designer | Propose constitutional properties and structure |
| Kernel Adversary | Search for loopholes, contradictions, bypasses, and perverse incentives |
| Enforcement Engineer | Map properties to controls, detection, recovery, and evidence |
| Researcher / Synthesizer | Collect and synthesize evidence |
| Planner / Architect | Translate decisions into bounded stages and contracts |
| Implementer | Execute authorized work in scope |
| Independent Evaluator | Evaluate against criteria not controlled by the implementer |
| Learning Curator | Convert repeated evidence into improvement proposals |
| Deterministic validators | Enforce objective structure and invariants |
| CI / repository protections | Apply non-bypassable execution controls |
| Models, tools, and services | Provide probabilistic reasoning or external effects |
| Freelancer Project | Future proposer and executor of bounded self-improvement |

These are functions, not a requirement to create permanent agents.

## 6. Implementer model

### HUMAN_DECISION

```text
common implementer role
→ specialized profile when justified
→ task-specific execution packet
```

An implementer works under:

- an explicit objective;
- bounded scope;
- authorized inputs and tools;
- allowed paths and effects;
- a criticality classification;
- validation requirements;
- stop conditions;
- a budget;
- an output state.

It may report `ASSIGNED_PROFILE_INSUFFICIENT`, but it cannot grant itself more permissions.

## 7. Specialization ladder

### HUMAN_DECISION

```text
task packet
→ reusable template
→ skill
→ specialized profile
→ permanent agent
```

The order between a skill and a profile may vary.

Signals for specialization include:

- repeated task classes;
- repeated context assembly;
- recurring tool or permission patterns;
- repeated defect classes;
- recurring specialist evaluation;
- excessive token cost;
- repeated human correction;
- continuity or memory needs;
- measurable improvement over a simpler baseline.

A repeated objective check should normally become a deterministic script rather than an agent.

## 8. Learning model

### HUMAN_DECISION

The Learning Curator begins as a role or skill, not a permanent agent.

It may:

- review defects, experiments, retrospectives, and releases;
- detect local and systemic patterns;
- recommend tests, policies, standards, skills, or architectural changes;
- identify affected decisions and artifacts;
- detect obsolete or contradictory learning.

It may not:

- amend the kernel;
- convert one anecdote into a global rule automatically;
- approve its own proposals;
- overwrite source evidence;
- present hypotheses as facts.

## 9. Validation architecture

### HUMAN_DECISION

Validation is layered and proportional:

1. Creator self-check.
2. Structural validation.
3. Deterministic validation.
4. Behavioral or semantic evaluation.
5. Adversarial evaluation when triggered.
6. Specialist evaluation when triggered.
7. Separate acceptance or release decision.

Critical work uses separate executions and, when justified, different contexts, rubrics, methods, models, tools, or permissions.

## 10. Failure analysis

### HUMAN_DECISION

A failure must be analyzed across the generating system:

```text
output or code
→ requirement or contract
→ data or source
→ context packet
→ model or tool
→ agent or skill
→ workflow or loop
→ evaluator
→ operator or environment
→ process
→ governance
```

The correction should target the causal layer. Significant failures should produce:

- defect classification;
- evidence;
- bounded correction cycles;
- regression protection when reasonable;
- explicit acceptance of remaining limitations;
- reusable learning.

## 11. Context and budget model

### HUMAN_DECISION

HugePlanning uses:

- separate sessions or passes;
- progressive disclosure;
- bounded task packets;
- repository-persisted state;
- periodic and event-based checkpoints;
- token, time, cost, compute, tool-call, and iteration budgets;
- `PAUSED` and `BLOCKED` states;
- resumable work.

The model must not be assumed to know hidden provider or subscription quotas. A harness or control plane should expose observable budget signals.

When provider usage is unknown:

- use conservative internal budgets;
- checkpoint periodically;
- avoid starting long work near internal limits;
- never invent a precise remaining percentage.

## 12. Minimum continuation checkpoint

### HUMAN_DECISION

A checkpoint contains:

- task and objective;
- current state;
- decisions already taken;
- artifacts and commits modified;
- validations performed;
- defects and blockers;
- observable budget consumption;
- exact next action;
- context required to resume.

Abrupt termination results in `ABRUPT_TERMINATION`; outputs are not accepted automatically.

## 13. Governance review cadence

### HUMAN_DECISION

Use:

```text
brief stage-close review
+ event-triggered review
+ periodic health review for long stages
```

A deep review is triggered by:

- serious or repeated defects;
- ineffective or bypassed controls;
- new actors or capabilities;
- authority or autonomy changes;
- new external or sensitive actions;
- refuted hypotheses;
- unknown hazards;
- constitutional amendment proposals.

## 14. Learning promotion

### HUMAN_DECISION

```text
isolated observation
→ record only

repeated or cross-cutting pattern
→ procedure, test, skill, standard, or policy candidate

single critical incident
→ immediate control or policy candidate

essential, stable, cross-cutting, technology-independent property
→ kernel candidate
```

Promotion requires evidence, impact analysis, and the correct authority.

## 15. Technology independence

### HUMAN_DECISION

Claude Code may be used initially where useful, but:

- the kernel must not depend on Claude, ChatGPT, one model, or one provider;
- tool-specific behavior belongs in adapters, policies, procedures, or configuration;
- substitution should be possible without constitutional redesign.

## 16. Legacy regularization and S2 adoption

### HUMAN_DECISION

S0a–S1 will be regularized retrospectively and proportionally:

```text
inventory
→ reconstruct actual objectives and contracts
→ identify available evidence
→ execute pending validation
→ review hazards and deviations
→ classify against Kernel v0.1
→ remediate material gaps only
→ issue formal status
```

Evidence must not be fabricated retroactively.

Before S2 begins as the first governed pilot, the project requires a **minimum executable governance package**, not a complete governance platform.
