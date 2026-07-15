# GOV-AUD-PROMPT-011 — Execute PASS-01 Repository Capability and Gap Audit

prompt_id: GOV-AUD-PROMPT-011
catalog_prompt_id: HP-PROMPT-024
version: 0.2.0
audit_id: GOV-AUD-001
audit_run_id: GOV-AUD-001-P01-R1
pass_id: PASS-01
role: Repository Capability and Gap Auditor
mode: REPOSITORY_FIRST_CAPABILITY_GAP_AUDIT
authority: PROJECT_OWNER_EXPLICIT
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_head: 2af090ccf00f2cf8fb6d49972f4dacf5e3ddea38

## Objective

Execute only PASS-01 of GOV-AUD-001.

Determine:

- what HugePlanning already supports;
- what work is repeatedly mechanical or unnecessarily semantic;
- what burdens, failures and gaps are demonstrated by repository evidence;
- what work should stop because existing mechanisms already solve it;
- which capability needs should be carried into later audit passes.

Produce a concise, evidence-backed capability inventory and ranked gap register.

Do not:

- execute PASS-02 or any later pass;
- perform broad external tooling research;
- select tools, graph technology, architecture or GOV-7 strategy;
- implement any recommendation;
- activate or implement GOV-7.

## Verified starting state

Expected repository state:

Branch:
governance/kernel-designer-revision-v0.1

HEAD:
2af090ccf00f2cf8fb6d49972f4dacf5e3ddea38

Kernel:
0.2.0 / RATIFIED
not implemented, enforceable or operational

GOV-5:
COMPLETED_CLOSED

GOV-6:
COMPLETED_CLOSED

OD-005:
RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION

OD-006:
UNRESOLVED_TRIGGER_GATED

GOV-7:
INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY

GOV-AUD-001:
PLANNED_NOT_EXECUTED

PASS-01:
PLANNED_NOT_EXECUTED

Passes executed:
0

Before analysis or modification:

1. Read the applicable repository instructions.
2. Verify:
   - current branch;
   - local HEAD;
   - remote HEAD;
   - local/remote alignment;
   - clean worktree;
   - empty staging area;
   - durable governance state;
   - audit state;
   - absence of identity conflicts.
3. Verify that these identities do not already exist:
   - GOV-AUD-001-P01-R1
   - GOV-AUD-AUTH-001
   - GOV-AUD-PROMPT-011
   - HP-PROMPT-024
4. Verify that PASS-01 remains unexecuted and that no conflicting PASS-01 run exists.

Stop without modification on:

- branch or HEAD mismatch;
- local/remote divergence;
- dirty worktree or staging;
- identity collision;
- conflicting authority;
- changed Kernel or phase state;
- evidence that GOV-7 has been activated;
- an already executed PASS-01.

Do not repair startup conflicts silently.

## Authority and scope

Authorized read-only analysis scope:

