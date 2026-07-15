---
prompt_id: HP-PROMPT-014
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct the property-based Controller model recordable gate and resume KGR-006 preparation
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: c330b729462ee578c02e8b717c1e0076a9b42c2f
authorization_scope:
  - inspect production and model accepted-record semantics
  - correct only the property-based model if production is unaffected
  - add regression coverage and preserve learning
  - selectively commit and push the correction
  - rebuild and separately publish KGR-006 after all validation passes
forbidden_actions:
  - change production Controller semantics
  - include pending KGR-006 preparation files in the correction commit
  - execute GOV-5 or perform GOV-8 work
  - modify Kernel, GOV-4 history, controls, policies, GOV-7, or product/runtime code
  - open a pull request, merge, release, ratify, or accept risk
exact_text_preserved: true
exact_text_sha256: c07c9a089c3ae154a0b3625947801752a1d07f958ca918caa884c855e8aee8cb
execution_interrupted: false
execution_resumed: true
result_artifacts:
  - governance/tests/controller/test_state_machine.py
  - governance/learning/records/HP-FAIL-013.yaml
result_commit: null
supersedes: null
---

# Controller Model Recordable-Gate Correction Prompt

## Exact executed text

Authorized bounded scope expansion for the current KGR-006 preparation session.

A pre-existing property-based test-model defect has been confirmed by Hypothesis in the isolated review-bundle copy.

Observable defect:

- TestControllerModel._calculate() always replaces self.last_record.
- It also does so when the calculated operation has recordable: false.
- A non-recordable attempt after CLOSURE_CONFIRMED therefore replaces the last accepted transition record.
- This causes terminal invariants to inspect an unaccepted attempt whose next_role is Kernel Adversary.

The current KGR-006 preparation delta did not introduce this defect, but the isolated full-suite failure blocks valid bundle publication and the second commit.

You are authorized to:

1. Inspect the property-based Controller model, its invariants, and the production Controller behavior.
2. Confirm that repository contracts distinguish:
   - attempted calculations;
   - recordable accepted transition records;
   - the latest accepted durable record used for replay and terminal invariants.
3. Apply the smallest correct fix to the test model so a result with recordable: false does not replace the latest accepted record used by terminal-state invariants.
4. Preserve any separate attempted-operation state only if required by existing test semantics.
5. Do not change production Controller semantics unless repository evidence proves the production implementation has the same defect; if that occurs, stop and report it as scope expansion instead.
6. Add or adjust regression coverage proving:
   - a non-recordable operation after CLOSURE_CONFIRMED does not replace the accepted terminal record;
   - terminal next_role and terminal-state invariants remain stable;
   - valid recordable transitions still update the accepted last record;
   - repeated or invalid attempts cannot reopen or mutate a terminal state through the model.
7. Preserve the defect, root cause, correction, and validation through the existing learning system.
8. Preserve this correction authority through the next valid prompt-custody record.
9. Run:
   - targeted Controller model and Hypothesis tests;
   - the full governance suite in the worktree;
   - the full governance suite in the isolated bundle copy;
   - all pending GOV-5 contract-preparation validations;
   - prompt-custody validation;
   - learning-system validation;
   - git diff --check;
   - deterministic review-bundle build and validation.
10. Create and push one bounded correction commit containing only:
    - the property-based test-model correction;
    - its regression coverage;
    - directly related learning and prompt-custody evidence.
11. Resume the preserved KGR-006 preparation delta.
12. Rebuild the formal input package and final review bundle from the corrected baseline.
13. Commit and push the complete KGR-006 preparation delta as a separate second commit if all validation passes and no further material blocker remains.
14. Verify local and remote HEAD alignment and a clean worktree.

Use selective staging so the correction commit does not include pending KGR-006 preparation files.

Do not:

- execute GOV-5;
- modify Kernel meaning;
- change Controller production semantics without separate authorization;
- alter GOV-4 history;
- perform GOV-8 work;
- implement controls, policies, GOV-7, or product/runtime functionality;
- open a pull request;
- merge;
- release;
- ratify;
- accept risk.

The obsolete review bundle currently in /tmp must not be reused, reviewed, or published. Build a new bundle only after the corrected isolated suite passes.

If repository evidence does not clearly establish the accepted-record semantics, stop and report the exact ambiguity instead of changing the model heuristically.

Return:

Branch:
Previous HEAD:
Defect location:
Production Controller affected:
Root cause:
Test-model correction:
Regression coverage:
Learning evidence:
Prompt ID/version:
Targeted Hypothesis validation:
Full worktree validation:
Full isolated-copy validation:
Correction commit:
KGR-006 package SHA-256:
KGR-006 preparation commit:
Review bundle:
Push:
Local/remote aligned:
Worktree:
Status:
Exact next action:
