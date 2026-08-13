---
audit_id: GOV-AUD-001
run_id: GOV-AUD-001-P02-R1
pass_id: PASS-02
version: 0.1.0
status: PROPOSED_UNACCEPTED_ARCHITECTURE_MODEL
compatibility_domain_count: 11
compatibility_mechanism_count: 7
compatibility_combination_count: 77
compatibility_domains:
  - kernel
  - executable_governance
  - methodology
  - stage_contract
  - client_project_lock
  - schema
  - agent
  - skill
  - control
  - validator
  - evidence_format
compatibility_mechanisms:
  - exact_lock
  - compatible_range
  - capability_declaration
  - migration_contract
  - adapter_projection
  - revalidation_requirement
  - unsupported_combination
---

# Version, Migration and Impact Model

## Boundary

**VERIFIED_FACT:** The repository already uses exact versions and hashes for Kernel, methodology locks, schemas, prompts, formal runs, controls and validators. The released client lock pins methodology version, commit, Claude Code version and schema versions. An intentional upgrade procedure is planned, but a complete cross-layer compatibility and migration contract is not implemented.

**VERIFIED_FACT:** KGR-006-R1 found zero ER-001 through ER-020 fully supported by implementation evidence. A compatibility declaration therefore cannot be inferred from requirement traceability or artifact existence.

**PROPOSAL:** Compatibility is a time-bounded claim by an accountable component owner, supported by evidence for an exact scope. Silence, successful parsing, a shared major version, a generated view or one successful run is not a compatibility declaration.

## Version domains and responsibility

| Domain | Canonical owner | Versioned subject | Who may declare compatibility | Minimum evidence |
|---|---|---|---|---|
| Kernel | Human Constitutional Authority | Ratified clause set and scope | Human Constitutional Authority for constitutional compatibility; lower-layer owners only for conformance claims | Ratification/amendment record, impact analysis, independent challenge and migration effect |
| Executable governance | Governance implementation owner for the exact release | Adopted controls and application contracts | Release owner plus independent validation; Project Owner for adoption | Clause/ER coverage, control tests, authority boundaries, unsupported effects, release manifest |
| Methodology | Methodology Owner | S0a-S9 method release | Methodology Owner | Changelog, contract tests, scenarios, schema compatibility, migration notes |
| Stage contract | Governance Derivation Owner and Methodology Owner jointly | Governance-application contract | Both owners for their respective authority; neither may silently declare the other's meaning | Clause/ER source, stage applicability, evidence claim, failure route, compatibility tests |
| Client/project lock | Project Owner through controlled lock procedure | Project's adopted versions | Project Owner for adoption after validator evidence | Exact lock, migration result, project validation, gate decision |
| Schema | Schema owner | Data contract and validation vocabulary | Schema owner | Valid/invalid fixtures, consumer inventory, migration or backward-compatibility tests |
| Agent | Agent contract owner | Role, permissions, inputs, outputs and stop rules | Agent contract owner | Contract diff, scenario evaluation, permission and artifact compatibility |
| Skill | Skill owner | Procedure, preconditions, outputs and checks | Skill owner | Procedure tests or reviewed executions against declared consumers |
| Control | Governance control owner | Prevention, detection, evidence, stop and recovery behavior | Control owner with independent validation for material claims | Effect-class tests, failure paths, evidence and coverage statement |
| Validator | Validator owner | Claim, criteria, fixtures and result semantics | Validator owner for supported input/claim versions | Positive and negative fixtures, regression suite, known limitations |
| Evidence format | Evidence custodian and consuming gate owner | Durable record shape and provenance | Joint declaration by producer and consumer owners | Parsing, semantic-field coverage, retention/correction behavior and historical readability |

**REJECTED:** A lower layer declaring that its own change is compatible with a higher authority when the change alters higher-layer meaning, reserved authority or constitutional guarantees.

## Compatibility mechanisms

