---
artifact_id: KIP-06
title: HugePlanning Open Questions and Assumptions
version: 0.1.0
date: 2026-07-13
status: READY_WITH_NON_BLOCKING_QUESTIONS
artifact_type: kernel-design-input
language: English
---

# HugePlanning Open Questions and Assumptions

## 1. Handoff assessment

### HUMAN_DECISION

The intake package is:

```text
READY_WITH_NON_BLOCKING_QUESTIONS
```

There are **no known BLOCKING questions** for beginning kernel design.

The remaining questions belong to kernel design, policy design, enforcement engineering, research, legacy regularization, or future stages.

## 2. Question classifications

- `BLOCKING`: must be resolved before kernel design or ratification can proceed correctly.
- `PRE-OPERATIONAL`: must be resolved before Kernel v0.1 is declared operational.
- `PRE-STAGE`: must be resolved before a named stage.
- `RESEARCH`: requires investigation or experiment.
- `POLICY-LEVEL`: belongs below the kernel.
- `DEFERRED`: intentionally postponed until relevant context exists.
- `WATCH`: monitored for change without immediate decision.
- `CLOSED`: resolved or no longer applicable.

## 3. Open-question register

### OQ-001 — Final constitutional clause set

- **Classification:** KERNEL-DESIGN
- **Owner:** Kernel Designer
- **Question:** Which candidate property families pass the admission test, and how can they be expressed with the smallest coherent clause set?
- **Evidence needed:** Hazard coverage, overlap analysis, enforceability direction, cost-benefit.
- **Review trigger:** Kernel design pass.
- **Blocking scope:** Ratification, not design start.

### OQ-002 — Exact lower-layer allocation

- **Classification:** POLICY-LEVEL
- **Owner:** Kernel Designer and Enforcement Engineer
- **Question:** Which rules belong in policy, standard, procedure, contract, configuration, or enforcement rather than the kernel?
- **Evidence needed:** Proposed clause and control mapping.
- **Review trigger:** After first kernel draft.

### OQ-003 — Minimum enforcement before automerge

- **Classification:** PRE-OPERATIONAL
- **Owner:** Enforcement Engineer / Repository owner
- **Question:** What exact branch protection, CI, classification, rollback, and audit controls are sufficient before low-criticality automerge is enabled?
- **Evidence needed:** Repository capability inventory and pilot results.
- **Review trigger:** Before automerge activation.

### OQ-004 — Detailed evaluation map by criticality

- **Classification:** POLICY-LEVEL
- **Owner:** Evaluation architect
- **Question:** Which structural, deterministic, semantic, adversarial, specialist, and human evaluations are mandatory for each action family and criticality level?
- **Evidence needed:** Kernel clauses, cost model, scenario coverage.
- **Review trigger:** Minimum policy derivation.

### OQ-005 — S0a–S1 retrospective evidence

- **Classification:** PRE-STAGE
- **Owner:** Human Owner / Independent Evaluator
- **Question:** Which S0a–S1 artifacts are conformant, require review, require migration, are temporarily exempt, or are incompatible with Kernel v0.1?
- **Evidence needed:** Repository inventory, actual historical contracts, test and evaluation results.
- **Review trigger:** Before S2 adoption gate.
- **Blocking scope:** S2 governed start.

### OQ-006 — S1 behavioral acceptance

- **Classification:** PRE-STAGE
- **Owner:** Human Owner / Independent Evaluator
- **Question:** Do the remaining manual behavioral scenarios and adversarial review support accepting S1, accepting with limitations, revising, or redesigning it?
- **Evidence needed:** Executed scenarios, findings, retrospective.
- **Review trigger:** S1 regularization.
- **Blocking scope:** S1 acceptance and S2 inheritance.

### OQ-007 — Context and budget calibration

- **Classification:** RESEARCH + PRE-OPERATIONAL
- **Owner:** Control-plane designer
- **Question:** Which internal thresholds, checkpoint cadence, and provider signals minimize lost work without excessive overhead?
- **Evidence needed:** Execution logs and provider/runtime observability.
- **Review trigger:** Pilot executions and repeated exhaustion events.

### OQ-008 — Specialization promotion thresholds

- **Classification:** POLICY-LEVEL + RESEARCH
- **Owner:** Learning Curator / Planner
- **Question:** What evidence is sufficient to promote a task pattern to template, skill, specialized profile, or permanent agent?
- **Evidence needed:** Comparative cost, defect rate, human correction, and quality data.
- **Review trigger:** Repeated task class or specialization proposal.

### OQ-009 — Exact external-action controls

- **Classification:** PRE-STAGE
- **Owner:** Enforcement Engineer / Domain specialist
- **Question:** Which credentials, approvals, dry runs, sandboxing, rollback, and incident controls apply to each future external effect class?
- **Evidence needed:** Concrete service, data, environment, and legal context.
- **Review trigger:** Before first use of each effect class.

### OQ-010 — Legal and privacy obligations

- **Classification:** PRE-STAGE + RESEARCH
- **Owner:** Human Owner / Legal or privacy specialist
- **Question:** What legal, privacy, retention, and client-consent obligations apply when real client or personal data is introduced?
- **Evidence needed:** Jurisdiction, data categories, client contracts, deployment model.
- **Review trigger:** Before processing real client or personal data.

