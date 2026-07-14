---
document_id: HP-ARCH-GOV-TOOLING-001
version: 0.1.0
status: PROPOSED_FOR_PROJECT_OWNER_ARCHITECTURE_REVIEW
produced_from: CURRENT_CODEX_SESSION_ARCHITECTURE_ANALYSIS
repository_head: c41fbbf2bc6d2c54d609dbadd52b429e43f77a15
repository_changes: NONE
kgr_005_execution: NOT_STARTED
kernel_status: PROPOSED_NOT_RATIFIED
enforcement_engineering: CLOSED
human_ratification: NOT_STARTED
---

# HugePlanning Governance Tooling, Learning, and Instruction Architecture

This document is a preview-only architecture proposal. It describes a bounded next capability; it does not implement that capability, execute KGR-005, ratify the Kernel, reopen Enforcement Engineering, or grant constitutional authority to tooling.

## 1. Repository checkpoint

The repository checkpoint was verified before analysis and reverified before this document was materialized.

| Check | Verified result |
|---|---|
| Repository | `/home/sugar/Documents/HugePlanning-governance` |
| Branch | `governance/kernel-designer-revision-v0.1` |
| HEAD | `c41fbbf2bc6d2c54d609dbadd52b429e43f77a15` |
| Local upstream | `origin/governance/kernel-designer-revision-v0.1` |
| Local/remote divergence | `0 0` |
| Live remote branch SHA | `c41fbbf2bc6d2c54d609dbadd52b429e43f77a15` |
| Worktree | Clean |
| Staging area | Empty |

The applicable repository instruction is `governance/AGENTS.md`; no repository-root `AGENTS.md` currently exists. The applicable instruction requires Spanish operator communication, English repository artifacts, immutable raw sources, explicit provenance, honest run status, and stopping on authority, provenance, package, path, or destructive ambiguity conflicts.

The raw-source checksum set passed in full. The canonical loop and KGR-005 control snapshot are byte-identical at SHA-256 `cf7855a85d4ab9f3d4bb42c14ebbb0e735abcde938796f88284160904031fbe1`. The canonical targeted-closure protocol and KGR-005 prompt snapshot are byte-identical at SHA-256 `171914d7d6ff7024330ecccc1d662055ee8b77c4402a0c4bcac4271cbc98f67a`.

The local KGR-005 formal transport ZIP exists, contains exactly 19 expected members, passes archive integrity checks, and matches the recorded SHA-256 `26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf`. This is validation of prepared input custody only, not KGR-005 execution.

The preserved authority state is:

```yaml
kernel:
  version: 0.2.0-proposed
  status: PROPOSED_NOT_RATIFIED

governance_phase: GOV-4
kgr_005:
  preparation: COMPLETED
  readiness: READY_FOR_EXECUTION
  execution: NOT_STARTED

enforcement_engineering: CLOSED
human_ratification: NOT_STARTED
```

## 2. Current architecture discovered

The repository already has a strong governance custody model but no deterministic governance-loop runtime.

The current architecture separates:

- immutable imported material under `governance/sources/raw/`;
- reusable governance methodology under `governance/methodology/`;
- exact run contracts, inputs, outputs, controls, and manifests under `governance/runs/`;
- proposed Kernel candidates under `governance/kernel/proposed/`;
- durable state, decisions, provenance, and planning in `CURRENT_STATE.md`, `DECISION_LOG.md`, `ARTIFACT_REGISTRY.yaml`, and `GOVERNANCE_MASTER_PLAN.md`.

`GOV-LOOP-001` version `0.1.0` already defines nine closed persistent states, typed pre-substantive attempt events, typed non-completion events, an ordered Adversary result matrix, a separate Designer remediation result matrix through `GOV-PROTOCOL-003`, counters, run limits, no-progress and repeated-finding guards, finding identity, re-entry, artifact resolution, immutable history, and Controller authority boundaries.

The current runtime methodology at repository root already establishes useful implementation conventions:

- Bash entry points with `set -euo pipefail`;
- Python helpers with explicit `0/1/2` exit semantics;
- PyYAML and JSON Schema validation;
- valid and invalid fixtures where invalid fixtures assert the intended failure reason;
- offline deterministic tests in paths containing spaces;
- staging before publication;
- refusal to overwrite non-empty targets;
- preservation of a clean real worktree;
- CI without live model or network requirements.

The installed environment contains Python 3.14.6, PyYAML 6.0.3, and jsonschema 4.26.0. The CI environment uses Python 3.12 and installs PyYAML and jsonschema explicitly.

Material architecture gaps and contradictions discovered are:

1. There is no root `AGENTS.md`, so Codex lacks durable repository-wide rules distinct from Claude runtime instructions.
2. `governance/AGENTS.md` is governance-specific but does not yet define deterministic tooling, learning records, Controller import behavior, or detailed instruction precedence.
3. The root `scripts/validate.sh` is intentionally the single progressive client-repository validator. Governance tooling must not pretend to extend that client-runtime contract or become a second general methodology runtime.
4. Existing YAML helpers use `yaml.safe_load`, which does not reject duplicate mapping keys. KGR-005 requires strict YAML parsing with duplicate-key rejection.
5. The loop is machine-readable but not a complete executable schema. Some transition conditions are symbolic identifiers whose constitutional truth must be supplied by the role result, not evaluated by the Controller.
6. KGR-005 output schemas are embedded in a prompt, not available as separately versioned enforcement schemas.
7. The Designer remediation protocol is only a future-instantiation basis. It has no concrete run ID, target version, envelope, prompt snapshot, or output set, so tooling must not fabricate KGR-006.
8. No durable Controller transition record exists yet, and no canonical path is assigned for one.
9. No machine state ledger exists. Counters and state are currently expressed in methodology and prepared run metadata, not replayed from Controller records.
10. The existing KGR-005 ZIP is content-valid and hash-bound but carries source timestamps. Its bytes cannot be promised reproducible from a fresh checkout. It must be preserved, not silently rebuilt or normalized.
11. `ARTIFACT_REGISTRY.yaml` and state documents are currently maintained manually. A tool may validate and propose changes but must not silently confer authority or rewrite historical records.
12. The current durable next execution says to launch KGR-005. Inserting implementation work before that execution is a Project Owner sequencing decision, not an inference this proposal can make.

## 3. Problems being solved

The proposed capability solves three connected but distinct problems.

First, the closure loop is precise enough to review but too expensive and error-prone to apply repeatedly by hand. Hash checks, archive safety, member identity, state references, counter arithmetic, matrix precedence, signatures, run ordinals, and guard exhaustion are deterministic work and should not consume high-capability model reasoning.

Second, material failures and lessons are dispersed across run notes, temporary working material, experiment reports, conversation context, and owner corrections. This weakens recurrence detection, cost learning, and durable process improvement.

Third, permanent project behavior is spread across external ChatGPT Project Instructions, Claude-specific runtime files, one governance-scoped `AGENTS.md`, methodology documents, protocols, prompts, and schemas without one explicit cross-surface precedence model.

The solution must keep three boundaries intact:

- tools validate declared structure and deterministic facts but never decide constitutional substance;
- learning records preserve evidence but do not replace formal runs, decisions, incidents, or operational logs;
- instructions govern behavior but do not create authorization, execution evidence, ratification, or enforcement readiness.

## 4. Proposed instruction hierarchy

### 4.1 Reference hierarchy and precedence

The proposed precedence is:

1. Platform and system safety constraints.
2. The Project Owner's explicit, current, bounded instruction.
3. Repository-root `AGENTS.md` for repository-wide Codex behavior.
4. The closest applicable path-scoped `AGENTS.md`, with `governance/AGENTS.md` adding stricter governance rules.
5. A formally bound run set: input envelope, exact prompt snapshot, exact loop/control snapshot, and run manifest. Any conflict inside that set blocks the run.
6. Canonical, versioned methodology contracts.
7. Role protocols that specialize the methodology.
8. Schemas and deterministic validation rules for structural enforcement.
9. Generated summaries, indexes, dashboards, and review bundles, which are derived views and never higher authority than their sources.

ChatGPT Project Instructions are external interaction configuration. They may shape conversation but cannot authorize repository mutation, replace repository truth, override a formally bound run, or establish governance state.

For historical or prepared runs, the exact bound snapshot governs that run even if canonical methodology later changes. New methodology never rewrites a prior prompt, envelope, output, or result. A conflict between a bound snapshot and current methodology is recorded and resolved through a new version or new run, not silent substitution.

### 4.2 Proposed ChatGPT Project Instructions

The following text is intentionally concise and contains no repository implementation detail or long schema:

