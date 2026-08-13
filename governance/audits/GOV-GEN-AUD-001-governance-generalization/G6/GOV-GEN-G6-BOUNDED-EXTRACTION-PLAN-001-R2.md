---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2
title: HugePlanning Governance Generalization — G6 Bounded Extraction Plan — B-01 Execution-Contract Correction R2
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
base_deliverable_sha256: 86aba6ab024c92f4c5e0c8cc0b241a6e26db8f29c0a69687a9e489be4dd0152f
prior_controlling_correction: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1/0.1.0
prior_controlling_correction_sha256: 9aa9ea026dc87ea50e02fd57150628fc1e51e60bf8f46aaba33c448b711f7f72
independent_review: GOV-GEN-G6-INDEPENDENT-BOUNDED-PLAN-REVIEW-001/0.1.0
correction_index: 2
version: 0.1.0
status: G6_R2_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
authority: BOUNDED_CORRECTION_OF_F_001_AND_F_002_ONLY_NOT_PACKET_EXECUTION_OR_OWNER_ACCEPTANCE
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
source_authority: Project Owner direct task “GOV-GEN G6 — Bounded Correction of B-01 Execution Contract”
---

# GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2 — B-01 Execution-Contract Correction

## 0. Scope and historical integrity

This is the minimum prospective correction of the accepted controlling G6
result, `GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0` read together with
`GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1/0.1.0`. It resolves only
`F-001` and `F-002` in
`GOV-GEN-G6-INDEPENDENT-BOUNDED-PLAN-REVIEW-001/0.1.0`.

The base plan, R1, their manifests, and the independent review remain
unmodified historical evidence. This R2 is a candidate correction, not
Project Owner acceptance. It does not execute or authorize B-01 or any other
packet.

Except for the B-01 input-construction, validation, and recovery/custody
clauses replaced below, every base/R1 packet field and plan invariant remains
unchanged: all eight packet identities; the per-packet `depends_on` DAG; the
recommended default serial order; the B-02/B-03/B-04/B-08 Option B
empirical-proof gate; B-05/B-06/B-07 planned status; L3/L5 project ownership;
instruction-surface gates; mutation boundaries; and the accepted architecture
decision. This correction does not address the known unrelated immutable
PASS-03 scaffold-validator condition.

## 1. F-001 — non-circular B-01 pre-execution input construction

The base-plan B-01 `bounded_inputs` and relevant `preconditions` are replaced
by this construction contract. The B-01 inventory is an output only; it is
never an input selector.

### 1.1 Fixed seed set

Before B-01 starts, a future authorized executor must freeze one clean
repository revision and assemble the following **fixed seed source set** from
that revision. A reference to a corrected G3 result means the named physical
artifact(s), not an inferred or reconstructed history.

```yaml
seed_fragments:
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001.md: ["§4", "§6", "§7", "§8", "§10"]
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R1.md: ["all"]
  - GOV-GEN-G3-LOGICAL-ARCHITECTURE-001-R2.md: ["all"]
  - GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001.md: ["§9"]
  - GOV-GEN-G4-CONSUMER-REQUIREMENTS-DELTA-001-R1.md: ["§4", "§7", "§8"]
  - GOV-GEN-G5-PHYSICAL-ARCHITECTURE-SYNTHESIS-001-R1.md: ["§4.2", "§7", "§8"]
  - GOV-GEN-GR-INDEPENDENT-ARCHITECTURE-REVIEW-001.md: ["§3", "§4", "§5"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001.md: ["§1", "§2", "§3:B-01", "§4"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R1.md: ["all"]
  - GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2.md: ["all"]
```

The fragment selector is deterministic: Markdown `§N` is the bytes from that
ATX heading through, but excluding, the next heading of equal-or-higher level;
`§3:B-01` is the B-01 YAML mapping only; and `all` is the complete UTF-8 file.
All selected files must exist, decode as UTF-8 without replacement, and match
the frozen revision. Otherwise construction fails before B-01 begins.

### 1.2 Deterministic source-root and import-closure discovery

From the rendered seed fragments only, extract every backticked or plain-text
repository-relative pathname matching `^[A-Za-z0-9][A-Za-z0-9._/-]*\.(md|py|yaml|yml|json)$`.
Normalize with POSIX separators; reject an absolute path, `..`, a missing
path, or a path outside the frozen Git tree. Retain only paths whose G3 §4
allocation is L0, L1, L2, or L6, or that are explicitly named by the G3
§6–§8 boundary/context sections. Deduplicate and sort bytewise. This ordered
list is the B-01 source-root set.

