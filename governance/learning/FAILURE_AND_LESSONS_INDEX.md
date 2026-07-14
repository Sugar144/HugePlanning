# Failure and Lessons Index

> GENERATED FILE — source of truth: `records/` plus append-only `events/`.
> Tool version: `0.1.0`. Deterministic input digest: `340f280d4ddd8fdcee0437978f2d4ef1f8f9d5918e67c5615d5a74a6ea3add1c`.
> Manual edits will be overwritten by `--apply` or rejected as generated-view drift.

| ID | Date | Title | Primary classification | Severity | Effective status | Component | Phase/run | Owner decision required | Measurement quality | Reusable lesson |
|---|---|---|---|---|---|---|---|---|---|---|
| HP-FAIL-001 | 2026-07-14 | Closure-loop control contract was initially under-specified | PROCESS_DEFECT | HIGH | CORRECTED | Kernel Design Closure Loop | GOV-4/none | no | UNAVAILABLE | A governance loop must be a closed, role-separated transition contract before any run is prepared against it. |
| HP-FAIL-002 | 2026-07-14 | Formal package and execution identity semantics were initially incomplete | PROCESS_DEFECT | HIGH | CORRECTED | Formal Run Package Identity | GOV-4/KGR-005 | no | UNAVAILABLE | Formal packages require separate custody, transport, execution, and import identities with exact stage-specific validation. |
| HP-FAIL-003 | 2026-07-14 | Deterministic governance checks were repeatedly assigned to high-capability models | COST_WASTE | MEDIUM | CORRECTED | Governance Validation and Model Routing | GOV-4/none | no | PARTIAL | Route exact governance checks to offline scripts and reserve model reasoning for judgment that code cannot settle. |
| HP-FAIL-004 | 2026-07-14 | Formal learning and analysis artifacts were dispersed across non-canonical surfaces | PROCESS_DEFECT | MEDIUM | CORRECTED | Durable Learning and Formal Analysis Output | GOV-4/none | no | PARTIAL | Declare and validate a durable output artifact before formal analysis, and store material learning in canonical indexed records. |