| Mechanism | Meaning | Appropriate use | Required evidence | Failure semantics |
|---|---|---|---|---|
| Exact lock | One exact version, commit or hash | Trust roots, formal prompts, immutable run inputs, critical schemas and released methodology | Existence, hash, identity and exact consumer validation | Any mismatch is unsupported and blocks |
| Compatible range | Declared set or semantic range | Stable lower-risk interfaces with tested backward compatibility | Range tests, version policy and excluded combinations | Outside range is unsupported; inside range still subject to declared conditions |
| Capability declaration | Version states supported effect classes and limits | Provider, agent, skill, validator or control capability | Named effect classes, limitations and evidence | Missing capability is unknown/unsupported, not assumed |
| Migration contract | Explicit before/after transformation and decision | Schema, methodology, control, project lock and evidence-format changes | Inventory, transformation, semantic fidelity, rollback/compensation and revalidation | Partial or failed migration remains visible and blocks dependent gates |
| Adapter/projection | Preserve old interface or derive a compatible view | Read-only compatibility, reporting, gradual transitions | Source provenance, freshness, semantic-loss statement and tests | Adapter does not upgrade canonical authority; stale view is discarded |
| Revalidation requirement | Keep version but require claims to be re-established | Validator, criteria, agent, skill, provider or control change | Trigger rule, affected claims and completed revalidation evidence | Previous result becomes stale for affected claims |
| Unsupported combination | Explicit refusal | Unknown, unsafe, untested or expired combinations | Reason, affected scope, owner and possible migration/research route | Operation/adoption remains blocked |

## 77-cell compatibility responsibility matrix

Each of the eleven rows is assessed against all seven mechanisms; this yields 77 declared combinations. The entries are architectural responsibilities, not current implementation claims.

| Domain | Exact lock | Compatible range | Capability declaration | Migration contract | Adapter/projection | Revalidation | Unsupported combination |
|---|---|---|---|---|---|---|---|
| Kernel | `PRIMARY` | `REJECTED_FOR_CONSTITUTIONAL_IDENTITY` | `N/A` | `REQUIRED_ON_AMENDMENT` | `READ_ONLY_VIEW_ONLY` | `REQUIRED_FOR_DERIVATIONS` | `REQUIRED` |
| Executable governance | `PRIMARY_FOR_RELEASE` | `CONDITIONAL` | `REQUIRED` | `REQUIRED` | `CONDITIONAL_READ_ONLY` | `REQUIRED` | `REQUIRED` |
| Methodology | `PRIMARY_FOR_PROJECT_LOCK` | `CONDITIONAL_BY_RELEASE_POLICY` | `REQUIRED_FOR_STAGE_SUPPORT` | `REQUIRED_ON_BREAKING_CHANGE` | `CONDITIONAL` | `REQUIRED` | `REQUIRED` |
| Stage contract | `PRIMARY_FOR_GOVERNED_TRANSITION` | `CONDITIONAL` | `REQUIRED` | `REQUIRED_ON_MEANING_OR_FIELD_CHANGE` | `READ_ONLY_ONLY` | `REQUIRED` | `REQUIRED` |
| Client/project lock | `PRIMARY` | `NOT_A_LOCK_SEMANTIC` | `REFERENCED_FROM_COMPONENTS` | `REQUIRED_FOR_UPGRADE` | `CONDITIONAL_FOR_READS` | `REQUIRED` | `REQUIRED` |
| Schema | `PRIMARY_FOR_INSTANCES` | `CONDITIONAL_WHEN_TESTED` | `REQUIRED_FOR_FEATURE_SUPPORT` | `REQUIRED_ON_BREAKING_CHANGE` | `CONDITIONAL_READ_ADAPTER` | `REQUIRED` | `REQUIRED` |
| Agent | `PRIMARY_FOR_FORMAL_RUNS` | `CONDITIONAL` | `REQUIRED` | `CONDITIONAL_ON_OUTPUT_OR_AUTHORITY_CHANGE` | `REJECTED_FOR_AUTHORITY_TRANSLATION` | `REQUIRED` | `REQUIRED` |
| Skill | `PRIMARY_FOR_FORMAL_USE` | `CONDITIONAL` | `REQUIRED` | `CONDITIONAL_ON_PROCEDURE_CHANGE` | `CONDITIONAL` | `REQUIRED` | `REQUIRED` |
| Control | `PRIMARY_FOR_COVERAGE_CLAIM` | `CONDITIONAL` | `REQUIRED_BY_EFFECT_CLASS` | `REQUIRED_ON_SUPERSESSION` | `REJECTED_IF_IT_WEAKENS_OUTCOME` | `REQUIRED` | `REQUIRED` |
| Validator | `PRIMARY_FOR_DURABLE_RESULT` | `CONDITIONAL_BY_INPUT_CONTRACT` | `REQUIRED_BY_CLAIM` | `CONDITIONAL_FOR_RESULT_FORMAT` | `CONDITIONAL_READ_ONLY` | `REQUIRED_ON_CRITERIA_OR_FIXTURE_CHANGE` | `REQUIRED` |
| Evidence format | `PRIMARY_FOR_HISTORICAL_RECORD` | `CONDITIONAL_FOR_READERS` | `REQUIRED_FOR_FIELDS_AND_PROVENANCE` | `REQUIRED_IF_SEMANTICS_CHANGE` | `PREFERRED_FOR_HISTORICAL_READS` | `REQUIRED_FOR_DEPENDENT_CLAIMS` | `REQUIRED` |

