{"cross_shard_relationships": [{"from_path": "governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md", "from_shards": ["B-01-S01"], "from_unit_id": "seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G3/GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md:all", "relationship": "CLASSIFIED_SEED_REFERENCE", "to_path": "governance/methodology/project-operating-contract.md", "to_shards": ["B-01-S03"], "to_unit_id": "source:governance/methodology/project-operating-contract.md"}, {"from_path": "governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md", "from_shards": ["B-01-S03"], "from_unit_id": "seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:\u00a77", "relationship": "CLASSIFIED_SEED_REFERENCE", "to_path": "governance/AGENTS.md", "to_shards": ["B-01-S02"], "to_unit_id": "source:governance/AGENTS.md"}, {"from_path": "governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md", "from_shards": ["B-01-S03"], "from_unit_id": "seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:\u00a77", "relationship": "CLASSIFIED_SEED_REFERENCE", "to_path": "governance/tools/validate_governance_state.py", "to_shards": ["B-01-S02"], "to_unit_id": "source:governance/tools/validate_governance_state.py"}, {"from_path": "governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md", "from_shards": ["B-01-S03"], "from_unit_id": "seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:\u00a77", "relationship": "CLASSIFIED_SEED_REFERENCE", "to_path": "governance/tools/validate_prompts.py", "to_shards": ["B-01-S02"], "to_unit_id": "source:governance/tools/validate_prompts.py"}], "frozen_revision": "6fc4fa1a14a665fabfcceb00729222527cd192ba", "logical_layers": ["L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7"], "projection": "GOV-GEN-G6-B-01-SHARDED", "shard_id": "B-01-S03"}

--- source_root governance/methodology/project-operating-contract.md EXACT_CLASSIFIED_PATH source:governance/methodology/project-operating-contract.md ---
---
document_id: GOV-METHOD-OPERATING-CONTRACT-001
version: 0.3.0
status: IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW
constitutional_authority: NONE
---

# Project Operating Contract

## Purpose and precedence

This contract defines stable operating semantics for repository work. It does not authorize an action, execute a protocol, validate an artifact, accept risk, ratify the Kernel, or open Enforcement Engineering.

Applicable authority descends from platform constraints, the Project Owner's explicit current instruction, repository and closest path-scoped `AGENTS.md`, a formally bound run set, canonical methodology, role protocols, schemas, and finally generated views. A lower layer may specialize but must not silently contradict a higher layer. Historical run snapshots govern their runs even after canonical methodology changes.

## Authority boundaries and preview-first workflow

The Project Owner retains authorization, sequencing, acceptance, risk, publication, and ratification authority. Designer, Adversary, future Controller, implementer, and validator authority is bounded by their explicit contracts. No actor inherits another actor's authority, and no prior authorization is reusable outside its stated scope.

For a material change, first identify intended paths, effects, validation, exclusions, and each separately authorized publication step. Perform only the authorized scope. Modification, staging, commit, push, pull request, merge, tag, release, deployment, and publication are distinct actions.

## Durable truth and status vocabulary

Durable truth is ordered: immutable source and run evidence; explicit decisions and transition records; accepted registry and state records; versioned methodology and schemas; then generated indexes, summaries, reports, and conversational context. Derived views must reconcile with their sources.

- `PROPOSED`: offered for review, without approval or authority.
- `PREPARED`: inputs or contracts are assembled; execution has not occurred.
- `EXECUTED`: the contracted activity occurred; validity is not implied.
- `VALIDATED`: declared checks passed against identified requirements.
- `ACCEPTED`: a competent owner accepted a bounded result or risk.
- `RATIFIED`: competent human constitutional approval was explicitly recorded.
- `IMPLEMENTED`: artifacts or controls exist locally or in the identified system.
- `OPERATIONAL`: implementation is adopted, active, and supported by operational evidence.

A protocol, prompt, package, generated artifact, or output directory is not proof of execution.

## Formal execution, orchestration, and output contract

Formal execution is a role-bound analysis with exact identity, inputs, prompt, applicable controls, outputs, status, and provenance. Orchestration selects, transfers, schedules, or validates work but does not itself perform the role's substantive analysis. A future deterministic Controller may replay declared facts and route allowed transitions; it must not decide constitutional sufficiency.

