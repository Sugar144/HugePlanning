# HugePlanning GOV-7 Enablement Audit Program Scaffold

Prompt identity:

prompt_id: GOV-AUD-PROMPT-000
version: 0.2.0
role: Audit Program Architect
mode: AUDIT_PROGRAM_SCAFFOLD
repository: Sugar144/HugePlanning
expected_branch: governance/kernel-designer-revision-v0.1
authority: PROJECT_OWNER_EXPLICIT

Authorized repository scope:

- governance/**

Authorized actions:

- inspect;
- design;
- create audit scaffold;
- register exact prompt;
- create pass contracts and prompt templates;
- create the minimum validation required for planning artifacts;
- validate;
- create one bounded commit;
- push without force.

Prohibited actions:

- execute audit passes;
- perform the substantive external research planned by the audit;
- change the Kernel;
- reinterpret the ratification record;
- reopen GOV-5 or GOV-6;
- resolve OD-006;
- activate GOV-7;
- implement GOV-7;
- implement policies, standards, procedures or controls;
- implement graph, projection, telemetry, prompt optimization or interviewer simulation;
- modify S0a–S9 planning or runtime;
- accept risk;
- claim enforceability, operation, compliance or maturity;
- open a pull request;
- merge;
- release;
- deploy.

You are implementing only the durable planning, prompt-custody and artifact scaffold for a bounded:

HugePlanning GOV-7 Enablement, Cross-Layer Architecture and Empirical Validation Audit

Repository artifacts and technical documentation must be written in English.

Return the final implementation report to the Project Owner concisely.

## 1. Mission

Create a complete but bounded repository structure that will preserve:

- the audit charter;
- the audit sequence and dependencies;
- exact prompts and their versions;
- input manifests;
- output contracts;
- future execution outputs;
- Owner checkpoints and decisions;
- evaluation evidence;
- final synthesis;
- independent evaluation;
- correction history if a material defect is later found.

Do not execute the audit in this run.

This execution creates only the audit program scaffold.

It is not:

- an audit execution;
- a new governance authority layer;
- GOV-7 activation;
- GOV-7 design approval;
- GOV-7 implementation;
- policy adoption;
- risk acceptance;
- a claim of enforceability;
- a claim of operational readiness.

## 2. Verified durable governance baseline

The current committed repository state establishes:

- GOV-5:
  COMPLETED / CLOSED

- KGR-006-R1:
  ACCEPTED_BY_PROJECT_OWNER

- GOV-5 closure review:
  EXECUTED_READY_FOR_PROJECT_OWNER_DECISION
  The Project Owner subsequently accepted KGR-006-R1 and closed GOV-5.

- GOV-6:
  COMPLETED / CLOSED

- OD-004:
  RESOLVED_RATIFY_EXACT_KERNEL_0_2_0

- Kernel:
  version: 0.2.0
  status: RATIFIED
  scope: HugePlanning level 3 under the Kernel scope rules

- Kernel implementation:
  NOT_PERFORMED

- Kernel enforceability:
  NOT_CLAIMED

- Operational status:
  false

- OD-005:
  RESOLVED_ACCEPT_MINIMUM_GOV_7_DIRECTION

- Minimum GOV-7 package:
  DIRECTION_ACCEPTED_NOT_IMPLEMENTED

- OD-006:
  UNRESOLVED_TRIGGER_GATED

- GOV-7:
  INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY

- GOV-8:
  INACTIVE

- GOV-9:
  INACTIVE

- Residual risk:
  NOT_ACCEPTED through the GOV-5/GOV-6 decisions

- Runtime projection:
  governance has not yet been projected into the S0a–S9 methodology runtime

This baseline means:

audit planning
≠ audit execution
≠ GOV-7 activation
≠ GOV-7 design authority
≠ GOV-7 implementation authority
≠ policy adoption
≠ risk acceptance
≠ enforceability
≠ operational status

## 3. Startup verification

Before modifying anything:

1. Read all applicable repository instructions, including:

   - root AGENTS.md;
   - governance/AGENTS.md;
   - governance/CURRENT_STATE.md;
   - governance/GOVERNANCE_MASTER_PLAN.md;
   - the governance operating contract;
   - prompt-custody methodology;
   - audit, review and formal-run conventions;
   - artifact and prompt registries;
   - schemas relevant to governance planning artifacts;
   - current learning-record and event conventions;
   - the S0a–S9 roadmap and system architecture documents, read-only.

2. Read the minimum current-state evidence needed to confirm the baseline:

   - governance/CURRENT_STATE.md;
   - governance/GOVERNANCE_MASTER_PLAN.md;
   - the GOV-5 Project Owner acceptance record;
   - the GOV-6 ratification record;
   - the OD-005 GOV-7 direction record;
   - the KGR-006-R1 manifest;
   - the minimum GOV-7 recommendation;
   - current prompt-custody conventions;
   - current review and audit conventions.

3. Prefer:

   - current-state records;
   - decision records;
   - manifests;
   - validated indexes;
   - accepted summaries.

4. Do not reread every historical KGR artifact merely because it exists.

5. Follow historical references only when required to:

   - resolve an actual discrepancy;
   - verify identity or provenance;
   - define a future pass input contract;
   - avoid conflicting with an existing repository convention.

6. Verify:

   - current branch;
   - current local HEAD;
   - current remote HEAD;
   - local/remote alignment;
   - clean worktree;
   - empty staging area;
   - GOV-5 is completed and closed;
   - GOV-6 is completed and closed;
   - exact Kernel 0.2.0 is ratified;
   - OD-005 accepts only the minimum GOV-7 direction;
   - OD-006 remains unresolved and trigger-gated;
   - GOV-7 remains inactive;
   - no audit scaffold with the same identity already exists;
   - no conflicting prompt or pass IDs exist.

7. Do not hard-code an expected starting HEAD.

8. Determine and report the current local and remote HEAD during startup.

9. Stop before modification if:

   - the branch differs from governance/kernel-designer-revision-v0.1;
   - local and remote diverge;
   - the worktree is not clean;
   - the staging area is not empty;
   - durable state differs materially from the baseline above;
   - GOV-7 has already been activated or implemented;
   - an audit scaffold with the same identity already exists;
   - the requested audit ID or prompt IDs conflict;
   - existing repository conventions require a materially different structure;
   - the requested work would overwrite completed evidence;
   - planning the audit would incorrectly change a governance-phase state.

Do not repair any conflict silently.

Report the blocker instead.

## 4. Durable project boundary

The audit program must preserve these distinctions:

audit planning
≠ audit execution
≠ recommendation acceptance
≠ implementation
≠ GOV-7 activation
≠ enforceability
≠ operational status

Do not change:

- Kernel version or status;
- GOV-5 status;
- GOV-6 status;
- ratification evidence;
- unresolved OD-006 state;
- any completed run;
- any completed evaluation;
- any historical prompt;
- any historical output;
- any existing decision record;
- S0a–S9 implementation state;
- product or methodology runtime outside governance/**.

The scaffold may reference read-only planning and runtime artifacts but may not modify them.

Completed prompts, runs, evaluations and outputs are immutable.

A future correction must create a new version rather than rewrite history.

## 5. Core audit principles

Encode the following principles in the charter, plan and every future pass contract.

### 5.1 Repository-first and gap-driven

Required reasoning order:

verified repository capability
→ demonstrated problem or gap
→ smallest sufficient response
→ candidate implementation or tool

Do not use:

available framework
→ search for a project use case

The audit must determine what HugePlanning already supports before recommending new architecture or tools.

Every recommendation must trace to at least one of:

- repository evidence;
- demonstrated failure;
- recurring burden;
- unresolved governance requirement;
- repeated mechanical work;
- empirical risk;
- future capability explicitly required by the accepted GOV-7 direction.

### 5.2 Prompt economy and anti-bloat

Do not inflate audit prompts, contracts or artifacts to appear thorough.

Before producing any material audit prompt or contract:

1. identify the exact objective;
2. identify the minimum repository evidence required;
3. identify the minimum authority required;
4. identify the minimum validation required by current risk or repository contract;
5. remove everything that does not materially affect correctness, authority, safety, validation or deliverables.

Use this rule:

required by current risk or contract
→ include

useful but not required
→ classify as OPTIONAL_IMPROVEMENT or FOLLOW_UP_CANDIDATE

habitual, ceremonial, speculative or “just in case”
→ omit

Do not automatically request:

- full historical rereads;
- every possible validation;
- isolated-copy validation;
- review bundles;
- new schemas;
- new registries;
- new profiles;
- new learning records;
- new tests;
- full-suite execution;
- independent evaluation;
- exhaustive return fields;
- broad framework comparisons;
- new infrastructure;

unless the current repository contract or demonstrated risk requires them.

Before preserving each future prompt template, perform an anti-bloat review.

Classify material sections as:

- KEEP
- REMOVE
- MAKE_CONDITIONAL
- MOVE_TO_FOLLOW_UP

### 5.3 AI-first effort model

Do not use generic enterprise schedules, developer-weeks or story points as the primary estimate.

HugePlanning operates through an AI-first delivery model.

Estimate each recommendation through:

- bounded AI execution cycles;
- Owner decision effort;
- deterministic validation burden;
- semantic or independent evaluation burden;
- expected correction loops;
- implementation novelty;
- integration risk;
- maintenance burden.

A bounded AI execution cycle means:

prepared contract
→ AI execution
→ deterministic validation
→ Owner or evaluator review

Use effort categories such as:

AI execution cycles:
- 1 cycle
- 2–3 cycles
- 4–6 cycles
- more than 6 cycles
- unknown until prototype

Owner effort:
- LOW
- MEDIUM
- HIGH

Validation burden:
- LOW
- MEDIUM
- HIGH

Implementation novelty:
- REUSE_EXISTING
- SMALL_EXTENSION
- NEW_BOUNDED_COMPONENT
- NEW_SUBSYSTEM
- RESEARCH_DEPENDENT

Correction uncertainty:
- LOW
- MEDIUM
- HIGH
- UNKNOWN

Maintenance burden:
- NEGLIGIBLE
- LOW
- MEDIUM
- HIGH

Calendar estimates are optional and secondary.

When used:

- state assumptions;
- assume intensive Owner availability;
- account for AI-first generation;
- distinguish active work from waiting time;
- avoid generic enterprise estimates;
- prefer focused sessions and execution/review cycles.

Do not state that something requires “two weeks” merely because a traditional team might estimate it that way.

### 5.4 Work-unit evaluation

Evaluate the complete work unit:

input package
+ prompt contract
+ model and reasoning mode
+ execution
+ artifacts
+ validation
+ corrections
+ Owner intervention
+ independent disposition

Do not optimize prompts only for:

- length;
- characters;
- estimated tokens;
- number of instructions.

A longer prompt may be more efficient if it prevents:

- retries;
- ambiguity;
- scope drift;
- authority violations;
- mechanical reconciliation;
- invalid output packages.

### 5.5 No predetermined GOV-7 strategy

The audit must compare:

- TOP_DOWN_LAYER_COMPLETION;
- BOTTOM_UP_CONTROL_FIRST;
- HYBRID_VERTICAL_SLICES;
- any evidence-supported alternative discovered during the audit.

A vertical slice is a candidate, not an approved strategy.

Do not create planning fields that presuppose a vertical slice.

Use strategy-neutral priority classes:

- P0_BEFORE_MATERIAL_GOV_7_WORK
- P1_FIRST_APPROVED_IMPLEMENTATION_INCREMENT
- P2_AFTER_INITIAL_EMPIRICAL_EVIDENCE
- DEFER
- REJECT

If a vertical strategy is later recommended, it must be justified against alternatives.

### 5.6 Required relationship graph; optional graph technology

The audit must produce a typed cross-layer relationship graph or equivalent formal relationship model.

The relationship model is required.

The implementation technology is not predetermined.

The audit must compare the smallest sufficient options, including:

- validated Python domain objects;
- dictionaries;
- sets;
- adjacency maps;
- NetworkX;
- relational projections;
- SQLite;
- DuckDB where analytical aggregation is relevant;
- RDF or knowledge-graph approaches;
- property-graph approaches;
- persistent graph databases;
- NO_PERSISTENT_GRAPH.

The derived graph or projection must remain:

- non-authoritative;
- regenerable from canonical repository artifacts;
- provenance-rich;
- deterministic where possible;
- protected against inferred semantic edges becoming canonical facts without review.

The graph must support:

- cross-layer traceability;
- impact analysis;
- missing-link detection;
- dependency queries;
- context-package generation;
- evidence routing.

It must not become a new source of truth.

### 5.7 Controlled self-hosting

Treat controlled self-hosting, reflexive improvement and dogfooding as primary audit topics.

The audit must determine how:

current governance
→ governs development of the methodology system

current methodology system
→ helps construct and evaluate itself and later governance artifacts

project and product execution
→ produces operational evidence

operational evidence
→ proposes changes to the correct layer

The audit must assess whether HugePlanning can progressively use its own:

- interviewer;
- requirements pipeline;
- specification pipeline;
- architecture pipeline;
- backlog pipeline;
- task-context generation;
- implementation loop;
- review mechanisms;
- validation mechanisms;
- learning system;

to improve HugePlanning itself.

It must define how to prevent:

- uncontrolled self-modification;
- self-certification;
- self-ratification;
- generated evidence being treated as independent evidence;
- silent changes to the trust root;
- circular authority;
- a newer methodology silently changing locked projects;
- the same agent creating, evaluating and accepting its own change;
- self-hosting being used to bypass independent evaluation;
- bootstrap artifacts being rewritten retrospectively.

The audit must examine:

- bootstrap trust root;
- seed artifacts versus generated artifacts;
- version pinning;
- release boundaries;
- migration boundaries;
- supersession;
- independence requirements;
- rollback;
- escape paths;
- manual fallback;
- progressive replacement of manual glue;
- recovery when the self-hosted process produces an invalid result.

Distinguish:

1. system self-hosting:
   HugePlanning using its own methodology and tooling to improve HugePlanning;

2. infrastructure self-hosting:
   running third-party tools locally or on Owner-controlled infrastructure.

Evaluate both separately.

### 5.8 Open-ended tool discovery

Named technologies form an initial candidate pool.

They are not:

- exhaustive;
- mandatory;
- an adoption checklist.

The audit may recommend other:

- frameworks;
- libraries;
- products;
- testing methods;
- research methods;
- prompt lifecycle systems;
- local-first tools;
- custom repository-native components;

when evidence supports them.

Every tool comparison must include:

- NO_NEW_TOOL;
- repository-native extension;
- smallest custom script or component.

## 6. Required audit sequence

Create the following planned sequence.

Do not execute any pass during this scaffold run.

### PASS-01 — Repository Capability, Repetition, Waste and Gap Audit

Purpose:

- inventory current capabilities;
- identify repeated mechanical work;
- identify repeated semantic workflows;
- identify recurring failures;
- identify avoidable prompt burden;
- identify avoidable Owner burden;
- distinguish existing capability from genuine gaps;
- build a ranked evidence-backed gap register.

Required analysis includes:

- prompts and prompt custody;
- formal runs;
- authorizations;
- input-package preparation;
- output packaging;
- hashes and inventories;
- imports and byte identity;
- independent evaluations;
- state reconciliation;
- review bundles;
- learning records;
- parsers;
- schemas;
- validators;
- state machines;
- Controllers and loops;
- scripts;
- skills;
- hooks;
- manual Owner work;
- temporary scripts and commands;
- repeated repository inspection;
- repeated prompt construction;
- repeated decision-pack construction;
- S0a–S9 assets;
- ER-001 through ER-020;
- work that should stop because an existing mechanism already solves it.

Use the work unit as the main unit of analysis.

Rank candidate improvements using:

frequency
× current burden
× failure risk
× expected reduction
÷ implementation and maintenance burden

No external framework research in this pass except what is strictly necessary to identify an existing repository capability.

Required outputs must include:

- verified capability inventory;
- repeated-work inventory;
- mechanical-work candidates;
- semantic-workflow candidates;
- ranked gap register;
- current prompt and Owner burden where honestly observable;
- historical evidence limitations;
- preliminary automation candidates;
- preliminary stop-doing list.

### PASS-02 — Cross-Layer Architecture, Graph, Versioning and Controlled Self-Hosting

Purpose:

Define how these separate axes interact.

Governance derivation:

Kernel
→ enforcement requirements
→ policy
→ standard
→ procedure
→ control
→ evidence

Methodology construction:

S0a
→ S0b
→ S1
→ ...
→ S9

Client lifecycle:

onboarding
→ discovery
→ specification
→ technical design
→ planning
→ implementation
→ validation
→ release
→ operation

Information architecture:

evidence
→ canonical data
→ human documents
→ operational views

Required outputs must cover:

- bounded contexts;
- canonical ownership;
- interfaces;
- exchanged artifacts;
- cross-layer application contracts;
- typed relationship graph;
- traceability from Kernel to product evidence and back;
- version compatibility;
- migration;
- supersession;
- upward feedback routing;
- controlled self-hosting;
- trust-root boundaries;
- independence boundaries;
- Controller or coordinator responsibilities;
- failure boundaries;
- stopping boundaries;
- recovery boundaries;
- comparison of architecture styles.

Compare at minimum:

- modular artifact-driven architecture;
- layered architecture;
- event-driven coordination;
- controller-led coordination;
- service-oriented architecture;
- microservices;
- repository-native workflow architecture;
- hybrid alternatives.

Do not recommend microservices merely because the system has multiple conceptual layers.

Define explicit adoption criteria before service-oriented or distributed architecture would be justified, including:

- independently deployable runtime components;
- stable network APIs;
- concurrent users;
- independent scaling;
- isolation requirements;
- persistent shared services;
- failure-domain separation;
- operational capacity to maintain distributed infrastructure.

The relationship model must support questions such as:

- Which Kernel clause supports this control?
- Which enforcement requirement derives from it?
- Which methodology stage implements it?
- Which agent, skill, script or hook executes it?
- Which artifact and test produce evidence?
- Which gate evaluates the evidence?
- Which project requirement triggered an additional governance control?
- Which finding should change a task, skill, procedure, control, policy or Kernel?
- Which downstream artifacts are affected by a proposed change?
- Which methodology versions are compatible with which governance versions?
- Which client projects require migration or revalidation after a change?

Determine whether each applicable S-stage needs a versioned governance-application contract declaring:

- governance baseline;
- applicable governance requirements;
- applicable controls;
- authority;
- allowed effects;
- prohibited effects;
- canonical inputs;
- required outputs;
- required evidence;
- stop conditions;
- recovery conditions;
- validations;
- human gates;
- handoff to the next stage.

Define compatibility among:

- Kernel version;
- executable-governance package version;
- methodology version;
- client-project methodology lock;
- artifact schema versions;
- agent versions;
- skill versions;
- control versions.

Define the upward feedback route:

operational evidence
→ finding
→ classification
→ owning layer
→ proposed change
→ validation
→ independent review where required
→ Owner decision
→ versioned release or constitutional amendment

Distinguish findings that should modify:

- final product implementation;
- client requirement;
- delivery task;
- agent;
- skill;
- procedure;
- control;
- policy;
- standard;
- methodology architecture;
- governance methodology;
- Kernel.

Do not choose graph implementation technology during this planning run.

### CHECKPOINT-A — Owner architecture review

After PASS-01 and PASS-02:

- confirm whether observed gaps are real;
- confirm whether system boundaries are correct;
- confirm whether the relationship model captures the intended project;
- confirm whether self-hosting preserves authority and independence;
- record corrections before subsequent passes.

Do not infer checkpoint approval.

### PASS-03 — Measurement, Prompt/Agent Evaluation and Interviewer Testing

Purpose:

Design honest historical baselines and prospective evaluation.

#### Historical metrics

Identify what can and cannot be recovered honestly.

Potentially recoverable metrics include:

- prompt characters;
- prompt bytes;
- estimated prompt tokens;
- input-package inventories;
- expected versus produced artifacts;
- validation results;
- number of execution attempts;
- number of corrections;
- Owner interventions;
- independent-evaluation results;
- failure types;
- status transitions;
- changed files;
- repeated mechanical steps;
- recurring instructions.

Never invent:

- exact historical token usage when not recorded;
- unrecorded execution time;
- exact historical subscription cost;
- hidden reasoning;
- unrecorded failed attempts;
- unavailable tool-call traces.

#### Prospective telemetry

Consider observable fields such as:

- work-unit ID;
- prompt ID;
- prompt version;
- prompt hash;
- input-package hash;
- model and reasoning mode when observable;
- session ID when available;
- starting and ending HEAD;
- artifact inventory;
- validation results;
- retries;
- correction cycles;
- Owner interventions;
- independent-evaluation result;
- observable token usage;
- observable cost;
- observable duration;
- permission events;
- stop reason;
- missing-data markers.

Operational telemetry must not become:

- canonical project truth;
- proof of semantic quality;
- proof of compliance;
- proof of accepted risk;
- authority for phase transitions.

Avoid hidden chain-of-thought collection.

Do not depend permanently on unstable transcript formats.

#### Prompt and agent evaluation

Cover:

- contract adherence;
- structural validity;
- semantic fidelity;
- completeness;
- contradiction detection;
- non-invention;
- authority safety;
- scope safety;
- cross-model stability;
- correction cycles;
- Owner cognitive burden;
- context burden;
- cost;
- regression detection;
- independent-evaluation disposition.

Determine which criteria should use:

- deterministic schemas;
- code-based graders;
- property-based tests;
- reference outputs;
- golden artifacts;
- mutation tests;
- metamorphic tests;
- pairwise comparison;
- LLM evaluators;
- independent-model evaluation;
- human review;
- trace grading.

#### Interviewer testing alternatives

The audit must find materially cheaper methods than requiring the Project Owner to manually play every client scenario.

Evaluate a layered interviewer-test architecture containing, where justified:

1. deterministic state-machine tests;
2. contract tests;
3. fixed scripted personas with hidden facts;
4. transcript replay;
5. regression conversations;
6. branching conversation fixtures;
7. model-based testing;
8. property-based testing;
9. mutation testing;
10. metamorphic testing;
11. synthetic multi-turn users;
12. cheaper-model user simulators;
13. adversarial personas;
14. contradictory personas;
15. incomplete or evasive personas;
16. non-technical personas;
17. overconfident personas;
18. privacy-sensitive personas;
19. trajectory evaluators;
20. artifact-level graders;
21. requirement-origin graders;
22. requirement-coverage graders;
23. contradiction-detection graders;
24. cross-model pairwise comparison;
25. limited human calibration samples;
26. occasional real-client validation when ethically and operationally appropriate.

The audit must examine:

- how to represent a hidden client truth model;
- how to prevent the interviewer from reading hidden facts directly;
- how to score information extraction;
- how to determine whether necessary questions were asked;
- how to detect unnecessary questioning;
- how to measure interview burden;
- how to test contradictions;
- how to test changing answers;
- how to test uncertainty;
- how to detect unsupported invention;
- how to test completion and refusal to close prematurely;
- how to test pause/resume;
- how to test state rehydration;
- how to test adaptive branching;
- how to test process-profile selection;
- how to test risk-trigger escalation;
- how to test sanitization;
- how to test PII handling;
- how to test domain-pack behavior;
- how to measure topic and hazard coverage;
- how to detect simulator/interviewer collusion;
- how to calibrate synthetic users against a small human baseline;
- how to avoid relying on one LLM judge;
- how to keep evaluation cost lower than full manual interviews.

The final recommendation must not eliminate human testing entirely.

It must minimize manual testing and reserve it for:

- calibration;
- usability;
- naturalness;
- high-value behavioral validation;
- final acceptance;
- cases where synthetic simulation is demonstrably unreliable.

### PASS-04 — Targeted Tooling, Prompt Lifecycle and Automation Research

Purpose:

Research only tools related to evidence-backed gaps from PASS-01 through PASS-03.

The named candidates below form an initial pool.

The pass must discover and assess other relevant technologies when appropriate.

#### Prompt registry, versioning, evaluation and improvement

Initial candidate pool:

- PromptLayer;
- Langfuse;
- Braintrust;
- Agenta;
- Promptfoo;
- LangSmith;
- Arize Phoenix;
- OpenAI Datasets;
- OpenAI trace grading;
- DSPy;
- Opik;
- GEPA or other supported prompt optimizers;
- TextGrad;
- repository-native Git-based prompt registry;
- other automatic prompt optimization approaches;
- other current alternatives discovered during research.

The audit must distinguish:

- versioning;
- immutable versions;
- labels and release channels;
- prompt diffs;
- experiment tracking;
- dataset management;
- offline evaluation;
- online evaluation;
- observability;
- traces;
- human review;
- automatic prompt rewriting;
- metric-driven prompt optimization;
- multi-stage agent optimization;
- provider neutrality;
- local or self-hosted deployment;
- cloud dependence;
- privacy;
- migration cost.

Automatic prompt optimization must not be recommended merely because it exists.

It requires:

- a stable task;
- a representative benchmark corpus;
- reliable evaluation metrics;
- bounded optimization authority;
- regression protection;
- human review of material semantic changes.

#### Scripts, hooks, skills and tools

Classify repeated work as:

- KEEP_AS_INSTRUCTION
- EXTRACT_TO_SCRIPT
- WRAP_WITH_HOOK
- EXTRACT_TO_SKILL
- EXPOSE_AS_QUERY
- EXPOSE_THROUGH_MCP_LATER
- REQUIRES_HUMAN_JUDGMENT
- RESEARCH_REQUIRED
- REJECT_AS_UNNECESSARY

Use these distinctions:

script:
deterministic operation

hook:
automatic execution tied to an observable event

skill:
reusable workflow involving judgment, sequence or references

query:
read-only deterministic retrieval from normalized project state

MCP:
stable tool interface exposed to agents after the underlying interface is mature

#### Query and projection technologies

Evaluate implementation options for the required relationship graph and projection/query capability.

Progression to consider:

existing parsers and validators
→ normalized in-memory model
→ deterministic queries
→ adjacency structures
→ optional NetworkX
→ optional persistence
→ optional MCP exposure

Do not assume:

- a graph database;
- SQLite;
- DuckDB;
- RDF;
- MCP;

are required.

#### Policy and validation technologies

Initial candidate pool:

- JSON Schema;
- Pydantic;
- CUE;
- Hypothesis;
- OPA/Rego;
- Cedar;
- static analysis;
- contract testing;
- provenance tooling;
- CI gates;
- custom deterministic validators;
- NO_NEW_TOOL.

Distinguish:

- human normative policy;
- machine-decidable rule;
- enforcement point;
- validation control;
- evidence artifact;
- semantic judgment.

Do not encode:

- constitutional judgment;
- proportionality;
- risk acceptance;
- semantic sufficiency;
- Owner authority decisions;

as simple machine-policy rules.

#### Workflow and orchestration

Initial candidate pool:

- plain Python;
- Make;
- Just;
- Task;
- a repository-native task runner;
- Codex Hooks;
- Codex Skills;
- GitHub Actions;
- MCP;
- Snakemake;
- Dagster;
- Prefect;
- Temporal;
- existing or extended deterministic Controller;
- no additional workflow engine.

Define adoption thresholds based on:

- number of repeated workflows;
- dependency complexity;
- resumability;
- parallelism;
- scheduling;
- caching;
- persistent execution history;
- failure recovery;
- observability;
- maintenance burden;
- operational complexity.

Do not recommend a workflow platform unless repository evidence demonstrates a problem that simpler tooling cannot control.

#### Model routing

Assess how available Codex models should be allocated to future audit passes and implementation work.

Include Terra and Luna only if they are actually available in the execution environment.

Do not infer their strengths from their names.

Use:

- observed model descriptions;
- official documentation where available;
- small pilot evidence;
- cost and reasoning characteristics;
- independence needs;
- task type.

Prefer the least expensive sufficient model.

Possible work classes include:

- repository inventory;
- deterministic implementation;
- architecture synthesis;
- adversarial review;
- independent evaluation;
- summarization;
- schema generation;
- test generation;
- external research.

#### Open discovery

Do not restrict research to the named candidates.

Discover other:

- tools;
- libraries;
- testing methods;
- prompt optimizers;
- observability systems;
- local-first platforms;
- evaluation frameworks;
- workflow patterns;
- research papers;

when they solve a demonstrated gap better.

For every recommendation include:

- repository evidence;
- target problem;
- current capability;
- smallest sufficient solution;
- expected benefit;
- AI execution cycles;
- Owner effort;
- validation burden;
- implementation novelty;
- correction uncertainty;
- integration risk;
- maintenance burden;
- privacy and hosting;
- provider dependence;
- lock-in;
- authority risk;
- rollback;
- adoption trigger;
- priority;
- disposition.

Permitted dispositions:

- ADOPT
- PILOT
- DEFER
- REJECT
- NO_NEW_TOOL

### CHECKPOINT-B — Owner tooling review

After PASS-04:

- approve recommendations for later planning;
- return recommendations;
- reject recommendations;
- defer recommendations;
- request additional research.

Do not infer adoption from a positive audit result.

Do not implement tools during the audit.

### PASS-05 — GOV-7 Strategy Comparison and Backlog Derivation

Purpose:

Compare implementation strategies without presupposing a vertical slice.

Compare at minimum:

- TOP_DOWN_LAYER_COMPLETION
- BOTTOM_UP_CONTROL_FIRST
- HYBRID_VERTICAL_SLICES

Consider additional evidence-supported strategies.

Evaluate:

- traceability;
- early empirical evidence;
- rework risk;
- AI execution cycles;
- Owner cognitive burden;
- validation burden;
- ability to reveal Kernel insufficiency;
- ability to test controls and evidence;
- preservation of layer boundaries;
- scalability;
- maintenance burden;
- stopping;
- recovery;
- migration complexity;
- ability to support controlled self-hosting.

If a vertical strategy is recommended, justify:

- why it is superior;
- which first slice should be used;
- why that slice is representative;
- what it exercises;
- what it cannot prove;
- what would trigger selection of another strategy.

The existing flow:

authorization
→ execution
→ import
→ validation
→ independent evaluation
→ Owner decision
→ state reconciliation

is a candidate only.

It must not be automatically selected.

Derive ER-001 through ER-020 into a proposed executable backlog:

governance component
→ epic
→ task
→ acceptance criteria
→ test or validator
→ evidence contract
→ gate
→ dependency

The pass must answer:

- what must exist before material GOV-7 work;
- what belongs in the first approved implementation increment;
- what should wait for empirical evidence;
- what lower-layer implementation is required to test upper-layer governance;
- how findings route upward;
- what evidence would indicate a methodology defect;
- what evidence would indicate a governance-control defect;
- what evidence would indicate a policy defect;
- what evidence would indicate a possible Kernel defect;
- what work should be rejected as unnecessary;
- how self-hosting should be introduced progressively;
- which functions must remain independently evaluated;
- which tasks should become backlog items;
- which backlog items can be generated by HugePlanning itself;
- which items require direct Owner design decisions;
- how OD-006 boundaries affect the proposed sequence.

### PASS-06 — Final Synthesis and Owner Decision Pack

Purpose:

Synthesize accepted pass outputs without repeating all research.

Required synthesis:

- verified repository baseline;
- ranked gaps;
- current capability map;
- cross-layer architecture;
- required relationship graph;
- graph implementation options;
- version and migration model;
- controlled self-hosting model;
- trust-root model;
- upward feedback architecture;
- historical metrics recovery;
- prospective telemetry;
- prompt and agent evaluation architecture;
- interviewer testing strategy;
- prompt lifecycle recommendation;
- prompt versioning and optimization recommendation;
- scripts, hooks, skills, queries and MCP candidates;
- tooling decisions;
- model-routing recommendation;
- strategy comparison;
- recommended GOV-7 approach;
- proposed GOV-7 backlog;
- minimum enablement;
- defer and reject list;
- AI-first implementation sequence;
- success criteria;
- stop criteria;
- escalation criteria;
- explicit Owner decisions;
- bounded first implementation-contract outline.

Use strategy-neutral horizons:

- BEFORE_MATERIAL_GOV_7_WORK
- FIRST_APPROVED_IMPLEMENTATION_INCREMENT
- AFTER_INITIAL_EMPIRICAL_EVIDENCE
- DEFERRED
- REJECTED

### PASS-07 — Independent Evaluation

Use an evaluator outside the synthesis author’s unilateral control.

Evaluate:

- repository fidelity;
- evidence support;
- completeness;
- cross-layer coherence;
- relationship-graph authority boundary;
- graph implementation neutrality;
- version and migration coherence;
- controlled self-hosting safety;
- trust-root protection;
- prevention of self-certification;
- prompt and interviewer evaluation quality;
- absence of framework shopping;
- open-ended tool discovery;
- AI-first effort fidelity;
- absence of predetermined vertical strategy;
- feasibility of the implementation sequence;
- unresolved Owner decisions;
- whether the audit became unnecessary bureaucracy;
- whether the audit delays GOV-7 without protective value;
- whether any recommendation creates more maintenance than value.

Permitted results:

- SUITABLE_FOR_PROJECT_OWNER_DECISION
- RETURN_FOR_BOUNDED_VERSIONED_CORRECTION
- INVALID_AUDIT_EXECUTION

### CHECKPOINT-C — Final Owner disposition

The Project Owner may:

- accept recommendations for later planning;
- partially accept;
- return for bounded correction;
- reject;
- defer;
- request research.

Acceptance of the audit report does not itself authorize GOV-7 implementation.

## 7. Pass dependencies

Encode:

PASS-01
↓
PASS-02
↓
CHECKPOINT-A
↓
PASS-03
↓
PASS-04
↓
CHECKPOINT-B
↓
PASS-05
↓
PASS-06
↓
PASS-07
↓
CHECKPOINT-C

Planning and registering the audit scaffold may occur now because:

- GOV-5 is closed;
- GOV-6 is closed;
- Kernel 0.2.0 is ratified;
- OD-005 accepts the minimum GOV-7 direction;
- GOV-7 remains inactive pending this audit and later authority.

Future pass prerequisites:

PASS-01:
- audit scaffold accepted;
- separately authorized execution;
- does not activate GOV-7.

PASS-02:
- accepted PASS-01 inputs;
- does not implement graph or projection;
- does not presume vertical slicing.

CHECKPOINT-A:
- explicit Project Owner disposition;
- silence is not approval.

PASS-03:
- accepted or explicitly bounded PASS-01 and PASS-02 outputs.

PASS-04:
- evidence-backed gaps from previous passes;
- may research unnamed alternatives;
- must include NO_NEW_TOOL and repository-native options.

CHECKPOINT-B:
- explicit Project Owner disposition;
- positive audit findings do not equal adoption.

PASS-05:
- accepted predecessor outputs;
- must compare strategies;
- must preserve OD-006 trigger-gated boundaries;
- proposes backlog only.

PASS-06:
- accepted predecessor evidence;
- synthesis only;
- no implementation authority.

PASS-07:
- evaluator outside synthesis author’s unilateral control.

CHECKPOINT-C:
- explicit Project Owner disposition;
- acceptance does not authorize implementation.

## 8. Artifact and custody architecture

Inspect existing repository conventions and implement the smallest compatible structure.

Preferred logical root:

governance/audits/GOV-AUD-001-gov7-enablement/

Use a different path only if existing repository conventions clearly require it.

Record the selected path and rationale.

The scaffold must contain equivalents of:

governance/audits/GOV-AUD-001-gov7-enablement/
├── 00-audit-charter.md
├── 01-audit-plan.yaml
├── 02-audit-status.yaml
├── 03-baseline-input-manifest.yaml
├── 04-artifact-and-custody-contract.md
├── 05-owner-checkpoints.md
├── 06-model-routing-policy.md
├── prompt-registry.yaml
│
├── prompts/
│   ├── GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md
│   └── templates/
│       ├── GOV-AUD-PROMPT-010-pass-01-capability-gap-v0.1.0.md
│       ├── GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.1.0.md
│       ├── GOV-AUD-PROMPT-030-pass-03-measurement-interviewer-evaluation-v0.1.0.md
│       ├── GOV-AUD-PROMPT-040-pass-04-targeted-tooling-v0.1.0.md
│       ├── GOV-AUD-PROMPT-050-pass-05-gov7-strategy-v0.1.0.md
│       ├── GOV-AUD-PROMPT-060-pass-06-synthesis-v0.1.0.md
│       └── GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.1.0.md
│
├── passes/
│   ├── PASS-01/
│   │   └── contract.yaml
│   ├── PASS-02/
│   │   └── contract.yaml
│   ├── PASS-03/
│   │   └── contract.yaml
│   ├── PASS-04/
│   │   └── contract.yaml
│   ├── PASS-05/
│   │   └── contract.yaml
│   ├── PASS-06/
│   │   └── contract.yaml
│   └── PASS-07/
│       └── contract.yaml
│
├── runs/
│   └── README.md
│
└── decisions/
    └── README.md

Do not create fake audit outputs.

Do not create empty files that imply a pass was executed.

Do not create completed output directories containing placeholder reports.

The runs/README.md file must define the future per-execution layout, for example:

runs/<audit-run-id>/
├── authorization/
├── input/
├── prompt/
├── output/
├── evaluation/
└── manifest.yaml

Reconcile this layout with existing formal-run conventions rather than duplicating established machinery.

## 9. Exact prompt custody

Preserve this entire received execution prompt verbatim as:

prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md

Calculate and register its SHA-256.

Do not silently:

- clean it;
- shorten it;
- normalize it;
- reformat it;
- reinterpret it;
- remove repeated constraints.

For each future pass:

- preserve a versioned prompt template now;
- do not pretend the template is a final instantiated execution prompt;
- require final prompt instantiation after dependencies and Owner checkpoints are satisfied;
- preserve the exact instantiated prompt before execution;
- bind it to an input manifest and hashes;
- preserve outputs separately;
- preserve independent evaluations separately;
- never overwrite completed prompts;
- never overwrite completed outputs;
- create new versions for corrections.

The prompt registry must distinguish planned lifecycle states equivalent to:

- TEMPLATE
- INSTANTIATED_NOT_EXECUTED
- EXECUTED
- EVALUATED
- SUPERSEDED

Use existing canonical status terminology when available.

Do not modify a global schema merely to force these local planning states unless repository methodology requires it.

## 10. Pass contracts

Every pass contract must define:

- pass ID;
- title;
- purpose;
- authority;
- required predecessors;
- checkpoint dependency;
- governance-phase prerequisites;
- canonical inputs;
- read-only repository scope;
- permitted external research;
- required questions;
- required outputs;
- output structure;
- required evidence;
- validation;
- stopping conditions;
- prohibited actions;
- prohibited claims;
- model-class recommendation;
- AI-first effort dimensions;
- correction protocol;
- handoff to the next pass.

Future outputs must clearly label statements as:

- VERIFIED_FACT
- INFERENCE
- PROPOSAL
- RECOMMENDATION
- OWNER_DECISION_REQUIRED
- DEFERRED
- REJECTED

Every contract must prohibit:

- modifying the repository during an analytical pass unless separately authorized;
- accepting its own recommendations;
- resolving Owner decisions;
- claiming implementation;
- claiming readiness without evidence;
- rewriting predecessor outputs;
- treating chat memory as durable truth.

## 11. Initial status

Use:

PLANNED_NOT_EXECUTED

or the closest existing repository-valid equivalent.

Record the contextual state as:

governance_baseline:
  kernel:
    version: 0.2.0
    status: RATIFIED
    implemented: false
    enforceability_claimed: false
    operational: false

  gov_5:
    status: COMPLETED_CLOSED

  gov_6:
    status: COMPLETED_CLOSED

  gov_7:
    status: INACTIVE_PENDING_AUDIT_AND_SEPARATE_DESIGN_OR_IMPLEMENTATION_AUTHORITY
    direction: ACCEPTED_MINIMUM_GOV_7_DIRECTION_NOT_IMPLEMENTED

  od_006:
    status: UNRESOLVED_TRIGGER_GATED

audit:
  status: PLANNED_NOT_EXECUTED
  authority: SCAFFOLD_CREATION_ONLY
  passes_executed: 0
  gov_7_activated: false
  recommendations_accepted: false
  implementation_authorized: false

Use existing repository terminology where required, but preserve this meaning.

## 12. Registration

Make the smallest repository-authored changes required to make the audit discoverable.

Use existing:

- artifact registries;
- prompt registries;
- review indexes;
- roadmap references;
- decision logs;
- validation profiles;
- learning indexes;

only when their contracts require registration.

Do not:

- alter canonical phase status;
- add the audit as a new governance phase;
- create a new governance authority layer;
- create a new Controller layer;
- activate GOV-7;
- add broad methodology changes;
- modify S0a–S9 planning artifacts;
- modify product implementation;
- modify existing governance evidence.

## 13. Validation

At minimum validate:

- exact prompt custody;
- exact prompt SHA-256;
- unique audit ID;
- unique pass IDs;
- unique prompt IDs;
- prompt-registry consistency;
- pass dependency graph;
- checkpoint dependencies;
- governance-phase prerequisites;
- all required contracts present;
- all referenced paths exist;
- no fake outputs;
- no placeholder execution artifacts;
- status remains planning-only;
- no audit pass marked executed;
- no GOV-7 implementation;
- no phase activation;
- no phase closure;
- no Kernel change;
- no Owner decision inferred;
- authored Markdown validity;
- authored YAML validity;
- applicable schemas;
- repository-authored diff checks;
- affected governance tests.

Run the full governance suite only if:

- existing repository methodology requires it for this artifact type; or
- the change touches shared validation, schemas, registries or state logic.

Run isolated-copy validation only if:

- existing repository methodology requires it; or
- shared tooling changes make repository-local validation insufficient.

Build a review bundle only if:

- existing repository methodology requires it for this change type.

Do not create new validation infrastructure, bundle profiles or schemas merely by habit.

Create or extend only the smallest validator or test support required for the new planning artifacts.

Do not implement:

- the future graph;
- the projection layer;
- telemetry collection;
- prompt-management platform integration;
- prompt optimizer;
- interviewer simulator;
- synthetic-user framework;
- workflow engine;
- MCP server;
- policy-as-code system;
- GOV-7 backlog execution;
- controlled self-hosting;
- self-hosted infrastructure.

## 14. Review bundle

Create a deterministic review bundle only if required by current repository methodology.

When required, include:

- exact received prompt;
- prompt hash;
- audit charter;
- audit plan;
- audit status;
- baseline input manifest;
- artifact and custody contract;
- Owner checkpoint definition;
- model-routing policy;
- pass contracts;
- prompt templates;
- prompt registry;
- registry changes;
- validation reports;
- changed-file inventory;
- final repository diff.

The review bundle is evidence of this scaffold implementation only.

It is not an audit result.

It does not prove that:

- any audit pass was executed;
- any framework was evaluated;
- any strategy was selected;
- GOV-7 is ready;
- GOV-7 is active;
- any recommendation is accepted.

## 15. Commit and push authority

The Project Owner authorizes exactly one bounded commit and a non-force push for this scaffold if and only if:

- startup verification succeeds;
- all changes remain within governance/**;
- all required validation passes;
- no audit pass is executed;
- no repository history is rewritten;
- no external evidence is modified;
- no phase status changes;
- no Kernel change occurs;
- no recommendation is implemented;
- no unresolved material blocker remains.

Suggested commit message:

docs(governance): plan GOV-7 enablement audit

Do not:

- open a pull request;
- merge;
- tag;
- release;
- deploy;
- create a branch;
- switch branches;
- force push.

If validation fails or a scope conflict appears:

- do not commit;
- do not push;
- preserve diagnostics;
- report the blocker.

## 16. Expected final status

If the scaffold is created, validated, committed and pushed successfully, use a final status equivalent to:

AUDIT_PROGRAM_SCAFFOLD_COMPLETED_AND_PUSHED_NOT_EXECUTED

The exact next action must be:

The Project Owner reviews the registered GOV-7 audit program scaffold and
separately decides whether to authorize PASS-01. Do not execute PASS-01,
activate GOV-7 or implement any audit recommendation through this scaffold
result.

## 17. Required return

Return only a concise implementation report with these fields:

Repository:
Branch:
Verified starting local HEAD:
Verified starting remote HEAD:
Startup verification:
Durable governance state:
GOV-5 verified status:
GOV-6 verified status:
Kernel verified version and status:
OD-005 verified status:
OD-006 verified status:
GOV-7 verified status:

Audit root:
Audit ID:
Audit status:
Exact scaffold prompt preserved:
Scaffold prompt SHA-256:
Passes planned:
Owner checkpoints:

Vertical-slice strategy status:
Cross-layer relationship graph requirement:
Graph implementation status:
Controlled self-hosting coverage:
Infrastructure self-hosting coverage:
Interviewer-testing coverage:
Prompt lifecycle and optimization candidate coverage:
Open-ended tool discovery:
Terra/Luna model-routing treatment:
AI-first effort model:

Files created:
Files modified:
Registry updates:
Validation:
Affected tests:
Full governance suite:
Isolated-copy validation:
Review bundle:
Review bundle SHA-256:

Commit:
Push:
Final local HEAD:
Final remote HEAD:
Local/remote aligned:
Worktree:

Audit executed:
Audit passes executed:
GOV-7 activated:
Implementation authorized:
Kernel changed:
Status:
Blockers:
Exact next action: