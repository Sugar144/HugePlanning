# GOV-AUD-PROMPT-021 — Execute PASS-02 Cross-Layer Architecture Audit

```yaml
prompt_id: GOV-AUD-PROMPT-021
version: 0.1.0
audit_id: GOV-AUD-001
audit_run_id: GOV-AUD-001-P02-R1
pass_id: PASS-02
role: Cross-Layer Architecture Auditor
mode: EVIDENCE_SUPPORTED_ARCHITECTURE_SYNTHESIS
authority: PROJECT_OWNER_EXPLICIT
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
expected_head: a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e
```

## Objective

Execute only PASS-02 of `GOV-AUD-001`.

Define an evidence-supported cross-layer architecture connecting:

```text
governance derivation
methodology construction
client lifecycle
information architecture
```

Produce:

* bounded contexts and canonical ownership;
* interfaces and exchanged artifacts;
* typed cross-layer relationships and query contracts;
* traceability and impact analysis;
* version compatibility, migration and supersession;
* upward feedback routing;
* trust-root and independence boundaries;
* controlled system self-hosting;
* controlled infrastructure self-hosting;
* architecture-style comparison and criteria for later distribution.

Do not select technology, implement architecture, activate GOV-7, authorize PASS-03 or complete CHECKPOINT-A.

## Starting state

Verify from the repository root:

```text
Branch:
governance/kernel-designer-revision-v0.1

Expected local and remote HEAD:
a4cbc500b2ca864b2eb35e9354df88c8c3d97a3e

PASS-01:
PASS_01_ACCEPTED_COMPLETED

PASS-02:
PLANNED_NOT_EXECUTED_UNAUTHORIZED

CHECKPOINT-A:
PENDING_PROJECT_OWNER_DISPOSITION

Kernel:
0.2.0 / RATIFIED
not implemented, enforceable or operational

GOV-7:
INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY

OD-006:
UNRESOLVED_TRIGGER_GATED
```

Also verify:

* local and remote HEAD are aligned;
* worktree and staging are clean;
* no conflicting PASS-02 execution exists;
* these identities are unused:

```text
GOV-AUD-001-P02-R1
GOV-AUD-AUTH-002
GOV-AUD-PROMPT-021
HP-PROMPT-029
```

Stop without modification on mismatch, conflict, dirty state or unauthorized phase change.

## Authority

Authorized:

* inspect repository evidence within the declared read scope;
* create exact PASS-02 authorization, prompt custody and input manifest;
* execute PASS-02 analysis;
* create the declared outputs and validation evidence;
* update the minimum audit lifecycle and registries needed to represent an unaccepted PASS-02 candidate;
* run applicable validation and tests.

Not authorized:

* commit or push;
* accept PASS-02;
* complete CHECKPOINT-A;
* execute PASS-03;
* select or adopt tools;
* select a graph database;
* implement graph, projection, services, Controller changes, MCP, runtime integration or self-hosting;
* activate or implement GOV-7;
* resolve OD-006;
* accept risk;
* modify product, planning or published runtime artifacts.

## Prospective custody

Before substantive analysis, create:

```text
governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P02-R1/
├── authorization/
│   └── owner-authorization.yaml
├── input/
│   └── input-manifest.yaml
├── prompt/
│   └── GOV-AUD-PROMPT-021-pass-02-execution-v0.1.0.md
├── output/
├── evaluation/
└── manifest.yaml
```

Preserve this complete prompt verbatim.

Do not summarize, normalize, reconstruct or improve the custody copy.

Calculate and bind:

* authorization SHA-256;
* exact prompt SHA-256;
* input-manifest SHA-256;
* input-package SHA-256.

Do not create placeholder outputs or fake evaluation artifacts.

## Canonical inputs

Include only the material evidence actually used:

* accepted PASS-01 C3 outputs and acceptance record;
* independent confirmation of C3;
* ratified Kernel and ER-001–ER-020;
* governance operating contract;
* current state and master plan;
* S0a–S9 architecture, artifact model and runtime-support surfaces;
* relevant schemas, validators, state machines, Controllers, skills and hooks;
* decision and learning evidence needed for authority, failure or feedback boundaries.

Every input must include a path and SHA-256.

Mark unavailable or missing evidence explicitly.

Do not perform a full historical reread by default.

## Required reasoning discipline

For every material architectural element use:

```text
VERIFIED_FACT
INFERENCE
PROPOSAL
RECOMMENDATION
OWNER_DECISION_REQUIRED
DEFERRED
REJECTED
```

Maintain this derivation:

```text
PASS-01 capability or gap
→ architectural requirement
→ proposed boundary or relationship
→ validation/query need
→ unresolved Owner decision
```

Do not treat a diagram, prompt, plan or schema as implementation evidence.

Do not treat a proposed model as approved architecture.

## Required analysis

### 1. Four-axis system model

Map separately and jointly:

