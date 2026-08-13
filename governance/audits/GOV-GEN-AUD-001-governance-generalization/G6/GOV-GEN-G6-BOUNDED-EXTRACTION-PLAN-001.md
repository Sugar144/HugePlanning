---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001
version: 0.1.0
program_id: GOV-GEN-AUD-001
phase: G6
contract: GOV-GEN-G6-CONTRACT-001/0.1.0
status: G6_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
authority: PLAN_ONLY_NOT_EXTRACTION_EXECUTION
controlling_architecture_decision: GOV-GEN-DECISION-019/0.1.0
---

# GOV-GEN-G6 — Bounded Extraction Plan

## 1. Decision-preserving result

Option B's minimum reusable physical boundary is an in-place, versioned
**L0–L2 core contract surface plus a declared L1 configuration seam**. It
must have no dependency on HugePlanning's L3 values, L5 evidence, or literal
project paths. L3 stays in HugePlanning as the adopting project's projection;
L5 stays there as its append-only evidence and historical custody. L4 remains
outside the core as provider-specific adapters. L6 is split only where a
capability is already infrastructure-pure; project-bound validation and all
L7 entrypoints remain project-owned until separately designed.

This is a physical boundary, not a claim of external reuse, provider
neutrality, distributed L0, or resolution of AP-1–AP-6. HugePlanning becomes
the first adopter by consuming the in-place core through an explicit local
binding while retaining its Owner, current L3 projections, L5 custody, and
existing governance instructions until a later authorized, semantics-proven
adoption change.

## 2. Dependency order and readiness

`B-01 → B-02 → B-03 → B-04 → B-05 → B-06 → B-07 → B-08`.

The safest first packet is **B-01**, a read-only boundary inventory and
semantic-baseline package. It changes no active behavior and makes B-02's
source/target boundary falsifiable before any artifact moves.

`READY` capability families that may move after B-01/B-02 boundary proof,
without semantic redesign, are pure L6 infrastructure (`CAP-NAV13-001` and
the record-type schema/tool helpers it supports), plus the reusable existing
mechanics represented by READY custody/manifest/check primitives. Their
individual inclusion is still determined by B-02's literal-dependency scan;
`READY` never authorizes a project-bound caller to move with them.

`NEEDS_NORMALIZATION` items require B-03's declared L1 configuration seam
first: run/program packaging (`CAP-NAV07-001/002`), phase/projection wiring
(`CAP-NAV01-004/005`), closure-loop naming (`CAP-NAV04-004`), prompt-index
reconciliation (`CAP-NAV05-001`), and project-coupled review/run instances.
`NEEDS_MODEL_CHANGE` items are blocked from extraction: project-specific
kernel/role content (`CAP-NAV02-001`, `CAP-NAV04-005/006/007`) remains L3;
the project-hardcoded state validator (`CAP-NAV06-004`/`CAP-NAV13-008`)
requires the later declarative model packet; query/index, DOA, second adapter,
identity, and program-state work require their named prerequisite packets.

## 3. Packet execution contract

Every packet below is prospective. Its bounded input projection is generated
from the listed exact pointers plus its immediate predecessor outputs, and is
targeted at <=20k model tokens. No packet may load the full GOV-GEN history.

