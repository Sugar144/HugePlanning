---
prompt_id: HP-PROMPT-011
version: 0.1.0
category: ORCHESTRATION
evidence_type: MATERIAL_PROMPT
status: EXECUTED
purpose: Prepare but do not execute the minimum-scope GOV-5 formal analysis contract
target_environment: Codex CLI
repository_branch: governance/kernel-designer-revision-v0.1
repository_base_head: 7cfc92ed63fbba06232ceba8e4c9b5e10f0258dc
authorization_scope:
  - prepare the KGR-006 GOV-5 formal analysis contract and custody
  - add minimum schemas, validator coverage, tests, readiness, report, and review bundle
  - commit and push only after all required validation passes
forbidden_actions:
  - execute GOV-5 or invoke the Enforcement Engineer
  - modify Kernel, Controller, closure-loop, or constitutional semantics
  - implement GOV-7, perform GOV-8 or GOV-9, or modify product/runtime code
  - open a pull request, merge, release, ratify, or accept risk
exact_text_preserved: true
exact_text_sha256: 901eb3ce93480eeb966c8ff84b063f08a8db5c1d227cd4b51077b59d7ee23ae7
execution_interrupted: false
execution_resumed: true
result_artifacts:
  - governance/runs/KGR-006-enforcement-analysis/
  - governance/reviews/gov-5-contract-preparation/implementation-report-v0.1.0.md
result_commit: null
supersedes: null
---

# GOV-5 Contract Preparation Prompt

## Exact executed text

You are working inside the HugePlanning repository.

TASK

Prepare, but do not execute, the minimum-scope GOV-5 formal analysis contract.

Repository:
Sugar144/HugePlanning

Branch:
governance/kernel-designer-revision-v0.1

Phase:
GOV-5 — Enforcement analysis and derived governance requirements

Mode:
CONTRACT_PREPARATION_ONLY

Use the current clean branch HEAD as the exact preparation baseline. Report it before modifying anything.

Use repository instructions, durable state, existing governance methodology, schemas, tools, skills, prompt custody, learning system, and the completed GOV-5 scope-review recommendation as authoritative context.

Do not restart discovery and do not reinterpret the Kernel.

OWNER DECISIONS

The Project Owner has decided:

gov_5_scope: MINIMUM

initial_operating_context:
  primary_user: PROJECT_OWNER
  current_scale: SINGLE_USER

future_scalability_intent:
  possible_commercialization: true
  priority_commercializable_component:
    - technical_document_discovery_and_generation

design_constraints:
  - avoid_irreversible_single_user_coupling
  - preserve_provider_portability
  - preserve_artifact_exportability
  - preserve_project_data_separation
  - preserve_future_multi_project_and_multi_user_evolution
  - do_not_implement_commercial_platform_features_now

specialist_strategy: TRIGGER_GATED

specialist_triggers:
  - material_legal_or_privacy_dependency
  - material_security_or_isolation_dependency
  - provider_capability_requires_empirical_validation
  - high_consequence_human_decision_usability_risk
  - operational_recovery_or_continuity_dependency

current_non_goals:
  - multi_tenant_platform
  - billing
  - enterprise_identity
  - commercial_sla
  - full_policy_suite
  - complete_provider_testing
  - control_implementation

Future scalability is a design constraint, not authorization to design or implement a commercial product.

GOV-5 PURPOSE

Prepare a bounded formal contract for analyzing the practical prevention, detection, evidence, stopping, recovery, compensation, feasibility, cost, and human-authority implications of Kernel 0.2.0-proposed.

GOV-5 must support a later human ratification decision and recommend the smallest GOV-7 executable governance package.

GOV-5 must not implement that package.

REQUIRED RESPONSIBILITIES OF THE FUTURE FORMAL RUN

The future Enforcement Engineer analysis must:

1. Bind the exact closed Kernel proposal and governance state.
2. Assess all seven Kernel clauses.
3. Consume the existing lower-layer routing rather than recreating it.
4. Consume KGR-003 findings, KGR-004 dispositions, and KGR-005 closure evidence without reopening closed findings unless contradictory repository evidence is found.
5. Identify for every clause and relevant effect family:
   - prevention implications;
   - detection implications;
   - evidence requirements;
   - stopping implications;
   - recovery or compensation implications;
   - feasibility limits;
   - cost and burden implications;
   - residual risks;
   - reserved human decisions.
6. Distinguish requirements from candidate mechanisms.
7. Inventory existing repository capabilities honestly.
8. Identify absent, partial, provider-dependent, specialist-dependent, or infeasible capabilities.
9. Recommend the minimum GOV-7 package for one bounded governed transition.
10. Produce a clear handoff for human ratification.
11. Preserve scalability concerns that are difficult to retrofit later without implementing future commercial functionality now.

MANDATORY CLASSIFICATIONS

Each relevant responsibility or requirement must receive a timing classification:

MUST_BEFORE_RATIFICATION
MUST_BEFORE_GOVERNED_PILOT
SHOULD_LATER
HUMAN_ONLY
NOT_FEASIBLE

Each clause implication must identify which lower layer is required:

policy
standard
procedure_or_contract
control
evidence
human_judgment

Each capability assessment must use a bounded status vocabulary such as:

SUPPORTED_BY_EVIDENCE
PARTIAL
GAP
DEPENDENT_ON_SPECIALIST
DEPENDENT_ON_PROVIDER_TEST
NOT_FEASIBLE
NOT_APPLICABLE

Define the exact enums in the formal output schemas rather than relying on prose alone.

REQUIRED FORMAL OUTPUTS

Prepare a formal output contract for exactly these seven future outputs:

