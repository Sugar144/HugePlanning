---
document_id: GOV-METHODOLOGY-BACKLOG-001
version: 0.3.0
status: ACTIVE_NON_AUTHORITATIVE_PROPOSAL_REGISTER
authority: NONE
---

# Methodology Backlog

This is the canonical non-authoritative register for material prospective methodology improvements discovered during orchestration. Proposals are not implemented state. Owner approval for future work is not authorization to modify the repository later; each implementation, including Phase 2.1, requires separate explicit implementation authorization. Repository truth and formal decisions override this backlog. Superseded proposals are marked with their successor and retained, never deleted.

## HP-MPROP-001 — Controller testing hardening with standard frameworks

```yaml
proposal:
  id: HP-MPROP-001
  title: Controller testing hardening with standard frameworks
  status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
  target_phase: PHASE_2_1
  scheduled_after: PHASE_2_COMMITTED_AND_PUSHED
  scheduled_before: KGR_005_EXECUTION

  rationale: >
    The current deterministic Controller suite passes its canonical cases,
    but standard testing frameworks can explore larger input and transition
    spaces without creating a custom testing framework.

  approved_scope:
    - Adopt pytest as the primary Controller test runner.
    - Preserve the twenty explicit transition fixtures as canonical examples.
    - Add Hypothesis property-based tests.
    - Add a Hypothesis RuleBasedStateMachine for generated loop sequences.
    - Keep run-controller-tests.sh only as a thin wrapper.
    - Capture generated-example, sequence, shrinking, seed, and runtime metrics where supported.

  required_properties:
    - Counters never decrease.
    - Invalid and non-completion events never consume counters.
    - A fourth targeted closure is impossible.
    - A third Designer remediation is impossible.
    - The Designer cannot emit CLOSURE_CONFIRMED.
    - Terminal states cannot continue automatically.
    - History replay is deterministic.
    - Blocking-finding signatures are independent of input ordering.

  future_evaluations:
    - Promptfoo for regression and adversarial testing of LLM prompts.
    - TLA+ and TLC for optional formal verification of the loop state model.
    - Schemathesis only if a Controller HTTP API is created.

  explicit_non_goals:
    - No Controller semantic change in Phase 2.1 unless a test exposes a defect.
    - No replacement of the canonical fixtures.
    - No KGR-005 execution as part of test-framework adoption.
    - No custom general-purpose testing framework.
```

Phase 2.1 locally implements the approved pytest and Hypothesis scope pending Project Owner review. This status does not mean accepted, operational, or exhaustive; it does not implement Promptfoo, TLA+, TLC, or Schemathesis, change Controller semantics, authorize KGR-005 execution, or apply a real Controller transition.

## HP-MPROP-002 — Extract reusable governance workflows into versioned skills

```yaml
proposal:
  id: HP-MPROP-002
  title: Extract reusable governance workflows into versioned skills
  status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
  target_phase: PHASE_2_2
  scheduled_after: PHASE_2_1
  scheduled_before: REPEATED_FUTURE_GOVERNANCE_RUNS

  first_skill:
    name: formal-governance-run-preparer
    status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
    purpose: >
      Prepare, validate, package, and present a formal governance run
      without executing it or crossing human authorization gates.

  candidate_follow_up_skills:
    - governance-result-importer
    - material-prompt-custodian
    - governance-review-packager
    - failure-learning-recorder

  phase_2_2_implementation:
    - governance-review-packager
    - agent-session-reviewer

  phase_2_3_implementation:
    - formal-governance-run-preparer
    - KGR-005 preparation validation evidence GOV-VAL-001

  phase_2_4_implementation:
    - governance-result-importer
    - KGR-005 completed-output import validation evidence GOV-VAL-002

  extraction_rule: >
    A skill is justified when a workflow has been executed repeatedly,
    has stable inputs and outputs, contains reusable judgment or sequencing,
    and is not better handled entirely by a deterministic script.

  non_goals:
    - No general autonomous governance agent.
    - No skill may ratify, accept risk, commit, push, or execute a run
      without explicit authorization.
    - Skills must call deterministic scripts for deterministic operations.
```

