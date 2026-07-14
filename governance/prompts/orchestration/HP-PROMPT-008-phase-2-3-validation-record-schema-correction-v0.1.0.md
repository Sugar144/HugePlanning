---
prompt_id: HP-PROMPT-008
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct the validation-record schema defect and resume Phase 2.3
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 74c5ea76c5b2f6ae2fe51ea683fed55b0b5cf759
authorization_scope:
  - correct governance-validation-record.schema.json according to its existing intended contract
  - add positive and negative regression tests for validation-record tool identity
  - preserve HP-FAIL-006 and resume affected Phase 2.3 validation and documentation
  - conditionally stage, commit, and push the complete authorized Phase 2.3 delta
forbidden_actions:
  - Controller, loop, protocol, KGR-005, or Kernel semantic changes
  - real Controller transition
  - KGR-005 execution
  - pull request, merge, release, or risk acceptance
exact_text_preserved: true
exact_text_sha256: c76d2d43996e34f2d932bd411756b435f75ee29bf3545d2c0c6344a0d48d8ca1
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/schemas/governance-validation-record.schema.json
  - governance/tests/test_phase_2_3_contracts.py
  - governance/learning/records/HP-FAIL-006.yaml
  - governance/reviews/phase-2-3-formal-run-preparation/implementation-report-v0.1.0.md
result_commit: null
supersedes: null
---

# Phase 2.3 Validation Record Schema Correction Prompt

## Exact executed text

Authorized scope expansion for the current Phase 2.3 execution:

Fix the material contract defect in:

```text
governance/schemas/governance-validation-record.schema.json
```

The schema currently requires `tool.name` and `tool.version` while also prohibiting them.

You are authorized to:

* correct the schema according to the existing intended contract;
* add a minimal regression test proving that one valid `GOV-VAL-*` record validates;
* add a negative test proving unexpected properties still fail;
* run only affected schema, validation-record, learning, prompt-custody, and `git diff --check` validations;
* preserve the defect in the learning system;
* resume and complete Phase 2.3 after the fix passes;
* commit and push the complete authorized Phase 2.3 delta if all validations pass and no further material scope drift appears.

Do not change Controller semantics, loop/protocol semantics, KGR-005 artifacts, Kernel content, or apply any real Controller transition.

Do not execute KGR-005.

If the intended schema meaning cannot be determined unambiguously from repository evidence, stop and report the exact ambiguity instead of inventing semantics.
