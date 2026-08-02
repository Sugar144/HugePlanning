---
document_id: GOV-GEN-G1B-CAPABILITY-MAP-001
title: HugePlanning Governance Generalization — G1B Governance Capability Map
program_id: GOV-GEN-AUD-001
phase: G1B
contract: GOV-GEN-G1B-CONTRACT-001/0.1.0
version: 0.1.0
status: G1B_READY_FOR_OWNER_REVIEW
authority: FACTUAL_CAPABILITY_MAPPING_ONLY_NO_ARCHITECTURE_OR_EXTRACTION_AUTHORITY
executor_acceptance: NOT_SELF_ACCEPTING_OWNER_ACCEPTANCE_IS_SEPARATE
---

# GOV-GEN-G1B — Governance Capability Map

## 0. Scope statement

This document is the single principal G1B deliverable required by
`GOV-GEN-G1B-CONTRACT-001/0.1.0` §8. It enumerates governance capabilities
and capability gaps realized (or absent) across the accepted 679-row G1A
index of `HugePlanning-governance` at `1899a3e7b41e9b4930a5d0f7f0b7e9d542fcb8dc`,
checked against every domain in the contract's §5 checklist, with every
record conforming to the §6 schema. It contains **zero** `generality`,
`target_layer`, `operating_burden`, `extraction_burden`, `candidate_disposition`,
`recommendation`, `description`, or `summary` fields (contract §6.4, §9.6).
It does not select, recommend, or compare a target architecture, decide
kernel ownership, or modify any artifact outside this contract's own
custody path.

## 1. Execution verification (contract §2.2, §9.1)

| Check | Expected | Observed | Result |
|---|---|---|---|
| Repository root | `/home/sugar/Documents/HugePlanning-governance` | `/home/sugar/Documents/HugePlanning-governance` | MATCH |
| Branch | `governance/kernel-designer-revision-v0.1` | `governance/kernel-designer-revision-v0.1` | MATCH |
| Worktree status (pre-execution) | clean | clean (`git status --short` empty) | MATCH |
| HEAD | descendant of accepted G1A baseline `1899a3e7b41e9b4930a5d0f7f0b7e9d542fcb8dc` | `4bf4c2d2baa4c9fb7eb83a187c97b668f938d581` — one commit ahead of `1899a3e7`, recording `docs(governance): accept GOV-GEN G1A and authorize G1B for execution` (`GOV-GEN-DECISION-001`, `GOV-GEN-DECISION-002`) | MATCH — no drift; the intervening commit is the G1A-acceptance/G1B-authorization record itself, not a G1A-index-affecting change |
| G1A index row count | 679 across 14 `path_family` values | 679 (independently recomputed from `G1A-artifact-authority-index.jsonl`, `~/Downloads/GOV-GEN-G1A-001/`) | MATCH |
| NAV-step row-count parity (contract §7) | `12+3+62+20+37+37+202+112+14+9+53+76+42 = 679` | recomputed identically: `ROOT`11+`archive`1=12, `kernel`3, `learning`62, `methodology`20, `prompts`37, `reviews`37, `runs`202, `audits`112, `schemas`13+`validation`1=14, `skills`9, `sources`53, `tests`76, `tools`42 | MATCH |

No baseline drift was triggered. Execution proceeds under contract §4.2.

## 2. Evidence base and method

Primary evidence is the JSONL **row bodies** of the accepted G1A index
(`relative_path`, `path_family`/`path_subfamily`, `declaration.fields`,
`git`, `content`), read progressively one NAV step at a time, plus
structural counts (subfamily/extension/declared-field aggregation) computed
by script. Per contract §3.1/§7, later-step row bodies were not opened
before the current step's records were written. The canonical planning
inputs at contract §2.1 (`GOV-GEN-DECISION-001`, `G1A-report.md`, the named
sections of the Compact Conceptual Baseline, `governance/AGENTS.md`) were
read in full before NAV-01. No file outside the G1A index rows and the
named §2.1 planning inputs was opened; this map does not re-derive meaning
from raw repository file content beyond what the index rows and their
`relative_path`/`declaration.fields` disclose.

## 3. Cross-cutting capability-domain coverage (contract §5)

| # | Domain | Status | Realizing capability / gap |
|---|---|---|---|
| 1 | `OWNER_RESERVED_AUTHORITY` | RESOLVED | CAP-NAV01-001, CAP-NAV01-002, CAP-NAV01-011, CAP-NAV05-002, CAP-NAV06-003, CAP-NAV08-004, CAP-NAV08-007; GAP-006 |
| 2 | `DELEGATED_OPERATIONAL_AUTHORITY` | RESOLVED | CAP-NAV04-001..007, CAP-NAV10-001..005 |
| 3 | `BOUNDED_TECHNICAL_DISCRETION` | RESOLVED | CAP-NAV13-001..011, CAP-NAV12-001..004 |
| 4 | `PROVIDER_NEUTRAL_SEMANTICS` | RESOLVED | CAP-NAV02-001, CAP-NAV09-001..008; GAP-001 |
| 5 | `EXECUTOR_EQUIVALENCE` | RESOLVED | CAP-NAV10-002..005, CAP-NAV11-004; GAP-004 |
| 6 | `PROJECTION_SURFACE_GOVERNANCE` | RESOLVED | CAP-NAV01-004, CAP-NAV02-001 |
| 7 | `PROJECTION_DRIFT_CONTROL` | RESOLVED | CAP-NAV07-002, CAP-NAV06-006; GAP-001, GAP-002 |
| 8 | `CLEAN_SESSION_EXECUTION` | RESOLVED | CAP-NAV07-001, CAP-NAV05-002, CAP-NAV08-005, CAP-NAV08-011, CAP-NAV08-012 |
| 9 | `TASK_CONTEXT_DECOMPOSITION` | RESOLVED | CAP-NAV04-004, CAP-NAV07-001, CAP-NAV08-008; GAP-005, GAP-006 |
| 10 | `EVIDENCE_NAVIGATION` | RESOLVED | CAP-NAV11-001..005, CAP-NAV03-001..005; GAP-005 |
| 11 | `VALIDATION_PUBLICATION_STOP_BOUNDARY` | RESOLVED | CAP-NAV12-001..004, CAP-NAV09-006..008, CAP-NAV06-004..005; GAP-003 |
| 12 | `GOVERNANCE_LEVEL_OR_PROFILE` | RESOLVED | CAP-NAV01-001, CAP-NAV01-005, CAP-NAV01-010, CAP-NAV04-001, CAP-NAV08-001 |

All 12 domains resolve to at least one realizing capability or explicit
gap. No domain is `UNASSIGNED`.

## 4. Family-to-NAV-step representation (contract §9.2)

| `path_family` | rows | NAV step |
|---|---|---|
| ROOT | 11 | NAV-01 |
| archive | 1 | NAV-01 |
| kernel | 3 | NAV-02 |
| learning | 62 | NAV-03 |
| methodology | 20 | NAV-04 |
| prompts | 37 | NAV-05 |
| reviews | 37 | NAV-06 |
| runs | 202 | NAV-07 |
| audits | 112 | NAV-08 |
| schemas | 13 | NAV-09 |
| validation | 1 | NAV-09 |
| skills | 9 | NAV-10 |
| sources | 53 | NAV-11 |
| tests | 76 | NAV-12 |
| tools | 42 | NAV-13 |

All 14 accepted `path_family` entries are represented; none silently
dropped.

---

## NAV-01 — ROOT + archive (12 rows)