```text
Communicate with the Project Owner in Spanish. Write durable repository artifacts in English.

Keep interaction bounded and neurodivergent-friendly: use short, explicit steps, stable terminology, and no more than three substantive questions per turn. Always distinguish facts, assumptions, proposals, decisions, authorized executions, and validated results.

The Project Owner retains decision and authorization authority. Never infer approval, continuation, commitment, execution, risk acceptance, or permission to mutate state. Use preview-first behavior for material changes and stop at human authorization gates.

Proactively identify material failures, near misses, ambiguities, owner corrections, process defects, cost waste, and tooling gaps, and propose durable capture in the project's approved learning system.

Use the least costly capable model and method. Prefer scripts for deterministic parsing, validation, counting, comparison, hashing, packaging, and state transitions. Do not recursively use agents or models to review work that deterministic checks can settle.

When context becomes overloaded, create a concise durable handoff that preserves authority, facts, open decisions, current state, and the exact next action. End substantial work with the explicit current state and exact next action.
```

### 4.3 Proposed repository-root `AGENTS.md`

The root file should contain only repository-wide Codex rules:

- Inspect all applicable instruction files before reading or modifying scoped content.
- Treat committed repository artifacts and explicit status records as durable truth; conversation memory is not a substitute.
- Use preview-first behavior for material changes and state the proposed paths, effects, validations, and authorization boundary.
- Do not infer authorization. Commit, push, PR creation, merge, tag, release, deployment, or external publication each requires its corresponding explicit approval.
- Prefer scripts for deterministic work and do not spend model reasoning on repeatable parsing, hashing, comparison, serialization, or validation.
- Do not claim completion until relevant deterministic tests and validations pass.
- Register material failures and lessons under the approved governance learning contract; do not bury them only in chat or temporary notes.
- Preserve historical artifacts and append-only records. Supersede; do not rewrite history.
- Use honest state language: proposed is not approved, prepared is not executed, generated is not validated, validated is not accepted, and closed is not ratified.
- Use the least costly capable model or mechanism when the environment exposes model choice or cost information.
- Repository artifacts are in English; operator communication follows the applicable project instruction.

It should reference, not duplicate, the canonical operating contract and the governance learning README.

### 4.4 Proposed `governance/AGENTS.md` additions

The governance-scoped file should add:

- The Kernel remains `PROPOSED_NOT_RATIFIED` until an explicit human ratification record says otherwise.
- Enforcement Engineering remains closed until a valid governance transition opens it; no tool, prompt, review, or closure result may infer that transition.
- Completed runs, imported outputs, raw sources, bound prompts, envelopes, control snapshots, and Controller records are immutable.
- A formal run requires an exact role/mode/run identity, prompt snapshot, envelope, control snapshot where applicable, complete hashed input set, output contract, honest status, and import validation.
- Designer, Adversary, Controller, and Project Owner authority are separate. The Controller cannot interpret constitutional substance; the Designer cannot self-close; the Adversary cannot mutate the Kernel or counters.
- Use governance validation tools before claiming package validity, result validity, transition validity, or reproducibility.
- Material governance failures and owner corrections require learning-record triage.
- `CURRENT_STATE.md` is the durable human-readable current-state view and must be updated in the same reviewed change as any accepted state transition; it must never lead or fabricate the underlying evidence.
- Applicable decisions, learning records, registry entries, run manifests, and plan status must be updated together when their triggering event is valid and authorized.
- Methodology changes create new versions and never rewrite completed run history to fit later rules.

### 4.5 Canonical methodology document

Create `governance/methodology/project-operating-contract.md`, not `project-operating-instructions.md`.

“Contract” better distinguishes durable project operating semantics from tool-loading instruction files. It should define authority vocabulary, preview-first behavior, record classes, deterministic-work routing, failure capture, handoff requirements, and the reference hierarchy. It should not duplicate every imperative from either `AGENTS.md` and should not contain executable schemas.

`AGENTS.md` files tell Codex what to do. The operating contract explains the stable method and why. Protocols define role-specific executions. Schemas enforce machine structure. Run snapshots bind a particular execution.

## 5. Proposed learning-record architecture

### 5.1 Directory structure

Refine the proposed structure to separate schemas, immutable base records, append-only events, generated indexes, and summaries:

```text
governance/
├── learning/
│   ├── README.md
│   ├── FAILURE_AND_LESSONS_INDEX.md
│   ├── records/
│   │   ├── HP-FAIL-001.yaml
│   │   └── ...
│   ├── events/
│   │   ├── HP-FAIL-001/
│   │   │   ├── HP-FAIL-001-E001.yaml
│   │   │   └── ...
│   │   └── ...
│   └── summaries/
│       └── lessons-by-category.md
└── schemas/
    ├── failure-record.schema.json
    └── failure-record-event.schema.json
```

Use JSON Schema expressed as JSON, rather than `failure-record-schema.yaml`, because the repository already uses draft 2020-12 JSON Schema and jsonschema validation. This avoids a second schema convention while keeping instances in YAML.

The index and category summary are generated views. Their headers must say they are generated and identify the tool version/input digest. They are never the source of truth.

### 5.2 Record-class boundaries

| Record class | Purpose | Canonical location |
|---|---|---|
| Failure and lesson record | Durable causal learning from a material failure, near miss, ambiguity, correction, defect, waste, or tooling gap | `governance/learning/records/` |
| Formal run record | Contract, formal inputs, execution status, outputs, result, and provenance for a governance role execution | `governance/runs/` |
| Operational session log | Chronology, transient observations, resume context, and non-material local events | Existing or future operational-log surface; not the learning index |
| Decision record | Explicit authoritative choice and consequences | `governance/DECISION_LOG.md` or a future structured decision register |
| Security or governance incident | Realized or credibly attempted material breach of security, privacy, authority, integrity, or a mandatory governance gate requiring containment and accountable response | Separate incident system, not a failure record substitute |
| Methodology parking-lot proposal | Speculative future improvement without an observed defect or material event | Methodology proposal/backlog surface, not the failure index |

A run may produce a failure record. An incident should normally produce or link to a learning record after containment. Neither relationship merges the record classes.

### 5.3 Creation criteria

Create a new individual failure record when at least one is true:

- it has a distinct causal chain, severity, accountable owner, containment, or validation path;
- it can change a control, schema, test, protocol, instruction, model route, or workflow;
- it materially affected authority, provenance, cost, quality, time, or execution risk;
- it is a Project Owner correction of a proposed or attempted action;
- recurrence must be detectable independently.

Create a subfinding inside an existing systemic record only when the observation has the same systemic root cause, same corrective control, compatible status, and no independent severity, owner, or acceptance decision. Subfindings keep their own evidence references and dates.

Create an incident when there is a realized or credibly attempted material security, privacy, governance-authority, integrity, external-effect, or mandatory-gate violation that requires containment, notification, forensic preservation, recovery, or explicit risk acceptance. Incident triage takes precedence over learning-record convenience.

Create only an operational-log entry when the event is transient, non-material, locally corrected, non-recurring, creates no control gap, involves no owner correction, and needs only session continuity.

Create only a methodology proposal when the item is a prospective enhancement without observed failure, near miss, ambiguity, correction, waste, or defect. If later evidence shows a failure, create a failure record and link the proposal.

### 5.4 Refined failure schema

Retain the requested minimum fields and add the following controls:

```yaml
failure_record:
  schema_version: 0.1.0
  id: HP-FAIL-###
  date: YYYY-MM-DD
  recorded_on: YYYY-MM-DD
  title: ""

  context:
    phase: ""
    run: null
    component: ""
    branch: ""
    commit: null
    environment: null

  primary_classification: PROCESS_DEFECT
  classification:
    - PROCESS_DEFECT
  severity: HIGH
  status: OPEN

  expected_behavior: ""
  observed_behavior: ""
  impact: ""
  detection_method: ""

  root_cause:
    immediate: ""
    systemic: ""
    contributing_factors: []

  response:
    containment: ""
    correction: ""
    prevention: []
    accountable_owner: ""
    validation_required: []

  learning:
    reusable_lesson: ""
    candidate_system_changes: []
    applicable_future_phases: []

  cost:
    measurement: UNAVAILABLE
    exact_tokens: null
    estimated_range: null
    model_runs: null
    human_time_minutes: null
    deterministic_rework_count: null
    basis: ""

  evidence_refs: []
  related_records: []
  subfindings: []
  owner_decision_required: false

  accepted_risk: null
  validation:
    validated_by: null
    validated_on: null
    validation_refs: []
```

`classification` is a non-empty unique list from the requested closed enum. `primary_classification` must be present in that list. Canonical classification order is `FAILURE`, `NEAR_MISS`, `AMBIGUITY`, `PROCESS_DEFECT`, `TOOLING_GAP`, `COST_WASTE`, `OWNER_CORRECTION`.

### 5.5 Date and ID rules

- `date` is the earliest supported occurrence or discovery date, in `YYYY-MM-DD` using the repository's declared operating timezone when a timestamp exists.
- `recorded_on` is the date the durable record is created.
- Unknown dates are not guessed; use the earliest supported date and describe uncertainty in context/evidence.
- IDs are `HP-FAIL-` plus exactly three digits.
- Allocate `max(existing numeric suffix) + 1`; never fill gaps, renumber, reuse, or derive the ID from category.
- Allocation is single-writer in this version. Parallel allocation is a detected conflict, not auto-merged.
- Event IDs are `<record-id>-E<three digits>` and are monotonically allocated within the record.

