---
prompt_id: HP-PROMPT-032
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Custody existing PASS-02 independent-review evidence and reconcile directly dependent records only.
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: d31f3a015710e831b8d8d2437afcb7afcfc77534
authorization_scope: [custody existing evidence, record documentary debt, validate, commit, push without force]
forbidden_actions: [rerun review, reconstruct prior review, alter PASS-02 R1, modify methodology, execute CHECKPOINT-A, accept PASS-02, prepare PASS-03, activate GOV-7, amend Kernel, resolve OD-006, PR, merge, tag, release, deploy]
exact_text_preserved: true
exact_text_sha256: 47fdb54663c94d1a9f16052c1f6daee3c805aad755c31d023869711b7eb9419e
execution_interrupted: false
execution_resumed: false
result_artifacts: [governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P02-R1/evaluation/GOV-AUD-001-P02-REVIEW-CUSTODY-001.yaml]
result_commit: null
supersedes: null
---

# HP-PROMPT-032 — PASS-02 Independent Review Custody

## Exact executed text

Custody the already completed PASS-02 independent-review evidence and reconcile only directly dependent records. Do not repeat, reinterpret or expand the review, or modify PASS-02 substantive outputs or audit methodology. Locate only existing local evidence; if exact output is unavailable, custody the strongest existing evidence, record non-blocking documentary debt, and do not reconstruct conclusions, findings or reviewer statements. Validate only directly affected custody, prompt, artifact and state records, PASS-02 R1 immutability, changed YAML/Markdown, references and `git diff --check`; then commit and push the bounded valid changes. Do not execute CHECKPOINT-A, accept PASS-02, prepare PASS-03, activate GOV-7, amend the Kernel, resolve OD-006, or open a PR, merge, tag, release or deploy.
