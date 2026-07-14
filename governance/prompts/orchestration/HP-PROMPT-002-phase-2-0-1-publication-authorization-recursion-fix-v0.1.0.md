---
prompt_id: HP-PROMPT-002
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Bounded Phase 2.0.1 publication-authorization recursion correction
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: dc1927b4891cf72ddcefd2ab4726f22dfbfc4b37
authorization_scope:
  - bounded prompt-custody methodology correction
  - prompt validator and affected tests
  - append-only learning evidence
  - concise implementation and review evidence
  - required registry and current-state reconciliation
forbidden_actions:
  - Controller semantic modification
  - pytest or Hypothesis installation
  - Phase 2.1 start
  - KGR-005 execution
  - Controller transition
  - staging
  - commit
  - push
  - pull request
exact_text_preserved: true
exact_text_sha256: 12533914400215055ad08e37852cf318ed91d6238c2d5abf211cd3705943ade7
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/methodology/project-operating-contract.md
  - governance/prompts/README.md
  - governance/AGENTS.md
  - governance/tools/validate_prompts.py
  - governance/tests/run-prompt-custody-tests.sh
  - governance/learning/records/HP-FAIL-005.yaml
  - governance/reviews/phase-2-0-1-publication-authorization-recursion/implementation-report-v0.1.0.md
result_commit: null
supersedes: null
---

# Phase 2.0.1 Publication-Authorization Recursion Fix Prompt

## Exact executed text

Implement the bounded Phase 2.0.1 publication-authorization recursion fix.

Repository:

```text
/home/sugar/Documents/HugePlanning-governance
```

Required branch:

```text
governance/kernel-designer-revision-v0.1
```

Required HEAD:

```text
dc1927b4891cf72ddcefd2ab4726f22dfbfc4b37
```

The worktree and staging area must be clean.

## Problem

The prompt-custody contract incorrectly classified an atomic Project Owner authorization to commit and push an already reviewed immutable change set as a new material prompt.

That created an infinite recursion:

```text
publication authorization
→ must be preserved before commit
→ preservation changes reviewed scope
→ requires renewed authorization
→ renewed authorization must also be preserved
```

## Required correction

Define a distinct evidence type:

```text
OWNER_PUBLICATION_AUTHORIZATION
```

It is not a material implementation prompt when all of these conditions hold:

* it comes explicitly from the Project Owner;
* it references an already reviewed immutable change set, bundle, inventory, or commit candidate;
* it adds no implementation scope;
* it authorizes only atomic publication actions such as stage, commit, and push;
* it does not authorize PR, merge, release, execution, ratification, risk acceptance, or additional modifications.

Such authorization may be preserved through publication evidence, commit metadata, operational records, or a subsequent append-only record. It must not require a new pre-publication repository file that changes the authorized change set.

## Modify only what is necessary

Expected affected areas:

```text
governance/methodology/project-operating-contract.md
governance/prompts/README.md
governance/AGENTS.md
governance/tools/validate_prompts.py
prompt-custody tests
learning event or record
artifact registry or current state only if required by existing conventions
```

Preserve this material implementation prompt as:

```text
HP-PROMPT-002 / 0.1.0
```

under `governance/prompts/orchestration/`, unless repository identity inspection proves that ID is unavailable.

Record the discovered recursion as append-only learning evidence. Use an event on an existing record only if semantically correct; otherwise create the next failure record. Do not silently force it into `HP-FAIL-004`.

## Validation

Run only affected and proportional checks:

```text
prompt-custody tests
learning tests
strict validation of modified YAML/front matter
git diff --check
```

Do not rerun the Controller suite or the 224 unrelated repository tests unless the affected-file analysis shows a real dependency.

## Boundaries

Do not:

```text
modify Controller semantics
install pytest or Hypothesis
start Phase 2.1
execute KGR-005
apply a Controller transition
stage
commit
push
open a PR
```

Produce a concise implementation report and review evidence sufficient to inspect this small delta. Do not generate an oversized review process.

Return:

```text
Branch:
Base HEAD:
Prompt ID/version:
Files created:
Files modified:
Learning evidence:
Prompt-custody tests:
Learning tests:
Other validation:
Controller files changed:
Worktree:
Staging:
Commit:
Push:
Status:
Exact next action:
```

Finish with:

```text
Status: PHASE_2_0_1_READY_FOR_PROJECT_OWNER_REVIEW
Exact next action: Review the bounded delta, then authorize commit and push.
```
