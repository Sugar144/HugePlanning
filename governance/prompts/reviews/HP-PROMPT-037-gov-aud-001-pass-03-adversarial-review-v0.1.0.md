---
prompt_id: HP-PROMPT-037
version: 0.1.0
category: REVIEW
evidence_type: MATERIAL_PROMPT
status: APPROVED_NOT_EXECUTED
purpose: One bounded independent adversarial review of PASS-03 using its immutable evidence package.
authority: PREPARED_REVIEW_CONTRACT_ONLY_REQUIRES_SEPARATE_PROJECT_OWNER_EXECUTION_AUTHORIZATION
target_environment: Codex
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 51b0134353b8670ce8c1b99f2b8c537c6b70829c
repository: Sugar144/HugePlanning
branch: governance/kernel-designer-revision-v0.1
review_id: GOV-AUD-001-P03-AR-001
reviewed_run: GOV-AUD-001-P03-R1
review_contract: GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT/0.1.0
immutable_review_package: GOV-AUD-P03-REVIEW-PACKAGE-001
authorization_scope: [execute one separately-authorized adversarial review only, create one review result only when validly authorized, validate and publish only when separately authorized]
forbidden_actions: [modify PASS-03 source run or package, prepare or execute PASS-03 R2, execute or authorize PASS-04, select tools, implement learning pipeline, activate GOV-7, amend Kernel, resolve OD-006, accept risk, accept PASS-03, pull request, merge, tag, release, deploy]
exact_text_preserved: true
exact_text_sha256: babbf21a06fe6fde08be087bd2985c3e51869756a8835526d2fd20e8f172c9e9
execution_interrupted: false
execution_resumed: false
result_artifacts: [governance/audits/GOV-AUD-001-gov7-enablement/review-executions/GOV-AUD-001-P03-AR-001]
result_commit: null
supersedes: null
---

## Exact executed text

# GOV-AUD-001 PASS-03 — Independent Adversarial Review

Execute only after a separate explicit Project Owner authorization binds this exact prompt and `GOV-AUD-001-PASS-03-ADVERSARIAL-REVIEW-CONTRACT/0.1.0`.

Verify repository `Sugar144/HugePlanning`, branch `governance/kernel-designer-revision-v0.1`, clean worktree and staging, aligned local/remote HEAD, the reviewed run `GOV-AUD-001-P03-R1`, and immutable package `GOV-AUD-P03-REVIEW-PACKAGE-001` at `governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P03-R1/review-package/manifest.yaml` with aggregate SHA-256 `d93c98535e38d952582b59e460d17ac62db8fea3ebfed794383d384a0b9f43fe`. Validate every package member and source-output hash before attack analysis.

Use only the reviewed immutable package, the bound review input manifest, contract, output specification, validation plan, and applicable repository instructions recorded in that manifest. Do not substitute chat memory, hidden chain-of-thought, unrecorded telemetry, PASS-04 materials, or external product claims.

Declare reviewer model and mode when observable; declare whether this is a fresh session, all prior involvement, and every shared prompt, model, session, or authoring dependency. Classify independence exactly as `INDEPENDENT`, `PARTIALLY_INDEPENDENT_WITH_DISCLOSED_LIMITATIONS`, `NOT_INDEPENDENT`, or `UNVERIFIABLE`. Do not claim model identity alone proves independence. If the classification is not permitted by the contract, return `PASS_03_REVIEW_INVALID_OR_INCOMPLETE` without advancing PASS-03.

Attempt to refute the strongest PASS-03 claims. Select relevant dimensions from false learning, unsupported promotion, authority escalation, privacy leak, telemetry overcollection, irrelevant context, stale learning, contradiction, metric gaming, bureaucracy and Owner burden, premature tool selection, vendor lock-in, rollback or deletion failure, unavailable observability, evidence canonicality, and self-validation or circular verification. Record a justified omission for any dimension not attacked.

Each attack must contain `attack_id`, `attack_dimension`, `target_claim_or_assumption`, `attack_method`, `counterexample_or_failure_scenario`, `evidence_examined`, `result`, and `impact`. Reject generic criticism, nominal adversarial claims, restated acceptance criteria, empty methods, unsupported conclusions, and survival conclusions without meaningful attempted refutation.

Separate material findings from non-blocking observations. A material finding must identify affected artifacts, evidence, materiality, impact, disposition, and a bounded R2 scope. Do not prepare or execute R2.

Emit exactly one result:

- `PASS_03_CONFIRMED_SUITABLE_FOR_PROJECT_OWNER_DISPOSITION` only after genuine required attacks, no remaining material finding, and no tool selection, implementation, or authority escalation. It does not accept PASS-03 or authorize PASS-04.
- `PASS_03_R2_REQUIRED` only for material findings affecting the contract-defined integrity, safety, burden, neutrality, or later-pass usability dimensions.
- `PASS_03_REVIEW_INVALID_OR_INCOMPLETE` for integrity, evidence, independence, execution, output, or verification failure. It must not consume the valid review opportunity or advance PASS-03.

Do not modify the reviewed run, the nine PASS-03 outputs, the immutable evidence package, PASS-03 execution prompt or contract. Do not execute or authorize PASS-04, select tools, implement a learning system, activate GOV-7, amend the Kernel, resolve OD-006, accept risk, or accept PASS-03 for the Project Owner.

Return only the YAML artifact specified by `GOV-AUD-001-P03-AR-001-OUTPUT-SPEC-001/0.1.0`, including all required fields and explicit unavailable markers. Validate it using the bound validation plan before any separately authorized publication.
