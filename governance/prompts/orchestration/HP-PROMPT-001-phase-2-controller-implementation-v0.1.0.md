---
prompt_id: HP-PROMPT-001
version: 0.1.0
category: ORCHESTRATION
status: EXECUTED
purpose: Phase 2 deterministic closure-loop tooling implementation
target_environment: Codex CLI
model: Sol
reasoning: Medium
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 5c3f0dc759969f443f7aa0946093ed874fbc0f4e
authorization_scope:
  - local repository modifications
  - deterministic scripts
  - schemas and validation profiles
  - synthetic fixtures and tests
  - local implementation report
  - local review bundle
forbidden_actions:
  - staging
  - commit
  - push
  - pull request
  - merge
  - tag
  - release
  - KGR-005 execution
  - real Controller transition
  - automatic LLM execution
exact_text_preserved: true
exact_text_sha256: 7012d88f0bb5ab0b7492fc78f79f3455ce5c4c0cf59524158915f847e093e102
execution_interrupted: true
execution_resumed: true
result_artifacts:
  - governance tooling implementation
  - /home/sugar/Downloads/HugePlanning-phase-2-controller-implementation-report-v0.1.0.md
  - /home/sugar/Downloads/HugePlanning-phase-2-controller-review-v0.1.0.zip
result_commit: null
supersedes: null
---

# Phase 2 Controller Implementation Prompt

## Exact executed text

You are implementing Phase 2 of the approved HugePlanning governance tooling architecture.

This is an authorized local repository implementation of the deterministic closure-loop tooling foundation.

## Authorization scope

Authorized:

```text
local repository modifications
local deterministic scripts
schemas and validation profiles
synthetic fixtures and tests
validation of the already-prepared KGR-005 input package
local implementation report
local review bundle
```

Not authorized:

```text
staging
commit
push
pull request
merge
tag
release
KGR-005 execution
LLM execution or automatic model launching
constitutional judgment
Kernel modification
KGR-006 creation
Enforcement Engineering
human ratification
```

