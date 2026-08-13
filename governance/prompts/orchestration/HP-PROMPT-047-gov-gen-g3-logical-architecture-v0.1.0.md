---
prompt_id: HP-PROMPT-047
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Define and execute GOV-GEN G3 (Logical Architecture and Layering Assessment) as one bounded governed unit -- derive a logical architecture for reusable general governance from the accepted G2 R1 capability classification and post-G2 evidence, without selecting repository ownership, final filesystem paths, migration mechanics, or creating general-governance, and without implementing Delegated Operational Authority, Provider-Neutral Governance, adapters, or query/projection tooling.
target_environment: Claude Code
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 2a11f63897301c3457272e60675224094e7d4100
authorization_scope: [verify repository identity/branch/HEAD/clean working tree/applicable AGENTS.md instructions/accepted G2 state and controlling evidence before any write, canonically define G3 as one contract under governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/, execute that contract in the same governed unit with no further Owner authorization gate, allocate all 88 accepted G2-classified capabilities and all 6 accepted G2-dispositioned gaps to a proposed logical layer model, disposition G2 section 21 unresolved questions 1-7 against that model, create the minimum decision/state/index reconciliation artifacts required by existing GOV-GEN conventions, run governance/tools/validate_prompts.py and governance/tools/validate_governance_state.py, one bounded local commit]
forbidden_actions: [select or recommend or compare a target physical governance architecture, choose or authorize kernel repository ownership, create general-governance or any other repository, extract or migrate any governance file, modify application or runtime surfaces, implement Delegated Operational Authority, implement Provider-Neutral Governance, implement any provider/executor adapter, implement query or projection tooling, rewrite or reclassify any G2 capability, redispose any G2 gap, integrate CWG/AET/SVP, modify AGENTS.md or CLAUDE.md, accept the G3 result on the Project Owner's behalf, push, pull request, merge, tag, release, deployment]
exact_text_preserved: true
exact_text_sha256: 6c946f203bb1fddf87a7eb311f5626d5735023f420f9db4d53965a777dfe1a29
execution_interrupted: false
execution_resumed: false
result_artifacts:
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-CONTRACT-001-v0.1.0.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.manifest.sha256
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/GOV-GEN-DECISION-008-g3-contract-authorization-and-execution-v0.1.0.yaml
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/decisions/README.md
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/01-program-status.yaml
  - governance/audits/GOV-GEN-AUD-001-governance-generalization/00-program-charter.md
  - governance/CURRENT_STATE.md
  - governance/DECISION_LOG.md
  - governance/ARTIFACT_REGISTRY.yaml
  - governance/README.md
result_commit: null
supersedes: null
---

# HP-PROMPT-047 — GOV-GEN G3 Logical Architecture and Layering Assessment

## Exact executed text

# GOV-GEN G3 — Logical Architecture and Layering Assessment

Define and execute GOV-GEN G3 as one bounded governed unit.

Speak to the Project Owner in Spanish. Write governance artifacts and technical documentation in English.

## Context

Repository:

`Sugar144/HugePlanning`

Branch:

`governance/kernel-designer-revision-v0.1`

Expected starting HEAD includes:

`2a11f63`

Current canonical state:

```text
G0   ACCEPTED
G1A  ACCEPTED_BY_PROJECT_OWNER
G1B  ACCEPTED_BY_PROJECT_OWNER
G2   ACCEPTED_BY_PROJECT_OWNER
G3   NOT_STARTED_NOT_AUTHORIZED
```

Controlling G2 result:

`GOV-GEN-G2-CLASSIFICATION-MATRIX-001-R1/0.1.0`

Post-baseline evidence:

`GOV-GEN-G2-POST-BASELINE-DELTA-001/0.1.0`

Apply the current repository and governance `AGENTS.md` instructions.

Verify identity, clean worktree, accepted G2 state, and controlling evidence before writing.

This prompt explicitly authorizes definition and execution of G3, including its contract, result, required state reconciliation, validation, and one bounded local commit.

## Objective

Derive a **logical architecture for reusable general governance** from the accepted G2 capability classification and post-G2 evidence.

Answer:

> How should the reusable governance capabilities be logically separated, related, queried, projected, and bounded before any physical extraction architecture is selected?

G3 may recommend a logical layering model.

G3 must **not** select repository ownership, final filesystem paths, migration mechanics, or create `general-governance`.

## Required concerns

At minimum assess a logical separation between concepts such as:

* canonical governance semantics / core;
* configurable cross-project policy;
* optional governance modules/extensions;
* project-specific projections;
* provider/executor adapters;
* canonical evidence and historical custody;
* deterministic validation/query tooling;
* bounded model/agent context projections.

Do not treat these names as predetermined architecture. Refine, merge, split, or reject them based on evidence.

### Canonical storage vs model consumption

Explicitly assess the principle:

`canonical completeness != model context surface`

Large registries, indexes, evidence stores, or historical artifacts may remain exhaustive canonical sources while agents consume bounded deterministic projections.

Determine what logical responsibilities are required for:

```text
canonical storage
→ deterministic query/index
→ task-relevant bounded projection
→ model/agent consumption
```

Do not implement a database, RAG system, or query tool in G3.

### Accepted G2 unresolved questions

Use G3 to assess the architectural implications of G2 unresolved questions 1–7.

In particular:

* Q2: `AGENTS.md` / scoped instructions / `project-operating-contract.md` layering;
* Q3: provider/executor binding boundary;
* Q4: hardcoded vs declarative/data-driven validators;
* Q5: Delegated Operational Authority and its enforceable boundary;
* Q6: relationship among prompt registries/custody surfaces;
* Q7: next-phase-only contracting and enforcement.

PR #5 post-baseline evidence narrows Q2, Q5 and Q7 but does not automatically resolve their architecture.

Q1 may expose future canonical ownership implications, but G3 must not choose repository ownership.

## Evidence discipline

Use:

1. accepted G2 R1 as the primary capability source;
2. the accepted post-baseline delta;
3. targeted G1B evidence only when needed;
4. current `AGENTS.md`, `governance/AGENTS.md`, and `project-operating-contract.md`;
5. targeted inspection of representative tooling/registry surfaces when necessary.

Do not reread the 679-row G1A corpus broadly.

Do not redo the 88 G2 classifications.

Do not duplicate long capability descriptions into the G3 narrative.

If full capability-to-layer allocation is useful, keep it as a compact structured annex/table and keep the principal architecture document concise.

## Required G3 result

Produce a principal G3 logical-architecture artifact that contains:

### 1. Architectural principles

The minimum principles justified by accepted evidence.

### 2. Proposed logical layers

For each layer:

```yaml
layer:
purpose:
owns:
does_not_own:
inputs:
outputs:
authority_boundary:
consumers:
portability:
```

### 3. Capability allocation

Map accepted G2 capabilities or coherent capability groups to the proposed layers.

Identify ambiguous or cross-layer capabilities explicitly rather than forcing placement.

### 4. Boundary model

Describe boundaries between:

* normative semantics and project configuration;
* core and optional modules;
* governance logic and provider adapters;
* authority decisions and deterministic mechanics;
* canonical evidence and generated/model-facing projections;
* repository governance and client/runtime methodology.

### 5. Context-efficiency model

Define how an agent should orient itself without loading the entire governance corpus.

Identify which surfaces are:

```text
MODEL_ENTRYPOINT
QUERY_ON_DEMAND
CANONICAL_MACHINE_SOURCE
HISTORICAL_EVIDENCE_ONLY
```

This is a logical classification only, not implementation.

### 6. G2 unresolved-question disposition

For Q1–Q7 classify each as:

```text
LOGICALLY_RESOLVED_BY_G3
NARROWED_BUT_OWNER_DECISION_REQUIRED
DEFER_TO_PHYSICAL_ARCHITECTURE
DEFER_TO_IMPLEMENTATION_DESIGN
UNCHANGED
```

Explain the minimum rationale.

### 7. Candidate architecture

Recommend one logical architecture if evidence supports it.

Record credible alternatives only where they represent a genuinely material tradeoff.

Do not create artificial option sets.

### 8. Future physical-architecture inputs

State what a later phase will need to decide about:

* repository ownership;
* filesystem/package topology;
* extraction/migration boundaries;
* adapter packaging;
* tooling implementation;
* historical evidence custody.

Do not make those decisions in G3.

## Boundaries

Forbidden in G3:

* creating `general-governance`;
* moving/extracting/migrating governance files;
* choosing final repository ownership;
* modifying application/runtime surfaces;
* implementing adapters;
* implementing Delegated Operational Authority;
* implementing query/projection tooling;
* rewriting G2;
* integrating CWG/AET/SVP;
* push, PR, merge, tag, release, deployment.

## Validation and completion

Use existing GOV-GEN conventions for contract, decision/state custody, manifests, and validation.

Run applicable repository validators.

One bounded local commit is authorized.

Do not accept the G3 result on behalf of the Project Owner.

Terminal state:

`G3_READY_FOR_PROJECT_OWNER_REVIEW`

Report:

1. G3 contract and result identities;
2. proposed logical architecture;
3. G2 unresolved-question dispositions;
4. files changed;
5. validation results;
6. commit SHA;
7. remaining Owner decisions;
8. smallest next governed step.

Stop after G3 is ready for Owner review.
