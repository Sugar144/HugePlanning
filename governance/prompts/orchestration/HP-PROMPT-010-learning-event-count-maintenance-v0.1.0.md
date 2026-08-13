---
prompt_id: HP-PROMPT-010
version: 0.1.0
category: CORRECTION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Correct the stale learning-event count assertion and preserve validated learning evidence
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: a9d891931d902dab7f17d2fadb2d80fc17b9b99a
authorization_scope:
  - locate and correct only the stale learning-event count expectation
  - add or update bounded multiple-event regression coverage
  - preserve the defect and correction through the learning system
  - run only affected validation
  - commit and push the validated bounded delta
forbidden_actions:
  - modify Kernel, Controller, loop, protocol, GOV-5 scope, formal-run artifacts, or product code
  - activate GOV-5 or create a formal run
  - open a pull request, merge, release, ratify, or accept risk
  - perform unrelated refactoring or validation
exact_text_preserved: true
exact_text_sha256: 78b6c1d45456276d0ed4b4a9f8bf9c2b1bddb462fa930fdaf52dbd4355173115
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/tests/run-learning-tests.sh
  - governance/learning/records/HP-FAIL-010.yaml
  - governance/learning/events/HP-FAIL-010/HP-FAIL-010-E001.yaml
  - governance/learning/FAILURE_AND_LESSONS_INDEX.md
result_commit: null
supersedes: null
---

# Learning Event Count Maintenance Prompt

## Exact executed text

You are working inside the HugePlanning repository.

Repository: Sugar144/HugePlanning
Branch: governance/kernel-designer-revision-v0.1
Expected HEAD: a9d891931d902dab7f17d2fadb2d80fc17b9b99a

Perform one bounded maintenance correction only.

## Confirmed defect

The GOV-5 read-only scope review found that the learning validation wrapper reports:

22 passed, 1 failed

The failing repository assertion still expects exactly one learning event, while the valid durable state now contains six events.

## Authorized work

1. Locate the stale expectation.
2. Confirm from repository contracts whether the assertion should:
   - expect the current valid count dynamically; or
   - validate multiple events without hardcoding a historical total.
3. Apply the smallest correct fix.
4. Add or update a regression test proving that multiple valid append-only events are accepted.
5. Preserve the defect and correction through the existing learning system.
6. Preserve this prompt under the next valid HP-PROMPT identifier if required by prompt custody.
7. Run only affected learning-system tests, generated-index consistency checks, prompt-custody validation if affected, and `git diff --check`.
8. If all validation passes and no scope drift occurs, commit and push the change.
9. Verify local and remote HEAD alignment and a clean worktree.

Do not modify Kernel, Controller, loop, protocol, GOV-5 scope, formal-run artifacts, or product code.

Do not activate GOV-5, create a formal run, open a pull request, merge, release, ratify, or accept risk.

If the expected behavior is ambiguous, stop and report the exact conflicting repository evidence.

Return:

Branch:
Previous HEAD:
Defect location:
Root cause:
Files changed:
Regression added:
Learning evidence:
Prompt ID/version:
Validation:
New commit:
Push:
Local/remote aligned:
Worktree:
Status:
Exact next action:
