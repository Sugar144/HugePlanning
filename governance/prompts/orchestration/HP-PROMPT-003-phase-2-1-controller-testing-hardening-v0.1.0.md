---
prompt_id: HP-PROMPT-003
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Phase 2.1 Controller testing hardening
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 5d4b8203f3dae8df8311a8ee0e14aa45587c0edf
authorization_scope:
  - local pytest and Hypothesis Controller test implementation
  - bounded dependency and test-entry-point updates
  - prompt custody, backlog status, implementation report, and review bundle
  - proportional validation
forbidden_actions:
  - Controller, loop, protocol, schema, or package semantic modification
  - Promptfoo, TLA+, Schemathesis, or skills implementation
  - KGR-005 execution or real Controller transitions
  - staging
  - commit
  - push
  - pull request
exact_text_preserved: true
exact_text_sha256: a7991b87124d7a31a0d5a6d995314fe3a026f22ce9153a52acef3e1a85e6c923
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/tests/controller/
  - governance/tests/run-controller-tests.sh
  - governance/reviews/phase-2-1-controller-testing-hardening/implementation-report-v0.1.0.md
  - Phase 2.1 bounded review bundle
result_commit: null
supersedes: null
---

# Phase 2.1 Controller Testing Hardening Prompt

## Exact executed text

Implement Phase 2.1: Controller testing hardening with pytest and Hypothesis.

## Checkpoint

```text
repository: /home/sugar/Documents/HugePlanning-governance
branch: governance/kernel-designer-revision-v0.1
required_head: 5d4b8203f3dae8df8311a8ee0e14aa45587c0edf
expected_worktree: clean
```

Read applicable `AGENTS.md` files and the canonical methodology backlog entry `HP-MPROP-001`.

Preserve this exact prompt as:

```text
HP-PROMPT-003 / 0.1.0
category: ORCHESTRATION
status: EXECUTED
purpose: Phase 2.1 Controller testing hardening
```

Do not alter this prompt text when preserving it.

## Objective

Adopt:

```text
pytest
Hypothesis
Hypothesis RuleBasedStateMachine
```

to improve coverage of the deterministic Controller without changing its semantics.

## Required implementation

Create a maintainable pytest suite, preferably under:

```text
governance/tests/controller/
```

Use a sensible structure such as:

```text
conftest.py
test_canonical_transitions.py
test_loop_properties.py
test_package_properties.py
test_state_machine.py
```

Exact filenames may differ if the repository structure supports a better arrangement.

### Canonical regression coverage

Preserve all existing 20 transition fixtures as authoritative, explicit regression cases.

Use pytest parametrization so each fixture appears as an individually identifiable test case.

The expected outcomes must remain unchanged.

Do not delete the existing evidence before proving replacement coverage. A thin compatibility wrapper may remain.

### Property-based tests

Use Hypothesis to test at least these invariants:

```text
counters never decrease
invalid or non-completion inputs do not consume counters
a fourth targeted closure cannot be accepted
a third Designer remediation cannot be accepted
Designer cannot produce CLOSURE_CONFIRMED
terminal states cannot continue automatically
history replay is deterministic
finding signatures are independent of input ordering
canonical JSON output is deterministic
dry-run does not write repository transition records
```

Generate only bounded inputs. Avoid unbounded ZIPs, large files, excessive test duration, or nondeterministic external resources.

When testing ZIP/package validation, generate bounded safe and hostile member names, duplicate or ambiguous paths, structured-data mutations, and integrity mismatches using temporary directories only.

### Stateful model testing

Implement one `RuleBasedStateMachine` comparing:

```text
a small independent reference model
vs
the actual Controller transition calculation
```

Generate valid and invalid sequences involving:

```text
targeted closure start/import
Designer remediation start/import
non-completion outcomes
owner-decision or research routes
validated re-entry
terminal or exhausted states
```

Required state-machine invariants:

```text
implementation state equals reference-model state
implementation counters equal model counters
limits are never exceeded
invalid operations do not mutate accepted history
terminal states expose no automatic continuation
history replay produces the same result
```

Keep the reference model small and independent. Do not duplicate the entire production implementation.

## Dependencies and execution

Use the repository’s existing Python dependency convention. Add only:

```text
pytest
hypothesis
```

Pin or bound versions according to the repository’s current dependency policy. Do not introduce another package manager or environment system.

Update:

```text
governance/tests/run-controller-tests.sh
```

so it remains a thin entry point that runs the pytest Controller suite.

Avoid relying on Hypothesis example databases outside controlled test paths. Preserve reproducible failure information through normal Hypothesis output and shrunk counterexamples.

Do not claim a fixed seed is required for normal successful runs. A failing example must be replayable using Hypothesis’s reported reproduction mechanism or persisted regression example.

## Scope protection

Do not change Controller, loop, protocol, schema, or package semantics merely to satisfy generated tests.

If a generated test exposes a likely production defect:

1. preserve the minimal failing example;
2. record it honestly;
3. do not silently weaken the test;
4. stop before changing production semantics unless the correction is unambiguously within the existing contract.

Do not implement:

```text
Promptfoo
TLA+
Schemathesis
skills
KGR-005 execution
real Controller transitions
```

Do not stage, commit, push, or open a PR.

## Documentation and learning

Update `HP-MPROP-001` honestly:

```text
IMPLEMENTED_LOCALLY_PENDING_REVIEW
```

or the closest valid existing backlog status. Do not mark it accepted or operational.

Create a concise repository implementation report for Phase 2.1.

Create learning evidence only if a material defect, unexpected invariant violation, dependency problem, or methodology failure actually occurs.

Do not manufacture a failure record merely because normal implementation debugging occurs.

## Validation

Run:

```text
new pytest Controller suite
all 20 canonical transition fixtures
Hypothesis property tests
RuleBasedStateMachine tests
existing learning tests
prompt-custody tests
git diff --check
```

Run the broader 224-test repository suite only if affected-file analysis shows dependency risk or existing test entry points are modified in a way that can affect it.

Record:

```text
pytest version
Hypothesis version
collected test count
canonical fixture count
configured Hypothesis examples
state-machine step/run settings
execution duration
any shrunk failing examples
```

Do not describe generated-example counts as exhaustive proof.

## Output

Produce a bounded review bundle and concise report containing:

```text
changed-file inventory
unified diff
new and modified files
dependency changes
test configuration
test outputs
property/state-machine coverage
hash manifest
repository status
```

Return:

```text
Branch:
Base HEAD:
Prompt ID/version:
Dependencies added:
Files created:
Files modified:
Canonical fixtures:
Pytest tests:
Hypothesis properties:
State-machine configuration:
Test result:
Material defects found:
Learning evidence:
Controller semantics changed:
Implementation report:
Review bundle:
Worktree:
Staging:
Commit:
Push:
Status:
Exact next action:
```

Finish with:

```text
Status: PHASE_2_1_READY_FOR_PROJECT_OWNER_REVIEW
Exact next action: Upload the Phase 2.1 report and review bundle.
```