### 5.6 Mandatory fields by classification

All records require context, expected/observed behavior, impact, detection, both root-cause levels, containment or an explicit `NOT_REQUIRED` rationale, reusable lesson, evidence references, and accountable owner.

Additional requirements:

- `FAILURE`: realized impact, correction, prevention, and validation plan.
- `NEAR_MISS`: credible avoided impact, detection point, containment, and why impact did not materialize.
- `AMBIGUITY`: competing interpretations, affected authority or behavior, and resolution owner.
- `PROCESS_DEFECT`: failed process step, violated or missing contract, and process-control change.
- `TOOLING_GAP`: deterministic capability missing, workaround used, and proposed test/script control.
- `COST_WASTE`: measurement mode, basis, repeated work count where known, and lower-cost routing.
- `OWNER_CORRECTION`: the prior proposal/assumption/action, the correction, the affected authorization boundary, and a preserved owner evidence reference or an explicit `NOT_PRESERVED` limitation.

### 5.7 Duplicate detection

The tool computes a non-authoritative duplicate fingerprint from normalized component, primary classification, expected behavior, observed behavior, systemic cause, and sorted evidence locators. Exact fingerprint matches block creation unless the new record explicitly links the candidate and records why it is distinct.

Overlapping evidence plus the same component/root cause generates a warning. Similar title alone never auto-merges. The tool may propose a subfinding but cannot decide materiality or incident classification.

### 5.8 Status transitions and immutability

Allowed normal progression:

```text
OPEN -> CONTAINED -> CORRECTED -> VALIDATED
OPEN|CONTAINED|CORRECTED -> ACCEPTED_RISK
ACCEPTED_RISK -> OPEN  (only on expiry, trigger, or new evidence)
```

Skipping a state requires an event with rationale and evidence. `VALIDATED` means the correction/prevention claim was checked; it does not mean the risk can never recur.

After `VALIDATED`, the base record is immutable. Later facts, recurrence, accepted risk, reopened status, supersession, or corrections are separate append-only event files. Effective status is derived from the base record plus ordered valid events.

Accepted risk requires:

- explicit competent owner decision reference;
- bounded scope and rationale;
- residual impact;
- review date or documented reason no date applies;
- expiry or reopening triggers;
- controls that remain mandatory.

`ACCEPTED_RISK` is not deletion, closure, or evidence that the condition is harmless.

### 5.9 Evidence references

Each evidence reference is structured:

```yaml
- type: REPOSITORY_PATH | COMMIT | RUN_ARTIFACT | DECISION | VALIDATION_RECORD | OWNER_STATEMENT | EXTERNAL
  locator: ""
  anchor: null
  sha256: null
  availability: PRESERVED | NOT_PRESERVED
  note: ""
```

Repository paths are relative. Commit locators use full SHAs. Run artifacts use `KGR-###:<relative path>`. Validation records use their stable ID. Missing conversation evidence must be marked `NOT_PRESERVED`; it must not be reconstructed as a verbatim quote.

### 5.10 Index, summary, and cost behavior

The index is regenerated from validated records and events, sorted by numeric ID. It includes ID, date, title, primary classification, severity, effective status, component, phase/run, owner-decision flag, and one-line lesson. Manual edits outside the generated header are rejected.

The category summary is regenerated deterministically from records, grouping IDs and lessons by classification, component, candidate system change, and future phase. It does not invent synthesis unsupported by the reusable lesson fields.

When exact token usage is unavailable, cost waste uses `measurement: UNAVAILABLE` or `ESTIMATED`, never a fabricated token count. Record observable substitutes such as number of high-capability model runs, repeated deterministic checks, repeated package builds, correction cycles, elapsed human time when known, and the estimation basis. Estimated ranges must be explicitly labeled and must not be aggregated with exact values as if equivalent.

## 6. Proposed deterministic tooling architecture

### 6.1 Tool boundary and consolidation decision

Keep five operational concerns separate because they have different authority and failure boundaries:

1. loop specification validation;
2. run-package validation;
3. Controller transition simulation/application;
4. reproducible run-package building;
5. reproducible review-bundle building.

Consolidate `record_failure.py` and `update_learning_index.py` into one `manage_learning.py` with subcommands. They share the same schema, ID allocation, duplicate detection, event replay, and generated views. Separate executables would duplicate parsing and mutation logic.

Do not consolidate validation with transition application. A read-only validator must remain usable without mutation authority. Do not consolidate run-package and review-bundle builders: one creates a formal transport governed by a run contract, while the other creates a non-authoritative review aid.

Use a small private library under `governance/tools/_lib/` for strict YAML, canonical JSON, hashing, path safety, ZIP safety, atomic single-file publication, schema loading, and common diagnostics. This is not a framework and exposes no agent orchestration or LLM launch capability.

Generated machine records should use canonical JSON where possible: UTF-8, lexicographically sorted keys, compact separators for hashes, a single trailing newline for files, and no timestamps unless supplied as explicit data. JSON is valid YAML but has a more stable canonical byte representation than PyYAML output.

### 6.2 `validate_closure_loop.py`

```yaml
tool:
  name: validate_closure_loop.py
  purpose: Validate one supported closure-loop specification and its cross-contract invariants without evaluating constitutional substance.
  inputs:
    - loop specification
    - pinned Adversary protocol profile
    - pinned Designer remediation protocol profile
    - versioned JSON Schemas
  outputs:
    - canonical JSON validation report on stdout
    - optional GOV-VAL record when explicitly requested
  read_paths:
    - governance/methodology/loops/kernel-design-closure/**
    - governance/methodology/roles/kernel-adversary/protocols/**
    - governance/methodology/roles/kernel-designer/protocols/**
    - governance/schemas/**
  permitted_write_paths:
    - governance/validation/records/GOV-VAL-###.json only with --record --apply
  command_line_interface: "python3 governance/tools/validate_closure_loop.py --loop PATH [--adversary-profile PATH] [--designer-profile PATH] [--record] [--apply]"
  exit_codes:
    0: valid or valid dry-run report
    1: schema or invariant failure
    2: usage or operational failure
  deterministic_guarantees:
    - strict duplicate-key rejection
    - closed-enum and reference validation
    - exact matrix priority and result consistency
    - canonical diagnostic ordering
    - no network, clock, random, or LLM input
  non_goals:
    - deciding whether a constitutional condition is substantively true
    - modifying the loop
    - executing a run
    - ratifying or authorizing anything
  failure_modes:
    - unsupported loop or protocol version
    - duplicate YAML key
    - undeclared state or result reference
    - missing or contradictory cross-contract invariant
    - invalid schema/profile identity
  tests:
    - every required loop-validation coverage item
    - one mutation fixture per invariant
    - duplicate-key and unknown-version fixtures
    - canonical diagnostic ordering
```

Required semantic checks include the closed persistent-state enum; declared transition endpoints; typed events; exact Adversary and Designer matrix order; final-result exclusivity; closure requirements; zero initial counters; exact increment rules; 3/2 limits; KGR-005 through KGR-009 maximum sequence; non-consumption events; signature canonicalization; both cross-run guards; re-entry; redesign exit; renewed-Adversary restriction; Designer closure prohibition; artifact resolution; and prompt/envelope/control identity binding.

### 6.3 `validate_run_package.py`

```yaml
tool:
  name: validate_run_package.py
  purpose: Validate formal run input, completed output, and repository-import packages using an explicit stage and role profile.
  inputs:
    - ZIP archive or directory
    - input envelope
    - exact prompt snapshot when required
    - loop/control snapshot
    - protocol validation profile
    - repository provenance paths for preparation/import stages
  outputs:
    - canonical JSON validation report
    - hashes, member inventory, and reconciliation facts
    - optional validation evidence record
  read_paths:
    - explicit package path
    - envelope-declared paths appropriate to the selected stage
    - governance/runs/**
    - governance/methodology/**
    - governance/schemas/**
  permitted_write_paths:
    - temporary extraction under system temp
    - governance/validation/records/GOV-VAL-###.json only with --record --apply
  command_line_interface: "python3 governance/tools/validate_run_package.py --stage preparation|isolated-input|output|import --role adversary|designer --package PATH --envelope PATH [--prompt-snapshot PATH] [--record] [--apply]"
  exit_codes:
    0: valid
    1: invalid package or contract conflict
    2: usage or operational failure
  deterministic_guarantees:
    - no repository extraction
    - exact sorted member-set validation
    - SHA-256 verification
    - strict YAML and schema validation
    - path, duplicate, link, encryption, and size-limit checks
    - stage-specific path semantics
  non_goals:
    - correcting a package
    - creating outputs
    - importing constitutional substance
    - launching an LLM
  failure_modes:
    - missing, extra, duplicate, unsafe, encrypted, unreadable, or oversized member
    - hash or identity mismatch
    - prompt/envelope/control mismatch
    - invalid structured output
    - repository source mismatch during preparation/import
  tests:
    - exact KGR-005 prepared package
    - package conflict fixture
    - invalid output and invalid import fixtures
    - prompt/envelope mismatch
    - ZIP traversal, symlink, duplicate, encryption, and decompression-limit cases
```