### OQ-011 — Reference fixtures and rubrics

- **Classification:** PRE-OPERATIONAL
- **Owner:** Evaluation architect
- **Question:** What concrete fixtures, expected outputs, rubrics, and independence methods implement the CORE, TARGETED, and DEEP catalog?
- **Evidence needed:** Kernel draft and enforcement mapping.
- **Review trigger:** Before Core-suite execution.

### OQ-012 — Operational pilot definition

- **Classification:** PRE-OPERATIONAL
- **Owner:** Human Owner / Planner
- **Question:** Which bounded end-to-end workflow is the smallest credible pilot for declaring Kernel v0.1 operational?
- **Evidence needed:** Kernel controls, S2 contract candidate, cost and risk analysis.
- **Review trigger:** After ratification and minimum enforcement.

### OQ-013 — Future delegation of acceptance

- **Classification:** DEFERRED / WATCH
- **Owner:** Human Owner
- **Question:** Which noncritical release and acceptance decisions should later be delegated, to whom, and under what evidence?
- **Evidence needed:** Stable operation and workload data.
- **Review trigger:** Human review becomes a demonstrated bottleneck.

### OQ-014 — Provider and tool substitution strategy

- **Classification:** DEFERRED / RESEARCH
- **Owner:** Architect
- **Question:** What interfaces and adapters are required for practical model/provider substitution?
- **Evidence needed:** Actual provider mix and failure modes.
- **Review trigger:** Second provider integration or material dependency issue.

## 4. Assumption model

Material assumptions use these states:

- `PROPOSED`
- `ACTIVE`
- `VALIDATED`
- `REFUTED`
- `EXPIRED`
- `SUPERSEDED`

An assumption must include rationale, evidence, uncertainty, dependencies, owner, expiry, refutation impact, and validation plan.

## 5. Active assumptions

### AS-001 — Current owner concentration

- **State:** ACTIVE
- **Statement:** The project owner currently combines Project Owner, Human Operator, and Ratification Owner functions.
- **Evidence:** Direct interview statement.
- **Uncertainty:** Low.
- **Dependencies:** Initial authority model.
- **Owner:** Human Owner.
- **Expiry:** Explicit delegation or organizational change.
- **If false:** Authority and acceptance ownership must be revised.

### AS-002 — Stage status

- **State:** ACTIVE
- **Statement:** S0a and S0b are complete; S1 is implemented and versioned but not accepted; S2 is next.
- **Evidence:** Direct interview statement.
- **Uncertainty:** Medium until repository and evidence are inspected.
- **Dependencies:** Legacy regularization and S2 gate.
- **Owner:** Human Owner / Repository reviewer.
- **Expiry:** Repository audit or new stage decision.
- **If false:** Update adoption plan and artifact statuses.

### AS-003 — Initial tool direction

- **State:** ACTIVE
- **Statement:** Claude Code may be used initially where useful, while the architecture remains provider-independent.
- **Evidence:** Human decision.
- **Uncertainty:** Low for initial direction, high for long-term provider mix.
- **Dependencies:** Adapter and configuration design.
- **Owner:** Architect.
- **Expiry:** Tool strategy change.
- **If false:** Replace adapters without changing constitutional properties.

### AS-004 — First product domain

- **State:** ACTIVE
- **Statement:** Freelancer Project v1 is focused on web-development projects.
- **Evidence:** Human decision.
- **Uncertainty:** Low.
- **Dependencies:** Scope and non-goals.
- **Owner:** Human Owner.
- **Expiry:** Formal expansion to other software domains.
- **If false:** Reassess scope, hazards, and reference scenarios.

### AS-005 — Solo-maintainability constraint

- **State:** ACTIVE
- **Statement:** The system must remain understandable and maintainable by a solo owner unless future evidence supports a different operating model.
- **Evidence:** Project context and explicit concern about bureaucracy and complexity.
- **Uncertainty:** Low for v1.
- **Dependencies:** Kernel minimality, process cost, specialization.
- **Owner:** Human Owner.
- **Expiry:** Team or organizational model changes.
- **If false:** Reassess role separation and operational procedures.

## 6. Evidence gaps

### EG-001 — Repository state not reverified during intake

- Current branch, HEAD, working tree, and exact canonical files must be checked before repository changes.

### EG-002 — S1 behavioral evidence incomplete

- Manual behavioral tests, independent adversarial findings, and the retrospective are not yet available.

### EG-003 — Provider usage observability unknown

- Exact visibility into remaining subscription or provider quotas depends on the runtime and provider.

### EG-004 — Enforcement capability inventory absent

- Existing branch protection, CI, permission, secret-management, and rollback mechanisms have not yet been mapped.

### EG-005 — No executed kernel scenarios

- The scenario catalog has been defined but not executed, as expected at intake time.

## 7. Intake readiness conclusion

The open questions above do not require another discovery interview before kernel design.

They must remain visible and be routed to the correct downstream function rather than being answered speculatively.
