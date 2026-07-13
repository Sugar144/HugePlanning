---
artifact_id: KD-04
project: HugePlanning
version: 0.1.0-designer
status: OPEN_NONBLOCKING_ITEMS
stage: KD-D4
language: English
date: 2026-07-13
blocks_adversarial_review: false
---

# HugePlanning Designer Open Questions

## 1. Design closure

The constitutional clause-set question (`OQ-001`) and the first lower-layer allocation question (`OQ-002`) were resolved at Designer level by `01-kernel-admission-analysis.md`, `02-kernel-v0.1-draft.md`, and `05-lower-layer-routing.md`.

No unresolved item requires an owner decision before independent adversarial review. The items below remain intentionally open because answering them requires enforcement design, repository evidence, operational calibration, domain context, or later adoption evidence.

## 2. Unresolved register

| ID | Question | Classification | Owner | Why unresolved | Blocking effect | Required evidence | Next trigger |
|---|---|---|---|---|---|---|---|
| OQ-003 | What exact branch protection, CI, classification, rollback, and audit controls are sufficient before low-criticality automerge is enabled? | PRE-OPERATIONAL / ENFORCEMENT | Enforcement Engineer / Repository owner | The Designer defines constitutional bounds, not repository mechanisms, and no enforcement capability inventory has been performed. | Does not block adversarial review or ratification; blocks automerge activation and any claim that automerge is enforceable. | Repository protection inventory, bypass analysis, rollback capability, and pilot results. | Before automerge activation. |
| OQ-004 | Which structural, deterministic, semantic, adversarial, specialist, and human evaluations are mandatory for each action family and criticality level? | POLICY-LEVEL / EVALUATION | Evaluation architect | K-003, K-005, and K-006 establish independence, evidence, and proportionality, but exact evaluation depth requires calibration. | Does not block adversarial review; blocks a complete evaluation policy and relevant operational gates. | Clause-to-claim map, cost model, defect history, and scenario coverage. | Minimum evaluation-policy derivation. |
| OQ-005 | Which S0a–S1 artifacts are conformant, require review, migration, temporary exemption, or are incompatible with Kernel v0.1? | PRE-STAGE / REPOSITORY AUDIT | Human Owner / Independent Evaluator | Historical repository state and actual evidence were deliberately not inspected by the Designer. | Does not block adversarial review or ratification; blocks governed S2 adoption to the extent S2 depends on unresolved S1 inheritance. | Repository inventory, reconstructed historical contracts, actual tests, and evaluation results. | Before the S2 governed-start gate. |
| OQ-006 | Does remaining S1 behavioral and adversarial evidence support acceptance, qualified acceptance, revision, or redesign? | PRE-STAGE / EVALUATION | Human Owner / Independent Evaluator | S1 behavioral testing remains incomplete and cannot be inferred constitutionally. | Blocks S1 acceptance and any S2 dependency that assumes S1 acceptance; does not block Kernel review. | Executed behavioral scenarios, findings, limitations, and retrospective. | S1 regularization. |
| OQ-007 | Which internal thresholds, checkpoint cadence, and provider signals minimize lost work without excessive overhead? | RESEARCH / PRE-OPERATIONAL | Control-plane designer | K-006 and K-007 define the property, but exact budgets and signals are runtime- and provider-dependent. | Does not block adversarial review or ratification; blocks calibrated operational claims. Conservative defaults may support a bounded pilot if explicitly treated as provisional. | Execution logs, observable provider/runtime signals, interruption data, and cost measurements. | Pilot executions or repeated exhaustion events. |
| OQ-008 | What evidence is sufficient to promote a task pattern to template, skill, profile, or permanent agent? | POLICY-LEVEL / RESEARCH | Learning Curator / Planner | K-006 prohibits unjustified complexity, but promotion thresholds require comparative operational evidence. | Does not block review, ratification, enforcement, or initial operation. | Comparative cost, defect rate, quality, continuity, token use, and human correction. | Repeated task class or specialization proposal. |
| OQ-009 | Which credentials, approvals, dry runs, sandboxing, rollback, and incident controls apply to each future external-effect class? | PRE-STAGE / ENFORCEMENT / DOMAIN | Enforcement Engineer / Domain specialist | K-001, K-002, K-006, and K-007 define the constitutional boundary; concrete controls depend on the service, data, environment, and reversibility. | Blocks first use of each unresolved external-effect class; does not block general adversarial review. | Concrete effect class, service capabilities, data sensitivity, failure modes, and recovery options. | Before first use of each effect class. |
| OQ-010 | What legal, privacy, retention, and client-consent obligations apply when real client or personal data is introduced? | PRE-STAGE / RESEARCH / DOMAIN | Human Owner / Legal or privacy specialist | Jurisdiction, data categories, contracts, and deployment model are not yet fixed. | Blocks processing real client, personal, confidential, or regulated data without an applicable determination. | Jurisdiction, data inventory, client terms, retention needs, and deployment model. | Before processing real client or personal data. |
| OQ-011 | What concrete fixtures, expected outputs, rubrics, and independence methods implement the CORE, TARGETED, and DEEP catalog? | PRE-OPERATIONAL / EVALUATION | Evaluation architect | The scenario catalog is a design fixture and has not been operationalized or executed. | Does not block Designer handoff; blocks executable scenario gates and contributes to the operational-readiness gate. | Final proposed clauses, enforcement map, test fixtures, rubrics, and independence design. | Before CORE-suite execution. |
| OQ-012 | Which bounded end-to-end workflow is the smallest credible pilot for declaring Kernel v0.1 operational? | PRE-OPERATIONAL / ADOPTION | Human Owner / Planner | Operational declaration requires ratification, minimum enforcement, and a concrete governed workflow; none is selected by constitutional design. | Does not block adversarial review or ratification; blocks `OPERATIONAL` declaration. | Ratified Kernel, minimum controls, S2 contract candidate, cost/risk analysis, and pilot evidence. | After ratification and minimum enforcement. |
| OQ-013 | Which noncritical release and acceptance decisions should later be delegated, to whom, and under what evidence? | DEFERRED / WATCH | Human Owner | The intake deliberately starts conservatively and delegation should follow observed workload and control effectiveness. | No current blocking effect. | Stable operation, review bottlenecks, defect rates, and delegation audit evidence. | When human review becomes a demonstrated bottleneck. |
| OQ-014 | What interfaces and adapters are required for practical model/provider substitution? | DEFERRED / RESEARCH / ARCHITECTURE | Architect | Technology independence is constitutional, but concrete substitution design depends on actual provider mix and failure modes. | Does not block review, ratification, or single-provider pilot operation; may block a later portability claim. | Second-provider requirements, capability gaps, dependency incidents, and adapter experiments. | Second provider integration or material dependency issue. |

## 3. Evidence gaps retained

The following evidence gaps remain nonblocking for adversarial review:

- Repository state and canonical artifact inventory were not reverified.
- S1 behavioral evidence is incomplete.
- Provider usage observability is unknown.
- Enforcement capabilities have not been inventoried.
- Kernel scenarios have not been executed.

They MUST NOT be represented as resolved by the Designer package.

## 4. Current status

```text
No constitutional owner decision is pending.
No unresolved item blocks independent adversarial review.
Operational and adoption claims remain unavailable.
```