The validator must distinguish `path`, `source_path`, and `package_member`. Isolated validation never requires repository custody paths. Preparation and import independently validate them. A package conflict is a valid non-completion attempt classification, not a completed result.

### 6.4 `apply_loop_transition.py`

```yaml
tool:
  name: apply_loop_transition.py
  purpose: Replay Controller history, validate one declared event or imported role result, simulate counters/guards/transition, and optionally create one immutable Controller record.
  inputs:
    - exact loop specification and validation profile
    - source run identity and role/mode
    - validated package evidence
    - imported result or typed event
    - prior Controller records
    - owner/research artifact for re-entry where applicable
  outputs:
    - canonical simulated transition JSON
    - optional immutable controller-transition.json
    - optional validation evidence
  read_paths:
    - governance/methodology/loops/**
    - governance/runs/*/controller/**
    - validated source package and evidence
    - explicit owner or research artifact for re-entry
  permitted_write_paths:
    - governance/runs/<source-run>/controller/controller-transition.json with --apply
    - governance/validation/records/GOV-VAL-###.json with --record --apply
  command_line_interface: "python3 governance/tools/apply_loop_transition.py import|event|reenter --loop PATH --source-run KGR-### --input PATH --history-root governance/runs [--authorization-ref REF] [--apply]"
  exit_codes:
    0: valid simulation or applied transition
    1: invalid result, state, history, counter, guard, or immutable-target conflict
    2: usage or operational failure
    3: valid proposed mutation stopped for missing explicit authorization reference
  deterministic_guarantees:
    - history replay rather than trusting mutable counters
    - counter increment only after valid completed import
    - exact signature and guard calculation
    - role-appropriate result enum
    - refuse overwrite and out-of-sequence run IDs
    - atomic publication of the new single record
  non_goals:
    - evaluating finding substance or severity
    - generating a role result
    - launching or resuming a model
    - updating constitutional text
    - opening Enforcement Engineering
  failure_modes:
    - missing prior transition
    - counter mismatch or history fork
    - wrong state/role/mode/result
    - matrix inconsistency
    - exhausted guard
    - missing authorization for mutation
  tests:
    - all 20 required synthetic fixtures
    - history fork and overwrite refusal
    - deterministic replay and signature tests
```

### 6.5 `build_run_package.py`

```yaml
tool:
  name: build_run_package.py
  purpose: Build a formal input or output ZIP only from an already-approved, complete, hash-bound package definition.
  inputs:
    - envelope or package definition
    - complete existing source files
    - package kind input|output
    - explicit output path
  outputs:
    - prospective manifest/hash in dry-run
    - canonical ZIP with --apply
  read_paths:
    - envelope-declared sources
    - versioned schema/profile files
  permitted_write_paths:
    - explicit --output path only with --apply
    - temporary staging directory
    - optional governance validation record
  command_line_interface: "python3 governance/tools/build_run_package.py --kind input|output --envelope PATH --output PATH [--authorization-ref REF] [--apply]"
  exit_codes:
    0: dry-run plan or package created
    1: incomplete, invalid, conflicting, or existing target
    2: usage or operational failure
    3: explicit authorization required for requested publication
  deterministic_guarantees:
    - lexicographic member order
    - ZIP_STORED entries
    - fixed 1980-01-01 ZIP timestamp
    - fixed regular-file permissions
    - empty archive comment and extra fields
    - source hashes reverified before and after staging
  non_goals:
    - generating substantive run outputs
    - instantiating KGR-006 without a valid trigger and approved contract
    - replacing the existing KGR-005 ZIP
    - launching an LLM
  failure_modes:
    - missing source
    - envelope/hash mismatch
    - unsafe member name
    - incomplete exact member set
    - target already exists
    - source changes during build
  tests:
    - two-build byte equality in different directories
    - source-mtime independence
    - exact member and permission metadata
    - overwrite refusal and mutation detection
```

The existing KGR-005 input ZIP remains preserved at its recorded hash. Canonical reproducible ZIP rules apply to future packages or an explicitly versioned replacement preparation, never silently to the current package.

### 6.6 `build_review_bundle.py`

```yaml
tool:
  name: build_review_bundle.py
  purpose: Build a reproducible, non-authoritative diff-review bundle for two explicit refs, directories, or packages.
  inputs:
    - base and candidate sources
    - allowlisted paths
    - optional validation reports
    - explicit output path
  outputs:
    - canonical ZIP containing manifest.json, hashes, unified diffs, and selected artifacts
  read_paths:
    - explicit base/candidate paths or git refs
    - allowlisted repository files
  permitted_write_paths:
    - explicit --output path with --apply
    - temporary staging directory
  command_line_interface: "python3 governance/tools/build_review_bundle.py --base REF_OR_PATH --candidate REF_OR_PATH --paths PATH... --output PATH [--apply]"
  exit_codes:
    0: dry-run or bundle created
    1: unsafe path, invalid source, conflict, or existing target
    2: usage or operational failure
  deterministic_guarantees:
    - stable path order and unified-diff parameters
    - canonical manifest JSON
    - canonical ZIP metadata
    - exact input hashes and no network access
  non_goals:
    - deciding review acceptance
    - changing repository state
    - including secrets or undeclared files
    - replacing formal run packages
  failure_modes:
    - invalid git ref or path
    - binary/size policy violation
    - allowlist escape
    - source changes during build
  tests:
    - repeatability across directories and mtimes
    - path allowlist and traversal refusal
    - text, binary, add/delete, and line-ending cases
```

### 6.7 `manage_learning.py`

```yaml
tool:
  name: manage_learning.py
  purpose: Validate, create, append events to, index, and summarize professional learning records under one schema-aware interface.
  inputs:
    - failure-record draft or command fields
    - event draft
    - existing records and events
    - failure and event schemas
  outputs:
    - canonical validation/duplicate report
    - optional new record or event
    - regenerated index and category summary
  read_paths:
    - governance/learning/**
    - governance/schemas/failure-record*.schema.json
    - evidence paths explicitly referenced by a draft
  permitted_write_paths:
    - governance/learning/records/HP-FAIL-###.yaml
    - governance/learning/events/HP-FAIL-###/HP-FAIL-###-E###.yaml
    - governance/learning/FAILURE_AND_LESSONS_INDEX.md
    - governance/learning/summaries/lessons-by-category.md
  command_line_interface: "python3 governance/tools/manage_learning.py validate|record|event|index|summarize ... [--apply]"
  exit_codes:
    0: valid dry-run or applied operation
    1: schema, duplicate, transition, evidence, or immutable-history failure
    2: usage or operational failure
    3: incident/owner-decision routing required before record mutation
  deterministic_guarantees:
    - single-writer monotonic IDs
    - strict YAML and schema validation
    - deterministic duplicate fingerprint
    - event replay and generated-view ordering
    - atomic single-file writes and staged generated-view replacement
  non_goals:
    - deciding whether a material event is an incident
    - accepting risk
    - fabricating missing evidence or costs
    - editing validated base records
  failure_modes:
    - ID race or collision
    - duplicate candidate
    - invalid status event
    - unresolved evidence locator
    - manual generated-index drift
  tests:
    - every classification's mandatory fields
    - duplicate and subfinding routing
    - status/event transitions
    - validated-record immutability
    - accepted-risk requirements
    - deterministic index and summary generation
```

## 7. CLI contracts

All CLIs share these conventions:

- `--help` exits 0 and documents inputs, writes, exit codes, and authority limits.
- Read-only behavior is the default.
- State-changing commands require `--apply`; absence of `--apply` emits the exact prospective result and writes nothing.
- A governance-state mutation also requires `--authorization-ref`; `--apply` without it exits 3.
- Diagnostics go to stderr; canonical result data goes to stdout.
- Paths are resolved without following an allowlist escape.
- Existing immutable targets are never overwritten.
- Validation evidence is opt-in through `--record --apply` and receives a monotonic `GOV-VAL-###` ID.
- No command accesses the network or calls an LLM.

Representative contracts:

```bash
# Static loop validation
python3 governance/tools/validate_closure_loop.py \
  --loop governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml

# Validate the prepared KGR-005 transport as isolated input
python3 governance/tools/validate_run_package.py \
  --stage isolated-input \
  --role adversary \
  --package /home/sugar/Downloads/KGR-005-formal-input-package.zip \
  --envelope governance/runs/KGR-005-kernel-adversary-targeted-closure/input-envelope.yaml \
  --prompt-snapshot governance/runs/KGR-005-kernel-adversary-targeted-closure/prompt/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md

# Simulate a result import; no write
python3 governance/tools/apply_loop_transition.py import \
  --loop governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml \
  --source-run KGR-005 \
  --input /path/to/validated/result-package.zip \
  --history-root governance/runs

# Apply only after separate explicit authorization
python3 governance/tools/apply_loop_transition.py import ... \
  --authorization-ref OWNER-AUTH-REF \
  --apply

# Rebuild generated learning views without changing records
python3 governance/tools/manage_learning.py index
python3 governance/tools/manage_learning.py summarize
```

