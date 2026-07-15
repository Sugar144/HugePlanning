---
artifact_id: KIP-02
title: HugePlanning Known Hazards
version: 0.1.0
date: 2026-07-13
status: READY_WITH_NON_BLOCKING_QUESTIONS
artifact_type: kernel-design-input
language: English
---

# HugePlanning Known Hazards

## 1. Purpose

This register identifies known failure mechanisms and unacceptable outcomes that the Kernel Designer must consider.

It is not a final risk assessment. Severity and likelihood are provisional design inputs.

## 2. Hazard scales

### Severity

| Level | Meaning |
|---|---|
| `MINOR` | Local, visible, easily reversible inconvenience |
| `SIGNIFICANT` | Wasted work or multi-artifact impact with practical recovery |
| `SERIOUS` | Stage, architecture, evidence, or major resource impact |
| `CRITICAL` | Security, privacy, money, external systems, authority, or difficult recovery |
| `CONSTITUTIONAL` | Kernel legitimacy, ratification, sovereignty, or fundamental authority |

### Likelihood

- `UNLIKELY`
- `PLAUSIBLE`
- `LIKELY`
- `OBSERVED`
- `UNKNOWN`

### Detectability

| Level | Meaning |
|---|---|
| `D0` | Detected automatically before effect |
| `D1` | Detected by routine validation |
| `D2` | Requires directed semantic, adversarial, or specialist evaluation |
| `D3` | Usually detected after propagation |
| `D4` | May remain hidden until incident, audit, or external information |

Harder-to-detect hazards require stronger controls for equal impact.

## 3. Priority hazards

The first kernel design should pay special attention to:

1. Loss or corruption of intent, requirements, and context.
2. Self-certification, self-amendment, and conflicts of interest.
3. Overplanning, bureaucracy, and unjustified complexity.
4. Token, context, and human-attention consumption.
5. Loss of traceability, evidence, and canonical sources.

## 4. Hazard register

### HZ-001 — Intent or requirement corruption

- **Status:** OBSERVED / PRIORITY
- **Mechanism:** A vague or missing stakeholder decision is silently replaced by a plausible model inference.
- **Affected assets:** Intent, requirements, trust, downstream architecture.
- **Severity:** SERIOUS
- **Likelihood:** LIKELY
- **Detectability:** D2–D3
- **Treatment:** AVOID, DETECT, CONTAIN
- **Required direction:** Preserve distinctions among fact, decision, proposal, assumption, inference, and open question. Block dependent work when a mandatory decision is missing.
- **Owner:** Planner / Interviewer / Human Owner
- **Review trigger:** Any inferred requirement enters a canonical artifact.

### HZ-002 — Self-certification or criterion weakening

- **Status:** PRIORITY
- **Mechanism:** An implementer changes tests, rubrics, thresholds, or acceptance criteria that prevent its own work from passing.
- **Affected assets:** Evaluation independence, legitimacy, quality.
- **Severity:** CONSTITUTIONAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D2
- **Treatment:** AVOID, DETECT
- **Required direction:** Separate implementation, criterion ownership, evaluation, and critical acceptance. Escalate proposed criterion changes.
- **Owner:** Independent Evaluator / Ratification Owner
- **Review trigger:** Repeated validation failure followed by criterion-change proposal.

### HZ-003 — Premature completion

- **Mechanism:** An artifact exists and is declared complete without evidence that it satisfies its purpose.
- **Affected assets:** Roadmap integrity, downstream decisions, trust.
- **Severity:** SERIOUS
- **Likelihood:** OBSERVED
- **Detectability:** D1–D2
- **Treatment:** DETECT, CONTAIN
- **Required direction:** `READY_FOR_EVALUATION` is not `ACCEPTED`; completion must be claim-specific and evidence-based.
- **Owner:** Evaluator / Acceptance authority
- **Review trigger:** Any gate relying only on creator statements or file existence.

### HZ-004 — Overplanning and governance inflation

- **Status:** PRIORITY
- **Mechanism:** Every uncertainty generates a new document, rule, agent, gate, or phase.
- **Affected assets:** Time, tokens, attention, maintainability, delivery.
- **Severity:** SERIOUS
- **Likelihood:** LIKELY
- **Detectability:** D2–D3
- **Treatment:** REDUCE, CONTAIN
- **Required direction:** Keep the kernel minimal; use proportional controls; require complexity to prove value over simpler baselines.
- **Owner:** Planner / Learning Curator / Human Owner
- **Review trigger:** Increasing process cost without measurable risk reduction.

### HZ-005 — Context, usage, or budget exhaustion

