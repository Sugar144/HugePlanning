# Governance Methodology

This area contains reusable governance-process contracts: role definitions, versioned protocols, rubrics, and interaction methods. It describes how governance work is to be performed; it does not record that the work occurred.

Actual executions belong in `governance/runs/`. A run record must preserve the exact execution contract, formal inputs, outputs, status, and provenance used for that execution. The existence of a methodology artifact or prompt does not prove execution, validation, acceptance, or authority.

Historical prompts remain at the paths where their executions are recorded. They are not silently replaced by later methodology. When a materially different workflow is needed, it receives a separately versioned protocol and a run preserves an exact snapshot of that protocol.

Current methodology areas:

- `roles/kernel-designer/` — Designer modes and versioned revision/remediation protocols.
- `roles/kernel-adversary/` — Adversary modes and the targeted-closure protocol.
- `loops/kernel-design-closure/` — bounded orchestration, transition, counter, finding-identity, and history rules for independent Kernel design closure.

Loop success is distinct from Kernel ratification. Methodology has no constitutional authority and does not itself execute a run.