Canonical validation evidence contains tool name/version, repository HEAD, invocation mode, subject identities and hashes, validation profile versions, ordered findings, result, write status, and authority disclaimer. It excludes private reasoning, secrets, absolute local paths where a repository-relative or package-member locator is sufficient, and fabricated execution metadata.

## 8. State and transition integration

### 8.1 Source of machine state

Do not introduce a mutable “current counters” file as a second source of truth. Derive machine state by replaying immutable Controller transition records in run order.

The initial state for `GOV-LOOP-001` is the validated KGR-005 envelope/control snapshot:

```yaml
state: READY_FOR_TARGETED_CLOSURE
counters:
  completed_targeted_closure_runs: 0
  completed_designer_remediation_runs: 0
```

Each valid completed import creates exactly one record at:

```text
governance/runs/<source-run>/controller/controller-transition.json
```

No record is created for package conflict, invalid output, invalid import, pause, interruption, or abandoned pre-completion work. Those create validation/attempt evidence only and preserve state/counters.

`CURRENT_STATE.md` is the durable human-readable view. After an authorized valid import, the Controller record, run manifest, artifact registry, current state, and applicable master-plan status must be updated in one reviewed commit. The transition record is the machine evidence; the documents must not contradict it.

### 8.2 Starting and importing a run

The ready-to-active transition is a real execution-state event, not package creation. The tool may record it only after an operator confirms that the separately authorized external execution actually began. It never launches the model.

A completed result import requires an active state. If no execution-start evidence exists, import fails rather than inferring that a prepared package was executed. Synthetic fixtures may provide an explicit synthetic active state.

### 8.3 Deterministic result validation

The Controller validates that:

- the selected result is role-appropriate;
- exactly one result is present;
- selected priority and result agree with the pinned matrix;
- all higher-priority condition identifiers are accounted for;
- finding arrays reconcile across the required output files;
- closure requirements and blocking-severity rules reconcile with the declared verdict facts;
- counters supplied by the role equal replayed counters before import;
- Controller fields were left pending by the role;
- prompt, protocol, loop, run, package, and authority identities match.

The Controller does not decide whether constitutional wording is adequate, whether a scenario substantively passed, or whether evidence really resolves a constitutional value conflict. It validates the role's structured declarations and cross-file consistency. False substantive declarations remain a review-quality problem, not something deterministic code can discover by semantic judgment.

### 8.4 Counters, guards, and run sequence

After a valid Adversary import, increment the targeted-closure counter before limit and guard evaluation. After a valid Designer remediation import, increment the remediation counter, including valid owner-decision, research, or redesign results.

The maximum sequence is exactly:

```text
KGR-005 TARGETED_CLOSURE #1
KGR-006 DESIGNER_REMEDIATION #1
KGR-007 TARGETED_CLOSURE #2
KGR-008 DESIGNER_REMEDIATION #2
KGR-009 TARGETED_CLOSURE #3
```

Only `READY_FOR_TARGETED_CLOSURE` permits preparation of another Adversary run. Attempted fourth closure or third remediation preparation is refused without inventing a transition absent from the loop. If KGR-009 validly requires remediation, the specified post-import transition is `LOOP_LIMIT_REACHED`.

The blocking-finding signature is canonical compact JSON, sorted exactly as the loop specifies, hashed with lowercase SHA-256. The no-progress guard compares two consecutive valid targeted closures, each following distinct valid remediations. The reappearance guard counts the same original ID reopened in two distinct valid closure runs with at least one valid remediation between.

### 8.5 Re-entry and exits

Owner-decision re-entry requires a new explicit formal owner-decision artifact. Research re-entry requires a new formal applicable research/evidence artifact. The Controller validates identity, applicability declaration, and allowed routing; it does not author the decision or research conclusion.

`STRUCTURAL_REDESIGN_REQUIRED` exits this bounded loop. Continuing requires a new or revised versioned protocol. `LOOP_LIMIT_REACHED` requires explicit Project Owner authorization and a versioned process decision. Neither condition auto-continues.

## 9. Test and fixture matrix

Fixture files are executable YAML inputs to the transition simulator. Every fixture sets `owner_authorization_required: true` because any subsequent execution, correction/resumption, re-entry, or state mutation remains human-gated even when the expected transition is deterministic.

```yaml
fixtures:
  - fixture: 01 valid KGR-005 CLOSURE_CONFIRMED
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: CLOSURE_CONFIRMED
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: CLOSURE_CONFIRMED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 02 first DESIGNER_REMEDIATION_REQUIRED
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: DESIGNER_REMEDIATION_REQUIRED
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: DESIGNER_REMEDIATION_REQUIRED
    expected_next_role: Kernel Designer
    expected_next_mode: CLOSURE_REMEDIATION
    owner_authorization_required: true

  - fixture: 03 owner decision required from Adversary
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: OWNER_DECISION_REQUIRED
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: OWNER_DECISION_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 04 research required from Adversary
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: RESEARCH_REQUIRED
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: RESEARCH_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 05 structural redesign required from Adversary
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: STRUCTURAL_REDESIGN_REQUIRED
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: STRUCTURAL_REDESIGN_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 06 package conflict before substantive execution
    input_state: READY_FOR_TARGETED_CLOSURE
    input_result: BLOCKED_BY_PACKAGE_CONFLICT_MEMBER_HASH_MISMATCH
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_PRE_SUBSTANTIVE_NON_COMPLETION
    expected_counters_after: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    expected_transition: READY_FOR_TARGETED_CLOSURE
    expected_next_role: Kernel Adversary
    expected_next_mode: TARGETED_CLOSURE
    owner_authorization_required: true

  - fixture: 07 invalid output package
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: INVALID_OUTPUT_PACKAGE
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: INVALID_NON_COMPLETION
    expected_counters_after: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    expected_transition: TARGETED_CLOSURE_IN_PROGRESS
    expected_next_role: Kernel Adversary
    expected_next_mode: TARGETED_CLOSURE
    owner_authorization_required: true

  - fixture: 08 invalid repository import
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: INVALID_IMPORT
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: INVALID_NON_COMPLETION
    expected_counters_after: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    expected_transition: TARGETED_CLOSURE_IN_PROGRESS
    expected_next_role: Kernel Adversary
    expected_next_mode: TARGETED_CLOSURE
    owner_authorization_required: true

  - fixture: 09 successful Designer remediation
    input_state: DESIGNER_REMEDIATION_IN_PROGRESS
    input_result: READY_FOR_TARGETED_CLOSURE
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    history: [KGR-005:DESIGNER_REMEDIATION_REQUIRED]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    expected_transition: READY_FOR_TARGETED_CLOSURE
    expected_next_role: Kernel Adversary
    expected_next_mode: TARGETED_CLOSURE
    owner_authorization_required: true

  - fixture: 10 Designer owner decision required
    input_state: DESIGNER_REMEDIATION_IN_PROGRESS
    input_result: OWNER_DECISION_REQUIRED
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    history: [KGR-005:DESIGNER_REMEDIATION_REQUIRED]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    expected_transition: OWNER_DECISION_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 11 Designer research required
    input_state: DESIGNER_REMEDIATION_IN_PROGRESS
    input_result: RESEARCH_REQUIRED
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    history: [KGR-005:DESIGNER_REMEDIATION_REQUIRED]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    expected_transition: RESEARCH_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 12 Designer structural redesign required
    input_state: DESIGNER_REMEDIATION_IN_PROGRESS
    input_result: STRUCTURAL_REDESIGN_REQUIRED
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    history: [KGR-005:DESIGNER_REMEDIATION_REQUIRED]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    expected_transition: STRUCTURAL_REDESIGN_REQUIRED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 13 third closure still requires remediation
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: DESIGNER_REMEDIATION_REQUIRED
    counters_before: {completed_targeted_closure_runs: 2, completed_designer_remediation_runs: 2}
    history: [KGR-005:REMEDIATION, KGR-006:READY, KGR-007:REMEDIATION, KGR-008:READY]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 3, completed_designer_remediation_runs: 2}
    expected_transition: LOOP_LIMIT_REACHED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 14 attempt to prepare a fourth targeted closure
    input_state: READY_FOR_TARGETED_CLOSURE
    input_result: PREPARE_TARGETED_CLOSURE_ORDINAL_4
    counters_before: {completed_targeted_closure_runs: 3, completed_designer_remediation_runs: 2}
    history: [KGR-005, KGR-006, KGR-007, KGR-008, KGR-009]
    expected_validity: REFUSED_BY_RUN_LIMIT
    expected_counters_after: {completed_targeted_closure_runs: 3, completed_designer_remediation_runs: 2}
    expected_transition: NO_TRANSITION_STATE_UNCHANGED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 15 attempt to prepare a third remediation
    input_state: DESIGNER_REMEDIATION_REQUIRED
    input_result: PREPARE_DESIGNER_REMEDIATION_ORDINAL_3
    counters_before: {completed_targeted_closure_runs: 2, completed_designer_remediation_runs: 2}
    history: [KGR-005, KGR-006, KGR-007, KGR-008]
    expected_validity: REFUSED_BY_RUN_LIMIT
    expected_counters_after: {completed_targeted_closure_runs: 2, completed_designer_remediation_runs: 2}
    expected_transition: NO_TRANSITION_STATE_UNCHANGED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 16 repeated reopened finding threshold
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: DESIGNER_REMEDIATION_REQUIRED_WITH_KA-F-003_REOPENED
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    history: [KGR-005:KA-F-003_REOPENED, KGR-006:VALID_REMEDIATION]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 2, completed_designer_remediation_runs: 1}
    expected_transition: LOOP_LIMIT_REACHED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 17 no-progress signature threshold
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: DESIGNER_REMEDIATION_REQUIRED_WITH_IDENTICAL_BLOCKING_SIGNATURE
    counters_before: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 1}
    history: [KGR-005:SIGNATURE_A_COUNT_2, KGR-006:VALID_REMEDIATION]
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 2, completed_designer_remediation_runs: 1}
    expected_transition: LOOP_LIMIT_REACHED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 18 LOW non-blocking new finding
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: CLOSURE_CONFIRMED_WITH_BOUNDED_NON_BLOCKING_LOW_FINDING
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: CLOSURE_CONFIRMED
    expected_next_role: null
    expected_next_mode: null
    owner_authorization_required: true

  - fixture: 19 blocking MEDIUM regression finding
    input_state: TARGETED_CLOSURE_IN_PROGRESS
    input_result: DESIGNER_REMEDIATION_REQUIRED_WITH_BLOCKING_MEDIUM_REGRESSION
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_COMPLETED_IMPORT
    expected_counters_after: {completed_targeted_closure_runs: 1, completed_designer_remediation_runs: 0}
    expected_transition: DESIGNER_REMEDIATION_REQUIRED
    expected_next_role: Kernel Designer
    expected_next_mode: CLOSURE_REMEDIATION
    owner_authorization_required: true

  - fixture: 20 prompt/envelope identity mismatch
    input_state: READY_FOR_TARGETED_CLOSURE
    input_result: BLOCKED_BY_PACKAGE_CONFLICT_PROMPT_ENVELOPE_IDENTITY_MISMATCH
    counters_before: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    history: []
    expected_validity: VALID_PRE_SUBSTANTIVE_NON_COMPLETION
    expected_counters_after: {completed_targeted_closure_runs: 0, completed_designer_remediation_runs: 0}
    expected_transition: READY_FOR_TARGETED_CLOSURE
    expected_next_role: Kernel Adversary
    expected_next_mode: TARGETED_CLOSURE
    owner_authorization_required: true
```