```yaml
- packet_id: B-01
  objective: Establish an immutable, semantic baseline and exact candidate boundary inventory for Option B; perform no extraction.
  source_scope: Current HugePlanning governance L0-L7 realizations named by G3 plus their direct imports.
  target_scope: A generated G6 evidence projection only; no runtime target.
  logical_layers: [L0, L1, L2, L3, L4, L5, L6, L7]
  capabilities: [boundary inventory, provenance map, semantic baseline]
  requirements_or_pressures: [AP-1, AP-2, AP-3, AP-4, AP-5, AP-6]
  preconditions: [Owner-authorized packet execution, clean scoped worktree, frozen source revision, B-01 input projection <=20k tokens]
  allowed_mutations: [packet-local inventory, dependency graph, hashes, baseline test/report]
  forbidden_mutations: [all implementation artifacts, AGENTS.md, CLAUDE.md, L3, L5, target directories]
  bounded_inputs: [G3 R2 §§4,6-8,10, G4 R1 §§4, G4 base §9, G5 R1 §4.2/§7/§8, GR §§3-5, direct source files named by inventory]
  validation: [source hashes, direct-import closure, baseline deterministic checks, explicit L3/L5 exclusion, no implementation diff]
  independent_review_required: true
  rollback_or_recovery: Delete only packet-local generated evidence; source tree remains unchanged.
  completion_state: B-01_BOUNDARY_BASELINE_REVIEW_READY
  depends_on: []

- packet_id: B-02
  objective: Create the minimum in-place L0-L2 physical core boundary and its local HugePlanning adopter binding, using only B-01-approved candidate content.
  source_scope: B-01-approved L0-L2/L1-seam candidates and direct dependencies.
  target_scope: In-place reusable-core boundary and explicit local adopter binding; exact paths chosen only from B-01 inventory.
  logical_layers: [L0, L1, L2, L3]
  capabilities: [core contract surface, configuration seam, local adoption binding]
  requirements_or_pressures: [AP-1]
  preconditions: [B-01 independently reviewed PASS, no L3/L5 candidate, immutable-history map approved]
  allowed_mutations: [move-only or reference-only core candidates, local binding, compatibility shims, tests, provenance map]
  forbidden_mutations: [semantic rewrites, L3/L5 movement, distribution mechanism, AGENTS.md/CLAUDE.md change, AP-1 implementation claim]
  bounded_inputs: [B-01 projection and review, G3 R2 §4 L0-L3/§6 boundary model, G5 R1 Option B and §7]
  validation: [pre/post semantic snapshot equivalence, no project literal/path imports from core, local adopter resolves identical rules, git provenance retained]
  independent_review_required: true
  rollback_or_recovery: Revert packet commit or restore compatibility binding; no history rewrite.
  completion_state: B-02_MINIMUM_OPTION_B_BOUNDARY_REVIEW_READY
  depends_on: [B-01]

- packet_id: B-03
  objective: Normalize the L1 configuration contract needed to keep reusable mechanisms separate from HugePlanning values.
  source_scope: B-02 seam violations and named NEEDS_NORMALIZATION L1 mechanisms.
  target_scope: Declarative, project-owned configuration inputs and core-consumed configuration schema.
  logical_layers: [L1, L3]
  capabilities: [run/program packaging shape, projection wiring, closure-loop parameterization]
  requirements_or_pressures: [AP-1, AP-6]
  preconditions: [B-02 review PASS, exhaustive literal/configuration dependency report]
  allowed_mutations: [configuration schemas, adapters, migrations with compatibility tests]
  forbidden_mutations: [L3 content extraction, L5 movement, program-state federation, instruction-surface change]
  bounded_inputs: [B-02 output, G3 R2 L1/L3 rows and §6, G2 records CAP-NAV01-004/005 CAP-NAV04-004 CAP-NAV07-001/002]
  validation: [same HugePlanning behavior under explicit configuration, no core hardcoded project values, configuration ownership test]
  independent_review_required: true
  rollback_or_recovery: Versioned configuration migration with retained old binding until equivalence PASS.
  completion_state: B-03_CONFIG_SEAM_REVIEW_READY
  depends_on: [B-02]

- packet_id: B-04
  objective: Extract only B-01-proven READY, infrastructure-pure L6 helpers into the in-place core without changing callers' semantics.
  source_scope: B-01 direct-import closure limited to READY L6 helpers and record-type schemas.
  target_scope: Reusable L6 infrastructure sublayer inside the Option B boundary.
  logical_layers: [L6]
  capabilities: [CAP-NAV13-001, selected pure helper/schema capabilities]
  requirements_or_pressures: [AP-4]
  preconditions: [B-01 review PASS, B-02 boundary PASS, per-file purity proof, unchanged caller baseline]
  allowed_mutations: [history-preserving move, import rewrites, compatibility exports, deterministic tests]
  forbidden_mutations: [project-bound validators, query/index implementation, L5 data movement, Option D execution]
  bounded_inputs: [B-01 file-level projection, B-02 boundary contract, G3 R2 L6 row, G2 §18 item 2]
  validation: [pre/post deterministic test parity, import-boundary scan, no HugePlanning literals in moved helpers, provenance check]
  independent_review_required: true
  rollback_or_recovery: Revert move/import commit while preserving source history.
  completion_state: B-04_READY_L6_SUBLAYER_REVIEW_READY
  depends_on: [B-02]

- packet_id: B-05
  objective: Design and implement a concurrency-safe, namespaced identity allocation boundary for future multi-writer use without renaming historical identities.
  source_scope: Current allocation sites and identity grammars; historical records are read-only.
  target_scope: L1/L6 identity service or protocol with compatibility mapping.
  logical_layers: [L1, L6, L5]
  capabilities: [identity allocation, namespace qualification]
  requirements_or_pressures: [AP-2]
  preconditions: [B-03 PASS, explicit Owner decision on identity compatibility and allocator authority]
  allowed_mutations: [new allocation protocol/tooling, tests, forward-only namespace mapping]
  forbidden_mutations: [historical ID rewrite, concurrent migration of all records, distribution/repository creation]
  bounded_inputs: [B-03 output, G4 R1 RD-B3/RD-C6/RD-C9, G4 base AP-2, direct allocation implementations]
  validation: [parallel allocation collision tests, namespace uniqueness, historical-reference resolution]
  independent_review_required: true
  rollback_or_recovery: Disable new allocator and retain forward-compatible mapping; historical IDs untouched.
  completion_state: B-05_IDENTITY_BOUNDARY_REVIEW_READY
  depends_on: [B-03]

- packet_id: B-06
  objective: Design and enforce Delegated Operational Authority at the L0-to-L6 execution boundary.
  source_scope: B-02 core authority semantics, B-04 tool interfaces, current bounded-discretion tools.
  target_scope: Enforceable authorization input/output contract and guarded execution path.
  logical_layers: [L0, L2, L6]
  capabilities: [delegated authority gate, bounded-discretion enforcement]
  requirements_or_pressures: [AP-3]
  preconditions: [B-02 and B-04 PASS, explicit Owner policy decisions for delegated scope and refusal behavior]
  allowed_mutations: [authority schema, gate implementation, refusal/audit tests]
  forbidden_mutations: [retrospective authority fabrication, L3/L5 extraction, claim of operational delegation before acceptance]
  bounded_inputs: [B-02/B-04 projections, G3 R2 P3/§6, G4 base AP-3, direct tool contracts]
  validation: [authorized/unauthorized boundary tests, no bypass paths, evidence emission without L5 rewrite]
  independent_review_required: true
  rollback_or_recovery: Feature-gated enforcement with documented safe disable path; evidence remains append-only.
  completion_state: B-06_DOA_ENFORCEMENT_REVIEW_READY
  depends_on: [B-02, B-04]

- packet_id: B-07
  objective: Build deterministic L5-to-L6-to-L7 query/index projections and separate program-scoped entrypoints without relocating project evidence.
  source_scope: HugePlanning L5 evidence and current L6/L7 indexes/state surfaces.
  target_scope: Project-owned deterministic index/query layer and program-scoped projections.
  logical_layers: [L5, L6, L7]
  capabilities: [deterministic query/index, bounded task projection, program/state namespacing]
  requirements_or_pressures: [AP-4, AP-6]
  preconditions: [B-03 PASS, B-05 identity protocol PASS, data ownership model approved]
  allowed_mutations: [derived indexes, query tools, program-local state projections, deterministic tests]
  forbidden_mutations: [L5 relocation or rewrite, nondeterministic retrieval, core claim of cross-project federation]
  bounded_inputs: [B-03/B-05 outputs, G3 R2 L5-L7 rows/§7, G4 base AP-4/AP-6, direct current-state/index sources]
  validation: [reproducible index build, bounded projection token measurement, source-to-index traceability, program isolation tests]
  independent_review_required: true
  rollback_or_recovery: Treat indexes as regenerable derived artifacts; retain canonical L5 evidence unchanged.
  completion_state: B-07_QUERY_AND_PROGRAM_PROJECTIONS_REVIEW_READY
  depends_on: [B-03, B-05]

- packet_id: B-08
  objective: Add a second provider/executor adapter against the proven core, then assess empirical Option B proof and instruction-surface readiness.
  source_scope: B-02 core, existing L4 adapter, and one separately selected second executor's documented interface.
  target_scope: Second L4 adapter and evidence-backed adoption/instruction change proposal.
  logical_layers: [L0, L1, L4, L7]
  capabilities: [provider-neutral binding abstraction, second adapter, adopter documentation]
  requirements_or_pressures: [AP-5]
  preconditions: [B-02/B-03 PASS, explicit Owner authorization for second provider, compatible executor contract]
  allowed_mutations: [adapter, conformance tests, bounded proposal to change active instructions]
  forbidden_mutations: [core semantic duplication, AGENTS.md/CLAUDE.md change without a separate accepted proposal, claim of external second consumer]
  bounded_inputs: [B-02/B-03 projections, G3 R2 L4/P5, G4 base AP-5, provider interface documentation, current adapter sources]
  validation: [same core semantic conformance on both adapters, no normative content inside adapters, context-budget measurement]
  independent_review_required: true
  rollback_or_recovery: Remove only the new adapter; core and existing adapter remain unchanged.
  completion_state: B-08_OPTION_B_EMPIRICAL_PROOF_REVIEW_READY
  depends_on: [B-02, B-03, B-04]
```

