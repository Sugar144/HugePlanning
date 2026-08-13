---
prompt_id: HP-PROMPT-036
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct the missing executable PASS-03 independent-adversarial-review package without conducting the review.
authority: PROJECT_OWNER_EXPLICIT_BOUNDED_REVIEW_PACKAGE_CORRECTION_AND_PUBLICATION
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 51b0134353b8670ce8c1b99f2b8c537c6b70829c
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
authorization_scope: [prepare the minimum PASS-03 adversarial-review execution package, preserve failed attempt as operational evidence, update dependent registry and audit state, validate, stage, commit, push without force]
forbidden_actions: [execute adversarial review, modify PASS-03 substantive outputs or execution contract, create PASS-03 R2, accept PASS-03, execute or authorize PASS-04, select tools, implement learning pipeline, activate GOV-7, amend Kernel, resolve OD-006, accept risk, pull request, merge, tag, release, deploy]
exact_text_preserved: true
exact_text_sha256: 91a828764d47e72f2ac568e1bb9dff0244e4a7aaa10a043e82921bdfc61d93ee
execution_interrupted: false
execution_resumed: false
result_artifacts: [governance/audits/GOV-AUD-001-gov7-enablement/review-executions/GOV-AUD-001-P03-AR-001, governance/tools/validate_pass_03_review_preparation.py, governance/tests/test_pass_03_adversarial_review_preparation.py]
result_commit: null
supersedes: null
---

## Exact executed text

# GOV-AUD-001 PASS-03 — Adversarial Review Execution Package Correction

Project Owner authorization: correct only the preparation defect in the valid immutable review-input package `GOV-AUD-P03-REVIEW-PACKAGE-001` for reviewed run `GOV-AUD-001-P03-R1`. Repository `Sugar144/HugePlanning`, branch `governance/kernel-designer-revision-v0.1`, expected local and remote HEAD `51b0134353b8670ce8c1b99f2b8c537c6b70829c`.

Before modification, verify repository identity, branch, aligned clean local and remote HEAD, immutable PASS-03 run and status `EXECUTED_VALIDATED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_AND_PROJECT_OWNER_DISPOSITION`, package identity and aggregate SHA-256 `d93c98535e38d952582b59e460d17ac62db8fea3ebfed794383d384a0b9f43fe`, no review execution or consumption, PASS-04 planned/unauthorized/unexecuted, GOV-7 inactive, OD-006 unresolved, and Kernel unchanged. Stop without modification on a material mismatch.

The accepted defect is absence of an instantiated and custodied PASS-03 adversarial-review prompt, review execution/output contract, canonical review identity and publication rules, PASS-03 result semantics and transitions, and a verifiable reviewer-independence basis. Preserve the failed attempt as operational evidence, not an executed adversarial review.

Prepare only the minimum complete package: review contract; instantiated review prompt; review input manifest referencing immutable package; identity and independence requirements; canonical output specification; PASS-03-specific results; validation plan; custody/publication rules; and direct registry/audit-state updates. Resolve identifiers from registries. Do not execute review, modify PASS-03 outputs, redesign PASS-03 or methodology, create R2, accept PASS-03, authorize/execute PASS-04, select tools, implement a learning system, activate GOV-7, amend Kernel, resolve OD-006, accept risk, or create a governance layer.

Require fresh-session observable independence disclosure, prohibited self-certification, explicit unavailable markers, genuine attacks with target/method/counterexample/evidence/result/impact, and exactly one result: `PASS_03_CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION`, `PASS_03_R2_REQUIRED`, or `PASS_03_REVIEW_INVALID_OR_INCOMPLETE`. Invalid/incomplete review must not consume the opportunity or advance PASS-03.

Validate package identity, prompt custody/hash, immutable evidence package, manifest, independence contract, attack structure, results, transitions, authority boundaries, output specification, registry/checksums, audit scaffold, state and `git diff --check`; add focused positive/negative tests. Run the full governance suite because shared lifecycle/scaffold/state validators change. Do not run runtime tests.

When all validation passes, stage only bounded artifacts, inspect staged diff, commit conventionally, push to `origin/governance/kernel-designer-revision-v0.1`, verify alignment and leave worktree/staging clean. The resulting package status is `PASS_03_ADVERSARIAL_REVIEW_EXECUTION_PACKAGE_PREPARED_AND_VALIDATED`; PASS-03 itself remains pending independent review and disposition. Next action is separate Project Owner authorization of one review using the prepared contract and prompt; do not execute PASS-04.