Additional mutation tests must independently cover every static invariant rather than relying only on the 20 scenario fixtures. Invalid fixtures must declare an expected diagnostic token, following the repository's existing test convention.

## 10. Existing failures to migrate

The observations supplied for GOV-4 should be grouped by systemic cause, not converted into one file per conversational correction.

### HP-FAIL-001 — Closure-loop control contract was initially under-specified

Proposed classification: `NEAR_MISS`, `AMBIGUITY`, `PROCESS_DEFECT`. Proposed severity: `HIGH`.

Subfindings:

- under-specified persistent-state model;
- missing Designer remediation exits;
- ambiguous counter increment and guard semantics;
- Adversary and Controller responsibilities conflated;
- known control ambiguities classified prematurely as non-blocking.

Systemic cause: natural-language orchestration was treated as sufficiently executable before closed states, exact authority separation, event typing, and guard semantics were reconciled.

Reusable lesson: a governance loop must be statically validated as a closed transition contract before any run is prepared against it.

### HP-FAIL-002 — Formal package identity and path semantics were incomplete

Proposed classification: `NEAR_MISS`, `PROCESS_DEFECT`, `TOOLING_GAP`. Proposed severity: `HIGH`.

Subfindings:

- repository custody paths confused with ZIP package members;
- package-conflict semantics conflated with completed runs;
- prompt/envelope binding incomplete.

Systemic cause: preparation, isolated execution, and repository import were not modeled as three distinct validation contexts.

Reusable lesson: every formal input needs explicit custody path, provenance source path, transport member, hash, and stage-specific validation responsibility.

### HP-FAIL-003 — High-capability models were used repeatedly for deterministic work

Proposed classification: `COST_WASTE`, `TOOLING_GAP`, `PROCESS_DEFECT`. Proposed severity: `MEDIUM`.

Subfindings:

- repeated high-capability-model use for hashing, counting, package inspection, and matrix checking;
- deterministic checks repeatedly performed by LLMs.

Systemic cause: the governance process accumulated contracts before acquiring small deterministic validators and builders.

Reusable lesson: route exact parsing, identity, count, diff, signature, counter, and packaging work to offline scripts; reserve model reasoning for constitutional judgment.

Cost must be recorded as unavailable or estimated unless exact usage is preserved. Observable model-run and rework counts are acceptable substitutes.

### HP-FAIL-004 — Learning evidence was dispersed across temporary surfaces

Proposed classification: `PROCESS_DEFECT`, `TOOLING_GAP`, `NEAR_MISS`. Proposed severity: `MEDIUM`.

Subfindings:

- lessons dispersed across temporary parking-lot files;
- session logs used as the only location for reusable learning;
- no deterministic index or duplicate detection.

Systemic cause: no durable record class existed between operational chronology, decisions, and formal run evidence.

Reusable lesson: material learning requires individual structured records, append-only events, and generated indexes, while logs remain chronology only.

### HP-FAIL-005 — Project Owner correction withdrew commit authorization

Proposed classification: `OWNER_CORRECTION`, `NEAR_MISS`, and, if supported by evidence, `PROCESS_DEFECT`. Proposed severity: `HIGH`.

Systemic cause candidate: authorization scope or persistence was assumed beyond the Owner's current instruction.

Reusable lesson: repository mutation and every publication step require current explicit authorization; a prior or anticipated approval is not reusable authority.

This record requires special evidence discipline. The correction is asserted in the current architecture task context but no repository-preserved conversation transcript was discovered. Migration must either reference a preserved owner statement or mark the evidence `NOT_PRESERVED` and obtain Project Owner confirmation of the concise factual record. It must not fabricate a quote or execution attempt.

### Migration evidence boundary

The final loop and KGR-005 contracts prove the corrected architecture, but Git history does not independently prove every intermediate conversational failure. Bootstrap records must distinguish repository-evidenced facts from Project Owner-supplied migration facts. Record creation should wait for explicit approval of the grouping and evidence limitations.

## 11. Exact affected-file plan

No file in this plan is created by this architecture pass. The proposed implementation scope is:

```text
AGENTS.md
governance/AGENTS.md
governance/ARTIFACT_REGISTRY.yaml
governance/CURRENT_STATE.md                  # tooling availability only; no gate advancement
governance/DECISION_LOG.md                   # only if Owner adopts the architecture/process decision
governance/methodology/README.md
governance/methodology/project-operating-contract.md

governance/learning/README.md
governance/learning/FAILURE_AND_LESSONS_INDEX.md
governance/learning/records/HP-FAIL-001.yaml
governance/learning/records/HP-FAIL-002.yaml
governance/learning/records/HP-FAIL-003.yaml
governance/learning/records/HP-FAIL-004.yaml
governance/learning/records/HP-FAIL-005.yaml
governance/learning/events/.gitkeep            # omit if empty directories are not retained
governance/learning/summaries/lessons-by-category.md

governance/schemas/failure-record.schema.json
governance/schemas/failure-record-event.schema.json
governance/schemas/governance-validation-record.schema.json
governance/schemas/controller-transition.schema.json
governance/schemas/kernel-design-closure-loop.schema.json
governance/schemas/protocols/GOV-PROTOCOL-002/0.1.0/finding-closure-verdicts.schema.json
governance/schemas/protocols/GOV-PROTOCOL-002/0.1.0/closure-result.schema.json
governance/schemas/protocols/GOV-PROTOCOL-003/0.1.0/designer-remediation-result.schema.json

governance/tools/validate_closure_loop.py
governance/tools/validate_run_package.py
governance/tools/apply_loop_transition.py
governance/tools/build_run_package.py
governance/tools/build_review_bundle.py
governance/tools/manage_learning.py
governance/tools/_lib/__init__.py
governance/tools/_lib/canonical.py
governance/tools/_lib/strict_yaml.py
governance/tools/_lib/safe_zip.py
governance/tools/_lib/schemas.py
governance/tools/_lib/atomic.py

governance/validation/README.md
governance/validation/records/.gitkeep          # omit if no initial evidence is committed

governance/tests/run-tests.sh
governance/tests/fixtures/loop-spec/**
governance/tests/fixtures/run-packages/**
governance/tests/fixtures/transitions/01-valid-kgr-005-closure-confirmed.yaml
governance/tests/fixtures/transitions/02-first-designer-remediation-required.yaml
governance/tests/fixtures/transitions/03-adversary-owner-decision.yaml
governance/tests/fixtures/transitions/04-adversary-research.yaml
governance/tests/fixtures/transitions/05-adversary-structural-redesign.yaml
governance/tests/fixtures/transitions/06-package-conflict.yaml
governance/tests/fixtures/transitions/07-invalid-output-package.yaml
governance/tests/fixtures/transitions/08-invalid-import.yaml
governance/tests/fixtures/transitions/09-successful-designer-remediation.yaml
governance/tests/fixtures/transitions/10-designer-owner-decision.yaml
governance/tests/fixtures/transitions/11-designer-research.yaml
governance/tests/fixtures/transitions/12-designer-structural-redesign.yaml
governance/tests/fixtures/transitions/13-third-closure-remediation.yaml
governance/tests/fixtures/transitions/14-fourth-closure-refused.yaml
governance/tests/fixtures/transitions/15-third-remediation-refused.yaml
governance/tests/fixtures/transitions/16-repeated-reopened-finding.yaml
governance/tests/fixtures/transitions/17-no-progress-signature.yaml
governance/tests/fixtures/transitions/18-low-nonblocking-new-finding.yaml
governance/tests/fixtures/transitions/19-medium-blocking-regression.yaml
governance/tests/fixtures/transitions/20-prompt-envelope-mismatch.yaml
governance/tests/fixtures/learning/**

.github/workflows/governance-tooling-ci.yml
```

