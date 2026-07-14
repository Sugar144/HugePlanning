---
document_id: GOV-METHODOLOGY-BACKLOG-001
version: 0.1.0
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
  status: OWNER_APPROVED_FOR_FUTURE_PHASE
  target_phase: PHASE_2_2
  scheduled_after: PHASE_2_1
  scheduled_before: REPEATED_FUTURE_GOVERNANCE_RUNS

  first_skill:
    name: formal-governance-run-preparer
    purpose: >
      Prepare, validate, package, and present a formal governance run
      without executing it or crossing human authorization gates.

  candidate_follow_up_skills:
    - governance-result-importer
    - material-prompt-custodian
    - governance-review-packager
    - failure-learning-recorder

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

This proposal does not create or install a skill, authorize Phase 2.2 implementation, execute a governance run, or cross any human authorization gate.

## HP-MPROP-003 — Extract deterministic review-bundle generation

```yaml
proposal:
  id: HP-MPROP-003
  title: Extract deterministic review-bundle generation
  status: OWNER_APPROVED_FOR_FUTURE_PHASE
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

## HP-MPROP-004 — Agent session supervision and workflow mining

```yaml
proposal:
  id: HP-MPROP-004
  title: Agent session supervision and workflow mining
  status: OWNER_APPROVED_FOR_FUTURE_PHASE
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

Both proposals require separate future implementation authorization. They do not create the proposed tool or skills, grant publication authority, authorize repository modification, or treat observable session traces as validated truth.