Phase 2.2 locally implements the reusable-skill extraction pattern with `governance-review-packager` and `agent-session-reviewer` pending review. Phase 2.3 locally implements `formal-governance-run-preparer` and validates KGR-005 preparation custody as `READY_FOR_EXPLICIT_FORMAL_EXECUTION_AUTHORIZATION`. Phase 2.4 implements `governance-result-importer`, validates and imports the exact KGR-005 completed-output package, and applies one authorized Controller transition. `HP-FAIL-006`, `HP-FAIL-007`, and `HP-FAIL-008` preserve validation-schema, result-import, and Controller-custody defects with bounded corrections. These skills and records do not ratify the Kernel, activate Enforcement Engineering, or grant future execution or publication authority.

## HP-MPROP-003 — Extract deterministic review-bundle generation

```yaml
proposal:
  id: HP-MPROP-003
  title: Extract deterministic review-bundle generation
  status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
  priority: HIGH
  evidence:
    - Codex repeatedly generated temporary review-bundle scripts.
    - Phase 2.1 generated `/tmp/build_phase_2_1_bundle.py`.
  proposed_tool: governance/tools/build_review_bundle.py
  proposed_skill: governance-review-packager
  goals:
    - deterministic changed-file inventory
    - unified diff capture
    - configurable validation execution
    - SHA-256 manifest generation
    - safe bounded review transport
    - lower repeated token use
  non_goals:
    - publication authority
    - automatic commit or push
    - hardcoded phase-specific paths
```

Phase 2.2 locally implements the configurable deterministic tool and bounded review-packager skill pending review. The tool generates transport evidence only; it does not stage, commit, push, publish, accept risk, or create governance authority.

## HP-MPROP-004 — Agent session supervision and workflow mining

```yaml
proposal:
  id: HP-MPROP-004
  title: Agent session supervision and workflow mining
  status: IMPLEMENTED_LOCALLY_PENDING_REVIEW
  proposed_skill: agent-session-reviewer
  trigger:
    - material implementation closure
    - formal run closure or interruption
    - material failure or near miss
    - creation of temporary scripts or repeated workflows
  goals:
    - inspect observable session traces
    - identify reusable tools, skills, tests, and controls
    - detect prompt and process defects
    - preserve only material findings
    - avoid manufacturing lessons
  non_goals:
    - access to hidden model reasoning
    - retention of every trivial interaction
    - treating transcripts as validated repository truth
    - automatic acceptance or repository modification
```

Phase 2.2 locally implements the bounded observable-evidence session-review skill pending review. It cannot access hidden reasoning, validate its own findings, manufacture lessons, or modify repository state without authorization.

These local implementations are not accepted or operational. They do not grant publication authority, execute a governance run, apply a Controller transition, alter Kernel or loop semantics, or treat observable session traces as validated truth.

## HP-MPROP-005 — Phase-transition methodology candidates

```yaml
proposal:
  id: HP-MPROP-005
  title: Phase-transition methodology candidates
  status: DOCUMENTED_CANDIDATES_NOT_ADOPTED
  authority: NONE
  source: HP-PROMPT-017/0.1.0
  trigger: Project Owner review of a separately prepared research or design contract
  candidates:
    - id: HP-MCAND-001
      title: Durable Owner Idea Ledger
      boundary: External personal-idea custody only; personal TFG ideas do not become canonical project requirements.
    - id: HP-MCAND-002
      title: Project strategic-idea capture
      boundary: Project methodology proposal only after separate research and Owner review.
    - id: HP-MCAND-003
      title: Governance hypothesis-to-evidence lifecycle
      boundary: Candidate evidence-lifecycle methodology, not an active requirement.
    - id: HP-MCAND-004
      title: Improved Governance Intake Interviewer
      boundary: Candidate future protocol revision, not a change to historical KGR-001.
    - id: HP-MCAND-005
      title: Governance Discovery Core plus Domain Packs
      boundary: Candidate methodology architecture, not a new governance layer.
    - id: HP-MCAND-006
      title: Prompt evaluation and optimization
      boundary: Candidate research; no prompt or model route is adopted here.
    - id: HP-MCAND-007
      title: Runtime distribution boundary
      boundary: Candidate research; no runtime projection or product change is authorized.
    - id: HP-MCAND-008
      title: Third-party documentation
      boundary: Candidate documentation method; no publication obligation is created.
    - id: HP-MCAND-009
      title: Formal-run automation
      boundary: Candidate deterministic tooling; human authority gates may not be automated away.
    - id: HP-MCAND-010
      title: Phase learning-promotion review
      boundary: Candidate phase-transition method; this entry does not execute a promotion review.
  class_distinctions:
    personal_idea: External Owner Idea Ledger only.
    project_methodology_proposal: This non-authoritative backlog after explicit capture.
    learning_record: Evidence-based record under governance/learning only.
    owner_decision: Explicit competent human decision record only.
    active_scope_requirement: Only an already authorized contract requirement; no candidate is one.
  non_goals:
    - No candidate is approved, accepted, implemented, validated, operational, or scheduled.
    - No personal TFG idea is added to canonical project requirements.
    - No new governance layer is created.
```