## Repository checkpoint

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
5c3f0dc759969f443f7aa0946093ed874fbc0f4e
```

Before modifying anything, verify:

1. branch is exact;
2. HEAD is exact;
3. local and remote branch HEADs are aligned;
4. worktree is clean;
5. staging area is empty;
6. applicable root and governance `AGENTS.md` files have been read;
7. KGR-005 remains `NOT_STARTED`;
8. Kernel remains `0.2.0-proposed / PROPOSED_NOT_RATIFIED`;
9. Enforcement Engineering remains `CLOSED`;
10. human ratification remains `NOT_STARTED`.

If any checkpoint differs materially, stop without modifying files and report:

```text
BLOCKED_BY_REPOSITORY_STATE_CONFLICT
```

## Durable design sources

Read and use:

```text
governance/reviews/phase-1-instructions-learning/architecture-report-v0.1.0.md
governance/methodology/project-operating-contract.md
governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml
governance/methodology/roles/kernel-adversary/protocols/targeted-closure/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md
governance/methodology/roles/kernel-designer/protocols/closure-remediation/06-kernel-designer-closure-remediation-prompt-sol-high-v0.1.0.md
governance/runs/KGR-005-kernel-adversary-targeted-closure/**
governance/learning/**
```

The architecture report is broader than this phase. This prompt defines the narrower authorized implementation scope.

Do not modify the existing loop, protocols, KGR-005 prompt, envelope, run manifest, control snapshot, historical runs, or raw sources.

# Phase 2 objective

Implement the minimum deterministic tooling required to validate and apply `GOV-LOOP-001` safely before executing KGR-005:

```text
validate_closure_loop.py
validate_run_package.py
apply_loop_transition.py
```

Also implement:

```text
versioned schemas and validation profiles
shared deterministic helper library
synthetic fixtures
offline tests
validation evidence contracts where required
```

Do not implement:

```text
build_run_package.py
build_review_bundle.py
automatic LLM execution
general multi-agent orchestration
KGR-006 generation
semantic constitutional evaluation
automatic repository state-document mutation
```

# Workstream 1 — Shared deterministic library

Create a small bounded private library:

```text
governance/tools/_lib/
├── __init__.py
├── strict_yaml.py
├── canonical.py
├── schemas.py
├── safe_zip.py
├── atomic.py
└── diagnostics.py
```

Reuse Phase 1 code where appropriate instead of duplicating logic.

Requirements:

* Python standard library plus existing PyYAML and jsonschema only;
* strict duplicate-key rejection;
* canonical compact JSON for hashing;
* lexicographically sorted keys;
* UTF-8;
* lowercase SHA-256;
* deterministic diagnostic ordering;
* no network;
* no LLM;
* no Git mutation;
* no wall-clock or random data in deterministic outputs unless explicitly supplied;
* safe path normalization;
* atomic writes;
* refusal to overwrite immutable targets.

Do not refactor `manage_learning.py` unnecessarily. Shared extraction is permitted only when bounded and fully tested.

# Workstream 2 — Loop and protocol schemas

Create:

```text
governance/schemas/kernel-design-closure-loop.schema.json
governance/schemas/controller-transition.schema.json
governance/schemas/governance-validation-record.schema.json

governance/schemas/protocols/GOV-PROTOCOL-002/0.1.0/
├── finding-closure-verdicts.schema.json
└── closure-result.schema.json

governance/schemas/protocols/GOV-PROTOCOL-003/0.1.0/
└── designer-remediation-result.schema.json
```

Use JSON Schema draft 2020-12.

These schemas are deterministic enforcement profiles for the current contracts. They must not silently add new constitutional semantics.

If the existing contracts cannot be represented without inventing meaning, stop the affected portion and report:

```text
BLOCKED_BY_ARCHITECTURE_CONFLICT
```

with the exact conflict.

# Workstream 3 — validate_closure_loop.py

Create:

```text
governance/tools/validate_closure_loop.py
```

Purpose:

```text
Validate the static structure and cross-contract invariants of GOV-LOOP-001
without evaluating constitutional substance.
```

CLI:

```bash
python3 governance/tools/validate_closure_loop.py \
  --loop PATH \
  [--adversary-protocol PATH] \
  [--designer-protocol PATH] \
  [--json]
```

Default behavior is read-only.

Exit codes:

```text
0 = valid
1 = schema or invariant failure
2 = usage or operational failure
```

Validate at minimum:

1. exactly nine declared persistent states;
2. no undeclared state references;
3. all transition sources and destinations resolve;
4. explicit exits from both active states;
5. typed attempt events;
6. typed non-completion events;
7. exact ordered Adversary result matrix;
8. exact ordered Designer remediation result matrix;
9. final-result mutual exclusivity;
10. Designer cannot emit `CLOSURE_CONFIRMED`;
11. closure-confirmed requirements;
12. initial counters are zero;
13. exact counter increment rules;
14. maximum three targeted closures;
15. maximum two Designer remediations;
16. maximum KGR-005 through KGR-009 sequence;
17. package conflict consumes no counter;
18. invalid output consumes no counter;
19. invalid import consumes no counter;
20. deterministic blocking-finding signature rules;
21. no-progress guard;
22. repeated-finding guard;
23. owner-decision re-entry;
24. research re-entry;
25. structural-redesign exit;
26. only `READY_FOR_TARGETED_CLOSURE` may prepare another Adversary run;
27. artifact-resolution rules;
28. prompt, envelope, loop, protocol, run, and mode identity bindings;
29. unknown loop or protocol versions fail closed;
30. duplicate YAML keys fail.

Output must be canonical and stable.

# Workstream 4 — validate_run_package.py

Create:

```text
governance/tools/validate_run_package.py
```

Purpose:

```text
Validate formal run input packages, completed output packages,
and repository-import packages using explicit stage semantics.
```

CLI:

```bash
python3 governance/tools/validate_run_package.py \
  --stage preparation|isolated-input|output|import \
  --role adversary|designer \
  --package PATH \
  --envelope PATH \
  [--prompt-snapshot PATH] \
  [--loop-snapshot PATH] \
  [--json]
```

Exit codes:

```text
0 = valid
1 = package or contract invalid
2 = usage or operational failure
```

Requirements:

* never extract into the repository;
* use a fresh temporary directory;
* distinguish:

  * repository custody path;
  * provenance source path;
  * transport package member;
* exact member-set validation;
* exact SHA-256 validation;
* strict YAML and JSON Schema validation;
* detect missing, extra, duplicate, unsafe, encrypted, unreadable, or oversized members;
* reject:

  * absolute paths;
  * `..`;
  * normalized duplicates;
  * symlinks;
  * devices;
  * ambiguous backslash paths;
  * encrypted entries;
* enforce bounded member count and decompression limits;
* validate prompt/envelope/loop/protocol/run/mode identity;
* validate stage-specific path responsibilities;
* classify package conflict as pre-substantive non-completion, not completed execution;
* never correct or rebuild a package;
* never import or decide constitutional substance.

It must validate the existing KGR-005 formal input ZIP without modifying it:

```text
/home/sugar/Downloads/KGR-005-formal-input-package.zip
```

Expected SHA-256:

```text
26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf
```

Expected members:

```text
19
```

If the local ZIP is unavailable, test the validator against a fixture and report the KGR-005 external validation as not executed. Do not fabricate the result.

# Workstream 5 — apply_loop_transition.py

Create:

```text
governance/tools/apply_loop_transition.py
```

Purpose:

```text
Replay immutable Controller history, validate one structured event or
role result, calculate counters and guards, and simulate or record exactly
one Controller transition.
```

Subcommands:

```text
import
event
reenter
```

Representative CLI:

```bash
python3 governance/tools/apply_loop_transition.py import \
  --loop PATH \
  --source-run KGR-005 \
  --input PATH \
  --history-root governance/runs
```

Write behavior:

```text
dry-run by default
--apply required for write
--authorization-ref required together with --apply
```

Exit codes:

```text
0 = valid dry-run or applied transition
1 = invalid result, history, state, counter, guard, identity, or immutable-target conflict
2 = usage or operational failure
3 = valid mutation blocked because explicit authorization reference is absent
```

Permitted future write path only:

```text
governance/runs/<source-run>/controller/controller-transition.json
```

Do not apply a real KGR-005 transition in this phase.

Requirements:

* replay history rather than trust mutable counter fields;
* refuse history forks;
* refuse duplicate source-run transition records;
* refuse overwrite;
* validate source state, role, mode, run, and result;
* validate exactly one role-appropriate result;
* validate matrix priority consistency;
* verify all higher-priority outcomes are accounted for;
* increment counters only after valid completed import;
* package conflicts and invalid output/import consume no counters;
* calculate deterministic blocking-finding signature;
* calculate no-progress guard;
* calculate repeated-finding guard;
* enforce KGR-005 to KGR-009 sequence;
* refuse fourth targeted closure;
* refuse third Designer remediation;
* require active-state evidence before completed import;
* validate re-entry artifact identity and applicability;
* never evaluate constitutional truth;
* never update `CURRENT_STATE.md`, registry, decisions, run manifest, or plan automatically in v0.1;
* output a deterministic proposed transition and a list of human-reviewed repository updates that would be required after an authorized real import.

Controller record format:

```text
canonical JSON
one trailing newline
immutable once created
```

The schema must preserve:

* loop ID/version/hash;
* source run;
* source role/mode;
* previous state;
* declared role result or typed event;
* package validation reference;
* counters before and after;
* guard calculations;
* resulting state;
* next role/mode where applicable;
* authorization reference;
* applied flag;
* constitutional authority: none;
* generated artifact not ratification or execution evidence beyond the validated transition record.

# Workstream 6 — Synthetic fixture matrix

Create executable fixtures under:

```text
governance/tests/fixtures/transitions/
```

Implement at least these 20 cases:

```text
01 valid KGR-005 CLOSURE_CONFIRMED
02 first DESIGNER_REMEDIATION_REQUIRED
03 owner decision required from Adversary
04 research required from Adversary
05 structural redesign required from Adversary
06 package conflict before substantive execution
07 invalid output package
08 invalid repository import
09 successful Designer remediation
10 Designer owner decision required
11 Designer research required
12 Designer structural redesign required
13 third closure still requires remediation
14 attempt to prepare a fourth targeted closure
15 attempt to prepare a third remediation
16 repeated reopened finding threshold
17 no-progress signature threshold
18 LOW non-blocking new finding
19 blocking MEDIUM regression finding
20 prompt/envelope identity mismatch
```

Each fixture must declare:

```yaml
fixture_id: ""
input_state: ""
source_run: ""
source_role: ""
source_mode: ""
input_result: ""
counters_before: {}
history: []
expected_validity: ""
expected_counters_after: {}
expected_transition: ""
expected_next_role: null
expected_next_mode: null
owner_authorization_required: true
expected_diagnostic: null
```

Synthetic fixtures must be clearly marked as test evidence, not real runs.

Also create targeted static mutation fixtures for every loop invariant that cannot be adequately covered by the scenario matrix.

# Workstream 7 — Package-security fixtures

Create bounded fixture generators or static fixtures covering:

* missing member;
* extra member;
* duplicate normalized member;
* wrong member hash;
* unsafe traversal path;
* absolute path;
* backslash ambiguity;
* symlink;
* encrypted member where feasible;
* excessive member count;
* excessive uncompressed size;
* excessive compression ratio;
* invalid UTF-8 structured file;
* duplicate YAML key;
* prompt/envelope mismatch;
* loop snapshot mismatch;
* preparation path mismatch;
* isolated-input validation without repository paths;
* output schema failure;
* import custody mismatch.

Do not commit large binary fixtures unnecessarily. Small deterministic fixture generation during tests is preferred.

# Workstream 8 — Tests

Create:

```text
governance/tests/run-controller-tests.sh
```

The test suite must cover:

## Static validation

* all loop invariants;
* exact state count;
* exact transition resolution;
* exact result matrices;
* unknown version rejection;
* duplicate key rejection.

## Package validation

* real KGR-005 input ZIP when available;
* all security and integrity fixtures;
* no repository extraction;
* stage-specific semantics.

## Transition behavior

* all 20 fixtures;
* history replay determinism;
* signature determinism across input ordering;
* counter increment rules;
* guard exhaustion;
* run-sequence limits;
* missing active-state evidence;
* invalid result enum;
* wrong role/mode;
* overwrite refusal;
* missing authorization exit code 3;
* `--apply` only writes expected path in an isolated temporary repository fixture;
* failed atomic write leaves no partial record.

## Regression

Run:

```text
governance/tests/run-learning-tests.sh
existing repository test suite
```

All tests must operate offline and leave the real repository unchanged except for the authorized source/test modifications.

# Workstream 9 — Validation records and documentation

Create:

```text
governance/validation/README.md
```

Do not create real `GOV-VAL-###` repository records unless the architecture and current authorization clearly require them.

Document:

* validation report structure;
* authority limitations;
* future record allocation;
* difference between transient test output and durable validation evidence.

Update only as necessary and truthfully:

```text
governance/ARTIFACT_REGISTRY.yaml
governance/CURRENT_STATE.md
governance/DECISION_LOG.md
governance/methodology/README.md
```

Rules:

* do not advance GOV-4;
* do not execute KGR-005;
* do not consume counters;
* do not claim the Controller is operational;
* describe tooling as locally implemented pending Project Owner review;
* preserve all existing KGR-005 and historical artifacts byte-for-byte;
* record new failures through the Phase 1 learning system when material issues occur;
* do not silently repair material implementation defects.

# Forbidden modifications

Do not modify:

```text
governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml
governance/runs/KGR-005-kernel-adversary-targeted-closure/**
governance/methodology/roles/kernel-adversary/protocols/targeted-closure/**
governance/methodology/roles/kernel-designer/protocols/closure-remediation/**
governance/sources/raw/**
governance/kernel/proposed/**
```

If implementation exposes a contract defect requiring changes to a forbidden path, stop and report the defect instead of changing it.

# Formal output artifacts

Every formal output must be materialized as a file.

## Implementation report

Create outside the repository:

```text
/home/sugar/Downloads/HugePlanning-phase-2-controller-implementation-report-v0.1.0.md
```

It must begin with:

```yaml
---
document_id: HP-IMPL-GOV-CONTROLLER-001
version: 0.1.0
status: IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
repository_base_head: 5c3f0dc759969f443f7aa0946093ed874fbc0f4e
repository_commit: null
repository_push: false
kgr_005_execution: NOT_STARTED
controller_status: IMPLEMENTED_LOCALLY_NOT_OPERATIONAL
kernel_status: PROPOSED_NOT_RATIFIED
enforcement_engineering: CLOSED
human_ratification: NOT_STARTED
---
```

Required sections:

```text
1. Repository checkpoint
2. Applicable instructions
3. Architecture and contract sources
4. Files created
5. Files modified
6. Shared deterministic library
7. Schemas and validation profiles
8. Loop validator implementation
9. Package validator implementation
10. Transition Controller implementation
11. Synthetic fixtures
12. Package-security fixtures
13. Tests executed
14. KGR-005 input validation result
15. Determinism evidence
16. Security and integrity validation
17. Material failures and learning records
18. Deviations from approved scope
19. Known limitations
20. Repository status
21. Exact next action
```

## Review bundle

Create:

```text
/home/sugar/Downloads/HugePlanning-phase-2-controller-review-v0.1.0.zip
```

Include:

```text
implementation report
exact changed-file inventory
unified diff
all new and modified files
test outputs
validation outputs
KGR-005 package validation output when available
synthetic fixture result matrix
SHA-256 manifest
branch and base-HEAD evidence
repository status evidence
```

Bundle requirements:

* safe relative paths;
* deterministic sorted inventory;
* no duplicate members;
* no `.git` data;
* no secrets;
* no unrelated files;
* exact SHA-256 for every member;
* validate the bundle after creation.

Do not import the report or bundle into the repository during this implementation. Repository custody will be decided during review, as in Phase 1.

# Required final validation

Before reporting completion:

1. run all Controller tests;
2. run all learning tests;
3. run all existing repository tests;
4. validate all JSON Schemas;
5. validate all YAML with duplicate-key rejection;
6. confirm forbidden paths are byte-identical;
7. run `git diff --check`;
8. confirm staging area empty;
9. confirm no commit or push;
10. confirm KGR-005 remains `NOT_STARTED`;
11. confirm no real Controller transition was applied;
12. confirm worktree contains only authorized Phase 2 changes.

# Final response

Return only:

```text
Branch:
Base HEAD:
Worktree before implementation:
Files created:
Files modified:
Total changed files:
Controller tests:
Learning tests:
Existing tests:
Schema validation:
Strict YAML validation:
KGR-005 input validation:
Forbidden paths unchanged:
Implementation report path:
Implementation report SHA-256:
Review bundle path:
Review bundle SHA-256:
Worktree after implementation:
Staged:
Commit:
Push:
KGR-005 status:
Real Controller transitions applied:
Controller status:
Kernel version/status:
Enforcement Engineering:
Human ratification:
Material failures recorded:
Known limitations:
Status:
Exact next action:
```

Finish with:

```text
Status: PHASE_2_IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
Exact next action: Upload HugePlanning-phase-2-controller-review-v0.1.0.zip and the implementation report to the orchestration conversation.
```
