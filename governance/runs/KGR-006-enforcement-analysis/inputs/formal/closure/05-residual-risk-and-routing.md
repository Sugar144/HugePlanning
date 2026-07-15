---
artifact_id: KA-C05
run: KGR-005
protocol: GOV-PROTOCOL-002
status: COMPLETE
language: English
owner_decision_required: false
research_required_for_closure: false
---

# KGR-005 Residual Risk and Routing

## Routing rule

Residual risk is recorded without converting a wording-level closure result into a capability claim. A route identifies future work and its owner; it does not establish that the destination, evidence, mechanism, or authority exists.

## Residual risk register

| ID | Source | Materiality | Affected clauses | Owner | Destination | Blocks closure | Evidence needed | Next trigger |
|---|---|---|---|---|---|---|---|---|
| RR-001 | KA-F-001, KA-S-018 | High downstream consequence | K-001, K-003, K-005 | Human Owner / Evaluation architect | Policy, standard, evaluation, later enforcement analysis | No | Competence/routing model, attributable decision packet, usability evidence | Before any C3/C4 or serious/critical/constitutional risk acceptance |
| RR-002 | KA-F-002, KA-S-009 | High downstream consequence | K-002, K-006, K-007 | Control-plane designer / Enforcement Engineer | Effect taxonomy, contracts, later enforcement analysis | No | Effect inventory, data flows, exposure/cost thresholds, classification tests | Before enabling each governed-effect class |
| RR-003 | KA-F-003, KA-S-002, KA-S-003 | High downstream consequence | K-003, K-004, K-005 | Evaluation architect | Evaluation policy, standards, later enforcement analysis | No | Appointment/control provenance, separation methods, correlation tests, independent evidence paths | Before any critical or materially conflicted gate operates |
| RR-004 | KA-F-004, KA-S-004, KA-S-010 | High downstream consequence | K-004, K-005, K-006 | Artifact owner / Evaluation architect | Claim/gate standards and evaluation | No | Objective-to-gate-to-claim mapping, mandatory dependencies, scope propagation tests | Before gate automation or acceptance |
| RR-005 | KA-F-005, KA-S-012 | High where sensitive data exists | K-004, K-007 | Human Owner / Legal, privacy, or security specialist | Domain research, policy, procedure, later enforcement analysis | No for semantic closure; blocks affected real-data processing | Jurisdiction, data inventory, obligations, retention/deletion basis, least-loss mechanism tests | Before processing sensitive, regulated, confidential, or actively harmful data |
| RR-006 | KA-F-006, KA-S-007, KA-S-008 | High downstream consequence | K-001, K-002, K-006, K-007 | Human Operator / Enforcement Engineer | Exception/emergency standards and controls | No | Cumulative lineage, duration/effect aggregation, renewal tests, disposition rehearsal | Before first exception or emergency mechanism |
| RR-007 | KA-F-007, KA-S-014 | High liveness consequence | K-006, K-007 | Control-plane designer | State standard, procedures, later enforcement analysis | No | Owner/reason/dependency schema, aging signals, review and terminal-disposition tests | Before governed workflow operation |
| RR-008 | KA-F-008, KA-S-017 | High false-status consequence | K-002 through K-007 | Enforcement Engineer / Independent Evaluator | Enforcement analysis and coverage evaluation | No; blocks every ENFORCEABLE declaration | Clause-by-effect prevention/detection/evidence/stop/recovery coverage, justified inapplicability, independent evidence | Only after independently validated/imported closure and separate authorization to open Enforcement Engineering |
| RR-009 | KA-F-009 | Medium integrity consequence | Package-wide | Artifact owner / Independent Evaluator | Parity standard and validation | No | Repeated semantic field comparison after each revision | Before machine-oriented use of any changed representation |
| RR-010 | KA-F-010, KA-S-020 | Medium burden consequence | K-006 | Planner / Learning Curator | Policy and research | No | Sampled governance cost, protective value, simplification experiments | After recurring operation or contested permanent burden |
| RR-011 | KA-F-011, KA-S-018 | Medium legitimacy consequence | K-001, K-003, K-005 | Evaluation architect / Human Owner | Human-decision standard and evaluation | No | Decision-packet content, presentation/usability tests, dissent and scope records | Before first reserved acceptance |
| RR-012 | KA-F-012, KA-S-001 | Medium epistemic consequence | K-004, K-005, K-007 | Artifact owner / Planner | Assumption policy and standard | No | Assumption classes, owners, dependency graph, validity/revalidation triggers | Before an assumption-dependent governed transition |
| RR-013 | KA-F-013, KA-S-019 | Medium classification consequence | K-001, K-006 | Architect / Human constitutional authority | Architecture policy and independent evaluation | No | Borderline examples and authority/autonomy/topology/guarantee impact analysis | Before a disputed material architecture change |
| RR-014 | KA-F-014 | Low implementation consistency | K-005, K-007 | Control-plane designer | State-machine standard | No | Complete state schema and transition tests | Before state-machine implementation |
| RR-015 | KA-F-015, KA-S-013 | Capability-dependent | Interpretation, K-002, K-003, K-004, K-007 | Architect / Enforcement Engineer | Provider research and later enforcement analysis | No; blocks equivalence/enforceability for unsupported effect classes | Provider stop, audit, permission, context, deletion, export, recovery, and isolation capability tests | Before provider substitution or scope expansion |

## Classification summary

- Constitutional wording defects remaining: none identified.
- Owner decisions required for closure: none.
- Closure-critical research required: none.
- Provider capability questions: routed; no capability asserted.
- Policy/control design: routed; no mechanism asserted.
- Enforcement analysis: remains closed and separately authorized.
- Human ratification: remains `NOT_STARTED`.

## Blocking boundary

The residual risks do not block the configured semantic closure criteria because the revised Kernel supplies the required constitutional boundaries and the remaining facts concern downstream classification, domain research, control design, evaluation, or empirical capability. They do block affected operational, enforceability, provider-equivalence, real-data, and acceptance claims until their named evidence exists.

## Exact next trigger

Independent repository import validation and a separately authorized Controller action must occur before this result can affect the durable loop state. Neither step is performed by the Adversary. Enforcement Engineering and ratification remain closed.
