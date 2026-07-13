# Governance Decision Log

Only explicit, supportable decisions are recorded here. Proposed constitutional content and unresolved interpretations belong elsewhere.

## GOV-DEC-001 — Same-repository governance custody

- Date: 2026-07-13
- Status: ACTIVE
- Statement: HugePlanning-specific governance remains in the HugePlanning repository.
- Rationale: Git and repository artifacts are the selected durable, versioned project memory, while governance remains clearly separated in `governance/`.
- Source: GOV-0 execution contract §2 and §11; supplied owner instruction.
- Consequences: governance history is reviewable with project history; it must not reorganize existing runtime, product, or planning areas.
- Supersedes: none

## GOV-DEC-002 — Separate bootstrap branch and worktree

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Governance bootstrap uses branch `governance/bootstrap-v0.1` in `/home/sugar/Documents/HugePlanning-governance`.
- Rationale: isolate GOV-0 from active S1 implementation.
- Source: GOV-0 execution contract §1 and supplied setup package.
- Consequences: no merge, rebase, inspection, or modification of the S1 worktree is part of GOV-0.
- Supersedes: none

## GOV-DEC-003 — GOV-0 write boundary

- Date: 2026-07-13
- Status: ACTIVE
- Statement: GOV-0 may commit changes only under `governance/**`.
- Rationale: bootstrap organizes governance history without changing the runtime or existing planning system.
- Source: GOV-0 execution contract §3 and root temporary override.
- Consequences: all other repository paths are read-only; forbidden-path drift blocks completion.
- Supersedes: none

## GOV-DEC-004 — S1 independence

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Active S1 work continues independently and must not be disturbed by governance bootstrap.
- Rationale: governance adoption is future work and cannot be imposed retroactively during source organization.
- Source: GOV-0 execution contract §1, §3, and §11.
- Consequences: GOV-0 performs no S1 inspection, audit, regularization, merge, or runtime projection.
- Supersedes: none

## GOV-DEC-005 — Repository artifacts as durable project memory

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Git and repository artifacts become the durable project memory for governance work.
- Rationale: durable history requires versioned, inspectable artifacts rather than reliance on prior chat state.
- Source: GOV-0 execution contract §11 minimum decision list; repository invariant “Git is truth.”
- Consequences: source custody, manifests, decisions, and status transitions are committed and reviewable.
- Supersedes: none

## GOV-DEC-006 — Version the governance execution record

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Prompts, inputs, outputs, decisions, and run manifests are versioned.
- Rationale: execution claims must be traceable to their contracts and evidence.
- Source: GOV-0 execution contract §2, §10, §11, and §12.
- Consequences: future completed runs update their manifest, registry, current state, and plan status.
- Supersedes: none

## GOV-DEC-007 — Hidden reasoning is not correctness evidence

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Hidden chain-of-thought is not treated as evidence of correctness.
- Rationale: correctness must rely on inspectable artifacts, evidence, validation, and decisions rather than private reasoning traces.
- Source: supplied role prompt index and Designer/Adversary prompt contracts.
- Consequences: no private chain-of-thought is exposed or manufactured; observable rationales and results carry the audit record.
- Supersedes: none

## GOV-DEC-008 — Proportional observable trace retention

- Date: 2026-07-13
- Status: ACTIVE
- Statement: Explicit decision rationales and observable execution traces are retained proportionally.
- Rationale: traceability must support review without turning private reasoning or unlimited logging into a requirement.
- Source: GOV-0 execution contract §11 minimum decision list and prompt provenance rules.
- Consequences: manifests record known interventions, limitations, and artifacts; missing traces remain explicit.
- Supersedes: none

## GOV-DEC-009 — Kernel remains proposed through required review

- Date: 2026-07-13
- Status: ACTIVE
- Statement: The Kernel remains proposed and requires Adversary review, Enforcement analysis, and human ratification.
- Rationale: Designer completion is neither independent validation, enforceability, nor constitutional authority.
- Source: role prompt index; KGR-002 outputs; GOV-0 execution contract §11 and §12.
- Consequences: all candidate copies remain `PROPOSED_NOT_RATIFIED`; no runtime authority is inferred.
- Supersedes: none

## GOV-DEC-010 — Honest S0a–S1 regularization

- Date: 2026-07-13
- Status: ACTIVE
- Statement: S0a–S1 will be regularized honestly without fabricated retrospective evidence.
- Rationale: controls that did not exist cannot be represented as historical compliance.
- Source: KIP-07 §11; GOV-0 execution contract §11.
- Consequences: the future audit distinguishes historical contracts, real evidence, new validation, gaps, migration, and exemptions.
- Supersedes: none

## GOV-DEC-011 — S2 as first governed pilot

- Date: 2026-07-13
- Status: ACTIVE
- Statement: S2 is intended as the first governed pilot after minimum adoption requirements are met.
- Rationale: governance should be exercised in a bounded real flow only after ratification, minimum executable controls, and sufficient S0a–S1 disposition.
- Source: KIP-07 §11 and §13; GOV-0 execution contract §11.
- Consequences: GOV-9 depends on GOV-6 through GOV-8 and does not authorize S2 now.
- Supersedes: none