00-enforcement-analysis-basis.md
01-clause-implication-matrix.yaml
02-existing-capability-inventory.md
03-feasibility-coverage-and-gap-assessment.md
04-owner-decisions-and-residual-risks.md
05-minimum-executable-package-recommendation.md
06-ratification-decision-handoff.md

The contract must ensure:

- all seven Kernel clauses are covered;
- all applicable lower-layer routing entries are accounted for;
- classifications use strict enums;
- gaps and limitations cannot be omitted;
- specialist dependencies are trigger-gated and tied to a specific issue;
- future-scalability implications are recorded without expanding current implementation scope;
- Markdown and structured outputs cannot materially contradict each other;
- the result cannot claim ratification, enforceability, implementation, operation, maturity, or compliance.

ROLE AND INDEPENDENCE

Prepare the narrowest necessary role/mode contract for the future Enforcement Engineer.

The role may analyze and recommend.

It may not:

- modify Kernel meaning;
- accept risk;
- ratify;
- implement controls;
- create a full policy suite;
- activate GOV-6 or GOV-7;
- declare enforceability;
- modify product or runtime code;
- allocate authority to itself.

Also prepare the required independent-evaluation handoff and independence boundary.

Do not execute the evaluator and do not prepare a second large formal process unless the existing methodology genuinely requires it.

FORMAL-RUN IDENTITY AND CUSTODY

Do not assume the next run is KGR-006.

Determine the next valid formal-run identifier from repository contracts and current durable state.

Prepare:

- run directory and manifest;
- immutable input envelope;
- exact prompt snapshot;
- role and mode contract;
- output contract;
- minimal schemas;
- deterministic validator profile;
- package inventory;
- readiness record;
- registry and current-state updates appropriate for a prepared but unexecuted run.

The formal input package must bind exact repository artifacts or immutable snapshots with hashes.

Do not include irrelevant repository history.

AUTHORITATIVE INPUT SET

At minimum, bind:

- current governance state and master plan;
- Kernel 0.2.0-proposed Markdown and YAML;
- KGR-001 hazards, authority and effects model, criticality model, scenarios, assumptions, and intake summary;
- KGR-003 findings and enforcement concerns;
- KGR-004 disposition register, lower-layer routing, open questions, and proposed Kernel package;
- KGR-005 closure result and residual-risk routing;
- current governance capability inventory represented by tools, schemas, skills, learning records, validation records, and operating contracts;
- S0a–S9 implementation roadmap;
- the Project Owner decisions contained in this prompt.

Prefer hash-bound repository references or byte-identical snapshots according to existing custody rules.

DETERMINISTIC VALIDATION

Extend existing tooling only where necessary for this formal contract.

Prefer existing tools and shared libraries.

Add only the minimum deterministic validation required to verify:

- run, role, mode, protocol, prompt, and envelope identities;
- exact input inventory and hashes;
- exact seven-output inventory;
- strict YAML parsing;
- JSON Schema validity;
- complete seven-clause coverage;
- allowed timing, layer, capability, and specialist classifications;
- lower-layer routing coverage;
- cross-file parity;
- forbidden status claims;
- future-scalability constraints remaining analysis-only;
- readiness without execution.

Do not build an enforcement platform.

Do not duplicate logic already present in repository tools.

SPECIALIST HANDLING

Specialists must not be assigned by default.

The contract must require each specialist dependency to identify:

trigger
affected_clause
affected_effect_or_requirement
why_general_analysis_is_insufficient
required_specialist_type
blocking_or_nonblocking
safe_interim_boundary
later_phase_destination

A specialist dependency may remain unresolved before ratification only when the affected capability is explicitly unsupported or blocked and this does not conceal a constitutional ambiguity.

HISTORICAL AND AUTHORITY BOUNDARIES

Do not:

- execute GOV-5;
- invoke the Enforcement Engineer;
- produce substantive enforcement conclusions;
- modify Kernel content;
- reopen GOV-4;
- create policies, standards, procedures, or controls beyond the analysis contract;
- implement GOV-7;
- perform GOV-8 regularization;
- run the S2 pilot;
- accept risk;
- ratify;
- open a pull request;
- merge;
- release.

Preparation is not execution.

Readiness is not acceptance.

Analysis is not enforceability.

LEARNING AND SESSION REVIEW

Use agent-session-reviewer before completion.

Preserve any material defect, ambiguity, unnecessary repeated work, portability problem, validation gap, or reusable lesson through the existing learning system.

Do not silently repair a material defect.

Stop if correction requires changing Kernel, Controller, closure-loop, or constitutional semantics.

VALIDATION AND PUBLICATION

Run proportional affected validation, including:

- new contract and schema tests;
- package-preparation validation;
- prompt-custody validation;
- learning-system validation;
- relevant existing pytest and Hypothesis tests;
- skill or role structure validation;
- registry and generated-view consistency;
- git diff --check;
- deterministic review-bundle validation.

Produce a Phase GOV-5 contract-preparation implementation report and external review bundle.

If all preparation work validates, no unresolved material blocker remains, and no scope drift occurs:

- commit the complete authorized preparation delta;
- push the current branch;
- verify local and remote HEAD alignment;
- verify a clean worktree.

Do not open a pull request.

STOP CONDITIONS

Stop and report instead of publishing when:

- the branch or worktree is not suitable;
- the prior maintenance correction is incomplete or validation remains red;
- the next run identity is ambiguous;
- the Kernel or routing evidence conflicts materially;
- the minimum contract cannot support ratification without substantive new owner decisions;
- the output contract would require designing controls;
- a specialist dependency changes constitutional meaning;
- scope expands into GOV-6, GOV-7, GOV-8, GOV-9, or product implementation;
- validation fails;
- a shared semantic contract would need modification beyond this authorization.

COMPLETION REPORT

Return the requested branch, identity, custody, validation, publication, session-review, and exact-next-action fields.