These candidates are preserved because they were explicitly requested for phase-readiness review. Each requires a separate evidence basis, Owner disposition, and implementation authorization before any repository or operational change.

## HP-MPROP-006 — Formal instruction-conflict policy derivation for future GOV-7

```yaml
proposal:
  id: HP-MPROP-006
  title: Derive a formal instruction-conflict policy, standard and procedure for future GOV-7
  status: DOCUMENTED_CANDIDATE_NOT_ADOPTED
  authority: NONE
  source:
    observed_event: >
      GOV-AUD-001 exposed a conflict between mandatory durable learning capture
      and bounded run write authority.
    learning_record: HP-FAIL-024
    temporary_control: GOV-AUD-001-METHOD-001/0.1.0
  candidate_classification:
    - GOVERNANCE_POLICY_GAP
    - OPERATING_PROTOCOL_GAP
    - AMBIGUOUS_OR_CONFLICTING_AUTHORITY
  future_target: GOV-7_POLICY_STANDARD_AND_PROCEDURE_DERIVATION
  required_questions:
    - Which durable obligations may operate inside a bounded run without expanding substantive authority?
    - Which append-only evidence classes are safe exceptions, and which require a stop and new Owner authority?
    - How are instruction hierarchy, conflict detection, exception custody, review, rollback and Owner burden controlled?
  current_temporary_rule: >
    Durable instructions do not silently expand run authority, and run prompts do
    not silently suppress durable obligations. Append-only learning evidence caused
    by the current run may be preserved only when it changes no authority, accepted
    state, prior evidence, implementation or risk; otherwise stop and request
    Project Owner authority.
  non_goals:
    - This entry is not an adopted policy, standard or procedure.
    - It does not amend the Kernel.
    - It does not activate GOV-7.
    - It does not authorize policy design or implementation beyond this proposal custody.
    - It does not retroactively validate or invalidate PASS-02 R1.
```

The temporary audit prompt rule is an operating containment only. Formal derivation, review, adoption and implementation require separate future Project Owner authority.

## HP-MPROP-007 — Execution Insight Capture and Learning Promotion Pipeline