Do not modify these bound historical/current artifacts in the initial implementation:

```text
governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml
governance/runs/KGR-005-kernel-adversary-targeted-closure/**
governance/methodology/roles/kernel-adversary/protocols/targeted-closure/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md
governance/methodology/roles/kernel-designer/protocols/closure-remediation/06-kernel-designer-closure-remediation-prompt-sol-high-v0.1.0.md
```

The new schemas are enforcement profiles for the existing versioned contracts, not silent edits to those contracts. If schema authoring exposes a real contract ambiguity that cannot be represented without adding semantics, stop and propose a new protocol/loop version rather than guessing.

Do not add general tooling checksums to `SOURCE_CHECKSUMS.sha256`; that file is primarily source/snapshot custody. Git, tests, registry identity, and validation records provide code integrity. Add a checksum entry only when a specific bound run snapshot contract requires it.

## 12. Dependency strategy

Use only:

- Python standard library: `argparse`, `dataclasses`, `datetime`, `hashlib`, `json`, `os`, `pathlib`, `re`, `shutil`, `stat`, `subprocess`, `tempfile`, and `zipfile`;
- existing PyYAML for parsing, with a custom loader that rejects duplicate keys;
- existing jsonschema for draft 2020-12 instance validation;
- installed Git for read-only ref/diff operations in review bundles.

No new dependency is justified.

Do not reuse `scripts/lib/schema-validate.py` directly for governance contracts because its duplicate-key behavior is weaker than KGR-005 requires. Do not change that runtime helper merely to serve this capability; a governance-local strict loader avoids an unrelated runtime behavior change.

Do not use a YAML canonicalization library. Use canonical JSON for hashes and generated machine records. Preserve source YAML bytes for custody and validate parsed structure separately.

Use `ZIP_STORED` rather than compressed entries for canonical future packages. This trades file size for reproducible bytes across zlib/runtime versions. If compression becomes materially necessary later, it requires a separately specified reproducibility contract.

CI installs the same two existing Python dependencies and runs fully offline. No model SDK, network client, database, task queue, or multi-agent framework is needed.

## 13. Security and integrity risks

1. **ZIP traversal or link escape.** Reject absolute paths, `..`, empty segments, backslashes as ambiguous separators, duplicate normalized members, symlinks, devices, and encrypted entries. Extract only into a fresh temporary directory.
2. **Decompression/resource abuse.** Enforce maximum member count, per-member uncompressed bytes, total uncompressed bytes, and compression-ratio policy before extraction.
3. **TOCTOU source mutation.** Hash every source before staging and again immediately before publication; abort if any value changes.
4. **Partial writes.** Write new single files to a same-directory temporary file, fsync, and `os.replace`; refuse existing immutable targets. Multi-file generated views are staged and validated before individual replacement, with a detectable generation digest.
5. **History fork.** Replay all prior Controller records and require a single contiguous run/counter chain. Reject duplicate source runs or conflicting transitions.
6. **Authority inflation.** Every report and generated artifact carries `constitutional_authority: NONE` or equivalent boundary language. `CLOSURE_CONFIRMED` never maps automatically to ratification, adoption, or Enforcement readiness.
7. **Semantic overreach.** Matrix validation checks declared facts and structure only. Code never decides that constitutional evidence is sufficient.
8. **Prompt or envelope substitution.** Validate ID, protocol, version, mode, run, and SHA binding at the appropriate stages; a mismatch stops pre-substantively.
9. **Path-class confusion.** Keep repository custody path, source provenance path, and archive member as separate typed fields.
10. **Silent historical normalization.** Never rebuild or replace existing raw/bound ZIPs merely to make metadata canonical. New reproducibility applies prospectively.
11. **Evidence fabrication.** Learning records allow `NOT_PRESERVED`; tools never invent timestamps, token counts, transcripts, decisions, or validation.
12. **Generated view mistaken for authority.** Indexes and summaries include generated/non-authoritative headers and can be reproduced from source records.
13. **Unsafe external output.** Builders require an explicit output path and refuse overwrite. Repository publication remains a separate authorized action.
14. **Validation profile drift.** Profiles are keyed to exact loop/protocol versions. Unknown versions fail closed.
15. **Dry-run ambiguity.** Machine output includes `applied: false`; state-changing success includes `applied: true`, authorization reference, and created path.

## 14. Cost and model-routing implications

The proposed tools remove model use from:

- YAML/JSON parsing and schema checks;
- duplicate-key detection;
- archive inventory and safety checks;
- file hashing and identity binding;
- counter arithmetic and run ordinals;
- matrix/result consistency;
- blocking-finding signature calculation;
- repeated-finding and no-progress guards;
- deterministic package and review-bundle generation;
- learning-record indexing and summary grouping.

High-capability reasoning remains appropriate for:

- Kernel Designer constitutional drafting and remediation;
- independent Adversary closure judgment;
- Project Owner value choices, risk acceptance, sequencing, and ratification;
- architecture changes where contracts are genuinely ambiguous.

No tool launches an LLM automatically. No “cheap model fallback” is needed for deterministic work because local code is both cheaper and more reliable. Model routing belongs in external execution planning, not the Controller engine.

Where the execution environment exposes model and cost data, formal run manifests should record actual model identity, reasoning setting, token usage, and interaction counts. Where it does not, use `UNKNOWN`, `UNVERIFIED`, or `UNAVAILABLE`; do not estimate unless a documented method and range are useful.

Anti-recursion rule: a model may propose or review a deterministic test once, but repeated application is performed by the script. A model must not spawn further agents merely to re-check hashes, counts, schemas, or state transitions.

## 15. Implementation sequence and commit plan

The original five-commit sequence leaves tested behavior temporarily absent and combines learning contracts with unrelated operating instructions. Use seven smaller commits with tests landing alongside each behavior.

### Commit 1 — `docs(governance): define professional learning record contracts`

- Scope: learning README, record/event schemas, empty generated-view contracts, validation/immutability/status/evidence rules.
- Paths: `governance/learning/**`, `governance/schemas/failure-record*.schema.json`, registry entries as needed.
- Validation: schema meta-checks; example valid/invalid records can be fixtures but no recorder yet.
- Dependencies: none.
- Review/revert: independently reviewable and revertible.
- Intermediate contradiction: none; the system is explicitly `CONTRACT_DEFINED_TOOLING_NOT_YET_IMPLEMENTED`.

### Commit 2 — `docs(repo): establish durable project instruction hierarchy`

- Scope: root Codex rules, governance additions, canonical operating contract, methodology navigation.
- Paths: `AGENTS.md`, `governance/AGENTS.md`, `governance/methodology/project-operating-contract.md`, `governance/methodology/README.md`, registry/decision updates if approved.
- Validation: link/path checks; duplicate-rule review; precedence examples.
- Dependencies: Commit 1, so failure-registration instructions reference an existing contract.
- Review/revert: independently reviewable; reverting removes behavior rules without touching runtime.
- Intermediate contradiction: none if it describes tooling as required when available, not already implemented.

### Commit 3 — `feat(governance): add deterministic learning record management`

- Scope: strict YAML/canonical/schema/atomic shared helpers needed by learning; `manage_learning.py`; learning fixtures; governance test runner; governance CI workflow.
- Paths: learning-related `governance/tools/_lib/**`, `manage_learning.py`, `governance/tests/**`, `.github/workflows/governance-tooling-ci.yml`.
- Validation: valid/invalid classification fixtures, duplicate detection, status/event replay, immutable validated records, two-pass index/summary byte equality, clean-worktree assertion.
- Dependencies: Commit 1.
- Review/revert: independently reviewable and revertible; learning records remain readable manually if reverted.
- Intermediate contradiction: none.