Every formal analysis intended for review, reuse, implementation, comparison,
or versioning must declare before execution its output artifact path,
filename, format, status, required sections, and validation requirements.

Before any formal execution, an exact Project Owner authorization record must
enter repository custody and bind the run, role, mode, protocol, formal input
package hash, permitted execution count, and forbidden actions. A deterministic
pre-execution gate must reject a missing or mismatched record. Readiness,
package custody, a prepared prompt, or retrospective attestation cannot satisfy
this prospective gate.

The declared output artifact must be materialized at that path, use the declared filename and format, contain every required section, state its honest status, and pass the declared validation before any completion claim.

Formal architecture and implementation reports used as durable design,
review, validation, or implementation evidence must be imported into
repository custody before the associated change is committed.

## Versioned formal-run correction identity

A correction of an immutable completed formal run uses
`<BASE_RUN_ID>-R<N>`, where `BASE_RUN_ID` is the original run identity and
`N` is a positive sequential integer beginning at 1. The first correction of
`KGR-006` is therefore `KGR-006-R1`. A correction identity does not overwrite
or replace the base run, does not consume the next unrelated sequential run
identity, and grants no execution, acceptance, risk, ratification, or phase
authority.

Each correction contract must bind the immutable base input package, base
output package, independent-evaluation result and correction findings, and an
explicit Project Owner authorization. It must state the bounded correction
scope, preserve unaffected meaning and evidence, declare a new output
contract, pass deterministic preparation and completed-output validation, and
receive a new independent evaluation outside the corrected source role's
unilateral control. `R<N>` increments only for a later correction of that same
base run; historical artifacts remain immutable. A pre-execution preparation
failure or interrupted preparation is repaired within the same unexecuted run
identity and is not a correction run.

Review bundles are temporary transport and review artifacts unless an
explicit custody decision registers them for long-term preservation.

## Material prompt custody

A prompt is material when it authorizes material repository modification; defines implementation or review scope, affected files, or validation requirements; prepares or executes a formal run; corrects a material defect; authorizes pull request, merge, tag, release, deployment, or publication beyond the bounded exception below; changes governance methodology, tooling, or authority boundaries; or produces formal architecture, implementation, review, or other durable artifacts. Brief questions, minor clarifications, formatting-only requests, status checks, and messages without repository, execution, authority, or durable-artifact effect are not material.

`OWNER_PUBLICATION_AUTHORIZATION` is a distinct evidence type, not a material implementation prompt, only when it comes explicitly from the Project Owner; identifies an already reviewed immutable change set, bundle, inventory, or commit candidate; adds no implementation scope; authorizes only atomic publication actions such as stage, commit, or push; and does not authorize a pull request, merge, release, execution, ratification, risk acceptance, or additional modification. Failure of any condition keeps the instruction subject to ordinary material-prompt custody.

Qualifying `OWNER_PUBLICATION_AUTHORIZATION` may be preserved through publication evidence, commit metadata, operational records, or a subsequent append-only record. Its custody must not require a new pre-publication repository file that changes the authorized change set. The authorization remains bounded to the identified immutable candidate and named atomic actions; it does not imply authority for any other publication or governance step.

Every material prompt receives a stable `HP-PROMPT-###` identifier and a semantic version. The identifier remains stable across corrections to the same prompt lineage; a correction increments the version and records supersession. Categories identify the prompt function without granting authority. Lifecycle states are `DRAFT`, `APPROVED_NOT_EXECUTED`, `EXECUTED`, `SUPERSEDED`, `ABORTED`, `INVALID_EXECUTION`, and `NOT_PRESERVED`.

Preserve the exact prompt text with its authorization scope, forbidden actions, environment, execution status, and links to resulting artifacts, reports, validation evidence, and commit when available. A material prompt must enter repository custody before or as part of the commit containing the work it authorized or defined. Once executed, its file is immutable execution-contract evidence; correction requires a new semantic version and an explicit supersession link. Prompt existence does not establish execution: execution status and evidence remain separate facts.

After interruption, recover from the repository-custodied prompt and durable worktree or result evidence, verify identity and status, record the interruption and resumption, and do not silently substitute a revised prompt. If an exact historical prompt is unavailable, record `NOT_PRESERVED`, describe the evidence limitation, and never reconstruct a plausible text as original evidence.