- governance/**
- planning/**
- product/** only where needed to identify existing capability or current boundaries
- repository runtime-support surfaces only where materially relevant

Authorized write scope:

- governance/audits/GOV-AUD-001-gov7-enablement/**
- governance/prompts/orchestration/**
- governance/ARTIFACT_REGISTRY.yaml
- existing audit indexes or status surfaces only when required to register this exact run

Do not modify:

- planning artifacts;
- product artifacts;
- runtime artifacts;
- Kernel artifacts;
- completed prompts;
- completed runs;
- completed evaluations;
- previous decisions;
- historical evidence.

## Run custody

Instantiate the PASS-01 run using the registered GOV-AUD-001 run and custody contracts.

Preserve before substantive analysis:

- Project Owner authorization;
- exact received prompt;
- exact prompt SHA-256;
- minimum input manifest;
- run manifest.

Use the existing audit run structure and lifecycle.

Do not restate or redesign the scaffold contracts.

Do not create fake output or evaluation artifacts.

### Authorization

Record authority equivalent to:

authorization_id: GOV-AUD-AUTH-001
version: 0.1.0
authority: PROJECT_OWNER
authorized_run: GOV-AUD-001-P01-R1
authorized_pass: PASS-01

authorized_actions:
  - inspect the declared read-only scope
  - execute PASS-01
  - create the four required outputs
  - validate them
  - register the run
  - create one bounded commit
  - push without force

not_authorized:
  - execute later audit passes
  - perform broad external research
  - activate or implement GOV-7
  - select architecture, graph technology or GOV-7 strategy
  - resolve OD-006
  - accept recommendations or risk
  - modify planning, product or runtime artifacts
  - open a pull request

### Exact prompt custody

Preserve this complete received prompt verbatim as the instantiated PASS-01 prompt.

Calculate and record its SHA-256 before substantive analysis.

Do not alter or overwrite the existing PASS-01 prompt template.

### Minimum input manifest

Include only inputs materially used to support a conclusion.

The manifest must include:

- repository;
- branch;
- starting local and remote HEAD;
- PASS-01 contract;
- audit charter, plan and status;
- exact prompt and authorization;
- current governance state and relevant decision records;
- relevant registries and validated indexes;
- KGR-006-R1 and ER-001 through ER-020 sources where actually used;
- S0a–S9 roadmap and architecture sources where actually used;
- learning records and work-unit evidence actually used;
- explicit exclusions;
- missing-data markers.

Do not inventory the entire repository by default.

## Analysis method

Use this order:

verified repository capability
→ demonstrated repetition, burden, failure or requirement
→ genuine gap or stop-doing conclusion
→ neutral capability need

Use the complete work unit:

input package
+ prompt contract
+ observable model or mode
+ execution
+ produced artifacts
+ deterministic validation
+ semantic or independent review
+ corrections
+ Owner intervention
+ final disposition

Do not start from a preferred framework, tool or architecture.

## 1. Capability inventory

Inspect only capability domains materially relevant to:

- GOV-7 enablement;
- repeated burden;
- recurring failures;
- cross-layer integration;
- prompt and execution custody;
- state and evidence control;
- stop-doing conclusions.

Relevant domains may include:

- prompt design, versioning and custody;
- authorization and formal runs;
- package preparation and import;
- hashes, inventories and byte identity;
- validation and evaluation;
- state reconciliation;
- review and decision packages;
- learning records;
- parsers and normalized data;
- schemas and validators;
- state machines, Controllers and loops;
- scripts, skills and hooks;
- deterministic queries;
- manual Owner operations;
- temporary or repeated commands;
- S0a–S9 assets;
- ER-001 through ER-020.

Do not create one capability record for every script, validator, schema or file.

Aggregate closely related mechanisms into capability families unless they differ materially in:

- ownership;
- failure history;
- authority;
- reuse value;
- adoption implication.

For each material capability family record:

- capability ID;
- label;
- concise description;
- owning component or path;
- evidence paths;
- current use;
- limitations;
- reuse assessment;
- whether an apparent gap is already solved by it.

Do not claim a capability merely because it appears in a plan or prompt.

Require implementation, execution or validated evidence.

## 2. Repeated-work and burden analysis

Identify only material repeated work.

Use these categories:

- REPEATED_MECHANICAL_WORK
- REPEATED_SEMANTIC_WORKFLOW
- REPEATED_OWNER_DECISION_WORK
- REPEATED_REPOSITORY_INSPECTION
- REPEATED_PROMPT_CONSTRUCTION
- REPEATED_STATE_RECONCILIATION
- REPEATED_VALIDATION_OR_PACKAGING

For each material item record:

- affected work-unit stages;
- observed occurrences or UNKNOWN;
- evidence;
- current actor;
- current burden;
- failure history;
- existing reusable mechanism;
- why repetition remains;
- whether it should be:
  - retained;
  - standardized;
  - automated;
  - researched;
  - stopped.

Do not infer exact historical:

- tokens;
- duration;
- cost;
- retries;
- tool calls;

when not captured.

## 3. Failure and learning analysis

Use existing learning evidence to identify:

- recurring defects;
- failed prevention;
- validation gaps;
- custody gaps;
- stale-state assumptions;
- authority confusion;
- avoidable model expense;
- repeated manual reconciliation.

Do not create new learning records merely because PASS-01 finds a gap.

Record uncaptured material issues as FOLLOW_UP_CANDIDATE unless an existing repository rule requires immediate capture.

## 4. Gap classification

Classify each material item as exactly one of:

- EXISTING_CAPABILITY
- PARTIAL_CAPABILITY
- DEMONSTRATED_GAP
- REQUIREMENT_WITHOUT_IMPLEMENTATION
- RESEARCH_REQUIRED
- OWNER_DECISION_REQUIRED
- NOT_A_GAP

A missing framework is not a gap.

A demonstrated gap must trace to at least one of:

- repository requirement;
- repeated failure;
- repeated burden;
- unavailable necessary capability;
- unresolved enforcement requirement;
- empirically justified risk.

## 5. Stop-doing analysis

Identify work that should stop because:

- an existing mechanism already solves it;
- it duplicates another artifact or validation;
- it creates ceremony without protective value;
- it repeatedly re-audits accepted evidence;
- it asks for unavailable historical metrics;
- it creates a new layer without a demonstrated controlling failure;
- deterministic work is repeatedly delegated to an LLM;
- it repeats repository inspection already represented by a validated index or manifest.

## 6. Neutral capability-need classification

Do not select tools or implementation mechanisms.

Classify candidate needs as:

- DETERMINISTIC_AUTOMATION_CANDIDATE
- REUSABLE_SEMANTIC_WORKFLOW_CANDIDATE
- EVENT_AUTOMATION_CANDIDATE
- QUERY_CAPABILITY_CANDIDATE
- HUMAN_JUDGMENT_REQUIRED
- RESEARCH_REQUIRED
- STOP_DOING
- NO_CHANGE_REQUIRED

These are preliminary need classes.

PASS-04 and PASS-05 will later determine whether any need should become:

- a script;
- a hook;
- a skill;
- a query layer;
- MCP;
- a workflow engine;
- another tool;
- no new tool.

## Ranking

Use two separate rankings.

### A. Evidence priority

Calculate:

frequency
× current burden
× failure risk

Use a declared ordinal 1–5 scale.

Record UNKNOWN where evidence is unavailable.

This ranking represents how material the demonstrated problem is.

### B. Preliminary leverage

Estimate provisionally:

expected reduction
÷ estimated solution burden

Use only:

- LOW
- MEDIUM
- HIGH
- UNKNOWN

Do not fabricate numerical precision.

Mark this estimate explicitly as provisional for PASS-04 and PASS-05.

Each gap entry must include:

- evidence-priority factors;
- evidence-priority score where calculable;
- preliminary leverage;
- confidence;
- missing-data markers;
- qualification where evidence is weak;
- strategy-neutral priority:

  - P0_BEFORE_MATERIAL_GOV_7_WORK
  - P1_FIRST_APPROVED_IMPLEMENTATION_INCREMENT
  - P2_AFTER_INITIAL_EMPIRICAL_EVIDENCE
  - DEFER
  - REJECT

A high ranking does not authorize implementation.

## Required outputs

Create exactly four substantive outputs:

1. output/01-verified-capability-inventory.yaml
2. output/02-repetition-waste-and-burden-analysis.md
3. output/03-ranked-gap-register.yaml
4. output/04-pass-01-findings-and-handoff.md

Do not duplicate detailed evidence across all four files.

Use YAML for detailed structured evidence.

Use Markdown for synthesis and explanation.

### 01-verified-capability-inventory.yaml

Include:

- capability families;
- evidence;
- current use;
- limitations;
- reuse assessment;
- apparent gaps already solved.

### 02-repetition-waste-and-burden-analysis.md

Include:

- material repeated mechanical work;
- material repeated semantic workflows;
- Owner burden;
- prompt and context burden;
- failure patterns;
- historical evidence limitations;
- neutral capability-need classes;
- stop-doing conclusions.

### 03-ranked-gap-register.yaml

Include:

- unique gap IDs;
- classification;
- evidence;
- evidence-priority factors;
- score where calculable;
- preliminary leverage;
- confidence;
- missing-data markers;
- neutral capability-need class;
- priority;
- dependencies;
- unresolved questions;
- authority boundary.

### 04-pass-01-findings-and-handoff.md

Keep concise.

Include:

- PASS-01 result;
- highest-confidence existing capabilities;
- highest-priority demonstrated gaps;
- strongest stop-doing conclusions;
- unavailable historical evidence;
- conflicts or ambiguities;
- bounded inputs for PASS-02;
- what remains unaccepted;
- Owner decisions, if any, required before PASS-02.

Material statements must use:

- VERIFIED_FACT
- INFERENCE
- PROPOSAL
- RECOMMENDATION
- OWNER_DECISION_REQUIRED
- DEFERRED
- REJECTED

## Validation

Create:

evaluation/pass-01-validation-report.yaml

Validate only what is affected by:

- PASS-01 run registration;
- authorization;
- prompt custody;
- input manifest;
- four PASS-01 outputs;
- audit status update;
- registry updates.

Validate at minimum:

- prompt and authorization identity;
- prompt SHA-256;
- input-manifest hashes;
- starting HEAD;
- required outputs;
- YAML and Markdown validity;
- unique capability and gap IDs;
- evidence-path existence;
- required ranking fields;
- ranking arithmetic where used;
- missing-data markers;
- required statement labels;
- no broad external-tool research;
- no tool selection;
- no graph implementation selection;
- no architecture selection;
- no GOV-7 strategy selection;
- no PASS-02 execution;
- no fake acceptance or independent evaluation;
- unchanged Kernel and governance-phase state;
- GOV-7 still inactive;
- OD-006 still unresolved;
- no planning, product or runtime modifications.

Run:

1. existing GOV-AUD-001 scaffold validation;
2. minimum directly applicable PASS-01 validation;
3. prompt-custody and registry validation affected by this run;
4. state validation only where status surfaces changed.

Run the full governance suite only if:

- shared validator, schema, registry or state logic is modified; or
- an existing repository contract requires it; or
- targeted validation indicates a cross-surface regression risk.

Do not create:

- a review bundle;
- an independent evaluation;
- new schemas;
- new validation infrastructure;

unless an existing mandatory contract requires them.

## Status and registration

If execution and validation succeed:

- mark PASS-01:
  EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION
  or the closest repository-valid equivalent;

- record exactly one audit pass executed;
- keep CHECKPOINT-A pending;
- keep PASS-02 unexecuted;
- keep GOV-7 inactive;
- keep recommendations unaccepted;
- keep implementation unauthorized.

Register only:

- run identity;
- authorization;
- instantiated prompt;
- four outputs;
- validation report;
- required audit status and registry changes.

Do not mark the overall audit completed.

## Stopping conditions

Stop before commit and push if:

- startup verification fails;
- authority or identity conflict exists;
- required canonical inputs are unavailable;
- evidence cannot distinguish facts from inference;
- broad external research becomes necessary;
- a write outside authorized scope is required;
- output validation fails;
- a material defect makes the ranking unreliable;
- Kernel or phase state changes;
- GOV-7 activation or implementation is detected.

Preserve diagnostics and report the blocker.

Do not fabricate a successful result.

## Prohibited actions

Do not:

- execute PASS-02 through PASS-07;
- complete CHECKPOINT-A;
- perform PASS-04 tooling research;
- design PASS-02 cross-layer architecture;
- select graph technology;
- select GOV-7 strategy;
- implement scripts, hooks, skills, queries, MCP, telemetry or controls;
- create a GOV-7 backlog;
- resolve OD-006;
- accept recommendations;
- accept residual risk;
- change the Kernel;
- activate or implement GOV-7;
- modify planning, product or runtime artifacts;
- rewrite completed evidence;
- treat chat memory as repository evidence;
- open a pull request;
- merge;
- tag;
- release;
- deploy.

## Publication authority

If and only if all required validation passes:

1. create one bounded commit;
2. push without force to the current branch;
3. do not open a pull request.

Suggested commit:

docs(governance): execute GOV-7 audit PASS-01

## Required return

Return concisely:

Repository:
Branch:
Starting local HEAD:
Starting remote HEAD:
Startup verification:

Audit ID:
Run ID:
Authorization:
Prompt custody:
Prompt SHA-256:
Input manifest:

Output paths:
Capability families recorded:
Repeated-work items:
Demonstrated gaps:
Stop-doing items:
Top findings:
Historical evidence limitations:
External research performed:

Validation:
Targeted tests:
Full governance suite:

Commit:
Push:
Final local HEAD:
Final remote HEAD:
Local/remote aligned:
Worktree:

Kernel status:
GOV-7 status:
OD-006 status:
PASS-02 executed:
Recommendations accepted:
Implementation authorized:

Status:
Blockers:
Exact next action:

Expected successful status:

PASS_01_EXECUTED_VALIDATED_AND_PUSHED_PENDING_PROJECT_OWNER_DISPOSITION

Expected exact next action:

The Project Owner reviews the validated PASS-01 outputs and separately decides
whether to accept them as bounded inputs and authorize PASS-02. Do not execute
PASS-02, activate GOV-7 or implement any recommendation through this result.