## Compatibility declaration contract

**PROPOSAL:** Every compatibility declaration contains:

```yaml
declaration_id:
declarer:
authority_scope:
source_component: {kind:, id:, version:}
target_component: {kind:, id:, version_or_range:}
mechanism:
supported_scope:
excluded_scope:
capabilities:
evidence:
tests:
known_limitations:
declared_at:
expires_or_review_due:
change_triggers:
migration_contract:
revalidation_required:
```

**PROPOSAL:** The declarer must own the source component and have evidence from the target owner or an agreed interface test. Cross-owner compatibility cannot be unilaterally declared when the target's meaning, safety or authority is material.

**OWNER_DECISION_REQUIRED:** OD-P02-011 — identify which actor may publish cross-owner compatibility declarations and what disputes require Project Owner disposition.

## Supersession

**PROPOSAL:** Supersession is append-only:

```text
old version remains addressable
→ new version identifies old version
→ change and reason are explicit
→ compatibility and migration effects are declared
→ affected locks and projects are inventoried
→ required revalidation occurs
→ release/adoption decision is recorded
```

**VERIFIED_FACT:** This matches existing Kernel and requirement history: the ratified Kernel supersedes the candidate as current constitutional authority while preserving the proposed source and completed run evidence.

**REJECTED:** Editing historical evidence or old accepted records so that they appear to have used the new version.

## Migration lifecycle

**PROPOSAL:** Use these states:

```text
IMPACT_UNKNOWN
→ INVENTORIED
→ MIGRATION_CONTRACT_PREPARED
→ READY_FOR_MIGRATION
→ MIGRATION_IN_PROGRESS
→ MIGRATED_PENDING_REVALIDATION
→ REVALIDATED
→ ADOPTED
```

Valid non-success states are:

```text
BLOCKED_UNSUPPORTED_COMBINATION
PARTIAL_EFFECTS_CONTAINED
ROLLED_BACK
COMPENSATION_REQUIRED
RETURNED_FOR_CONTRACT_CORRECTION
TERMINATED_ON_PRIOR_SUPPORTED_VERSION
```

**PROPOSAL:** A migration contract names source/target versions, affected canonical entities, transformation, semantic-fidelity checks, authority, irreversible effects, backup/rollback or compensation, validation, independent evaluation if required, adoption decision and historical preservation.

## Revalidation triggers

**PROPOSAL:** Revalidation is mandatory when any of the following changes for a dependent claim:

