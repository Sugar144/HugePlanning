---
document_id: GOV-METHOD-OPERATING-CONTRACT-001
version: 0.2.0
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

The declared output artifact must be materialized at that path, use the declared filename and format, contain every required section, state its honest status, and pass the declared validation before any completion claim.

Formal architecture and implementation reports used as durable design,
review, validation, or implementation evidence must be imported into
repository custody before the associated change is committed.

Review bundles are temporary transport and review artifacts unless an
explicit custody decision registers them for long-term preservation.

## Material prompt custody

A prompt is material when it authorizes material repository modification; defines implementation or review scope, affected files, or validation requirements; prepares or executes a formal run; corrects a material defect; authorizes staging, commit, push, pull request, merge, tag, release, deployment, or publication; changes governance methodology, tooling, or authority boundaries; or produces formal architecture, implementation, review, or other durable artifacts. Brief questions, minor clarifications, formatting-only requests, status checks, and messages without repository, execution, authority, or durable-artifact effect are not material.

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
