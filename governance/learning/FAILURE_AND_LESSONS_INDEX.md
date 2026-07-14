# Failure and Lessons Index

> GENERATED FILE — source of truth: `records/` plus append-only `events/`.
> Tool version: `0.1.0`. Deterministic input digest: `d9068b8d01d4bfe7726210844604d125fa2ea0f49d3c8e6dca4a795423e10d50`.
> Manual edits will be overwritten by `--apply` or rejected as generated-view drift.

| ID | Date | Title | Primary classification | Severity | Effective status | Component | Phase/run | Owner decision required | Measurement quality | Reusable lesson |
|---|---|---|---|---|---|---|---|---|---|---|
| HP-FAIL-001 | 2026-07-14 | Closure-loop control contract was initially under-specified | PROCESS_DEFECT | HIGH | CORRECTED | Kernel Design Closure Loop | GOV-4/none | no | UNAVAILABLE | A governance loop must be a closed, role-separated transition contract before any run is prepared against it. |
| HP-FAIL-002 | 2026-07-14 | Formal package and execution identity semantics were initially incomplete | PROCESS_DEFECT | HIGH | CORRECTED | Formal Run Package Identity | GOV-4/KGR-005 | no | UNAVAILABLE | Formal packages require separate custody, transport, execution, and import identities with exact stage-specific validation. |
| HP-FAIL-003 | 2026-07-14 | Deterministic governance checks were repeatedly assigned to high-capability models | COST_WASTE | MEDIUM | CORRECTED | Governance Validation and Model Routing | GOV-4/none | no | PARTIAL | Route exact governance checks to offline scripts and reserve model reasoning for judgment that code cannot settle. |
| HP-FAIL-004 | 2026-07-14 | Formal learning and analysis artifacts were dispersed across non-canonical surfaces | PROCESS_DEFECT | MEDIUM | CORRECTED | Durable Learning and Formal Analysis Output | GOV-4/none | no | PARTIAL | Declare and validate a durable output artifact before formal analysis, and store material learning in canonical indexed records. |