For each source root and each discovered Python file, parse UTF-8 Python with
the standard-library `ast` parser and resolve `import` and `from ... import`
targets only to repository-local `.py` files using Python's normal package
resolution from that importing file. Recurse breadth-first, processing paths
in bytewise order, until no new repository-local Python target remains.
Non-Python source roots contribute no imports. A parse error, ambiguous local
resolution, missing local target, symlink escaping the frozen tree, or an
unsupported source-root extension is a deterministic construction failure;
the executor must not silently omit it. The resulting ordered source roots
plus closure are the source-file portion of the projection. This procedure
does not read any path named by a B-01 inventory because no B-01 inventory
exists yet.

### 1.3 Projection, provenance, measurement, and refusal

The executor renders the projection in this exact order: (1) a YAML header
recording frozen revision; (2) seed fragments in the order above; (3) source
roots plus closure in bytewise pathname order. Each member must carry its
repository-relative canonical path, selection rule, SHA-256 of the exact
source bytes, and, for closure members, its importing parent path. A
content-addressed `B-01-input-projection-manifest.yaml` records the ordered
members, their byte counts and SHA-256 values, the rendered-projection
SHA-256, and the measurement below. It is provisional packet-local evidence
until B-01 completion/review custody applies under §2.

Token measurement is over the complete rendered UTF-8 projection, including
the header and provenance fields, using `tiktoken` **0.12.0**,
`cl100k_base`, and `encoding.encode(rendered_text, disallowed_special=())`.
The manifest records the package version, encoding name, token count, and
the limit `20000`. B-01 may begin only when the count is `<= 20000`.

If any construction check fails or the measured count is greater than 20,000,
the executor must record `B-01_INPUT_PROJECTION_REFUSED` with the failing
rule, ordered candidate paths, hashes available before failure, and measured
count where applicable; discard only provisional construction output; make no
source or implementation mutation; do not start B-01; and return to the
Project Owner for a separately authorized bounded-plan correction or changed
execution authority. It must not trim, summarize, substitute, or load the
full GOV-GEN history to force compliance.

Accordingly, B-01 validation additionally requires successful verification of
the manifest's member hashes, selection/provenance chain, rendered hash,
tokenizer/version, and `<=20000` count before any B-01 semantic work begins.

## 2. F-002 — B-01 recovery and immutable custody

The base-plan B-01 `rollback_or_recovery` is replaced with the following:

> During a failed, refused, or rolled-back B-01 execution, only provisional,
> unaccepted packet-local construction and draft outputs may be discarded.
> Source-tree bytes remain unchanged. Once a B-01 semantic baseline, its
> input-projection manifest, source/provenance map, and required independent
> review record have been completed and accepted, they are immutable
> historical custody and may not be deleted or rewritten. A later correction
> or replacement requires explicit authorization and a new prospective,
> versioned/superseding artifact that preserves the earlier baseline, its
> manifest, review record, and provenance.

This lifecycle makes the B-02 prerequisite retrievable: only an accepted,
custodied B-01 baseline and its approved immutable-history map can support
B-02. A provisional B-01 draft is not a baseline, cannot satisfy B-02, and
may be discarded without altering historical custody.

## 3. Correction disposition

```yaml
completion:
  status: G6_R2_EXTRACTION_PLAN_READY_FOR_PROJECT_OWNER_REVIEW
  findings_resolved: [F-001, F-002]
  f_001_resolution: non_circular_fixed_seed_deterministic_closure_content_addressed_manifest_pinned_token_measurement_pre_execution_cap_and_refusal
  f_002_resolution: provisional_outputs_discardable_accepted_baseline_manifest_provenance_and_review_immutable_prospective_supersession_only
  base_deliverable_modified: false
  r1_modified: false
  independent_review_modified: false
  packets_added_removed_merged_split_or_reordered: false
  b_02_through_b_08_materially_changed: false
  authoritative_hard_dependency_graph: per_packet_depends_on_fields_in_base_plan
  displayed_sequence_semantics: recommended_default_serial_execution_order
  option_b_empirical_proof_packets: [B-02, B-03, B-04, B-08]
  b_05_b_06_b_07_status: planned_unchanged
  b_01_status: NOT_STARTED_NOT_AUTHORIZED
  packet_execution_authorized_or_performed: false
  extraction_executed: false
  active_instruction_surfaces_modified: false
  project_owner_acceptance: PENDING
  next_authority_required: PROJECT_OWNER_REVIEW_AND_ACCEPTANCE_OR_BOUNDED_REVISION_OF_G6_PLAN
```
