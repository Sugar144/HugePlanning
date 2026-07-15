---
prompt_id: HP-PROMPT-013
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Reconcile the pre-existing Phase 2.3 backlog and test incompatibility before KGR-006 publication
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 7cfc92ed63fbba06232ceba8e4c9b5e10f0258dc
authorization_scope:
  - inspect and minimally reconcile the committed Phase 2.3 backlog/test contract
  - preserve learning and prompt custody
  - validate, selectively commit, and push the bounded correction
  - resume and separately publish the validated KGR-006 preparation
forbidden_actions:
  - include KGR-006 preparation files in the first correction commit
  - change Kernel, Controller, closure-loop, protocol, or constitutional semantics
  - execute GOV-5 or perform GOV-8 work
  - implement controls, policies, GOV-7, or product/runtime functionality
  - open a pull request, merge, release, ratify, or accept risk
exact_text_preserved: true
exact_text_sha256: 4eb2bb5be3945b9198d3f8b631623f4691757adf5a14b437fd657c8c0c573c2f
execution_interrupted: false
execution_resumed: true
result_artifacts:
  - governance/tests/test_phase_2_3_contracts.py
  - governance/learning/records/HP-FAIL-012.yaml
result_commit: null
supersedes: null
---

# Phase 2.3 Backlog/Test Reconciliation Prompt

## Exact executed text

Authorized bounded scope expansion for the current KGR-006 preparation session.

A pre-existing baseline incompatibility has been confirmed between:

- the committed Phase 2.3 test:
  test_phase_2_3_registry_and_backlog_status
- the committed methodology backlog:
  governance/methodology/METHODOLOGY_BACKLOG.md

The current GOV-5 preparation delta did not create this incompatibility, but it blocks required validation and publication.

You are authorized to:

1. Inspect the exact committed test and backlog contract.
2. Determine from repository evidence whether:
   - the backlog prose is missing a required authority/status statement; or
   - the test contains a stale or overly literal expectation.
3. Apply the smallest semantically correct reconciliation.
4. Add or adjust regression coverage so the contract is tested semantically where practical, rather than depending on fragile incidental prose.
5. Preserve the baseline defect, cause, correction, and validation through the existing learning system.
6. Preserve any required correction authority through prompt custody.
7. Run targeted Phase 2.3 backlog/registry tests and the full affected governance suite.
8. Create a first bounded commit containing only:
   - the baseline backlog/test correction;
   - its regression;
   - directly related learning and prompt-custody evidence.
9. Push that bounded correction commit.
10. Resume the existing authorized KGR-006 preparation delta without discarding valid drafts.
11. Re-run all required GOV-5 preparation validations.
12. Build the review bundle.
13. Commit and push the complete KGR-006 preparation delta as a second commit if all validation passes and no further material blocker remains.

Use selective staging so the first commit does not include the existing KGR-006 preparation files.

Do not rewrite historical run artifacts.
Do not change Kernel, Controller, closure-loop, protocol, or constitutional semantics.
Do not execute GOV-5.
Do not perform GOV-8 work.
Do not implement controls, policies, GOV-7, or product/runtime functionality.
Do not open a pull request, merge, release, ratify, or accept risk.

If repository evidence does not determine whether the backlog or the test is authoritative, stop and report the exact ambiguity instead of choosing arbitrarily.

Completion reporting must distinguish the two commits, validation, learning, custody, review bundle, alignment, worktree, and exact next action.