- **Status:** PRIORITY
- **Mechanism:** A session exhausts context, provider limits, tokens, time, compute, or iterations before externalizing state.
- **Affected assets:** Continuity, evidence, cost, human attention.
- **Severity:** SIGNIFICANT to SERIOUS
- **Likelihood:** OBSERVED
- **Detectability:** D0–D4 depending on provider visibility
- **Treatment:** REDUCE, DETECT, RECOVER
- **Required direction:** Harness-exposed budgets, conservative internal limits, periodic checkpoints, resumable work.
- **Owner:** Control plane / Operator
- **Review trigger:** Long execution, hidden usage limits, repeated compaction, or nearing internal threshold.

### HZ-006 — Loss of provenance or canonical authority

- **Status:** PRIORITY
- **Mechanism:** Decisions and requirements are duplicated across chats and documents, becoming stale or contradictory.
- **Affected assets:** Traceability, evidence, reproducibility.
- **Severity:** SERIOUS
- **Likelihood:** LIKELY
- **Detectability:** D2–D3
- **Treatment:** AVOID, DETECT, RECOVER
- **Required direction:** One canonical source per concept, stable identifiers, version references, explicit supersession.
- **Owner:** Artifact owner / Learning Curator
- **Review trigger:** Same decision represented differently in multiple authoritative files.

### HZ-007 — Correlated evaluation

- **Mechanism:** Implementer and evaluator share the same context, assumptions, flawed test, model, or narrative.
- **Affected assets:** Evaluation independence, evidence quality.
- **Severity:** SERIOUS
- **Likelihood:** PLAUSIBLE
- **Detectability:** D3–D4
- **Treatment:** REDUCE, DETECT
- **Required direction:** Multidimensional independence: contextual, criterial, executive, technical, cognitive, organizational, and evidential.
- **Owner:** Evaluation architect
- **Review trigger:** Two nominally independent evaluators rely on the same oracle.

### HZ-008 — Autonomy outruns control

- **Mechanism:** Permissions, external effects, or self-hosting expand faster than observability, stopping, validation, or recovery.
- **Affected assets:** Authority, security, repository, external systems.
- **Severity:** CRITICAL to CONSTITUTIONAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D2–D4
- **Treatment:** AVOID, CONTAIN, DETECT
- **Required direction:** Conservative defaults, explicit authorization, least privilege, criticality floors, human gates.
- **Owner:** Human Owner / Enforcement Engineer
- **Review trigger:** New permission, actor, autonomy level, or external system.

### HZ-009 — Local patch hides systemic cause

- **Mechanism:** A code or document defect is repaired while the contract, context, workflow, skill, evaluator, or policy that generated it remains defective.
- **Affected assets:** Reusability, future quality, resources.
- **Severity:** SIGNIFICANT to SERIOUS
- **Likelihood:** OBSERVED
- **Detectability:** D2–D3
- **Treatment:** DETECT, REDUCE
- **Required direction:** Diagnose across causal layers and add regression protection at the correct layer.
- **Owner:** Implementer / Evaluator / Learning Curator
- **Review trigger:** Repeated defect class or repeated human correction.

### HZ-010 — Unjustified agent and workflow proliferation

- **Mechanism:** Repeated tasks immediately become permanent agents, memories, loops, or complex orchestration.
- **Affected assets:** Maintainability, tokens, comprehension, security.
- **Severity:** SIGNIFICANT
- **Likelihood:** LIKELY
- **Detectability:** D1–D2
- **Treatment:** REDUCE
- **Required direction:** Use the promotion ladder from task packet to template, skill, profile, and only then permanent agent if evidence supports it.
- **Owner:** Planner / Learning Curator
- **Review trigger:** New permanent component without comparative evidence.

### HZ-011 — Unsafe automerge

- **Mechanism:** Misclassification, bypassable checks, or weak rollback allows harmful automated merges.
- **Affected assets:** Main branch, releases, evidence, architecture.
- **Severity:** SERIOUS to CRITICAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D1–D3
- **Treatment:** CONTAIN, DETECT, RECOVER
- **Required direction:** Only low-criticality, authorized, reversible changes with non-bypassable checks and post-merge audit.
- **Owner:** Enforcement Engineer / Repository owner
- **Review trigger:** First automerge activation or change to classification rules.

### HZ-012 — Sensitive or external effect without adequate controls

- **Mechanism:** An agent affects accounts, money, publication, production, credentials, personal data, or external services beyond authorization.
- **Affected assets:** Security, privacy, legal standing, money, reputation.
- **Severity:** CRITICAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D1–D4
- **Treatment:** AVOID, CONTAIN, DETECT, RECOVER
- **Required direction:** Isolation, least privilege, explicit authorization, bounded cost, dry run, preconditions, replay protection, observability, rollback or compensation, and human gate.
- **Owner:** Human Owner / Security or domain specialist
- **Review trigger:** First use of each external effect class.

### HZ-013 — Abrupt termination leaves ambiguous state

