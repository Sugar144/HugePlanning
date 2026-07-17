---
prompt_id: HP-PROMPT-039
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct only the missing startup-evidence bindings for the canonical PASS-03 adversarial review package.
authority: PROJECT_OWNER_EXPLICIT_BOUNDED_STARTUP_EVIDENCE_CORRECTION_AND_CONDITIONAL_PUBLICATION
target_environment: Codex
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 8eef4bac2074230d803aa4fcd7573273b3da55f9
authorization_scope: [bind applicable root/project instructions, create one prospective Owner review-execution authorization, bind direct dependent package surfaces, add focused startup validation, preserve both invalid attempts, validate, commit and push only if all tests pass]
forbidden_actions: [execute adversarial review, modify PASS-03 outputs, create R2, authorize PASS-04, change methodology, add governance layer, pull request, merge, tag, release, deploy]
exact_text_preserved: true
exact_text_sha256: 89737eb71ef6b2cf9952bf3ba27762e05c073057e674cb5d40e6c6db00def7f5
execution_interrupted: false
execution_resumed: false
result_artifacts: [governance/audits/GOV-AUD-001-gov7-enablement/review-executions/GOV-AUD-001-P03-AR-001, governance/tools/validate_pass_03_review_preparation.py, governance/tests/test_pass_03_adversarial_review_preparation.py]
result_commit: null
supersedes: null
---

## Exact executed text

# GOV-AUD-001 PASS-03 — Startup Evidence Binding Correction

Correct only the missing startup-evidence bindings for the canonical PASS-03 adversarial review package. Bind applicable root and project instructions by exact path and SHA-256. Create one prospective Project Owner authorization for one pending review execution and bind it to the review contract, canonical review prompt, input manifest, reviewed run and evidence package, and review execution identity. Update only direct registries, hashes and validation evidence. Preserve the two prior invalid review attempts as immutable historical evidence. Add focused startup validation proving missing root bindings and missing Owner authorization fail, the complete package passes, and invalid attempts do not advance PASS-03. Run focused affected tests, the complete governance suite and git diff --check. Commit and push only if all tests pass.

Do not execute the adversarial review, modify PASS-03 outputs, create R2, authorize PASS-04, change methodology or add another governance layer.
