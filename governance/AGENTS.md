# Governance Workspace Instructions

These instructions apply only to work launched from `governance/` or its descendants.

Apply the repository-wide `../AGENTS.md` and the canonical `methodology/project-operating-contract.md` before these stricter governance rules.

- Scope is governance design, review, provenance, adoption planning, and explicitly authorized later governance implementation.
- Read `README.md`, `CURRENT_STATE.md`, `GOVERNANCE_MASTER_PLAN.md`, the applicable run manifest, and then task-specific inputs.
- Proposed artifacts are not ratified, enforceable, operational, or runtime authority.
- Treat `sources/raw/` as immutable; verify it against `SOURCE_CHECKSUMS.sha256`.
- The Kernel remains `PROPOSED_NOT_RATIFIED` until explicit competent human ratification is recorded. Enforcement Engineering remains `CLOSED` until a valid authorized transition opens it.
- Completed runs, bound prompts, inputs, outputs, imported raw sources, decisions, and future Controller records are immutable.
- A formal run requires exact role, mode, and run identity; an exact prompt snapshot; an envelope; the applicable control snapshot; a complete hashed input set; an output contract; honest status; and independent import validation.
- Keep authority separate: the Designer drafts but cannot self-close; the Adversary assesses but cannot mutate the Kernel or counters; a future Controller may validate declared structure and route transitions but cannot make constitutional judgments; the Project Owner retains authorization, risk, acceptance, and ratification decisions.
- Register prompts, inputs, outputs, decisions, limitations, provenance, and honest run status.
- For every material orchestration prompt, preserve the exact executed text, assign a stable prompt ID and version, record its authorization boundary and execution status, and link it to resulting artifacts, validation evidence, and commit when available.
- Executed prompts are immutable. Corrections require a new version.
- If the exact historical prompt is unavailable, record `NOT_PRESERVED` and do not reconstruct it as original evidence.
- Formal run prompts already preserved under `governance/runs/<run>/prompt/` remain authoritative for those runs and need only be catalogued or referenced, not duplicated unnecessarily.
- Triage material governance failures and owner corrections under `learning/README.md`. Route incidents and decisions to their own record classes.
- On completion of a governance run, update its manifest, `ARTIFACT_REGISTRY.yaml`, `CURRENT_STATE.md`, and the relevant plan status.
- Use governance validation tools when available before claiming structural, package, result, transition, or generated-view validity.
- `CURRENT_STATE.md` must follow evidence and never fabricate or lead it. After a valid authorized event, update applicable learning, decision, registry, run, plan, and state records consistently.
- Correct methodology defects prospectively through versioning. Never rewrite historical evidence to conform to newer methodology.
- Do not change runtime surfaces without an explicit integration or adoption task that authorizes exact paths.
- Never fabricate retrospective evidence, execution, independence, validation, acceptance, enforceability, or ratification.
- Stop on authority conflict, provenance conflict, a missing core package, a forbidden-path change, or destructive ambiguity.
- Validate Markdown links, YAML, registered paths, checksums, IDs, and changed paths before completion.
- Communicate with the operator in Spanish; write repository artifacts in English.
