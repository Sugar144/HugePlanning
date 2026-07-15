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

## GOV-DEC-012 — GOV-0 acceptance and GOV-3 readiness

- Date: 2026-07-14
- Status: ACTIVE
- Statement: The Project Owner accepts the reviewed GOV-0 repository bootstrap, completing GOV-0 and making GOV-3 `READY_TO_START` while KGR-003 remains `NOT_STARTED`.
- Rationale: GOV-0 bootstrap head `4dfe8e8fb2fc4f5a6b1e857c64112886789242d8` completed human review and was merged through PR #3 into `main` as merge commit `538523eed50a0f36fd51b99c3701e354ebd85146`.
- Source: Project Owner post-merge state-transition instruction; PR #3 and merge commit `538523eed50a0f36fd51b99c3701e354ebd85146`.
- Consequences: GOV-0, GOV-1, and GOV-2 are `COMPLETED`; GOV-3 may begin only through a separate execution of the recorded KGR-003 prompt and seven unchanged inputs. This acceptance is not Kernel ratification, does not start human ratification, and does not design or implement enforcement.
- Supersedes: none

## GOV-DEC-013 — Versioned Kernel Designer input modes and revision provenance

- Date: 2026-07-14
- Status: ACTIVE
- Statement: Kernel Designer executions must select an explicit input mode: a Kernel Intake package starts `INITIAL_DESIGN`, while a Kernel Adversary package starts `ADVERSARIAL_REVISION`. The workflow must be selected by formal run inputs rather than inferred from informal chat context.
- Rationale: Initial design and adversarial revision have materially different inputs, responsibilities, gates, and outputs. Durable, inspectable provenance requires each workflow to have its own versioned protocol and formal package identity; chat memory alone is insufficient.
- Source: Project Owner KGR-004 preparation instruction dated 2026-07-14.
- Consequences: Each materially different Designer workflow receives an independently versioned protocol. Historical executed prompts remain immutable. A new loop preserves the earlier run and its contract, creates a new run record, and records all formal inputs without overwriting or retroactively modifying prior execution history. KGR-004 therefore uses `ADVERSARIAL_REVISION` and preserves the exact KGR-002 prompt and proposal. This is a governance-process and provenance decision, not Kernel ratification, constitutional authority, independent validation, Enforcement Engineering authorization, or adoption.
- Supersedes: none

## GOV-DEC-014 — Bounded and versioned Kernel Design Closure Loop

- Date: 2026-07-14
- Status: ACTIVE
- Statement: Independent closure of a proposed Kernel revision uses the bounded, versioned `GOV-LOOP-001` Kernel Design Closure Loop, initially at version `0.1.0`.
- Rationale: Closure requires independent Designer and Adversary roles, deterministic routing, explicit finding identity, finite repetition guards, and immutable run history. These constraints prevent Designer self-validation, Adversary mutation of the Kernel, Controller design decisions, indefinite remediation/review ping-pong, and authority inflation.
- Source: Project Owner approval of the Kernel Design Closure Loop blueprint dated 2026-07-14.
- Consequences:

  ```yaml
  loop:
    id: GOV-LOOP-001
    initial_version: 0.1.0

  guards:
    maximum_designer_remediation_runs: 2
    maximum_targeted_closure_runs: 3

  finding_identity:
    reopened_findings_preserve_original_id: true
    reopened_findings_add_reopen_event: true
    regression_findings_receive_new_id: true
    regression_relationship_required: REGRESSION_OF
    genuinely_new_findings_receive_new_id: true
    discovered_in_run_required: true

  history:
    completed_runs_are_immutable: true
    completed_outputs_are_immutable: true
    process_changes_require_a_new_version: true
    historical_results_are_not_rewritten_to_fit_new_processes: true
  ```

  Only Controller-validated completed runs consume the explicit `completed_targeted_closure_runs` and `completed_designer_remediation_runs` counters. Package-conflicted, paused, interrupted, or invalid attempts without a valid completed run consume no iteration or formal output set. The Adversary applies one ordered substantive-result matrix and reports exactly one result; the deterministic Loop Controller validates import, increments counters, evaluates limits and cross-run guards, and records the transition. `CLOSURE_CONFIRMED` records only configured independent adversarial closure and is not ratification or adoption.
- Authority boundary: This decision is governance methodology only. It does not revise the Kernel, close KGR-003 findings, execute targeted closure, authorize Enforcement Engineering, or ratify or adopt the Kernel.
- Supersedes: none

## GOV-DEC-015 — Phase 1 instruction and professional-learning foundation

- Date: 2026-07-14
- Status: ACTIVE
- Statement: Adopt the approved reduced Phase 1 governance tooling architecture for local implementation of a durable instruction hierarchy, canonical operating contract, professional failure-and-learning records, minimal deterministic learning tooling, and four initial GOV-4 learning records.
- Rationale: Durable learning, honest metrics, deterministic record validation, and explicit operating boundaries are required before later Controller implementation. The Project Owner explicitly authorized local repository modifications, tests, validation, and review artifacts for this bounded phase.
- Source: Project Owner Phase 1 implementation authorization dated 2026-07-14 and repository-custodied architecture report `governance/reviews/phase-1-instructions-learning/architecture-report-v0.1.0.md` (`HP-ARCH-GOV-TOOLING-001` v0.1.0), original source SHA-256 `bd4451f4407197f292b19c948ee90587cf77b9217ed86ea19c98c38ff29959e1`.
- Consequences: Root and governance instructions reference a canonical operating contract; material failures use schema-validated base records and append-only events; deterministic learning commands are dry-run first; historic evidence and missing metrics are not reconstructed; the initial four records are `CORRECTED` pending preventive-control validation. Automatic category summarization and CI integration are deferred.
- Authority boundary: This decision does not execute KGR-005, advance GOV-4, implement the Controller or closure-loop runtime, open Enforcement Engineering, accept risk, ratify or adopt the Kernel, begin human ratification, or authorize commit, push, PR, merge, tag, release, deployment, or publication.
- Supersedes: none

## GOV-DEC-016 — Minimum GOV-5 scope and complete routing disposition

- Date: 2026-07-15
- Status: ACTIVE
- Statement: Prepare one minimum-scope KGR-006 Enforcement Engineer analysis contract for the current single-user Project Owner context, preserving future portability and separability constraints without implementing commercial functionality. Account for all 20 canonical KGR-004 lower-layer routes; classify Historical repository audit and S1 regularization as `NOT_APPLICABLE_TO_GOV_5_EXECUTION` and route it to GOV-8 with explicit justification.
- Rationale: GOV-5 must expose practical clause implications and recommend the smallest later GOV-7 package while avoiding premature controls, provider testing, historical regularization, or platform design. The canonical source contains 20 routes even though the historical scope review reported 19.
- Source: Project Owner GOV-5 contract-preparation instruction and routing disposition preserved as `HP-PROMPT-011/0.1.0` and `HP-PROMPT-012/0.1.0`.
- Consequences: KGR-006 may be prepared with strict seven-clause and 20-route coverage, trigger-gated specialists, analysis-only scalability constraints, and a separate evaluation handoff. GOV-5 remains unexecuted; GOV-8 remains unperformed.
- Authority boundary: This decision does not execute GOV-5, open Enforcement Engineering, perform independent evaluation, accept risk, ratify, implement GOV-7, perform GOV-8/GOV-9, modify Kernel/Controller/product code, open a PR, merge, or release.
- Supersedes: none