```yaml
- capability_id: CAP-NAV01-001
  obligation: Maintain a single durable, evidence-following governance state ledger
  realized_by: [{relative_path: governance/CURRENT_STATE.md, role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY, GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: GOVERNANCE_SOURCE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "CURRENT_STATE.md durable-state YAML blocks cited by GOV-GEN CURRENT_STATE.md itself"}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: "AGENTS.md repository instruction: \"CURRENT_STATE.md must follow evidence and never fabricate or lead it\""}

- capability_id: CAP-NAV01-002
  obligation: Preserve an append-only record of Owner and governance decisions
  realized_by: [{relative_path: governance/DECISION_LOG.md, role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-003
  obligation: Maintain a canonical, countable artifact registry/inventory
  realized_by: [{relative_path: governance/ARTIFACT_REGISTRY.yaml, role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "G1A baseline check governance_regular_files/artifact_registry_top_level_entries = 221 (G1A-report.md §9)"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-004
  obligation: Declare which runtime/projection surfaces the governance state feeds
  realized_by: [{relative_path: governance/RUNTIME_PROJECTION_MAP.yaml, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty for this row (no ALLOWED_KEYS root key matched); document's own declared status not captured by G1A parser — content not reopened at G1B, per contract row-body-only bound"]
  capability_domain: [PROJECTION_SURFACE_GOVERNANCE]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: PROJECTION_SURFACE
  drift_control_observed: UNRESOLVED
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-005
  obligation: Record the phase/plan roadmap for the governance program
  realized_by: [{relative_path: governance/GOVERNANCE_MASTER_PLAN.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty (NO_SUPPORTED_DECLARATION); no root-level allowed key present"]
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "GOVERNANCE_MASTER_PLAN.md filename itself, root-level program document"}

- capability_id: CAP-NAV01-006
  obligation: Report import provenance for externally sourced material
  realized_by: [{relative_path: governance/IMPORT_REPORT.md, role: OPERATING_EVIDENCE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/IMPORT_REPORT.md relative_path itself"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-007
  obligation: Register open questions arising from import for Owner disposition
  realized_by: [{relative_path: governance/OPEN_IMPORT_QUESTIONS.md, role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [OWNER_RESERVED_AUTHORITY, EVIDENCE_NAVIGATION]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-008
  obligation: Maintain an integrity ledger of immutable-source checksums
  realized_by: [{relative_path: governance/SOURCE_CHECKSUMS.sha256, role: OPERATING_EVIDENCE}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "AGENTS.md: \"Treat sources/raw/ as immutable; verify it against SOURCE_CHECKSUMS.sha256\""}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-009
  obligation: Plan runtime adoption of governance into the S0A/S1 execution surface
  realized_by: [{relative_path: governance/S0A_S1_ADOPTION_PLAN.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [PROJECTION_SURFACE_GOVERNANCE]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: PROJECTION_SURFACE
  drift_control_observed: UNRESOLVED
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "CURRENT_STATE.md: \"Runtime/S1 context | S1 continues independently; governance has not been projected into runtime\""}

- capability_id: CAP-NAV01-010
  obligation: Provide a repository orientation entrypoint
  realized_by: [{relative_path: governance/README.md, role: DOCUMENTATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV01-011
  obligation: Provide repository-wide operating instructions binding every agent session
  realized_by: [{relative_path: governance/AGENTS.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["cross-references methodology/project-operating-contract.md (CAP-NAV04-001) as \"canonical operating semantics\" per governance/AGENTS.md line 18 — two-tier instruction/contract split observed, not reconciled into one file"]
  capability_domain: [OWNER_RESERVED_AUTHORITY, GOVERNANCE_LEVEL_OR_PROFILE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "governance/AGENTS.md: \"These instructions apply only to work launched from governance/ or its descendants.\""}

- capability_id: CAP-NAV01-012
  obligation: Preserve historical/archived instruction material outside active custody
  realized_by: [{relative_path: governance/archive/README.md, role: HISTORICAL_EVIDENCE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OBSOLETE
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: 12 rows = 12 capability realizations (1:1); 0 residual.

---

## NAV-02 — kernel (3 rows)

```yaml
- capability_id: CAP-NAV02-001
  obligation: Specify the proposed governance kernel clause set pending ratification
  realized_by:
    - {relative_path: governance/kernel/proposed/0.1.0/02-kernel-v0.1-draft.md, role: SPECIFICATION}
    - {relative_path: governance/kernel/proposed/0.1.0/03-kernel-clauses.yaml, role: SPECIFICATION}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: PROPOSED
  unresolved_items:
    - "declared fields for 02-kernel-v0.1-draft.md: artifact_id=KD-02, authority=pending_human_ratification, status=PROPOSED, version=0.1.0-proposed — this is the 0.1.0 draft; CURRENT_STATE.md records the ratified kernel as version 0.2.0, whose text is not present anywhere under this path_family (see GAP-001)"
  capability_domain: [PROVIDER_NEUTRAL_SEMANTICS, PROJECTION_SURFACE_GOVERNANCE]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: GOVERNANCE_SOURCE
  drift_control_observed: MECHANISM_PLANNED_NOT_IMPLEMENTED
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared status=PROPOSED, authority=pending_human_ratification (verbatim, governance/kernel/proposed/0.1.0/02-kernel-v0.1-draft.md)"}

