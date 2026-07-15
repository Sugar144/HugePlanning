---
run: KGR-006
role: Enforcement Engineer
mode: MINIMUM_ENFORCEMENT_ANALYSIS
protocol: GOV-PROTOCOL-004/0.1.0
status: ANALYSIS_COMPLETE_PENDING_INDEPENDENT_EVALUATION
source_of_truth: 01-clause-implication-matrix.yaml
requirement_count: 20
---

# Existing Capability Inventory

## Inventory method

Only package-bound files were treated as evidence. A tool, schema, skill, or record supports only the behavior its bytes and validation record demonstrate; naming, intended purpose, or planned use is not capability proof. The inventory classifies each of ER-001 through ER-020 using the matrix enum and does not inspect live provider, product, runtime, branch-protection, credential, data-flow, or external-system behavior.

## Supported capabilities

No derived enforcement requirement is classified `SUPPORTED_BY_EVIDENCE`. The package does contain useful primitives—strict YAML parsing, schemas, hashing, ZIP safety, byte-identity checks, prompt custody, review packaging, learning records, and scoped Controller/closure validation—but each maps only partially to the broader enforcement requirement it informs.

## Partial capabilities

Seven requirements are `PARTIAL`:

| Requirement | Bound evidence | Supported portion | Missing portion |
|---|---|---|---|
| ER-001 | Operating contract, prompt authority fields | Explicit scope, authority vocabulary, custody | Competence/delegation/expiry/revocation registry and comprehension evidence |
| ER-003 | Structured prompts, state and handoff patterns | Attributable scope, evidence and limitation patterns | Tested high-consequence decision-packet usability |
| ER-008 | Independent-evaluation handoff | Separation and evaluator-authority boundary | Appointed evaluator and executed independent evidence |
| ER-009 | Validation records and schemas | Scoped claim/result records | General objective-to-gate-to-acceptance lineage |
| ER-010 | Registry, hashes, immutable snapshots | Custody, provenance, supersession discipline | Complete semantic-fidelity evaluation |
| ER-013 | Strict parsers and package validators | Structural and selected cross-file parity | Universal material semantic parity |
| ER-016 | Closure-loop schema and transition tool | Narrow managed governance-state behavior | General pilot/workflow state ownership and lifecycle |

These capabilities may be reused as evidence or design constraints later; this analysis does not extend or operate them.

## Gaps and dependencies

Nine requirements are `GAP`: ER-002, ER-004, ER-005, ER-006, ER-011, ER-014, ER-017, ER-018, and ER-020. They cover architecture-effect classification, governed-effect taxonomy/authorization, cumulative deviations, cross-workstream aggregation, assumption dependencies, qualified acceptance, operational burden evidence, emergency containment, and scoped clause/effect capability evidence.

Three requirements are `DEPENDENT_ON_SPECIALIST`: ER-012 (legal/privacy evidence lifecycle), ER-015 (high-consequence decision usability), and ER-019 (operational recovery/continuity). ER-007 is `DEPENDENT_ON_PROVIDER_TEST`. Each dependency carries an explicit unsupported boundary; none is treated as existing capability.

No requirement is classified `NOT_FEASIBLE` or `NOT_APPLICABLE`. Particular universal claims remain impossible—especially full reversal of irreversible external effects—but the associated requirements are feasible as scoped evidence, limitation, compensation, or blocking requirements.

## Capability count parity

| Classification | Count |
|---|---:|
| `SUPPORTED_BY_EVIDENCE` | 0 |
| `PARTIAL` | 7 |
| `GAP` | 9 |
| `DEPENDENT_ON_SPECIALIST` | 3 |
| `DEPENDENT_ON_PROVIDER_TEST` | 1 |
| `NOT_FEASIBLE` | 0 |
| `NOT_APPLICABLE` | 0 |
| Total | 20 |

These counts match `01-clause-implication-matrix.yaml`.