## 4. Instruction, proof, and decision gates

Active instruction surfaces may change only after B-02 proves the core/local
adopter boundary and a separately authorized adoption packet demonstrates
semantic equivalence. `AGENTS.md` changes must additionally wait for B-03's
configuration seam; `CLAUDE.md` remains outside this governance plan unless a
separate methodology-runtime authority is granted. B-08 may propose, never
self-apply, instruction changes after its two-adapter conformance evidence.

Option B is empirically proven only when B-02's boundary and local adoption
pass independent review, B-03 proves no HugePlanning values are embedded in
the reusable mechanism, B-04 proves an actual READY L6 move retains semantics,
and B-08 proves the same core semantics through a second adapter. This proves
the Option B boundary/adopter hypothesis, not external reuse, L0 distribution,
Option C readiness, or AP-1–AP-6 completion. Option C remains deferred until
that proof, a real second consumer, and designed resolution paths for all six
pressures; Option D remains separately authorized only.

## 5. Completion

```yaml
completion:
  status: G6_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
  extraction_packets: 8
  extraction_executed: false
  option_d_executed: false
  option_c_created: false
  ap_1_through_ap_6_implemented: false
  active_instruction_surfaces_modified: false
  independent_review_required_before_any_packet_execution: true
  context_risk_packets: []
  next_authority_required: PROJECT_OWNER_REVIEW_AND_ACCEPTANCE_OR_BOUNDED_REVISION_OF_G6_PLAN
```