### Commit 4 — `feat(governance): add closure-loop and run-package validators`

- Scope: loop and protocol enforcement schemas/profiles, strict validation, archive safety, validation evidence schema, static mutation fixtures.
- Paths: `validate_closure_loop.py`, `validate_run_package.py`, remaining shared helpers, loop/protocol schemas, validation README, test fixtures.
- Validation: every required loop invariant; exact KGR-005 prepared-input validation; unsafe ZIP and contract mismatch cases; no-write default.
- Dependencies: Commit 3 shared helpers/test runner.
- Review/revert: independently reviewable; no state mutation behavior included.
- Intermediate contradiction: none; validation availability does not claim loop execution.

### Commit 5 — `feat(governance): add Controller transition simulation and application`

- Scope: transition schema, immutable history replay, counters, matrices, signatures, guards, re-entry validation, all 20 fixtures.
- Paths: `apply_loop_transition.py`, `controller-transition.schema.json`, transition fixtures/tests.
- Validation: full 20-fixture matrix, history fork, overwrite refusal, missing authorization, replay determinism, state/counter reconciliation.
- Dependencies: Commit 4 validators and profiles.
- Review/revert: independently reviewable; existing run state is untouched until explicitly applied.
- Intermediate contradiction: none if current state continues to say no Controller record exists.

### Commit 6 — `feat(governance): add reproducible package and review builders`

- Scope: canonical future ZIP builder and non-authoritative review bundle builder.
- Paths: `build_run_package.py`, `build_review_bundle.py`, safe ZIP helper extensions, builder fixtures/tests.
- Validation: byte-equal builds in separate directories/mtimes/Python CI; metadata inspection; source mutation and overwrite refusal; exact member sets.
- Dependencies: Commit 4 validation profiles.
- Review/revert: independently reviewable.
- Intermediate contradiction: none; KGR-005's existing package remains untouched and explicitly excluded.

### Commit 7 — `docs(governance): migrate approved GOV-4 failure and lesson records`

- Scope: only Project Owner-approved bootstrap records/events and generated index/summary; registry and current-state note that learning migration occurred.
- Paths: `governance/learning/records/HP-FAIL-001.yaml` through approved final ID, possible events, generated views, registry.
- Validation: schemas, evidence resolution/limitations, duplicate scan, deterministic regeneration, no incident misclassification.
- Dependencies: Commits 1 and 3; Project Owner approval of grouping and evidence basis.
- Review/revert: independently reviewable; reverting removes migrated records but not the learning system.
- Intermediate contradiction: none if records distinguish repo evidence from owner-supplied facts.

Tests must not be deferred to a standalone later commit after feature code. Each feature commit carries its own fixtures and leaves CI green.

## 16. Decisions requiring Project Owner approval

1. Approve or revise the complete architecture scope and seven-commit sequence.
2. Decide whether implementation should occur before KGR-005 execution. The current durable next execution is KGR-005; this proposal cannot silently interpose tooling work.
3. Approve the external ChatGPT Project Instructions text and configure it outside Git if accepted.
4. Approve creation of root `AGENTS.md`, the governance additions, and `project-operating-contract.md` as the precedence hierarchy.
5. Approve the learning taxonomy, record/event immutability model, accepted-risk contract, and use of `governance/schemas/`.
6. Approve the five proposed bootstrap failure groupings and the evidence treatment for owner-supplied facts not preserved in repository history.
7. Confirm whether the withdrawn commit-authorization correction should be a HIGH standalone record and provide or approve its concise factual evidence statement.
8. Approve `governance/runs/<run>/controller/controller-transition.json` as the canonical Controller record path and canonical JSON as its format.
9. Approve `GOV-VAL-###` validation evidence IDs and the central `governance/validation/records/` location.
10. Approve prospective canonical ZIP rules and explicitly confirm that the existing KGR-005 ZIP must not be replaced.
11. Approve the boundary that tools validate declared constitutional facts but do not assess their substantive truth.
12. Decide whether the architecture adoption itself requires a new `GOV-DEC-015`; recommended: yes, because it establishes durable process, instruction, and evidence contracts.

None of these approvals constitutes KGR-005 execution, Kernel ratification, Enforcement Engineering authorization, or human ratification.

## 17. Explicit non-goals

- Executing, launching, resuming, simulating the substantive content of, or completing KGR-005.
- Automatically launching any LLM or building a general multi-agent framework.
- Evaluating constitutional wording, evidence sufficiency, scenario truth, proportionality, operability, or risk acceptance.
- Editing the Kernel or changing finding severity.
- Creating KGR-006 before a valid `DESIGNER_REMEDIATION_REQUIRED` import and separately approved concrete contract.
- Rebuilding or replacing the existing KGR-005 formal ZIP.
- Rewriting any completed run, output, prompt, raw source, or historical result.
- Opening Enforcement Engineering, starting ratification, adopting the Kernel, or claiming enforceability, implementation, operation, compliance, or maturity.
- Replacing root `scripts/validate.sh` or extending governance tooling into a general client-repository runtime.
- Introducing a database, service, network dependency, model SDK, queue, daemon, or web UI.
- Automatically accepting risk, merging duplicate learning records, deciding incident classification, or making owner decisions.
- Auto-committing, staging, pushing, opening PRs, merging, tagging, releasing, or publishing.
- Treating generated indexes, summaries, validation reports, packages, or review bundles as authority.
- Fabricating token usage, timestamps, execution transcripts, model identity, owner statements, validation, or closure evidence.

## 18. Validation plan

Implementation is complete only when all of the following pass.

### Static and schema validation

- Python syntax via `ast.parse`, with no bytecode residue.
- Bash syntax for the governance test runner.
- JSON Schema draft 2020-12 meta-validation and versioned `$id` checks.
- Strict YAML duplicate-key rejection tests.
- All valid fixtures pass; every invalid fixture fails for its declared reason.
- Markdown links, registered paths, IDs, and generated references resolve.

### Loop contract validation

- Every required loop-validation item listed in the architecture task has at least one positive assertion and one targeted negative mutation where meaningful.
- Adversary and Designer matrices are independently checked for exact priority, enum, exclusivity, and routing.
- Unknown loop/protocol versions fail closed.
- The canonical loop and KGR-005 control snapshot validate identically without modifying either.

### Package validation

- The existing KGR-005 input package validates at its recorded 19 members and hash.
- Preparation, isolated-input, output, and import modes exercise different path responsibilities.
- Missing/extra/duplicate members, hash conflicts, prompt binding conflicts, traversal, absolute paths, backslashes, symlinks, devices, encryption, unreadable UTF-8 where required, excessive size, and decompression ratio all fail safely.
- Validation never extracts into the repository.

### Transition validation

- All 20 required fixtures pass exactly.
- Counters increment only on valid completed imports.
- Package conflict, invalid output, invalid import, pause, interruption, and aborted pre-completion attempts consume nothing.
- Both guard signatures are stable across dictionary/list input ordering.
- History forks, missing active-state evidence, wrong run ordinal, fourth closure, third remediation, overwrite, and missing authorization fail closed.
- Re-entry requires a new validated owner/research artifact.

### Reproducibility

- Build the same future test package twice in separate temporary roots with different filesystem mtimes; SHA-256 must match.
- Inspect member order, timestamp, permissions, compression method, comments, and extra fields.
- Build the same review bundle twice and compare bytes.
- Regenerate learning index and summary twice and compare bytes.

### Mutation and authority safety

- Every state-changing CLI writes nothing without `--apply`.
- Every governance-state apply exits 3 without `--authorization-ref`.
- Existing immutable targets are never overwritten.
- Failure injection during staging leaves no published partial target.
- Tools never modify the Kernel, bound KGR-005 tree, raw sources, or current state during tests.
- Tests leave the real repository status exactly as found.

### Integration and CI

- `governance/tests/run-tests.sh` passes locally and in a dedicated offline CI workflow.
- Existing `tests/run-tests.sh` remains green and behaviorally unchanged.
- CI uses no secrets, network calls beyond dependency setup, live CLI, or model.
- Final implementation review verifies changed paths against the authorized commit scope.
- A final `git status --short`, staged diff check, and repository checksum verification show no unintended drift.

## 19. Exact next action

The Project Owner reviews this proposed architecture, especially the sequencing conflict with the currently recorded KGR-005 next execution, the instruction hierarchy, the learning-record grouping/evidence limitations, the Controller record format/path, and the prospective-only reproducible ZIP rule.

If the architecture is accepted, the Project Owner should explicitly authorize or revise the implementation scope and identify whether Commit 1 begins before KGR-005. No implementation, repository mutation, or KGR execution follows from this document alone.

Status: READY_FOR_PROJECT_OWNER_ARCHITECTURE_REVIEW
Repository changes: NONE
Exact next action: Project Owner reviews the proposed architecture and explicitly authorizes or revises the implementation scope.
