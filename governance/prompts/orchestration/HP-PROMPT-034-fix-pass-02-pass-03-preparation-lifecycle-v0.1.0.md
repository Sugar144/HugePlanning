---
prompt_id: HP-PROMPT-034
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct the PASS-02 validator's conflation of PASS-03 preparation and execution authority.
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 245e157ea64647d8af99b9bb98ae41fac677505f
authorization_scope: [modify minimum PASS-02 validator and directly related tests, validate, commit, push without force]
forbidden_actions: [redesign PASS-03, modify PASS-03 substantive artifacts, execute PASS-03, reopen methodology, alter PASS-02 R1 outputs, relax authority controls generally, add run-specific exceptions, pull request, merge, tag, release, deploy]
exact_text_preserved: true
exact_text_sha256: 4232387fcabab0149a6a197b8befc78409979472eaa6daf6b0cc648f1d343437
execution_interrupted: false
execution_resumed: false
result_artifacts: [governance/tools/validate_pass_02.py, governance/tests/test_pass_02_architecture.py]
result_commit: null
supersedes: null
---

# HP-PROMPT-034 — Fix PASS-02 PASS-03 Preparation Lifecycle

## Exact executed text

Fix the single remaining full-governance-suite regression at HEAD `245e157ea64647d8af99b9bb98ae41fac677505f`.

Observed deterministic result:

* `195 passed`
* `1 failed`
* failing test:
  `governance/tests/test_pass_02_architecture.py::test_canonical_pass_02_candidate_is_valid`
* validator diagnostic:
  `PASS-03 executed or authorized`

Root cause to verify:

The PASS-02 validator appears to treat PASS-03 preparation authority or prepared state as equivalent to PASS-03 execution authority.

Correct only this semantic defect.

Requirements:

1. Distinguish explicitly among:

   * authorized for preparation;
   * prepared pending execution authorization;
   * authorized for execution;
   * executed.

2. PASS-02 validation must remain valid when PASS-03 is only:

   * `AUTHORIZED_FOR_PREPARATION_NOT_EXECUTION`, or
   * `PASS_03_PREPARED_VALIDATED_PENDING_PROJECT_OWNER_EXECUTION_AUTHORIZATION`.

3. PASS-02 validation must still fail if PASS-03 is:

   * authorized for execution without the required lifecycle authority;
   * executed prematurely;
   * represented as accepted or completed without the required decisions.

4. Modify only the minimum validator and directly related tests.

5. Add or update focused tests proving:

   * preparation authority is allowed;
   * prepared-pending-execution-authority is allowed;
   * execution authority is not silently inferred;
   * premature execution still fails.

6. Run:

   * the focused PASS-02 validator tests;
   * `governance/tests/test_pass_02_architecture.py`;
   * relevant PASS-03 lifecycle tests;
   * the complete governance suite;
   * `git diff --check`.

7. Publish only if the complete governance suite finishes with zero failures.

8. Commit and push within this bounded scope.

Do not:

* redesign PASS-03;
* modify PASS-03 substantive artifacts;
* execute PASS-03;
* reopen methodology;
* alter PASS-02 R1 outputs;
* relax authority controls generally;
* add run-specific hard-coded exceptions.

Return:

Root cause:
Files modified:
Focused tests:
Full governance suite:
PASS-02 validator result:
PASS-03 state preserved:
Authority controls preserved:
Commit:
Push:
Remote HEAD:
Worktree:
Status:
Blockers:
Exact next action:
