# HugePlanning — Repository Execution Contract

This file governs work **on this repository**. It is provider-neutral repository-maintenance guidance; it is not the client-facing methodology runtime that HugePlanning distributes.

Speak to the Project Owner in Spanish unless requested otherwise. Write repository artifacts, governance records, prompts, schemas, reports, commit/PR text, and technical documentation in English unless an accepted artifact intentionally uses another language.

## Repository identity and dual role

HugePlanning contains two related but distinct products:

1. the released methodology runtime consumed by client projects (`CLAUDE.md`, `.claude/`, `schemas/`, `scripts/`, `templates/`, `tests/`, `knowledge/`, `VERSION`, `CHANGELOG.md`); and
2. the repository's own product, planning, governance, research, review, and execution evidence (`product/`, `planning/`, `governance/`, `reports/`).

Do not collapse these surfaces. A repository-maintenance rule does not automatically become client methodology, and a client-runtime rule does not automatically authorize repository maintenance.

`CLAUDE.md` is a versioned client-runtime invariant surface loaded into client sessions by the established distribution mechanism. It is **not** the Claude adapter for maintaining this repository. Do not convert it to an `AGENTS.md` import, duplicate this file into it, or otherwise change its runtime role without an explicit methodology-runtime change that includes the required design, compatibility, tests, versioning, and release consequences.

A ChatGPT Project, repository, branch, worktree, execution session, client project, and methodology runtime are distinct concepts. Verify identity rather than inferring one from another.

## Durable truth and grounding

Repository state and accepted canonical artifacts are durable truth. Chat history, model memory, summaries, and generated views are working context only.

Before material repository work, resolve from the repository itself:

- exact repository/worktree, branch, HEAD, remotes, and working-tree state;
- root and applicable nested `AGENTS.md` files;
- the controlling state, plan, decision, contract, packet, or task;
- exact canonical inputs and their status;
- permitted write/effect surface, validation, publication boundary, and stop condition.

For methodology-runtime work, begin with `README.md`, `VERSION`, `CHANGELOG.md`, `planning/README.md`, and the exact controlling V2 plan/runtime artifacts. For governance work, also apply `governance/AGENTS.md`, `governance/CURRENT_STATE.md`, `governance/GOVERNANCE_MASTER_PLAN.md`, and the applicable governance contracts/run records.

If identity, state, authority, or controlling inputs are unclear, use bounded read-only discovery until resolved.

## Authority

Preserve these distinctions:

```text
design != modify
modify != commit/push
commit/push != PR
PR/review != merge/release/publication/acceptance/ratification
```

Repository access, a prepared artifact, validation PASS, roadmap order, prior work, model recommendation, or an open PR does not grant the next authority stage.

The Owner retains material authority unless an exact accepted instruction, task, contract, or governance artifact delegates a bounded operation. Once a bounded material outcome is authorized, do not manufacture additional Owner gates for routine mechanics that the controlling authority already covers. Never infer commit, push, PR, merge, release, publication, acceptance, ratification, cross-repository mutation, or formal-run execution when it is not covered.

Reserve Owner attention for material decisions: methodology/product intent, scope or requirement change, consequential architecture or policy, risk acceptance, governance adoption or constitutional decisions, canonical-state transitions, formal-run authority when required, client-runtime compatibility, release/publication, cross-project adoption, acceptance, and ratification.

Nested `AGENTS.md` files may narrow local practice but may not enlarge authority.

## Proportional governance

Use the minimum sufficient process for actual material risk. Governance exists to control risk and preserve trustworthy evidence, not to multiply ceremony.

```text
packet != session != commit != branch != PR != review != Owner decision
```

Several bounded steps may produce one coherent result and one PR when authority, evidence, context, validation, and acceptance boundaries align. Do not require a separate report, PR, independent review, or Owner approval for every small mutation merely because work was decomposed.