- Kernel clause or derived requirement meaning;
- stage applicability, gate criteria or governance-application contract;
- schema required field, enum, identity, provenance or status semantics;
- agent authority, permissions, context construction, output contract or stop behavior;
- skill preconditions, procedure or validation checks;
- control effect-class coverage;
- validator claim, fixtures, criteria or result semantics;
- evidence format fields or correction behavior;
- provider capability used by the claim;
- migration or adapter behavior.

**INFERENCE:** Patch-level version labels alone cannot settle whether revalidation is required; the change contract and affected claim decide it.

## Impact-analysis semantics

### Direct impact

**PROPOSAL:** `DIRECT` requires a validated typed path from the changed entity to the affected entity through applicability, dependency, lock, control, execution, validation, evidence, release or migration relationships.

Examples:

- schema → project artifact instance;
- Kernel clause → ER → control → stage contract;
- validator → validation result using that validator version;
- methodology release → project exact lock.

### Probable impact

**PROPOSAL:** `PROBABLE` applies when evidence shows shared interface, duplicated meaning, common executor, provider capability or conditional applicability, but the canonical typed path is incomplete.

Examples:

- agent prompt changes while task contracts omit explicit agent version;
- shared safety wording appears in multiple contracts without a canonical source link;
- provider capability changes and affected effect classes are known but project usage inventory is incomplete.

### Unknown impact

**PROPOSAL:** `UNKNOWN` applies when provenance, version, applicability, ownership or inventory is missing or stale. Unknown does not mean unaffected and must block a claim that requires complete impact knowledge.

## Required impact queries

| Change | Direct traversal | Probable expansion | Unknown condition | Required disposition |
|---|---|---|---|---|
| Kernel clause | derived requirements → policies/contracts → controls → stages/projects | duplicated boundaries and shared constitutional terms | missing clause/requirement provenance | constitutional impact review and lower-layer revalidation |
| Methodology stage | applicability/contracts → gates/artifacts/agents | adjacent stages and shared profiles | incomplete stage-contract inventory | methodology change contract and project migration assessment |
| Schema | locks/instances/validators → gates/releases | generated documents and external consumers | unregistered instances | migration or exact unsupported declaration |
| Agent or skill | executed controls/contracts → outputs/tests | shared context, permissions and knowledge | unbound version in historical work unit | scenario evaluation and affected claim revalidation |
| Validator | validated subjects/results → gates/releases | similar profiles and fixtures | result lacks validator/criteria version | mark result stale and rerun |
| Control supersession | requirements/contracts → executors/validators/projects | related effect classes | incomplete control inventory | migration, compatibility and coverage reassessment |
| Client project migration | current lock → component versions → artifacts/releases | external providers and local manual procedures | missing project inventory or backup | block until inventory and recovery basis exist |
| Historical evidence correction | evidence → claims/findings/decisions | summaries and projections | source bytes unavailable | append limitation/correction; never rewrite old evidence |

## Release and rollback boundary

**VERIFIED_FACT:** The planned client release architecture already distinguishes release manifest, verification snapshot, migrations, backup and rollback. Governance adoption is not yet integrated into that runtime.

**PROPOSAL:** A future governance-aware release must additionally bind executable-governance version, stage-contract version, control/validator versions and evidence-format version. Rollback may restore software and locks; it cannot erase disclosures, costs, communications, decisions or other irreversible effects, which require reconciliation or compensation.

## Owner decisions and deferred work

**OWNER_DECISION_REQUIRED:** OD-P02-012 — choose the compatibility and migration evidence threshold for CHECKPOINT-A acceptance as a design basis.

**OWNER_DECISION_REQUIRED:** OD-P02-011 — assign publication authority for cross-owner compatibility declarations.

**DEFERRED:** Select a migration engine, compatibility service, artifact database or graph/query implementation.

**DEFERRED:** Instantiate project migrations before an executable-governance version and adopted stage contract exist.
