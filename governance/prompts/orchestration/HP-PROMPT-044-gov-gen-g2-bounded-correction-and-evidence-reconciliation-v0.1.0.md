---
prompt_id: HP-PROMPT-044
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Perform a bounded prospective correction of the already Owner-reviewed and executed GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0 — three internal cross-reference defects, an inaccurate current-state description of the G2 contract's §9 validation-check count, a stale governance/README.md paragraph, and clarification of a program-status field — plus honest reconciliation of the check-8 evidence-custody gap with Owner-review revalidation evidence, without reclassifying any capability, redisposing any gap, redesigning G2, or opening G3.
target_environment: Claude Code
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: bb9c863ea9805f53d06ddabe9040bda2eca34b42
authorization_scope: [read-only inspection needed to identify the repository's existing correction/versioning convention, creation of the minimum prospective correction artifact(s) for GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0, minimum current-state/index/reference reconciliation required by that correction, deterministic validation, one bounded local commit if existing authority permits routine prospective correction mechanics inside this already-authorized Owner-review correction request]
forbidden_actions: [modification of substantive G2 capability classifications, modification of G2 gap dispositions, rewriting historical decision semantics, deletion or replacement of immutable execution evidence, target-architecture selection, kernel ownership decision, repository creation, kernel extraction or migration, G3 definition/opening/authorization/execution, Delegated Operational Authority implementation, Provider-Neutral Governance implementation, modification of AGENTS.md or CLAUDE.md, AET/CWG/SVP modification, push, pull request, merge, tag, release, deployment]
exact_text_preserved: true
exact_text_sha256: bad4abb922cff1387d9a367632bf90babc7e9885fdefebfeb27affbadc44ae0d
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1.manifest.sha256
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-005-g2-correction-r1-v0.1.0.yaml
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/README.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/00-program-charter.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/01-program-status.yaml
  - governance/CURRENT_STATE.md
  - governance/DECISION_LOG.md
  - governance/ARTIFACT_REGISTRY.yaml
  - governance/README.md
result_commit: null
supersedes: null
---

# HP-PROMPT-044 — GOV-GEN G2 Bounded Correction and Owner-Review Evidence Reconciliation

## Exact executed text

You are performing a bounded prospective correction of the already-executed:

`GOV-GEN-G2-CLASSIFICATION-MATRIX-001/0.1.0`

Speak to the Project Owner in Spanish.

Write repository artifacts, governance records, identifiers, commit text, and technical documentation in English.

## Repository identity

Repository:

`Sugar144/HugePlanning`

Expected worktree branch:

`governance/kernel-designer-revision-v0.1`

Expected starting HEAD:

`bb9c863ea9805f53d06ddabe9040bda2eca34b42`

Before any write, verify repository/worktree, branch, HEAD, working-tree cleanliness, applicable `AGENTS.md` files, and the controlling GOV-GEN state.

Stop on identity drift or pre-existing uncommitted changes.

## Purpose

Perform only the minimum prospective correction and evidence reconciliation required before Project Owner disposition of G2.

The substantive G2 classification has already been Owner-reviewed and is not being reopened.

Do not reclassify any capability.

Do not redisposition any G1B gap.

Do not redesign G2.

Do not select target architecture.

Do not authorize or begin G3.

## Preserved historical artifact

Treat the executed and hash-bound:

`governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md`

and its current manifest as historical execution evidence.

Do not silently mutate an immutable/hash-bound executed artifact.

Use the repository's existing prospective/versioned correction mechanism. Inspect the applicable correction conventions before choosing exact correction IDs/paths.

## Confirmed correction findings

The following bounded defects were identified during Project Owner review:

1. The Delegated Operational Authority evaluation refers to unresolved question `§20.5`; the actual corresponding question is `§21.5`.

2. The Provider-Neutral Governance discussion refers to the provider-binding ambiguity as `§20.3`; the corresponding unresolved question is `§21.3`.

3. `GAP-006` refers to the Delegated Operational Authority evaluation as `§11`; the actual evaluation is §19.

4. The current GOV-GEN projection in `governance/README.md` is stale: it still represents G1B as accepted/authorized for future execution even though G1B has executed and been accepted and G2 has executed and is pending Owner disposition.

Do not rewrite historical decision entries merely because they describe an earlier state correctly.

5. `governance/DECISION_LOG.md` states that G2 "passed all 7 self-check items in the G2 contract's §9 plus a verified SHA-256 manifest".

The contract actually defines 8 validation checks; manifest verification is check #7 and applicable repository validators are check #8.

Correct the prospective/current representation without falsifying historical evidence.

6. Historical custody reviewed during Owner review did not expose a durable concrete execution record for G2 validation check #8 beyond statements that it was recorded separately.

Do not fabricate or retrospectively claim an unavailable historical validator execution record.

Project Owner review subsequently revalidated the exact G2 candidate at:

`bb9c863ea9805f53d06ddabe9040bda2eca34b42`

with these results:

```text
python governance/tools/validate_prompts.py
→ {"lineages":38,"prompts":40,"valid":true}
→ exit status 0

python governance/tools/validate_governance_state.py
→ {"diagnostics":[],"result":"VALID"}
→ exit status 0

sha256sum -c governance/audits/GOV-GEN-AUD-001-governance-generalization/G2/GOV-GEN-G2-CLASSIFICATION-MATRIX-001.manifest.sha256
→ GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md: OK
→ exit status 0
```

The working tree was unchanged before and after this validation.

Record this honestly as **Owner-review revalidation evidence**, not as reconstructed evidence of what the original G2 executor ran.

7. `01-program-status.yaml` currently contains:

`worktree_modified_by_this_program: false`

Inspect the field's intended semantics and provenance.

If it means that the original G1A reference worktree/snapshot was not mutated while constructing the deterministic source index, preserve it and clarify the semantics if necessary.

If it purports to mean that GOV-GEN has never modified its active HugePlanning governance worktree, identify it as stale and correct it prospectively.

Do not change the value merely because its wording appears surprising.

## Scope boundaries

Permitted:

* read-only inspection needed to identify the repository's existing correction/versioning convention;
* creation of the minimum prospective correction artifact(s);
* minimum current-state/index/reference reconciliation required by that correction;
* deterministic validation;
* one bounded local commit if existing authority permits routine prospective correction mechanics inside the already-authorized Owner-review correction request.

Forbidden:

* modification of substantive G2 capability classifications;
* modification of G2 gap dispositions;
* rewriting historical decision semantics;
* deletion or replacement of immutable execution evidence;
* target-architecture selection;
* kernel ownership decision;
* repository creation;
* kernel extraction or migration;
* G3 definition, opening, authorization, or execution;
* Delegated Operational Authority implementation;
* Provider-Neutral Governance implementation;
* modification of `AGENTS.md` or `CLAUDE.md`;
* AET, CWG, or SVP modification;
* push;
* pull request;
* merge;
* tag;
* release;
* deployment.

## Validation

At minimum, after correction:

```text
python governance/tools/validate_prompts.py
python governance/tools/validate_governance_state.py
```

Verify all new/affected manifests and any repository validator required by the correction mechanism.

Verify that the working tree contains only the bounded authorized correction surfaces before commit.

## Completion

Report:

1. exact correction identity/version;
2. files changed;
3. how each of the seven findings above was dispositioned;
4. confirmation that no substantive capability classification or gap disposition changed;
5. validation results;
6. commit SHA if a bounded local commit is validly created;
7. remaining Project Owner decision.

The required terminal state is:

`G2_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE`

or an existing semantically equivalent correction status required by repository convention.

Do not accept G2 on behalf of the Project Owner.

Stop after the corrected G2 evidence is ready for Owner disposition.