Formal run prompt snapshots under `governance/runs/<run>/prompt/` retain authoritative custody for their runs. The prompt catalogue references those snapshots and their run evidence without unnecessary byte duplication. Prompt custody carries only the authority explicitly stated in the prompt and cannot expand, reuse, or transfer it.

Prompt custody does not itself prove that the prompt was executed correctly, that its outputs were validated, or that its authorized actions occurred.

## Record classes

Failure and lesson records capture causal learning. Formal run records capture an execution contract and evidence. Operational logs capture transient chronology. Decision records capture authoritative choices. Incident records govern material security or authority breaches. Methodology parking-lot proposals capture prospective improvements without asserting an observed failure. One class may link to another but never substitutes for it.

Material methodology proposals discovered during orchestration must be captured in the canonical methodology backlog before the current reviewed change is closed. They must not remain only in chat or an external working note.

## Deterministic and cost-aware routing

Use offline scripts for exact parsing, duplicate detection, hashing, path safety, member counts, schema checks, comparisons, indexing, serialization, packaging, and state replay. Reserve capable model reasoning for synthesis and judgment that cannot be represented deterministically. Use the least costly capable model or method, and record actual cost data only when preserved. A model may help design a deterministic check, but repeated application belongs to the check; do not recursively launch agents to settle exact machine facts.

## Failure, learning, and immutability

Material failures, near misses, ambiguities, owner corrections, defects, tooling gaps, and cost waste require triage under `../learning/README.md`. Never silently repair a material error. Preserve the observation, impact, cause, containment, correction, prevention, evidence limits, owner, and validation plan. Missing evidence, timestamps, tokens, and quotes remain explicitly unavailable.

Completed runs, bound artifacts, decisions, validated learning bases, and raw sources are historical evidence. Correct methodology prospectively through new versions and append-only events. Supersede; do not rewrite history to match a newer method.

## Traceability, handoffs, and anti-recursion

Lower-layer artifacts must identify the higher-layer source, applicable version, derived requirement, and validation evidence. A lower layer may add implementation detail but may not relax authority, safety, or evidence requirements without an explicit competent decision.

When context is overloaded, create a durable handoff containing scope and authority, verified facts, artifact identities, completed work, open risks and decisions, exact current status, validation state, and exact next action. The handoff is continuity evidence, not new authority.

Stop recursive review when deterministic validation settles the question or when the next step requires owner authority, independent role judgment, new evidence, or a versioned contract correction.

--- seed_fragment governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §3 seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:§3 ---
## 3. Finding F2 — Two wrong "G3 §21 UQ4" citations

The independent review found that base §4.2 (Option B,
`config_projection_boundary`) and base §8 (Recommended candidate) each cite
"G3 §21 UQ4" as the source of the L6 boundary principle Option B's package
boundary is said to functionally resolve the "visibility half" of. This is
defective: `GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md` has no §21 (its highest
section is §12, Completion disposition); `UQ4` is defined and dispositioned in
G3 §8 ("G2 unresolved-question disposition"), item 4. "§21" is G2's own
unresolved-questions section (`GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md` §21),
not G3's — the two documents' numbering was conflated.

**Both citations are corrected from "G3 §21 UQ4" to "G3 §8 UQ4"**, with no
other change to either sentence:

- §4.2, Option B, `config_projection_boundary`: "...directly answering
  G3 §21 UQ4's boundary principle without performing the declarative L6
  rewrite itself" → "...directly answering G3 §8 UQ4's boundary principle
  without performing the declarative L6 rewrite itself."
- §8, Recommended candidate: "...functionally resolving the *visibility*
  half of G3 §21 UQ4 without yet performing its declarative rewrite" →
  "...functionally resolving the *visibility* half of G3 §8 UQ4 without yet
  performing its declarative rewrite."

The substantive claim both sentences make — that Option B's package boundary
functionally answers UQ4's boundary-*visibility* principle without performing
its declarative-rewrite *mechanics* — is independently accurate against the
corrected location (G3 §8's UQ4 disposition, "`LOGICALLY_RESOLVED_BY_G3`" for
the boundary principle, mechanics deferred) and is unaffected by this
citation fix.


