---
document_id: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R5
title: HugePlanning Governance Generalization — G6 B-01 Sharded Bounded-Projection Correction R5
program_id: GOV-GEN-AUD-001
phase: G6
base_deliverable: GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001/0.1.0
prior_controlling_corrections: [GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R2/0.1.0, GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R3/0.1.0, GOV-GEN-G6-BOUNDED-EXTRACTION-PLAN-001-R4/0.1.0]
correction_index: 5
version: 0.1.0
status: G6_R5_B01_SHARDED_EXECUTION_AUTHORIZED
authority: PROJECT_OWNER_DIRECT_G6_B01_CONTEXT_SCALING_DECISION_AND_PHASE_CONTINUATION
source_authority: Project Owner direct task “GOV-GEN G6 — Owner Decision on B-01 Context Scaling”
---

# GOV-GEN-G6-R5 — B-01 sharded bounded projections

## 1. Scope and preservation

This prospective correction replaces only the single-projection execution
model in R2 §1.3 after its deterministic token-cap refusal. The fixed seed
set, R3 selector, R4 path classification, source-root filter, direct-import
closure, accepted Option B architecture, packet DAG, L3/L5 ownership, and
B-02–B-08 contracts remain unchanged. The prior refusals and provisional
single projection remain immutable historical evidence.

## 2. Deterministic sharded construction

The constructor first produces one full canonical inventory and provenance
graph exactly as R2/R3/R4 require. It then creates indivisible semantic units
from each selected seed fragment and each source-root/import-closure member.
It labels units by their accepted artifact family and logical-layer role,
orders family and member identity bytewise, and first-fit packs them to the
18,000-token operational target. The hard limit remains 20,000.

No source is selected manually for size. A unit exceeding the operational
target is subdivided deterministically at Markdown headings, then paragraph
boundaries, then line boundaries; the manifest records that subdivision and
retains the hash of its complete source. Shard membership, token measurement,
source hash, selection rule, layer/capability-family labels, and provenance
are rendered in the resulting manifest.

Classified seed references and repository-local Python imports form the
provenance graph. Every relationship whose endpoints lie in distinct shards
is recorded in both affected shard records and the bounded reconciliation
projection. That reconciliation contains identities, hashes, memberships, and
relationships only; it does not reload source text.

## 3. Completion and continuation

B-01 succeeds only if each semantic shard and the reconciliation projection
measure `<=20,000` tokens with `tiktoken 0.12.0 / cl100k_base`; all shard
semantic-baseline results are recorded; and the final baseline manifest proves
that covered canonical units equal the accepted canonical source set with no
unexplained omissions. No extraction, L3/L5 movement, historical rewrite, or
implementation change is authorized by this correction.

On that PASS, B-01 reaches `B-01_BOUNDARY_BASELINE_REVIEW_READY`. Continue
only with dependency-ready G6 work already authorized by the controlling
packet authority; preserve every subsequent independent-review and material
Owner gate.