- capability_id: CAP-NAV02-002
  obligation: Provide kernel-directory orientation
  realized_by: [{relative_path: governance/kernel/README.md, role: DOCUMENTATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: 3 rows = 3 capability realizations (1:1); 0 residual.

---

## NAV-03 — learning (62 rows)

```yaml
- capability_id: CAP-NAV03-001
  obligation: Maintain a durable index of failures and lessons
  realized_by: [{relative_path: governance/learning/FAILURE_AND_LESSONS_INDEX.md, role: STATE_OR_INDEX}]
  requires: [CAP-NAV03-002, CAP-NAV03-003]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty; G1A-report.md §10.1 item 7 notes: \"a machine-generated Markdown index has no front matter\""]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/learning/FAILURE_AND_LESSONS_INDEX.md relative_path itself"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV03-002
  obligation: Record each material failure as a schema-conformant, append-only artifact
  realized_by: [{relative_path: "governance/learning/records/HP-FAIL-001.yaml .. HP-FAIL-026.yaml (26 files)", role: HISTORICAL_EVIDENCE}]
  requires: [CAP-NAV09-002]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty for all 26 rows; front-matter/root-key extraction not exercised against these YAML records at G1A time (no ALLOWED_KEYS match at their root)"]
  capability_domain: [EVIDENCE_NAVIGATION, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/learning/records/ 26 sequential HP-FAIL-NNN.yaml files, one per failure ID"}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV03-003
  obligation: Preserve narrative learning-event history per failure, including corrections
  realized_by: [{relative_path: "governance/learning/events/HP-FAIL-* (33 files across 22 failure IDs; some IDs have 2-4 event files: HP-FAIL-006(2), HP-FAIL-014(2), HP-FAIL-015(2), HP-FAIL-016(2), HP-FAIL-017(4), HP-FAIL-020(3), HP-FAIL-021(2))", role: HISTORICAL_EVIDENCE}]
  requires: [CAP-NAV09-002]
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["multiple event files per failure ID observed as a structural fact (event count 33 > record count 26); AGENTS.md instructs \"Correct prospectively through a new version or event\" — consistent with, not necessarily proof of, an append-only correction pattern for those 7 multi-event IDs"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/learning/events/README.md present alongside the 33 event files"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV03-004
  obligation: Synthesize recorded lessons by category for reuse
  realized_by: [{relative_path: governance/learning/summaries/lessons-by-category.md, role: DOCUMENTATION}]
  requires: [CAP-NAV03-002]
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV03-005
  obligation: Define the triage rule routing material failures/corrections into learning custody
  realized_by: [{relative_path: governance/learning/README.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty; rule itself is also stated in governance/AGENTS.md line 21 (\"Triage material governance failures and owner corrections under learning/README.md\") — cross-referenced, not duplicated content"]
  capability_domain: [OWNER_RESERVED_AUTHORITY, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: 1 (index) + 26 (records) + 33 (events, incl. its README) + 1
(summaries) + 1 (learning/README.md) = 62; 0 residual.

---

## NAV-04 — methodology (20 rows)

```yaml
- capability_id: CAP-NAV04-001
  obligation: State the canonical operating semantics binding every governance session
  realized_by: [{relative_path: governance/methodology/project-operating-contract.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["declared: document_id=GOV-METHOD-OPERATING-CONTRACT-001, status=IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW, version=0.3.0; referenced by governance/AGENTS.md as \"the canonical operating semantics\" (CAP-NAV01-011)"]
  capability_domain: [DELEGATED_OPERATIONAL_AUTHORITY, EXECUTOR_EQUIVALENCE, GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "status=IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW (verbatim declared field)"}

- capability_id: CAP-NAV04-002
  obligation: Maintain a non-authoritative register of proposed methodology changes
  realized_by: [{relative_path: governance/methodology/METHODOLOGY_BACKLOG.md, role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: PROPOSED
  unresolved_items: []
  capability_domain: [DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared: document_id=GOV-METHODOLOGY-BACKLOG-001, authority=NONE, status=ACTIVE_NON_AUTHORITATIVE_PROPOSAL_REGISTER, version=0.3.0"}

- capability_id: CAP-NAV04-003
  obligation: Provide methodology-directory and loops-directory orientation
  realized_by:
    - {relative_path: governance/methodology/README.md, role: DOCUMENTATION}
    - {relative_path: governance/methodology/loops/README.md, role: DOCUMENTATION}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty for both rows"]
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV04-004
  obligation: Specify the kernel-design-closure loop mechanism
  realized_by:
    - {relative_path: governance/methodology/loops/kernel-design-closure/README.md, role: DOCUMENTATION}
    - {relative_path: governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml, role: SPECIFICATION}
  requires: [CAP-NAV09-004, CAP-NAV13-002, CAP-NAV13-007]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["declaration.fields empty for both rows"]
  capability_domain: [TASK_CONTEXT_DECOMPOSITION, CLEAN_SESSION_EXECUTION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: L1
  decomposition_mechanism_observed: {present: true, citation: "governance/methodology/loops/kernel-design-closure/kernel-design-closure-loop-v0.1.0.yaml (loop mechanism, name implies bounded-loop decomposition)"}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [STOP]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV04-005
  obligation: Define the Enforcement Engineer role protocol
  realized_by:
    - {relative_path: governance/methodology/roles/enforcement-engineer/README.md, role: DOCUMENTATION}
    - {relative_path: governance/methodology/roles/enforcement-engineer/enforcement-engineer-modes.yaml, role: SPECIFICATION}
    - {relative_path: governance/methodology/roles/enforcement-engineer/protocols/README.md, role: DOCUMENTATION}
    - {relative_path: "governance/methodology/roles/enforcement-engineer/protocols/minimum-analysis/06-enforcement-engineer-minimum-analysis-prompt-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/methodology/roles/enforcement-engineer/protocols/minimum-analysis/07-enforcement-engineer-minimum-analysis-correction-prompt-v0.2.0.md", role: TEMPLATE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["06-...-v0.1.0.md declares phase=GOV-5, prompt_id=GOV-PROMPT-008, status=APPROVED_NOT_EXECUTED, version=0.1.0; the v0.2.0 correction file's declaration.fields is empty (no root-level allowed key matched)"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: L1
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "phase=GOV-5 (verbatim declared field)"}

- capability_id: CAP-NAV04-006
  obligation: Define the Kernel Adversary role protocol
  realized_by:
    - {relative_path: governance/methodology/roles/kernel-adversary/README.md, role: DOCUMENTATION}
    - {relative_path: governance/methodology/roles/kernel-adversary/adversary-modes.yaml, role: SPECIFICATION}
    - {relative_path: governance/methodology/roles/kernel-adversary/protocols/README.md, role: DOCUMENTATION}
    - {relative_path: "governance/methodology/roles/kernel-adversary/protocols/targeted-closure/05-kernel-adversary-targeted-closure-prompt-sol-high-v0.1.0.md", role: TEMPLATE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty across all 4 rows"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV04-007
  obligation: Define the Kernel Designer role protocol
  realized_by:
    - {relative_path: governance/methodology/roles/kernel-designer/README.md, role: DOCUMENTATION}
    - {relative_path: governance/methodology/roles/kernel-designer/designer-modes.yaml, role: SPECIFICATION}
    - {relative_path: governance/methodology/roles/kernel-designer/protocols/README.md, role: DOCUMENTATION}
    - {relative_path: "governance/methodology/roles/kernel-designer/protocols/adversarial-revision/04-kernel-designer-adversarial-revision-prompt-sol-high-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/methodology/roles/kernel-designer/protocols/closure-remediation/06-kernel-designer-closure-remediation-prompt-sol-high-v0.1.0.md", role: TEMPLATE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty across all 5 rows"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: IMPLICIT_TOOL_AGNOSTIC
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: 1+1+2+2+5+4+5 = 20; 0 residual.

---

## NAV-05 — prompts (37 rows)

```yaml
- capability_id: CAP-NAV05-001
  obligation: Define the prompt-custody and orchestration convention
  realized_by: [{relative_path: governance/prompts/README.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: IMPLEMENTED
  unresolved_items:
    - "declared: document_id=GOV-PROMPT-CUSTODY-001, authority=prompt_custody_and_orchestration_evidence_only, status=IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW, version=0.1.1"
    - "see GAP-005: this convention indexes only governance/prompts/; audit-program prompts (CAP-NAV08-010/011) and per-run embedded prompt copies (CAP-NAV07-001) are not cross-referenced by this file's declared scope"
  capability_domain: [CLEAN_SESSION_EXECUTION, EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/prompts/README.md (GOV-PROMPT-CUSTODY-001)"}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV05-002
  obligation: Preserve one immutable, versioned prompt artifact per material orchestration act
  realized_by: [{relative_path: "governance/prompts/orchestration/HP-PROMPT-001..039.md (35 files)", role: HISTORICAL_EVIDENCE}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items:
    - "34 of 35 rows declare status=EXECUTED with an explicit prompt_id and version; HP-PROMPT-030 exists in three declared versions (0.1.0, 0.2.0 [supersedes 0.1.0], 0.3.0) — the 0.3.0 row's declaration.fields is empty (no root-level allowed key matched), an extraction gap distinct from a content gap"
    - "a subset (HP-PROMPT-035, 036, 038, 039) additionally declares an explicit `authority` value (e.g. PROJECT_OWNER_EXPLICIT, PROJECT_OWNER_EXPLICIT_BOUNDED_REVIEW_PACKAGE_CORRECTION_AND_PUBLICATION) not present on the other 31 — an observed, not reconciled, authority-annotation inconsistency across the register"
  capability_domain: [CLEAN_SESSION_EXECUTION, TASK_CONTEXT_DECOMPOSITION, OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "sequential prompt_id numbering HP-PROMPT-001 through HP-PROMPT-039"}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV05-003
  obligation: Prepare an adversarial-review prompt contract pending separate execution authorization
  realized_by: [{relative_path: "governance/prompts/reviews/HP-PROMPT-037-gov-aud-001-pass-03-adversarial-review-v0.1.0.md", role: TEMPLATE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [STOP]}
  governance_level_or_profile_evidence: {value: "declared: authority=PREPARED_REVIEW_CONTRACT_ONLY_REQUIRES_SEPARATE_PROJECT_OWNER_EXECUTION_AUTHORIZATION, review_id=GOV-AUD-001-P03-AR-001, status=APPROVED_NOT_EXECUTED"}
```

Row accounting: 1 (README) + 35 (orchestration) + 1 (reviews) = 37; 0 residual.

---

## NAV-06 — reviews (37 rows)

```yaml
- capability_id: CAP-NAV06-001
  obligation: Bundle a review's evidence under one reproducible profile
  realized_by: [{relative_path: "review-bundle-profile-v*.yaml, recurring in gov-5-contract-preparation, kgr-006-r1-contract-preparation, kgr-006-r1-controlled-import-and-owner-review (v0.1.0 and v0.2.0), phase-2-2-durable-review-packaging, phase-2-3-formal-run-preparation, phase-2-4-formal-result-import", role: TEMPLATE}]
  requires: [CAP-NAV09-005, CAP-NAV13-003]
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty across all instances (plain YAML, no root-level allowed key)"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY, CLEAN_SESSION_EXECUTION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV06-002
  obligation: Report implementation status per governance phase/run for Owner review
  realized_by: [{relative_path: "implementation-report-v0.1.0.md, one per reviews/* subfamily (gov-5-contract-preparation, gov-5-provenance-reconciliation, kgr-006-r1-contract-preparation, kgr-006-r1-controlled-import-and-owner-review [x2], kgr-006-r1-owner-decisions-state-reconciliation, phase-1-instructions-learning, phase-2-0-1, phase-2-1, phase-2-2, phase-2-3, phase-2-4)", role: OPERATING_EVIDENCE}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: UNRESOLVED
  unresolved_items:
    - "declared status values span the full observed lifecycle honesty vocabulary verbatim: PREPARED_VALIDATED_NOT_EXECUTED, IMPORTED_RECONCILED_RETURNED_FOR_VERSIONED_CORRECTION, IMPLEMENTED_AND_VALIDATED_READY_FOR_PROJECT_OWNER_DECISION, IMPLEMENTED_AND_VALIDATED_PENDING_PROJECT_OWNER_REVIEW, IMPLEMENTED_AND_VALIDATED_PENDING_PROJECT_OWNER_ACCEPTANCE, PROPOSED_FOR_PROJECT_OWNER_ARCHITECTURE_REVIEW, IMPLEMENTED_LOCALLY_PENDING_PROJECT_OWNER_REVIEW, IMPLEMENTED_LOCALLY_PENDING_REVIEW, IMPLEMENTED_APPLIED_VALIDATED_PENDING_COMMIT"
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION, PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV06-003
  obligation: Preserve a Project Owner decision dossier/record for a bounded review scope
  realized_by:
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/project-owner-decision-dossier-v0.1.0.md", role: STATE_OR_INDEX}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/project-owner-decision-record-v0.1.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/project-owner-decision-record-v0.2.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/reviews/gov-6-ratification/kernel-ratification-decision-record-v0.1.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/reviews/gov-7-direction/od-005-gov-7-direction-decision-record-v0.1.0.yaml", role: STATE_OR_INDEX}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declared: dossier document_id=GOV-REVIEW-011, status=PREPARED_FOR_PROJECT_OWNER_REVIEW; decision-record .yaml rows declaration.fields empty"]
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV06-004
  obligation: Validate cross-surface state consistency after an Owner decision
  realized_by: [{relative_path: "governance/reviews/kgr-006-r1-owner-decisions-state-reconciliation/cross-surface-state-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}]
  requires: [CAP-NAV13-008]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV06-005
  obligation: Validate a corrected/imported package against its declared readiness/import criteria
  realized_by:
    - {relative_path: "governance/reviews/gov-5-contract-preparation/kgr-006-readiness-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/gov-5-provenance-reconciliation/kgr-006-import-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-contract-preparation/kgr-006-r1-execution-authorization-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-contract-preparation/kgr-006-r1-readiness-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/kgr-006-r1-import-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/gov-5-phase-closure-readiness-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/gov-5-phase-closure-readiness-v0.2.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/kgr-006-r1-controlled-import-and-owner-review/gov-5-phase-closure-readiness-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/phase-2-3-formal-run-preparation/kgr-005-readiness-v0.1.0.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/reviews/phase-2-4-formal-result-import/kgr-005-import-validation-v0.1.0.yaml", role: OPERATING_EVIDENCE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty across all 10 rows"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV06-006
  obligation: Report a proposed architecture for Owner review
  realized_by: [{relative_path: "governance/reviews/phase-1-instructions-learning/architecture-report-v0.1.0.md", role: DOCUMENTATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: PROPOSED
  unresolved_items: []
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE, PROJECTION_DRIFT_CONTROL]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PLANNED_NOT_IMPLEMENTED
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared: document_id=HP-ARCH-GOV-TOOLING-001, status=PROPOSED_FOR_PROJECT_OWNER_ARCHITECTURE_REVIEW"}
```

Row accounting: 7 (CAP-001) + 12 (CAP-002) + 5 (CAP-003) + 1 (CAP-004) + 10
(CAP-005) + 1 (CAP-006) = 36; the remaining 1 row
(`kgr-006-r1-owner-decisions-state-reconciliation/review-bundle-profile-v0.1.0.yaml`)
is an additional CAP-NAV06-001 realization not separately enumerated above
by name; total 37. No residual.

---

## NAV-07 — runs (202 rows, sub-stepped by KGR run per contract §7)

```yaml
- capability_id: CAP-NAV07-001
  obligation: Package one formal governance run as README + prompt + inputs + outputs + manifest
  realized_by:
    - {relative_path: "governance/runs/KGR-001-intake/{README.md, prompt/, inputs/, outputs/(8), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-002-kernel-designer/{README.md, prompt/, inputs/(8), outputs/(7), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-003-kernel-adversary/{README.md, prompt/, inputs/(7), outputs/(7), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-004-kernel-designer-revision/{README.md, prompt/, inputs/(14), outputs/(8), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-005-kernel-adversary-targeted-closure/{README.md, prompt/, inputs/(17), outputs/(9), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-006-enforcement-analysis/{README.md, prompt/, inputs/(42), outputs/(8), run-manifest.yaml}", role: TEMPLATE}
    - {relative_path: "governance/runs/KGR-006-R1-enforcement-analysis-correction/{README.md, prompt/, inputs/(13), outputs/(8), run-manifest.yaml}", role: TEMPLATE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["identical top-level pattern (README/prompt/inputs/outputs/run-manifest.yaml) recurs across all 7 runs; this same pattern also recurs in audits/*/runs/* (CAP-NAV08-012), an explicit cross_cutting realization link"]
  capability_domain: [CLEAN_SESSION_EXECUTION, TASK_CONTEXT_DECOMPOSITION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: L1
  decomposition_mechanism_observed: {present: true, citation: "one directory per formal run (KGR-NNN), each independently bounded"}
  evidence_navigation_mechanism_observed: {present: true, citation: "run-manifest.yaml present in every one of the 7 runs"}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV07-002
  obligation: Progressively harden the formal-run input/output contract envelope
  realized_by:
    - {relative_path: "governance/runs/KGR-004-kernel-designer-revision/input-envelope.yaml", role: SPECIFICATION}
    - {relative_path: "governance/runs/KGR-005-kernel-adversary-targeted-closure/input-envelope.yaml", role: SPECIFICATION}
    - {relative_path: "governance/runs/KGR-006-enforcement-analysis/{input-envelope.yaml, input-inventory.yaml, output-contract.yaml}", role: SPECIFICATION}
    - {relative_path: "governance/runs/KGR-006-R1-enforcement-analysis-correction/{input-envelope.yaml, input-inventory.yaml, output-contract.yaml}", role: SPECIFICATION}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["envelope/inventory/output-contract files absent from KGR-001..003 (earliest 3 runs); present from KGR-004 onward and further extended (input-inventory.yaml, output-contract.yaml) from KGR-006 onward — an observed progressive-hardening structural fact, not a maturity judgment"]
  capability_domain: [PROJECTION_DRIFT_CONTROL]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV07-003
  obligation: Record a deterministic Controller state transition for a run
  realized_by: [{relative_path: "governance/runs/KGR-005-kernel-adversary-targeted-closure/{control/, controller/(3)}", role: STATE_OR_INDEX}]
  requires: [CAP-NAV09-001, CAP-NAV13-002]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [CLEAN_SESSION_EXECUTION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV07-004
  obligation: Custody an independent-evaluation package inside its originating run
  realized_by:
    - {relative_path: "governance/runs/KGR-006-enforcement-analysis/{evaluation/(3), independent-evaluation-handoff.md}", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/runs/KGR-006-R1-enforcement-analysis-correction/evaluation/(3)", role: OPERATING_EVIDENCE}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV07-005
  obligation: Record the execution authorization consumed by a specific run
  realized_by: [{relative_path: "governance/runs/KGR-006-R1-enforcement-analysis-correction/authorization/", role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV07-006
  obligation: Record provenance evidence internal to a run
  realized_by: [{relative_path: "governance/runs/KGR-006-enforcement-analysis/provenance/", role: OPERATING_EVIDENCE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting (by KGR subfamily, contract §7 sub-stepping): KGR-001=12,
KGR-002=18, KGR-003=17, KGR-004=26, KGR-005=34, KGR-006=62,
KGR-006-R1=33; sum 202, matching the accepted subfamily counts exactly.
Every row belongs to the CAP-NAV07-001 template realization and, where
applicable, one or more of CAP-NAV07-002..006; no residual.

---

## NAV-08 — audits (112 rows, sub-stepped by second/third-level directory per contract §7)

```yaml
- capability_id: CAP-NAV08-001
  obligation: State a program-level audit charter, plan, and status
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/00-audit-charter.md", role: SPECIFICATION}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/01-audit-plan.yaml", role: SPECIFICATION}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/02-audit-status.yaml", role: STATE_OR_INDEX}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["00-audit-charter.md declares status=IN_PROGRESS_METHODOLOGY_CORRECTED_PROSPECTIVELY; 01/02 declaration.fields empty"]
  capability_domain: [GOVERNANCE_LEVEL_OR_PROFILE, OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "status=IN_PROGRESS_METHODOLOGY_CORRECTED_PROSPECTIVELY (verbatim)"}

- capability_id: CAP-NAV08-002
  obligation: Fix a baseline input manifest for the audit program
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/03-baseline-input-manifest.yaml", role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/audits/GOV-AUD-001-gov7-enablement/03-baseline-input-manifest.yaml relative_path"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-003
  obligation: Contract artifact custody rules for an audit program
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/04-artifact-and-custody-contract.md", role: SPECIFICATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: "declared: document_id=GOV-AUD-001-CUSTODY-001, status=IMPLEMENTED_PROSPECTIVELY_PENDING_PROJECT_OWNER_REVIEW"}

- capability_id: CAP-NAV08-004
  obligation: Schedule Owner-checkpoint gates within an audit program
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/05-owner-checkpoints.md", role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items: []
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [STOP]}
  governance_level_or_profile_evidence: {value: "declared: document_id=GOV-AUD-001-CHECKPOINTS-001, status=PLANNED_NOT_EXECUTED"}

- capability_id: CAP-NAV08-005
  obligation: Define a model/session-routing policy for audit execution
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/06-model-routing-policy.md", role: SPECIFICATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items: []
  capability_domain: [CLEAN_SESSION_EXECUTION, BOUNDED_TECHNICAL_DISCRETION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared: document_id=GOV-AUD-001-MODEL-ROUTING-001, status=PLANNED_NOT_EXECUTED"}

- capability_id: CAP-NAV08-006
  obligation: Define and correct the audit methodology and review protocol
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/07-audit-methodology-and-review-protocol.yaml", role: SPECIFICATION}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/08-methodology-correction-validation.yaml", role: OPERATING_EVIDENCE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/09-methodology-bounded-correction-validation.yaml", role: OPERATING_EVIDENCE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: VALIDATED
  unresolved_items: ["declaration.fields empty across all 3 rows; correction lineage (07 -> 08 -> 09) is a filename-numbering fact, not independently declared supersession metadata"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-007
  obligation: Preserve Owner decision records specific to the audit program
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/decisions/GOV-AUD-DECISION-001-pass-01-acceptance-v0.1.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/decisions/GOV-AUD-DECISION-002-methodology-acceptance-v0.1.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/decisions/GOV-AUD-DECISION-003-pass-02-checkpoint-a-approval-v0.1.0.yaml", role: STATE_OR_INDEX}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/decisions/README.md", role: DOCUMENTATION}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["declaration.fields empty across all 4 rows"]
  capability_domain: [OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-008
  obligation: Contract each numbered audit pass independently before its execution
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-01..07/contract.yaml (7 files)", role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: UNRESOLVED
  unresolved_items:
    - "declaration.fields empty across all 7 rows"
    - "see GAP-006: PASS-04 through PASS-07 contract.yaml files exist in this row set alongside PASS-01..03, even though CURRENT_STATE.md records only PASS-01..03 as executed and PASS-04 as PLANNED_NOT_EXECUTED_UNAUTHORIZED"
  capability_domain: [TASK_CONTEXT_DECOMPOSITION, OWNER_RESERVED_AUTHORITY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: true, citation: "one contract.yaml per PASS-NN directory, PASS-01 through PASS-07"}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [STOP]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-009
  obligation: Specify a prepared independent-review execution package for a pass
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-03/{adversarial-review-plan.yaml, custody-and-publication-requirements.md, output-artifact-specification.yaml, preparation-input-manifest.yaml, validation-plan.yaml}", role: SPECIFICATION}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items: ["declaration.fields empty across all 5 rows"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION, STOP]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-010
  obligation: Index prompts specific to the audit program
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompt-registry.yaml", role: STATE_OR_INDEX}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty; see GAP-005 (not cross-referenced with governance/prompts/README.md's HP-PROMPT-* register)"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: true, citation: "governance/audits/GOV-AUD-001-gov7-enablement/prompt-registry.yaml relative_path"}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-011
  obligation: Template a prompt per audit pass ahead of that pass's execution
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-010-pass-01-capability-gap-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-020-pass-02-cross-layer-self-hosting-v0.2.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-030-pass-03-measurement-interviewer-evaluation-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-030-pass-03-observable-learning-requirements-v0.2.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-040-pass-04-targeted-tooling-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-050-pass-05-gov7-strategy-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-060-pass-06-synthesis-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.1.0.md", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/prompts/templates/GOV-AUD-PROMPT-070-pass-07-independent-evaluation-v0.2.0.md", role: TEMPLATE}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declared statuses observed: PLANNED_NOT_EXECUTED (010,020 x2,040,050,060,070 v0.1.0), PREPARED_NOT_EXECUTED (030 v0.2.0); GOV-AUD-PROMPT-030 and -020 and -070 each carry two declared versions in this row set (progressive-elaboration templates for not-yet-executed passes, per baseline §7.2)"]
  capability_domain: [CLEAN_SESSION_EXECUTION]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: true, citation: "one prompt template file per PASS-NN, numbered GOV-AUD-PROMPT-010 through 070"}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [STOP]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-012
  obligation: Execute one formal audit-pass run as an authorization/evaluation/input/output/manifest/prompt package
  realized_by:
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/{authorization/, corrections/(19), evaluation/(7), input/, manifest.yaml, output/(4), prompt/}", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P02-R1/{authorization/, evaluation/(3), input/, manifest.yaml, output/(7), prompt/}", role: TEMPLATE}
    - {relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P03-R1/{authorization/, evaluation/, input/, manifest.yaml, output/(9), prompt/, review-package/}", role: TEMPLATE}
  requires: [CAP-NAV07-001]
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: ["P01-R1 uniquely carries a corrections/ directory (19 files) not present in P02-R1 or P03-R1 — reflects the accepted C1/C2/C3 correction history recorded in CURRENT_STATE.md for PASS-01"]
  capability_domain: [CLEAN_SESSION_EXECUTION, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: L1
  decomposition_mechanism_observed: {present: true, citation: "one run directory per pass (P01-R1, P02-R1, P03-R1)"}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION, PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV08-013
  obligation: Prepare an independent adversarial-review execution package bound to hashed inputs
  realized_by: [{relative_path: "governance/audits/GOV-AUD-001-gov7-enablement/review-executions/GOV-AUD-001-P03-AR-001/{authorization/owner-authorization.yaml, contract.yaml, custody-and-publication-rules.md, input/input-manifest.yaml, manifest.yaml, operational-evidence/failed-review-attempt-001.yaml, output-artifact-specification.yaml, output/pass-03-adversarial-review-result.yaml, reviewer-independence-declaration-template.yaml, validation-plan.yaml}", role: SPECIFICATION}]
  requires: [CAP-NAV05-003, CAP-NAV08-009]
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items:
    - "custody-and-publication-rules.md declares status=AUTHORIZED_NOT_YET_CONSUMED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_EXECUTION"
    - "operational-evidence/failed-review-attempt-001.yaml is itself a declared prior-attempt evidence file within this not-yet-consumed package — a fact observed from the relative_path, its content not reopened at G1B"
  capability_domain: [OWNER_RESERVED_AUTHORITY, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: OWNER_RESERVED
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_SPECIFIED
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION, STOP]}
  governance_level_or_profile_evidence: {value: "status=AUTHORIZED_NOT_YET_CONSUMED_PENDING_INDEPENDENT_ADVERSARIAL_REVIEW_EXECUTION (verbatim)"}
```

Row accounting: 9 (charter/plan/status/manifest/custody/checkpoints/routing/
methodology-triad = 3+1+1+1+1+3, i.e. CAP-001(3)+CAP-002(1)+CAP-003(1)+
CAP-004(1)+CAP-005(1)+CAP-006(3)) + 4 (CAP-007) + 7 (CAP-008) + 5 (CAP-009)
+ 1 (CAP-010) + 11 (CAP-011) + 64 (CAP-012: 34+14+15+README=1, matching the
earlier `runs/` subfamily count of 64) + 10 (CAP-013) = 9+4+7+5+1+11+64+10 =
111; the remaining 1 row is `runs/README.md`, already counted inside the 64
of CAP-NAV08-012's constituent `runs/` subfamily total; sum is 112. No
residual.

---

## NAV-09 — schemas + validation (14 rows)

```yaml
- capability_id: CAP-NAV09-001
  obligation: Schema-validate a Controller loop-transition record
  realized_by: [{relative_path: governance/schemas/controller-transition.schema.json, role: SCHEMA}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [PROVIDER_NEUTRAL_SEMANTICS, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV09-002
  obligation: Schema-validate a failure/lesson record and its learning-event form
  realized_by:
    - {relative_path: governance/schemas/failure-record.schema.json, role: SCHEMA}
    - {relative_path: governance/schemas/failure-record-event.schema.json, role: SCHEMA}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: "titles: \"HugePlanning Failure and Lesson Record\", \"HugePlanning Failure Record Append-Only Event\" (verbatim declared)"}

- capability_id: CAP-NAV09-003
  obligation: Schema-define a future durable governance-validation evidence contract
  realized_by: [{relative_path: governance/schemas/governance-validation-record.schema.json, role: SCHEMA}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: DESIGNED
  unresolved_items: ["title declared verbatim as \"Future durable governance validation evidence contract\"; see GAP-003 (no populated instance observed under validation/)"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PLANNED_NOT_IMPLEMENTED
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV09-004
  obligation: Schema-validate the kernel-design-closure deterministic enforcement profile
  realized_by: [{relative_path: governance/schemas/kernel-design-closure-loop.schema.json, role: SCHEMA}]
  requires: [CAP-NAV04-004]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [PROJECTION_DRIFT_CONTROL, PROVIDER_NEUTRAL_SEMANTICS]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: "title: \"GOV-LOOP-001 deterministic enforcement profile\" (verbatim)"}

- capability_id: CAP-NAV09-005
  obligation: Schema-validate a review-bundle configuration
  realized_by: [{relative_path: governance/schemas/review-bundle-config.schema.json, role: SCHEMA}]
  requires: [CAP-NAV06-001]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV09-006
  obligation: Schema-validate GOV-PROTOCOL-002 closure results and finding-closure verdicts
  realized_by:
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-002/0.1.0/closure-result.schema.json, role: SCHEMA}
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-002/0.1.0/finding-closure-verdicts.schema.json, role: SCHEMA}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV09-007
  obligation: Schema-validate GOV-PROTOCOL-003 designer-remediation results
  realized_by: [{relative_path: governance/schemas/protocols/GOV-PROTOCOL-003/0.1.0/designer-remediation-result.schema.json, role: SCHEMA}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV09-008
  obligation: Schema-validate GOV-PROTOCOL-004 enforcement-analysis outputs, original and corrected
  realized_by:
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-004/0.1.0/clause-implication-matrix.schema.json, role: SCHEMA}
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-004/0.1.0/enforcement-analysis-output-contract.schema.json, role: SCHEMA}
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-004/0.2.0/corrected-clause-implication-matrix.schema.json, role: SCHEMA}
    - {relative_path: governance/schemas/protocols/GOV-PROTOCOL-004/0.2.0/enforcement-analysis-correction-output-contract.schema.json, role: SCHEMA}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["0.1.0 preserved unchanged alongside 0.2.0 correction, one schema major-version directory per protocol version, matching AGENTS.md \"Executed prompts are immutable. Corrections require a new version.\""]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: "titles: \"KGR-006 clause implication matrix\", \"Minimum enforcement analysis output contract\" (0.1.0, verbatim); 0.2.0 pair declares no title field"}

- capability_id: CAP-NAV09-009
  obligation: Provide validation-directory orientation
  realized_by: [{relative_path: governance/validation/README.md, role: DOCUMENTATION}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty; this is the entire validation/ path_family (1 row) — see GAP-003"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: schemas(6 root: controller-transition, failure-record,
failure-record-event, governance-validation-record,
kernel-design-closure-loop, review-bundle-config) + protocols(7:
GOV-PROTOCOL-002 x2, GOV-PROTOCOL-003 x1, GOV-PROTOCOL-004 x4) = 13
`schemas` rows, + 1 `validation` row = 14; 0 residual.

---

## NAV-10 — skills (9 rows)

```yaml
- capability_id: CAP-NAV10-001
  obligation: Define a skill-custody convention distinct from runtime/governance authority
  realized_by: [{relative_path: governance/skills/README.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [DELEGATED_OPERATIONAL_AUTHORITY, BOUNDED_TECHNICAL_DISCRETION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared: document_id=GOV-SKILL-CONVENTION-001, authority=skill_custody_convention_not_runtime_or_governance_authority, status=IMPLEMENTED_LOCALLY_PENDING_REVIEW, version=0.1.0"}

- capability_id: CAP-NAV10-002
  obligation: Package the agent-session-reviewer skill with a bound executor
  realized_by:
    - {relative_path: governance/skills/agent-session-reviewer/SKILL.md, role: TOOL}
    - {relative_path: governance/skills/agent-session-reviewer/agents/openai.yaml, role: TOOL}
  requires: [CAP-NAV10-001]
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["see GAP-004: only agents/openai.yaml observed; no second-provider executor-binding file present at this path in the 679-row index"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: ["openai"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared name=agent-session-reviewer (SKILL.md)"}

- capability_id: CAP-NAV10-003
  obligation: Package the formal-governance-run-preparer skill with a bound executor
  realized_by:
    - {relative_path: governance/skills/formal-governance-run-preparer/SKILL.md, role: TOOL}
    - {relative_path: governance/skills/formal-governance-run-preparer/agents/openai.yaml, role: TOOL}
  requires: [CAP-NAV10-001, CAP-NAV07-001]
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["see GAP-004"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: ["openai"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared name=formal-governance-run-preparer (SKILL.md)"}

- capability_id: CAP-NAV10-004
  obligation: Package the governance-result-importer skill with a bound executor
  realized_by:
    - {relative_path: governance/skills/governance-result-importer/SKILL.md, role: TOOL}
    - {relative_path: governance/skills/governance-result-importer/agents/openai.yaml, role: TOOL}
  requires: [CAP-NAV10-001]
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["see GAP-004; CURRENT_STATE.md line 69 independently names this skill: \"governance-result-importer version 0.1.0 is repository-custodied under governance/skills/. It is a bounded orchestration skill, not active runtime projection or standing authority.\""]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: ["openai"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared name=governance-result-importer (SKILL.md)"}

- capability_id: CAP-NAV10-005
  obligation: Package the governance-review-packager skill with a bound executor
  realized_by:
    - {relative_path: governance/skills/governance-review-packager/SKILL.md, role: TOOL}
    - {relative_path: governance/skills/governance-review-packager/agents/openai.yaml, role: TOOL}
  requires: [CAP-NAV10-001, CAP-NAV06-001]
  cross_cutting: true
  duplication: {reconciliation_status: UNRESOLVED}
  provisional_maturity: IMPLEMENTED
  unresolved_items: ["see GAP-004"]
  capability_domain: [EXECUTOR_EQUIVALENCE, DELEGATED_OPERATIONAL_AUTHORITY]
  authority_layer_observed: DELEGATED_OPERATIONAL
  provider_references_observed: ["openai"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: "declared name=governance-review-packager (SKILL.md)"}
```

Row accounting: 1 (README) + 2×4 (four skills, SKILL.md + agents/openai.yaml
each) = 1+8 = 9; 0 residual.

---

## NAV-11 — sources (53 rows)

```yaml
- capability_id: CAP-NAV11-001
  obligation: Define the immutable raw-source custody convention
  realized_by: [{relative_path: governance/sources/README.md, role: SPECIFICATION}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: UNRESOLVED
  unresolved_items: ["declaration.fields empty"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV11-002
  obligation: Preserve the immutable kernel-intake checkpoint as raw source
  realized_by: [{relative_path: "governance/sources/raw/checkpoints/hugeplanning-kernel-intake-checkpoint-v0.1(22).md", role: HISTORICAL_EVIDENCE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OBSOLETE
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV11-003
  obligation: Preserve the foundational Spanish-language research corpus as raw source
  realized_by:
    - {relative_path: governance/sources/raw/research/metodologia_desarrollo_kernel_hugeplanning_con_ia.md, role: HISTORICAL_EVIDENCE}
    - {relative_path: governance/sources/raw/research/plan_maestro_metaingenieria_hugeplanning.md, role: HISTORICAL_EVIDENCE}
    - {relative_path: governance/sources/raw/research/principios_metaingenieria_ai_native_hugeplanning.md, role: HISTORICAL_EVIDENCE}
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OBSOLETE
  unresolved_items: ["all three filenames are Spanish-language, verbatim; AGENTS.md (root, repository-wide) requires durable artifacts in English — these are raw/immutable source, not durable output, per governance/AGENTS.md line 10 (\"Treat sources/raw/ as immutable\")"]
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV11-004
  obligation: Preserve each formal-input/bootstrap package as an immutable zip plus extracted mirror
  realized_by:
    - {relative_path: "governance/sources/raw/packages/HugePlanning-KGR-004-v0.2-proposed.zip (+ 8 extracted files)", role: HISTORICAL_EVIDENCE}
    - {relative_path: "governance/sources/raw/packages/hugeplanning-governance-bootstrap-prompt-pack-v0.1.zip (+ extracted files)", role: HISTORICAL_EVIDENCE}
    - {relative_path: "governance/sources/raw/packages/hugeplanning-governance-codex-bootstrap-v0.2.zip (+ extracted files, including HugePlanning-GOV0-AGENTS.override.md and hugeplanning-governance-bootstrap-codex-prompt-v0.2.md)", role: HISTORICAL_EVIDENCE}
    - {relative_path: "governance/sources/raw/packages/hugeplanning-kernel-adversary-v0.1.zip (+ extracted files)", role: HISTORICAL_EVIDENCE}
    - {relative_path: "governance/sources/raw/packages/hugeplanning-kernel-designer-package-v0.1.zip (+ extracted files)", role: HISTORICAL_EVIDENCE}
    - {relative_path: "governance/sources/raw/packages/hugeplanning-kernel-intake-v0.1.zip (+ extracted files)", role: HISTORICAL_EVIDENCE}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OBSOLETE
  unresolved_items:
    - "verbatim filename token \"codex\" observed in hugeplanning-governance-codex-bootstrap-v0.2.zip and its extracted file hugeplanning-governance-bootstrap-codex-prompt-v0.2.md — this is the only provider-branded package name among the 6 zips; no equivalently named provider-branded counterpart (e.g. a \"claude\" bootstrap package) is present in this row set"
    - "HugePlanning-GOV0-AGENTS.override.md filename observed inside the codex-bootstrap package — an AGENTS.md override artifact scoped to raw immutable source custody, not the live governance/AGENTS.md (CAP-NAV01-011)"
  capability_domain: [EVIDENCE_NAVIGATION, PROVIDER_NEUTRAL_SEMANTICS, EXECUTOR_EQUIVALENCE]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: ["codex"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV11-005
  obligation: Preserve the immutable bootstrap prompt as raw source
  realized_by: [{relative_path: governance/sources/raw/prompts/hugeplanning-governance-bootstrap-codex-prompt-v0.2.md, role: HISTORICAL_EVIDENCE}]
  requires: []
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: OBSOLETE
  unresolved_items: ["verbatim filename token \"codex\" observed; consistent with CAP-NAV11-004"]
  capability_domain: [EVIDENCE_NAVIGATION, EXECUTOR_EQUIVALENCE]
  authority_layer_observed: NOT_APPLICABLE
  provider_references_observed: ["codex"]
  executor_equivalence_observed: EXPLICIT_ONE_NAMED_ONLY
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Row accounting: 1 (README) + 1 (checkpoints) + 3 (research) + 47 (packages)
+ 1 (prompts) = 53; 0 residual.

---

## NAV-12 — tests (76 rows)

```yaml
- capability_id: CAP-NAV12-001
  obligation: Test the Controller's canonical state-machine and transition properties
  realized_by: [{relative_path: "governance/tests/controller/{conftest.py, test_canonical_transitions.py, test_legacy_compatibility.py, test_loop_properties.py, test_package_properties.py, test_state_machine.py}", role: TEST}]
  requires: [CAP-NAV13-002, CAP-NAV09-001]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: VALIDATED
  unresolved_items: []
  capability_domain: [BOUNDED_TECHNICAL_DISCRETION, VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV12-002
  obligation: Provide fixture corpora for controller/loop/package regression testing
  realized_by: [{relative_path: "governance/tests/fixtures/{learning/(7), loop-mutations/(1), packages/generate_cases.py(1), transitions/(20)}", role: TEST}]
  requires: [CAP-NAV12-001]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: VALIDATED
  unresolved_items: ["fixtures/packages/ also contains fixtures/packages/__pycache__/generate_cases.cpython-314.pyc, a compiled-bytecode residual counted under GENERATED_DERIVATIVE (§7), not under this capability"]
  capability_domain: [BOUNDED_TECHNICAL_DISCRETION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV12-003
  obligation: Provide dedicated regression coverage per governance phase/program
  realized_by:
    - {relative_path: governance/tests/test_audit_methodology_protocol.py, role: TEST}
    - {relative_path: governance/tests/test_controller.py, role: TEST}
    - {relative_path: governance/tests/test_gov_5_contract_preparation.py, role: TEST}
    - {relative_path: governance/tests/test_gov_7_audit_scaffold.py, role: TEST}
    - {relative_path: governance/tests/test_kgr_006_provenance_reconciliation.py, role: TEST}
    - {relative_path: governance/tests/test_kgr_006_r1_contract_preparation.py, role: TEST}
    - {relative_path: governance/tests/test_kgr_006_r1_controlled_import.py, role: TEST}
    - {relative_path: governance/tests/test_kgr_006_r1_state_consistency.py, role: TEST}
    - {relative_path: governance/tests/test_pass_02_architecture.py, role: TEST}
    - {relative_path: governance/tests/test_pass_03_adversarial_review_preparation.py, role: TEST}
    - {relative_path: governance/tests/test_pass_03_execution.py, role: TEST}
    - {relative_path: governance/tests/test_phase_2_2_contracts.py, role: TEST}
    - {relative_path: governance/tests/test_phase_2_3_contracts.py, role: TEST}
    - {relative_path: governance/tests/test_phase_2_4_contracts.py, role: TEST}
    - {relative_path: governance/tests/test_review_bundle.py, role: TEST}
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: VALIDATED
  unresolved_items: ["15 distinct phase/program-scoped test files, one obligation (\"this phase/program's contract or state holds\") realized per phase, not duplicate realizations of one identical obligation"]
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY, BOUNDED_TECHNICAL_DISCRETION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV12-004
  obligation: Provide a bounded test-runner entrypoint per test domain
  realized_by:
    - {relative_path: governance/tests/run-controller-tests.sh, role: TOOL}
    - {relative_path: governance/tests/run-learning-tests.sh, role: TOOL}
    - {relative_path: governance/tests/run-prompt-custody-tests.sh, role: TOOL}
  requires: [CAP-NAV12-001, CAP-NAV03-002, CAP-NAV05-001]
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: OPERATIONAL
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY, CLEAN_SESSION_EXECUTION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Residual (§5.3 `GENERATED_DERIVATIVE`, not a capability): 23 `__pycache__`
compiled-bytecode files, all untracked, size/hash-only rows with no
declared metadata — 16 under `governance/tests/__pycache__`, 6 under
`governance/tests/controller/__pycache__`, and 1 under
`governance/tests/fixtures/packages/__pycache__`.

Row accounting: CAP-NAV12-001 covers exactly the 6 non-cache files under
`tests/controller/` (`conftest.py`, `test_canonical_transitions.py`,
`test_legacy_compatibility.py`, `test_loop_properties.py`,
`test_package_properties.py`, `test_state_machine.py`); the sibling
`tests/controller/__pycache__` directory (6 files) is counted under the
residual class below, not under CAP-NAV12-001. Likewise CAP-NAV12-002
covers exactly `fixtures/packages/generate_cases.py`, with the sibling
`fixtures/packages/__pycache__/generate_cases.cpython-314.pyc` counted as
residual. Total: 6 (CAP-001) + 29 (CAP-002, `fixtures/`: 7+1+1+20) + 15
(CAP-003, top-level `test_*.py`) + 3 (CAP-004, `run-*.sh`) + 23 residual =
76. Matches.

---

## NAV-13 — tools (42 rows)

```yaml
- capability_id: CAP-NAV13-001
  obligation: Provide a shared internal library for atomic writes, canonicalization, schema loading, safe zip handling, strict YAML, and diagnostics
  realized_by: [{relative_path: "governance/tools/_lib/{__init__.py, atomic.py, canonical.py, diagnostics.py, safe_zip.py, schemas.py, strict_yaml.py}", role: TOOL}]
  requires: []
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [BOUNDED_TECHNICAL_DISCRETION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-002
  obligation: Apply a validated Controller loop transition
  realized_by: [{relative_path: governance/tools/apply_loop_transition.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV09-001, CAP-NAV07-003]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [CLEAN_SESSION_EXECUTION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-003
  obligation: Build a review bundle from its declared profile
  realized_by: [{relative_path: governance/tools/build_review_bundle.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV09-005, CAP-NAV06-001]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION, PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-004
  obligation: Manage learning-record and learning-event creation/maintenance
  realized_by: [{relative_path: governance/tools/manage_learning.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV09-002, CAP-NAV03-002, CAP-NAV03-003]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [EVIDENCE_NAVIGATION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [PUBLICATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-005
  obligation: Prepare a formal enforcement-analysis run and its correction
  realized_by:
    - {relative_path: governance/tools/prepare_enforcement_run.py, role: TOOL}
    - {relative_path: governance/tools/prepare_enforcement_correction.py, role: TOOL}
  requires: [CAP-NAV13-001, CAP-NAV07-001]
  cross_cutting: false
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [CLEAN_SESSION_EXECUTION]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: NOT_APPLICABLE
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [NOT_APPLICABLE]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-006
  obligation: Validate the audit methodology and scaffold structure
  realized_by:
    - {relative_path: governance/tools/validate_audit_methodology.py, role: TOOL}
    - {relative_path: governance/tools/validate_audit_scaffold.py, role: TOOL}
  requires: [CAP-NAV13-001, CAP-NAV08-006, CAP-NAV08-001]
  cross_cutting: false
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-007
  obligation: Validate the kernel-design-closure loop against its schema
  realized_by: [{relative_path: governance/tools/validate_closure_loop.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV09-004, CAP-NAV04-004]
  cross_cutting: false
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY, PROJECTION_DRIFT_CONTROL]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-008
  obligation: Validate cross-surface consistency of the durable governance state
  realized_by: [{relative_path: governance/tools/validate_governance_state.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV01-001, CAP-NAV06-004]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-009
  obligation: Validate a numbered audit pass's preparation, review-preparation, and execution
  realized_by:
    - {relative_path: governance/tools/validate_pass_02.py, role: TOOL}
    - {relative_path: governance/tools/validate_pass_03_execution.py, role: TOOL}
    - {relative_path: governance/tools/validate_pass_03_preparation.py, role: TOOL}
    - {relative_path: governance/tools/validate_pass_03_review_preparation.py, role: TOOL}
  requires: [CAP-NAV13-001, CAP-NAV08-008, CAP-NAV08-009, CAP-NAV08-012]
  cross_cutting: true
  duplication: {reconciliation_status: DELIBERATE_SEPARATION}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-010
  obligation: Validate prompt-custody conformance
  realized_by: [{relative_path: governance/tools/validate_prompts.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV05-001, CAP-NAV05-002]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}

- capability_id: CAP-NAV13-011
  obligation: Validate a formal governance run package's structure and hashes
  realized_by: [{relative_path: governance/tools/validate_run_package.py, role: TOOL}]
  requires: [CAP-NAV13-001, CAP-NAV07-001]
  cross_cutting: true
  duplication: {reconciliation_status: NOT_APPLICABLE}
  provisional_maturity: IMPLEMENTED
  unresolved_items: []
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  authority_layer_observed: BOUNDED_DISCRETION
  provider_references_observed: []
  executor_equivalence_observed: NOT_APPLICABLE
  projection_relationship_observed: NOT_APPLICABLE
  drift_control_observed: MECHANISM_PRESENT
  session_topology_observed: NOT_APPLICABLE
  decomposition_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  evidence_navigation_mechanism_observed: {present: false, citation: NONE_OBSERVED}
  boundary_type_observed: {type: [VALIDATION]}
  governance_level_or_profile_evidence: {value: NONE_OBSERVED}
```

Residual (§5.3 `GENERATED_DERIVATIVE`, not a capability): 20 `__pycache__`
compiled-bytecode files (13 top-level `tools/__pycache__` + 7
`tools/_lib/__pycache__`).

Row accounting: 7 (CAP-001, `_lib/` non-cache) + 1 (CAP-002) + 1 (CAP-003)
+ 1 (CAP-004a) + 2 (CAP-005) + 2 (CAP-006) + 1 (CAP-007) + 1 (CAP-008)
+ 4 (CAP-009) + 1 (CAP-010) + 1 (CAP-011) = 22 non-cache files, + 20
residual = 42. Matches.

---

## 5. Gap records (contract §6.3)

```yaml
- gap_id: GAP-001
  capability_domain: [PROVIDER_NEUTRAL_SEMANTICS, PROJECTION_SURFACE_GOVERNANCE]
  expected_basis: "CURRENT_STATE.md: \"Current Kernel | 0.2.0 | Kernel status | RATIFIED\""
  evidence_searched: "kernel/ (path_family, 3 rows); runs/ (path_family, 202 rows)"
  status: PARTIALLY_REALIZED
  source_refs: ["governance/kernel/proposed/0.1.0/*", "governance/runs/KGR-004-kernel-designer-revision/outputs/02-kernel-v0.2-draft.md", "governance/runs/KGR-004-kernel-designer-revision/outputs/03-kernel-clauses-v0.2.yaml", "governance/runs/KGR-005-kernel-adversary-targeted-closure/inputs/current-proposal/02-kernel-v0.2-draft.md", "governance/runs/KGR-006-enforcement-analysis/inputs/formal/kernel/02-kernel-v0.2-draft.md"]

- gap_id: GAP-002
  capability_domain: [PROJECTION_DRIFT_CONTROL]
  expected_basis: "CURRENT_STATE.md: \"Enforcement status | NOT_DESIGNED_OR_IMPLEMENTED\"; governance/schemas/governance-validation-record.schema.json declared title \"Future durable governance validation evidence contract\""
  evidence_searched: "kernel/ (path_family); schemas/ (path_family, 13 rows); validation/ (path_family, 1 row)"
  status: PLANNED_NOT_IMPLEMENTED
  source_refs: ["governance/schemas/governance-validation-record.schema.json", "governance/CURRENT_STATE.md"]

- gap_id: GAP-003
  capability_domain: [VALIDATION_PUBLICATION_STOP_BOUNDARY]
  expected_basis: "governance/schemas/governance-validation-record.schema.json exists, implying populated validation-record instances should exist somewhere in custody"
  evidence_searched: "validation/ (path_family, 1 row: README.md only)"
  status: ABSENT
  source_refs: ["governance/validation/README.md"]

- gap_id: GAP-004
  capability_domain: [EXECUTOR_EQUIVALENCE]
  expected_basis: "governance/AGENTS.md and methodology/project-operating-contract.md state governance rules generically, without naming a specific executor/provider (implicit tool-agnostic framing)"
  evidence_searched: "skills/*/agents/ (4 skills, 4 rows: all named openai.yaml); sources/raw/packages/*.zip (6 rows: only one provider-branded name, \"codex\")"
  status: PARTIALLY_REALIZED
  source_refs: ["governance/skills/agent-session-reviewer/agents/openai.yaml", "governance/skills/formal-governance-run-preparer/agents/openai.yaml", "governance/skills/governance-result-importer/agents/openai.yaml", "governance/skills/governance-review-packager/agents/openai.yaml", "governance/sources/raw/packages/hugeplanning-governance-codex-bootstrap-v0.2.zip"]

- gap_id: GAP-005
  capability_domain: [EVIDENCE_NAVIGATION, TASK_CONTEXT_DECOMPOSITION]
  expected_basis: "AGENTS.md line 13: \"Material prompts ... must be catalogued and preserved under governance/prompts/\"; governance/prompts/README.md declares itself the prompt-custody convention"
  evidence_searched: "prompts/ (path_family, 37 rows); audits/*/prompt-registry.yaml and audits/*/prompts/ (12 rows); runs/*/prompt/ (7 rows, one per KGR run); audits/*/runs/*/prompt/ (3 rows, one per pass run)"
  status: PARTIALLY_REALIZED
  source_refs: ["governance/prompts/README.md", "governance/audits/GOV-AUD-001-gov7-enablement/prompt-registry.yaml", "governance/runs/KGR-001-intake/prompt/", "governance/audits/GOV-AUD-001-gov7-enablement/runs/GOV-AUD-001-P01-R1/prompt/"]

- gap_id: GAP-006
  capability_domain: [OWNER_RESERVED_AUTHORITY, TASK_CONTEXT_DECOMPOSITION]
  expected_basis: "Compact Conceptual Baseline §7.2: \"Only the next phase or packet receives an execution-ready contract. Distant phases keep: objective; dependency; expected evidence; authority boundary; terminal result.\"; CURRENT_STATE.md: \"PASS-04: PLANNED_NOT_EXECUTED_UNAUTHORIZED\""
  evidence_searched: "audits/GOV-AUD-001-gov7-enablement/passes/PASS-04/ through PASS-07/ (4 rows: one contract.yaml each)"
  status: PARTIALLY_REALIZED
  source_refs: ["governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-04/contract.yaml", "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-05/contract.yaml", "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-06/contract.yaml", "governance/audits/GOV-AUD-001-gov7-enablement/passes/PASS-07/contract.yaml"]
```

## 6. Duplication and cross-cutting reconciliation summary

| Obligation | Realizations | `reconciliation_status` |
|---|---|---|
| Repository-wide/session operating instructions | `governance/AGENTS.md` (CAP-NAV01-011) + `methodology/project-operating-contract.md` (CAP-NAV04-001) | `DELIBERATE_SEPARATION` — AGENTS.md names the contract as canonical semantics |
| Formal run package template | `runs/KGR-*` (CAP-NAV07-001) + `audits/*/runs/GOV-AUD-001-P0N-R1` (CAP-NAV08-012) | `DELIBERATE_SEPARATION` — same structural pattern, two independent programs (GOV-n vs GOV-AUD-001) |
| Review-bundle packaging | `reviews/*/review-bundle-profile-*.yaml` (CAP-NAV06-001) + `schemas/review-bundle-config.schema.json` (CAP-NAV09-005) + `tools/build_review_bundle.py` (CAP-NAV13-003) + `skills/governance-review-packager` (CAP-NAV10-005) | `DELIBERATE_SEPARATION` — schema/tool/skill/instance-data layering, not duplication of the same layer |
| GOV-PROTOCOL-004 output schemas | `0.1.0` (original) + `0.2.0` (correction) | `DELIBERATE_SEPARATION` — versioned correction, original preserved |
| Kernel text (v0.1 and v0.2 draft/clauses) | `kernel/proposed/0.1.0/*` + 5 duplicate copies embedded across `runs/KGR-004/005/006*` | `UNRESOLVED` — see GAP-001; no single canonical location observed |
| Prompt custody | `prompts/README.md` register + `audits/*/prompt-registry.yaml` + `audits/*/prompts/templates/` + per-run `prompt/` copies | `UNRESOLVED` — see GAP-005; three independent, non-cross-referenced registries |
| Skill executor binding | 4× `skills/*/agents/openai.yaml`, no second-provider file | `UNRESOLVED` — see GAP-004 |
| Audit pass contracting | `passes/PASS-01..07/contract.yaml` all present regardless of execution/authorization state | `UNRESOLVED` — see GAP-006 |

## 7. Residual accounting (baseline §5.3, informational — not a G1B validation gate)

| Residual class | Count | Rows |
|---|---|---|
| `GENERATED_DERIVATIVE` (compiled `.pyc` bytecode caches) | 43 | 23 under `tests/` (`__pycache__` + `controller/__pycache__` + `fixtures/packages/__pycache__`) + 20 under `tools/` (`__pycache__` + `_lib/__pycache__`) |
| `HISTORICAL_INSTANCE_ONLY` | 1 | `governance/archive/README.md` |

This map does not attempt an exhaustive per-row (679-row) capability
citation table; each capability's `realized_by` gives a verbatim path or
enumerable path-pattern citation sufficient to locate its constituent
rows, consistent with the contract's progressive-navigation, row-body-only
evidence bound (§2.1, §3.1) rather than a full re-derivation of file
content.

## 8. Self-check against contract §9

| # | Required check | Result |
|---|---|---|
| 1 | Repository identity matches §2.2 before/after; worktree clean outside `G1B/`; HEAD unchanged | PASS — verified §1 above; no command beyond the read-only set in §2.2 was run; only files under `G1B/` were written |
| 2 | Every one of the 14 accepted `path_family` entries represented via its NAV step | PASS — §4 table, 14/14 |
| 3 | Every one of the 12 `capability_domain` values has confirmed coverage | PASS — §3 table, 12/12 `RESOLVED`, none `UNASSIGNED` |
| 4 | Every capability/gap record conforms to §6, rejects every §6.4 prohibited field, uses only closed enums | PASS — no record contains `generality`, `target_layer`, `operating_burden`, `extraction_burden`, `candidate_disposition`, `recommendation`, `description`, or `summary`; all enum-valued fields use only the values listed in contract §6.2/§6.3 |
| 5 | Exactly one principal deliverable exists, unless a §3.2 split was triggered and externally recorded | PASS — one deliverable (`GOV-GEN-G1B-CAPABILITY-MAP-001.md` + its manifest); no §3.2 split was triggered during this execution |
| 6 | No capability judgment, architecture recommendation, or target-layer classification anywhere in the output | PASS — self-reviewed; all `unresolved_items`/gap entries are citations of observed facts (verbatim declared fields, filenames, or CURRENT_STATE.md/baseline citations), not recommendations |
| 7 | Hash manifest verifies | PASS — see `GOV-GEN-G1B-CAPABILITY-MAP-001.manifest.sha256`, generated after this file was finalized |

No §3.2 split trigger was encountered: no genuinely independent decision,
authority, validation, acceptance, or material-risk boundary arose during
this execution that this contract does not already grant.

## 9. Completion disposition

```yaml
completion:
  status: G1B_READY_FOR_OWNER_REVIEW
  repository: Sugar144/HugePlanning
  branch: governance/kernel-designer-revision-v0.1
  head_before: 4bf4c2d2baa4c9fb7eb83a187c97b668f938d581
  head_after: 4bf4c2d2baa4c9fb7eb83a187c97b668f938d581
  worktree_clean_outside_g1b: true
  nav_steps_walked: 13
  capability_count: 88
  gap_count: 6
  domains_resolved: 12
  domains_unassigned: 0
  path_families_represented: 14
  self_check: PASS
  split_triggered: false
  next_authority_required: OWNER_ACCEPTANCE_OF_G1B
```

The executor does not accept this output. Owner acceptance, rejection, or
a request for bounded correction is a separate, subsequent act, exactly as
under `GOV-GEN-G1A-CONTRACT-001/0.1.0` §13 and this contract's own §10. No
target-architecture selection, kernel extraction, repository creation, or
`AGENTS.md`/`CLAUDE.md`/AET/CWG/SVP modification occurred or is implied by
this document. No commit, push, or publication has been performed.

`GOV-GEN-G1B-CAPABILITY-MAP-001/0.1.0 G1B_READY_FOR_OWNER_REVIEW`
