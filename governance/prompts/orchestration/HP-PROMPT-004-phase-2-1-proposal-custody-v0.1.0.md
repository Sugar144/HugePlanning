---
prompt_id: HP-PROMPT-004
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Preserve Phase 2.1 methodology proposals before closure
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 5d4b8203f3dae8df8311a8ee0e14aa45587c0edf
authorization_scope:
  - add HP-MPROP-003 and HP-MPROP-004 to the methodology backlog
  - reconcile the artifact registry if required by convention
  - update the Phase 2.1 implementation report
  - regenerate the bounded Phase 2.1 review bundle
  - strict YAML and front-matter validation
forbidden_actions:
  - Controller code, test, dependency, or CI modification
  - modification of HP-PROMPT-003
  - functional test-suite execution
  - implementation of either proposal
  - staging
  - commit
  - push
  - pull request
exact_text_preserved: true
exact_text_sha256: fa82a5082f7d828af5cda30f384ea667a9b33d1a1bb0a9ec230e124c73382ed3
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/methodology/METHODOLOGY_BACKLOG.md
  - governance/ARTIFACT_REGISTRY.yaml
  - governance/reviews/phase-2-1-controller-testing-hardening/implementation-report-v0.1.0.md
  - Phase 2.1 regenerated bounded review bundle
result_commit: null
supersedes: null
---

# Phase 2.1 Proposal Custody Prompt

## Exact executed text

Before closing Phase 2.1, preserve the two material proposals discovered during this implementation session.

Add to `governance/methodology/METHODOLOGY_BACKLOG.md`:

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

State that both proposals require separate future implementation authorization.

Register them in `governance/ARTIFACT_REGISTRY.yaml` if required by the current convention.

Update the Phase 2.1 implementation report and regenerate the review bundle.

Do not modify Controller code, tests, dependencies, CI, or prompt HP-PROMPT-003. Do not rerun functional suites. Run only strict YAML/front-matter validation and `git diff --check`.

Return the updated changed-file count and regenerated report/bundle hashes.