```text
A. Governance derivation
Kernel
→ enforceable requirements
→ policy
→ standard
→ procedure or contract
→ control
→ evidence
→ finding or decision

B. Methodology construction
S0a
→ S0b
→ S1
→ ...
→ S9

C. Client lifecycle
intake
→ discovery
→ specification
→ design
→ implementation
→ validation
→ delivery
→ operation
→ maintenance or closure

D. Information architecture
source evidence
→ canonical structured data
→ derived artifacts
→ projections and views
→ operational state
→ historical evidence
```

Identify where these axes intersect and where they must remain decoupled.

### 2. Bounded contexts and canonical ownership

For each bounded context define:

* context ID;
* purpose;
* canonical owner;
* owned state and artifacts;
* accepted inputs;
* produced outputs;
* allowed writers;
* allowed readers;
* authority level;
* source of truth;
* derived/non-authoritative projections;
* failure boundary;
* stopping condition;
* recovery path;
* manual escape path.

At minimum consider:

* Kernel and governance authority;
* governance derivation;
* audit and evidence custody;
* methodology definition;
* methodology runtime;
* client/project state;
* agent and skill execution;
* validation and evaluation;
* learning and feedback;
* release and migration;
* projections and queries.

Do not create a bounded context merely because a folder exists.

### 3. Interfaces and application contracts

Determine whether each applicable S-stage needs a versioned governance-application contract.

Define the minimum generic contract fields required to connect a governance rule to a methodology stage, such as:

* source clause or requirement;
* applicable stage or transition;
* responsible role or Controller;
* required control;
* expected evidence;
* validation method;
* failure route;
* escalation authority;
* version compatibility;
* supersession and migration;
* exceptions and expiry.

Do not instantiate every contract unless needed to prove the model.

### 4. Typed cross-layer relationship model

Produce a technology-neutral relationship vocabulary.

It must support questions such as:

```text
Which controls derive from this Kernel clause?
Which stages apply this requirement?
Which agent, skill, script or hook executes or validates it?
Which artifact or test proves it?
Which gate blocks progression?
Which findings route back to which owner?
What changes if this schema or requirement version changes?
Which projects or artifacts need migration?
```

For every relationship type define:

* type name;
* source entity kinds;
* target entity kinds;
* direction;
* cardinality;
* required provenance;
* validity/version fields;
* whether authoritative or derived;
* validation rule;
* invalidation or supersession behavior.

The model must be:

* derived from canonical sources;
* regenerable;
* provenance-rich;
* non-authoritative;
* neutral regarding storage technology.

Do not select graph technology.

### 5. Traceability and impact analysis

Define how to trace:

```text
intake decision or hazard
→ Kernel clause
→ requirement
→ policy or standard
→ procedure or contract
→ control
→ executor or validator
→ evidence
→ finding
→ decision
```

Define impact queries for:

* changing a Kernel clause;
* changing a methodology stage;
* changing a schema;
* changing an agent or skill;
* changing a validator;
* superseding a control;
* migrating a client project;
* correcting historical evidence without rewriting it.

Distinguish direct impact, probable impact and unknown impact.

### 6. Version compatibility, migration and supersession

Define compatibility responsibilities among:

* Kernel version;
* executable-governance version;
* methodology version;
* stage-contract version;
* client/project lock version;
* schema version;
* agent version;
* skill version;
* control version;
* validator version;
* evidence format version.

Compare at minimum:

```text
exact lock
compatible range
capability declaration
migration contract
adapter/projection
revalidation requirement
unsupported combination
```

Specify who may declare compatibility and what evidence is required.

Prevent silent compatibility claims.

### 7. Feedback and finding ownership

Define how operational evidence routes upward without modifying higher authority automatically.

Create a finding taxonomy that distinguishes:

* project-specific defect;
* methodology defect;
* governance-application defect;
* governance requirement defect;
* tooling defect;
* prompt/agent defect;
* evidence or measurement defect;
* Owner decision;
* research need;
* personal or cross-project idea.

For each category identify:

* canonical owner;
* permitted actions;
* escalation path;
* whether lower layers may propose changes;
* who validates closure;
* who may accept residual risk.

No layer may certify or ratify its own authority change.

### 8. Controlled system self-hosting

Assess HugePlanning using HugePlanning to improve itself.

Define boundaries for:

* immutable bootstrap trust root;
* seed versus generated artifacts;
* human authority;
* independent review;
* self-modification;
* self-certification;
* self-ratification;
* release boundaries;
* rollback;
* recovery;
* manual fallback;
* loop exhaustion;
* corrupted or contradictory state;
* tool/model unavailability.

Separate:

```text
proposal generation
validation
independent evaluation
Owner acceptance
implementation
release
operation
```

Do not claim that self-hosting is currently implemented.

### 9. Infrastructure self-hosting

Assess separately:

* local models;
* local runners;
* local artifact storage;
* databases;
* graph/query infrastructure;
* CI/runtime infrastructure;
* secrets and credentials;
* telemetry;
* backups and disaster recovery.

Identify what could be self-hosted later, but do not recommend adoption without a demonstrated gap and later tool research.

### 10. Architecture-style comparison

Compare:

* repository-native modular artifact-driven;
* layered;
* event-driven;
* Controller-led;
* service-oriented;
* microservices;
* hybrid alternatives.