- **Mechanism:** A session stops before a final checkpoint, leaving written but unvalidated changes.
- **Affected assets:** Repository state, evidence, continuity.
- **Severity:** SIGNIFICANT to SERIOUS
- **Likelihood:** PLAUSIBLE
- **Detectability:** D1
- **Treatment:** DETECT, RECOVER
- **Required direction:** Mark `ABRUPT_TERMINATION`, reconstruct from Git/logs/checkpoint, identify unvalidated changes, resume or revert.
- **Owner:** Control plane / Operator
- **Review trigger:** Missing terminal execution record.

### HZ-014 — Rollback is assumed but ineffective

- **Mechanism:** Reversibility is claimed because Git or backups exist, but restoration is incomplete or untested.
- **Affected assets:** Recovery, availability, trust.
- **Severity:** SERIOUS to CRITICAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D3
- **Treatment:** DETECT, RECOVER
- **Required direction:** Claims of reversibility require evidence; high-risk rollback requires rehearsal or a credible recovery plan. Rollback failure is an incident.
- **Owner:** Implementer / Operator / Enforcement Engineer
- **Review trigger:** R3 or R4 action, failed restore, or first deployment class.

### HZ-015 — Assumptions silently become permanent facts

- **Mechanism:** A provisional assumption remains in canonical artifacts after its expiry or refutation.
- **Affected assets:** Intent, architecture, decisions.
- **Severity:** SERIOUS
- **Likelihood:** LIKELY
- **Detectability:** D2–D3
- **Treatment:** DETECT, RECOVER
- **Required direction:** Explicit assumption states, owners, dependencies, expiry, and refutation impact.
- **Owner:** Assumption owner / Planner
- **Review trigger:** Stage boundary, expiry condition, or contrary evidence.

### HZ-016 — Critical change fragmented into low-risk pieces

- **Mechanism:** A material change is split across commits or tasks so each appears low criticality.
- **Affected assets:** Authority, architecture, validation gates.
- **Severity:** SERIOUS to CONSTITUTIONAL
- **Likelihood:** PLAUSIBLE
- **Detectability:** D2–D3
- **Treatment:** DETECT, CONTAIN
- **Required direction:** Classify the cumulative effect of related changes by shared intent, release, subsystem, and propagation.
- **Owner:** Planner / Evaluator / Release reviewer
- **Review trigger:** Multiple related automerges or coordinated C1 tasks.

### HZ-017 — Provider or model dependence

- **Mechanism:** Constitutional rules assume capabilities or commands available only in one model or tool.
- **Affected assets:** Continuity, maintainability, bargaining power.
- **Severity:** SIGNIFICANT
- **Likelihood:** LIKELY
- **Detectability:** D1–D2
- **Treatment:** REDUCE
- **Required direction:** Keep kernel technology-independent; isolate provider details in adapters and configuration.
- **Owner:** Architect / Kernel Designer
- **Review trigger:** Tool replacement requires normative change.

### HZ-018 — False retrospective compliance

- **Mechanism:** S0a–S1 are described as compliant with controls that did not exist, or missing evidence is reconstructed as if observed.
- **Affected assets:** Historical truth, learning, trust.
- **Severity:** SERIOUS
- **Likelihood:** PLAUSIBLE
- **Detectability:** D2
- **Treatment:** AVOID, DETECT
- **Required direction:** Honest retrospective regularization, explicit evidence gaps, proportional remediation.
- **Owner:** Human Owner / Independent Evaluator
- **Review trigger:** Migration to Kernel v0.1.

## 5. Unacceptable outcomes

### HUMAN_DECISION

HugePlanning has failed materially when it:

- builds the wrong thing convincingly;
- loses requirements or decisions between phases;
- turns inventions into canonical facts;
- declares completion without evidence;
- creates unmaintainable complexity;
- consumes more time, tokens, or attention than its value justifies;
- produces low professional quality despite technical validity;
- allows actors to expand authority or weaken blocking criteria;
- removes human control or comprehension;
- introduces so much bureaucracy that automation ceases to help;
- accumulates contradictory or obsolete agents, skills, documents, or rules;
- repeats failures without learning;
- relies on superficial or correlated evaluation;
- causes loss of code, evidence, credentials, privacy, money, or reputation.

## 6. Treatment model

Available treatments:

- `AVOID`
- `REDUCE`
- `CONTAIN`
- `DETECT`
- `RECOVER`
- `ACCEPT`
- `DEFER`

AI may recommend treatment. Human authority accepts serious, critical, or constitutional residual risk.

## 7. Promotion rule

- Isolated observation: record it.
- Repeated or cross-cutting pattern: consider procedure, test, skill, standard, or policy.
- Single critical incident: consider immediate control or policy.
- Essential, stable, cross-cutting, technology-independent property: consider kernel admission.

Not every hazard becomes a constitutional clause.
