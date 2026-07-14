# KGR-005 — Kernel Adversary Targeted Closure

Execution status: `NOT_STARTED`  
Preparation status: `COMPLETED`  
Readiness: `READY_FOR_EXECUTION`  
Mode: `TARGETED_CLOSURE`  
Kernel: `PROPOSED_NOT_RATIFIED`  
Kernel version: `0.2.0-proposed`

## Prepared contract

KGR-005 is prepared to independently verify the KGR-004 closure claims under `GOV-PROTOCOL-002` and `GOV-LOOP-001` version `0.1.0`. The formal input is `GOV-INPUT-002`: one input envelope, one byte-identical loop-control snapshot, eight byte-identical KGR-004 current-proposal aliases, seven byte-identical KGR-003 original-review aliases, and two byte-identical KGR-002 predecessor-Kernel aliases. Each formal non-envelope file has a repository custody `path`, historical `source_path`, exact archive `package_member`, and SHA-256. Isolated execution resolves only archive members; preparation and later repository import independently validate repository provenance.

The run prompt snapshot `GOV-PROMPT-007` is byte-identical to the canonical targeted-closure protocol. Its exact SHA-256 is `171914d7d6ff7024330ecccc1d662055ee8b77c4402a0c4bcac4271cbc98f67a`, recorded in `GOV-INPUT-002`, this run manifest, the Artifact Registry, and checksums. The exact snapshot is delivered separately from the 19-file formal input ZIP, whose SHA-256 is `26291b32594f2b73e12107bec9572b528e4ec3e32e4ca08f9746c5aba1adf9cf`. Isolated execution validates prompt/envelope metadata identity; preparation and repository import verify snapshot SHA-256. The formal transport package excludes the prompt, outputs, manifests, repository state, methodology navigation, and raw historical packages.

`GOV-LOOP-001` supplies the single ordered substantive-result matrix. KGR-005 begins with counters `completed_targeted_closure_runs: 0` and `completed_designer_remediation_runs: 0`. The Controller increments the targeted counter only after a valid completed result import, evaluates deterministic limits/signatures, and creates the durable transition record.

## Execution boundary

Preparation created no targeted-closure evidence. KGR-005 has not been executed, no findings have been independently closed or reopened, and no transition result exists. The outputs directory contains only a preparation notice.

Allowed substantive completed Adversary results are `CLOSURE_CONFIRMED`, `DESIGNER_REMEDIATION_REQUIRED`, `OWNER_DECISION_REQUIRED`, `RESEARCH_REQUIRED`, or `STRUCTURAL_REDESIGN_REQUIRED`. The Loop Controller validates and maps that result, increments validated counters, and records the durable transition.

`BLOCKED_BY_PACKAGE_CONFLICT` is a pre-substantive attempt outcome, not a completed result. It stops before KA-C1, preserves counters, produces neither the eight formal outputs nor an output ZIP, and permits correction and resumption of KGR-005. `PAUSED` is interaction-only.

After a valid substantive completed execution, the exact eight outputs must be packaged as `HugePlanning-KGR-005-targeted-closure-v0.2-proposed.zip`. That ZIP gains no automatic authority and receives `GOV-PKG-007` only after independent repository import validation.

Neither readiness nor a future `CLOSURE_CONFIRMED` result ratifies or adopts the Kernel, authorizes Enforcement Engineering, or establishes enforceability, implementation, operation, compliance, or maturity.