For each compare:

* fit to demonstrated gaps;
* authority clarity;
* auditability;
* failure isolation;
* migration burden;
* deterministic validation;
* AI execution cycles;
* Owner burden;
* integration complexity;
* maintenance burden;
* rollback;
* premature-distribution risk.

Define explicit criteria that must be satisfied before introducing distributed architecture or services.

Do not select a final architecture.

## Required outputs

Create exactly:

```text
output/01-bounded-context-and-ownership-model.yaml
output/02-cross-layer-interface-and-contract-assessment.md
output/03-typed-relationship-and-query-model.yaml
output/04-version-migration-and-impact-model.md
output/05-controlled-self-hosting-and-trust-boundaries.md
output/06-architecture-style-comparison.yaml
output/07-pass-02-findings-and-checkpoint-a-handoff.md
```

### Output requirements

`01-bounded-context-and-ownership-model.yaml`

* bounded contexts;
* canonical owners;
* authority boundaries;
* inputs/outputs;
* failure, stop and recovery boundaries.

`02-cross-layer-interface-and-contract-assessment.md`

* four-axis interaction;
* interface model;
* governance-application contract assessment;
* unresolved decisions.

`03-typed-relationship-and-query-model.yaml`

* entity types;
* relationship types;
* endpoint constraints;
* provenance;
* versioning;
* required queries;
* validation rules.

`04-version-migration-and-impact-model.md`

* compatibility model;
* migration;
* supersession;
* revalidation;
* impact-analysis semantics.

`05-controlled-self-hosting-and-trust-boundaries.md`

* system self-hosting;
* infrastructure self-hosting;
* trust root;
* independence;
* rollback and recovery;
* prohibited circular authority.

`06-architecture-style-comparison.yaml`

* compared styles;
* evidence-based strengths and weaknesses;
* adoption criteria;
* explicit `NO_DISTRIBUTION_YET` option;
* no selected winner.

`07-pass-02-findings-and-checkpoint-a-handoff.md`

* verified architectural facts;
* strongest proposals;
* unresolved conflicts;
* Owner decisions required;
* rejected or deferred ideas;
* exact scope that CHECKPOINT-A may accept, bound, return, reject, defer or research.

## Validation

Create:

```text
evaluation/pass-02-validation-report.yaml
```

Validate generically:

* exact prompt and authorization custody;
* input hashes;
* required outputs;
* unique IDs;
* source-path existence;
* statement labels;
* bounded-context ownership completeness;
* relationship endpoint validity;
* no orphan relationship types;
* required query coverage;
* compatibility-matrix completeness;
* authority and trust-root boundaries;
* distinction between system and infrastructure self-hosting;
* no graph technology selection;
* no architecture implementation;
* no selected architecture winner;
* no PASS-03 execution;
* no CHECKPOINT-A completion;
* unchanged Kernel, GOV-7 and OD-006 state.

Validators and tests must enforce structural and semantic invariants generically.

Do not hard-code expected conclusions, named bounded contexts, named relationship IDs or preferred architecture styles as permanent truth.

Run:

* audit lifecycle and prompt-custody validation;
* PASS-02-focused tests;
* governance-state and checksum validation;
* YAML, Markdown, references and `git diff --check`.

Run the full governance suite only if executable validator/test support changes or targeted validation indicates cross-surface risk.

Run the published runtime suite only if its executable support is modified or an existing contract requires it.

## Terminal status

If valid, set:

```text
PASS-02:
EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION

CHECKPOINT-A:
PENDING_PROJECT_OWNER_DISPOSITION

PASS-03:
PLANNED_NOT_EXECUTED_UNAUTHORIZED

GOV-7:
INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY
```

PASS-01 remains accepted and immutable.

The audit remains incomplete.

## Publication boundary

Do not commit or push.

Return the validated uncommitted candidate for separately controlled independent review.

## Required return

Return only:

```text
Repository:
Branch:
Starting local HEAD:
Starting remote HEAD:
Startup verification:
Audit ID:
Run ID:
Authorization record:
Prompt custody:
Prompt SHA-256:
Input manifest:
Input package SHA-256:
PASS-01 status:
PASS-02 status:
CHECKPOINT-A status:
Bounded contexts:
Relationship types:
Required queries:
Compatibility combinations:
Architecture styles compared:
System self-hosting status:
Infrastructure self-hosting status:
Owner decisions identified:
Files created:
Files modified:
Validation:
Focused tests:
Full governance suite:
Published runtime suite:
Commit:
Push:
Final HEAD:
Worktree:
Staging:
Kernel status:
GOV-7 status:
OD-006 status:
PASS-03 executed:
Status:
Blockers:
Exact next action:
```

Expected status:

```text
PASS_02_EXECUTED_VALIDATED_PENDING_INDEPENDENT_EVALUATION_AND_PROJECT_OWNER_DISPOSITION
```

Expected next action:

```text
Conduct a separately controlled independent review of PASS-02 before CHECKPOINT-A disposition. Do not accept PASS-02 or complete CHECKPOINT-A from this run.
```