--- seed_fragment governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §7 seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:§7 ---
## 7. Correction-session validation

1. Worktree clean before this correction's writes began; no Git command
   beyond read-only inspection (including the one targeted G2 lookup, §2) was
   run outside this correction's authorized paths.
2. G5-A is not redone; no option is added, removed, or redefined; no L0–L7
   mapping cell outside §4's citation fix is changed; no G3 capability is
   reallocated; no G2 capability is reclassified; no G2 gap is redisposed; G2,
   G3, and G4 are not reopened.
3. No target-architecture selection, kernel-ownership decision, or
   implementation of any G4 requirement, architecture pressure, Delegated
   Operational Authority, Provider-Neutral Governance, adapter, or
   query/projection tooling exists anywhere in this correction.
4. This correction is not independently reviewed, and G5 (base or corrected)
   is not accepted, rejected, or self-accepted anywhere in this document.
5. `governance/AGENTS.md` and root `AGENTS.md` are unmodified.
6. Exactly one correction artifact (this file) plus its manifest exists for
   the base deliverable; the minimum current-state reconciliation paths
   listed in §6 are the only other paths touched.
7. Hash manifest for this file verifies
   (`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.manifest.sha256`), and
   the base deliverable's own manifest independently re-verifies unmodified
   (`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001.manifest.sha256`,
   SHA-256 `a57d34c73e64495214db96278f9d9176898ca68a14263db63bf77b10cd806e2e`,
   unchanged from the independent review's own recorded
   `reviewed_candidate_sha256`).
8. `python governance/tools/validate_prompts.py` and
   `python governance/tools/validate_governance_state.py` pass against the
   fully corrected working tree — see completion disposition (§8) for the
   actual run result.


--- seed_fragment governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md §8 seed:governance/audits/GOV-GEN-AUD-001-governance-generalization/G5/GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md:§8 ---
## 8. Completion disposition

```yaml
completion:
  status: G5_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  base_head: f25f7fba4aecf382f1124971474f24ecbbc72574
  findings_corrected: 4
  finding_ids: [GOV-GEN-G5-IR-001-F1, GOV-GEN-G5-IR-001-F2, GOV-GEN-G5-IR-001-F3, GOV-GEN-G5-IR-001-F4]
  base_deliverable_modified: false
  base_deliverable_sha256: a57d34c73e64495214db96278f9d9176898ca68a14263db63bf77b10cd806e2e
  correction_manifest: GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.manifest.sha256
  targeted_lookups_performed_by_this_correction: 1
  targeted_lookup_target: "GOV-GEN-G2-CLASSIFICATION-MATRIX-001.md §17.2 and §23 (reuse_readiness_counts)"
  options_added_removed_or_redefined: 0
  l0_l7_mapping_cells_changed: 0
  requirements_compliance_cells_changed: 1
  requirements_compliance_cell_changed_id: RD-C5
  requirements_compliance_cell_change: STRUCTURALLY_ENABLED_to_NOT_ADDRESSED
  blocks_reuse_entries_individually_reasoned: 6
  recommendation_shape_unchanged: true
  recommended_candidate_shape: STAGED_SEQUENCE_B_THEN_OPTIONAL_D_THEN_DEFERRED_C_WITH_A_AS_FALLBACK
  g3_capability_reallocation_performed: false
  g2_capability_reclassification_performed: false
  g2_gap_redisposition_performed: false
  g2_g3_g4_reopened: false
  target_architecture_selected: false
  repository_created: false
  file_extracted_or_migrated: false
  agents_md_modified: false
  correction_independently_reviewed: false
  g5_accepted_or_rejected: false
  next_authority_required: OWNER_ACCEPTANCE_OF_G5_CORRECTED_R1_RESULT
```

The executor does not accept this correction, does not independently review
it, and does not accept, reject, or select among G5's options. Project Owner
acceptance, rejection, or a request for further bounded correction is a
separate, subsequent act, exactly as under the base deliverable (§12 of the
base) and under `GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1/0.1.0` §8. No
push has been performed.

`GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1/0.1.0 G5_CORRECTION_READY_FOR_PROJECT_OWNER_ACCEPTANCE`