```yaml
proposal:
  id: HP-MPROP-007
  title: Execution Insight Capture and Learning Promotion Pipeline
  classification: METHODOLOGY_PROPOSAL
  scope: GOV-AUD-001
  status: OWNER_ACCEPTED_FOR_FUTURE_AUDIT_CLARIFICATION
  implementation_status: NOT_STARTED
  incorporation_point: AFTER_CHECKPOINT_A_BEFORE_PASS_03
  target_passes:
    - PASS-03
    - PASS-04
    - PASS-06
    - PASS-07

  future_audit_requirement: >
    The audit will explicitly assess a minimal pipeline from observable execution
    data and explicit model outputs through verified learning, controlled procedural
    promotion, selective retrieval and effectiveness measurement.

  minimal_pipeline:
    - observable execution event
    - visible execution insight
    - hypothesis
    - planned verification
    - confirmed, refuted, partially confirmed or unresolved conclusion
    - learning candidate
    - evidence-aware triage
    - durable destination
    - procedural promotion
    - selective retrieval
    - effectiveness measurement

  pipeline_notation: >
    observable execution event → visible execution insight → hypothesis →
    planned verification → confirmed, refuted, partially confirmed or unresolved conclusion → learning candidate →
    evidence-aware triage → durable destination → procedural promotion → selective retrieval →
    effectiveness measurement

  boundaries:
    - No hidden chain-of-thought collection.
    - Visible model updates, hypotheses and conclusions are distinct from hidden chain-of-thought and may be captured only when observable.
    - Operational telemetry, model inference, verified repository evidence, durable learning, methodology proposals, Owner decisions, and implemented procedural controls remain distinct evidence classes.
    - Repository evidence remains canonical.
    - Traces are non-authoritative.
    - Hypotheses remain distinct from verified conclusions.
    - No silent procedural promotion.
    - No automatic governance or Kernel modification.
    - No automatic risk acceptance.
    - Material learning requires human or independent disposition.
    - Low-value and duplicate learning must be controlled.
    - Effectiveness must include recurrence reduction and retrieval usefulness.
    - Executor self-assertion is not sufficient verification.
    - Operational traces are non-authoritative and repository evidence remains canonical.
    - Define privacy, redaction, retention, rollback, telemetry disablement, and manual-fallback boundaries before any implementation.

  observable_data_design:
    include_when_observable: [run and session identity, prompt ID version and hash, input-package hash, model and reasoning mode, visible model updates, tool calls and results, commands and validations, changed files, retries and correction cycles, Owner interventions, stop reason, artifact inventory, tokens cost and duration]
    unavailable_data_rule: Record explicit unavailable-data markers rather than inferring missing telemetry.

  verification_states: [HYPOTHESIS_PENDING_VERIFICATION, CONFIRMED, REFUTED, PARTIALLY_CONFIRMED, UNRESOLVED]
  verification_rule: Refuted and unresolved items must not become accepted procedural learning.
  candidate_destinations: [operational observation, formal-run evidence, failure or lesson record, methodology proposal, Owner decision candidate, tooling candidate, prompt candidate, skill candidate, validator candidate, regression-test candidate, control candidate, research required, duplicate/link to existing record, discard]
  candidate_extraction_boundary: Candidate extraction cannot decide authority, risk acceptance, ratification, phase transitions, or implementation approval.
  promotion_targets: [repository instructions, prompt contracts, schemas, validators, regression tests, scripts, hooks, skills, routing rules, deterministic queries, model-selection rules, formal-run protocols, adversarial-review attack cases, Owner checklists]
  promotion_states: [captured, implemented, validated, shown effective]
  selective_retrieval_dimensions: [phase or pass, role, component, operation, artifact type, failure class, risk class, authority boundary, validation type, model or execution mode]
  retrieval_rule: Use small justified context packages linked to durable evidence; do not inject all learning records into every run.
  effectiveness_metrics: [recurrence rate, repeated Owner corrections, repeated manual repairs, correction cycles, lessons promoted into controls, promoted controls independently validated, relevant lessons retrieved, irrelevant-context rate, false-learning rate, duplicate-learning rate, added token burden, added Owner burden, failures prevented, candidates discarded as noise]
  effectiveness_rule: Record volume alone is not successful learning.
  tooling_boundary: trace capture ≠ insight extraction ≠ evidence verification ≠ candidate triage ≠ procedural promotion ≠ selective retrieval ≠ effectiveness evaluation
  tooling_options_for_future_comparison: [REPOSITORY_NATIVE_MVP, PILOT_EXTERNAL_FRAMEWORK, HYBRID_REPOSITORY_AND_FRAMEWORK, NO_ACTION, DEFER_PENDING_RUNTIME_CONTROL]
  candidate_technologies: [repository-native JSONL, Codex hooks/events, OpenTelemetry, OpenInference, Phoenix, Langfuse, Braintrust, PromptLayer, Promptfoo, Opik, other evidence-supported alternatives]

  future_allocation:
    PASS-03: telemetry, insight representation, verification, metrics and retrieval requirements.
    PASS-04: repository-native and external tooling comparison.
    PASS-06: synthesis, minimum scope and adoption sequence.
    PASS-07: independent evaluation of usefulness, safety, burden and bureaucracy risk.

  contract_clarification_requirement: >
    Perform a bounded contract clarification after CHECKPOINT-A and before PASS-03
    instantiation. That separately authorized clarification may update the directly
    affected future pass contracts and templates; this proposal does not modify
    PASS-03 or PASS-04 contracts now and does not authorize their execution.

  authority_boundary:
    checkpoint_a_completed: false
    pass_03_or_later_execution_authorized: false
    methodology_implemented: false
    governance_or_kernel_modification_authorized: false
    risk_acceptance_authorized: false
```

This Owner-accepted prospective audit clarification is durable input to a later bounded contract clarification only. It is not started, implemented, validated, operational, adopted as GOV-7 policy, or authority to execute CHECKPOINT-A or any later pass.