Formal GOV/KGR executions, constitutional decisions, independent evaluations, and other explicitly contracted governance activities may require stricter prospective authorization, custody, independence, immutability, or validation. Those controls apply because the governing contract requires them; do not generalize formal-run ceremony to unrelated routine repository maintenance.

Do not fix unrelated defects. Record them separately unless they block the authorized result.

## Context and token economy

Treat Owner attention, model context, tokens, subscription usage, model calls, source access, and repeated repository reading as constrained resources.

Use canonical artifacts as context compression. Prefer exact paths, IDs, versions, hashes, commits, manifests, registries, schemas, sections, and validators over retelling plans, kernels, reports, research corpora, or prior chats.

Read indexes/manifests and targeted sections before broad trees. Do not duplicate accepted contracts, stable methodology, or validator-enforced rules in prompts or new instruction files when a precise reference is sufficient. Prompt length is not evidence of safety.

Use deterministic scripts for exact parsing, hashing, comparison, serialization, counting, packaging, state replay, and validation. Reserve model judgment for genuinely semantic work and use the least costly capable route.

## Decomposition and prompt discipline

Choose the smallest coherent result-producing unit. Combine work sharing one objective, authority, context, write surface, validation/publication boundary, and stop. Split when transformation, authority, evidence, semantic risk, role independence, rollback, acceptance, or context burden are materially independent.

Do not split mechanically by file, command, action type, or governance artifact. For complex work, design the session topology first; fully author only the next authorized execution packet and describe later work by objective, dependency, gate, and expected result until active.

Material execution prompts must work in a clean session and contain only the task delta: objective/result; repository/ref and preconditions; active authority/contract/packet; necessary canonical references; write/effect surface; task-specific invariants and exclusions; completion/validation; publication boundary; mandatory stop; and evidence for the next gate.

Apply persistent repository and methodology rules by reference. Material-prompt custody, formal-run snapshots, and correction/versioning requirements are governed by the applicable canonical governance contract; do not create duplicate prompt-custody systems.

## Evidence, learning, and historical integrity

Preserve distinctions such as:

```text
source evidence != interpretation != proposal != accepted decision
prepared != executed != validated != accepted != ratified != operational
```

Do not rewrite historical evidence to make it conform to newer methodology. Supersede or correct prospectively according to the controlling lifecycle.

When the governance learning system applies, route material failures, near misses, Owner corrections, ambiguity, tooling gaps, or repeated cost waste through `governance/learning/README.md`. A learning record, methodology proposal, Owner decision, and active requirement are distinct classes and do not substitute for one another.

Do not silently promote an idea, lesson, research result, experiment, methodology proposal, or backlog entry into active scope or accepted methodology.

## Runtime and cross-repository boundaries

The methodology repository contains no client data. Client-session execution treats the methodology runtime as read-only according to its accepted runtime controls.

Do not modify a client repository, `book-exporter`, AKC, AET, CWG, SVP, Dopis, MyLearning, or any other repository from HugePlanning authority unless an exact accepted cross-repository task grants the bounded operation.

Changes to client-facing methodology runtime must preserve its tested distribution/read-only model and follow the applicable versioning, compatibility, validation, CHANGELOG, lock/upgrade, and release requirements. Repository-maintenance improvements do not silently alter client runtime behavior.

## Validation and completion

Declare publication-blocking checks before mutation. Validate the smallest affected surface first; broaden only when dependencies or material risk justify it.

For runtime changes, use the applicable methodology tests and smoke/compatibility checks. For governance changes, use the applicable governance validators, schemas, cross-surface checks, and exact formal-run requirements. Agent claims are not evidence.

Do not claim completion, canonicality, integration, acceptance, ratification, release, publication, operational status, or client adoption without durable evidence at the controlling revision.

Completion reports should state only: outcome; changed surfaces; validation evidence; commit/push/PR/merge/release state; blockers or residual risks; and the smallest next authorized action or Owner decision.

Stop at the next genuine material authority boundary.