# HugePlanning / Freelance Methodology — Capabilities

This document explains, in plain language, what the HugePlanning repository currently provides and what problem each capability solves.

HugePlanning is a versioned operating methodology for AI-assisted freelance software work. It combines planning documents with a runnable client-project bootstrap/validation layer so the method can be applied consistently instead of living only in chat history.

## How to read this document

Each capability explains **what it does**, **the problem it solves**, **an example**, **its limits**, and the **technical references** for deeper inspection.

## Capability: Create a new client repository from a controlled template

**What it does.** The methodology can generate a new client project with the required directory structure, starter governance files and a lock to the exact methodology version being used.

**Problem it solves.** Starting every freelance project manually leads to missing files, inconsistent naming and uncertainty about which methodology version the project follows.

**Example.** Running `scripts/new-client.sh ~/Clients/acme-web ACME-WEB` creates the project in a staging area, validates it, initializes Git and only then moves the completed project into the target location.

**Limits.** Bootstrapping creates a valid project shell; it does not discover the client's requirements or build the product automatically.

**Technical references.** `scripts/new-client.sh`, `templates/client-repo/`, bootstrap tests.

## Capability: Pin each client project to an exact methodology revision

**What it does.** Every generated client can record the exact HugePlanning/methodology revision it was created against.

**Problem it solves.** The methodology evolves over time. Without a lock, an old client project could silently start using new rules that did not exist when its work was planned.

**Example.** `methodology.lock.yaml` stores the exact methodology commit, so a later session can detect that the checkout has moved and warn rather than pretending nothing changed.

**Limits.** A lock records identity; it does not automatically migrate a client to a new methodology version.

**Technical references.** `methodology.lock.yaml` schema/template, `scripts/new-client.sh`, `scripts/start-agent.sh`.

## Capability: Launch an AI work session with the methodology loaded

**What it does.** The repository can start a Claude Code session from inside a client repository while exposing the methodology's instructions, rules and selected agent definition to that session.

**Problem it solves.** If every new AI session depends on the user manually pasting the operating rules, context becomes inconsistent and expensive. The launcher makes the methodology available from files instead.

**Example.** `scripts/start-agent.sh ~/Clients/acme-web client-discovery` validates the client and methodology state, then starts the configured agent in the client repository.

**Limits.** The launcher does not make the model autonomous beyond the agent's actual contract, and it does not grant permission to modify the methodology repository from a client session.

**Technical references.** `scripts/start-agent.sh`, `CLAUDE.md`, `.claude/agents/`, `.claude/rules/`.

## Capability: Protect the methodology from accidental client-session writes

**What it does.** The runtime separates the methodology repository from the client repository and tests that agent sessions can write to the client while methodology paths remain protected.

**Problem it solves.** An AI agent given both the methodology and client context could accidentally "fix" the rules themselves while trying to complete client work, changing the process mid-engagement.

**Example.** The SPK-01 smoke test verifies that a methodology write is denied while an allowed client-repository write can still succeed.

**Limits.** This protection is bounded to the configured Claude Code/runtime behavior and should be rechecked after relevant CLI changes.

**Technical references.** `scripts/spk-01-smoke-check.sh`, `.claude/` permission/rule surfaces, experiment reports.

## Capability: Represent discovery information as validated artifacts

**What it does.** The methodology defines schemas and templates for discovery-stage information such as open questions, requirements, solution context, interview state and handoff records.

**Problem it solves.** Client discovery often lives in free-form notes or chat transcripts. That makes it difficult for later agents to know which requirement is accepted, which question is still open and which facts belong to the current solution context.

**Example.** A requirement can be recorded in a schema-valid artifact with a stable ID and references to related discovery information instead of being copied repeatedly into prompts.

**Limits.** A schema-valid requirement is not automatically a correct or client-approved requirement. Semantic validation and stakeholder decisions remain separate.

**Technical references.** `schemas/`, `templates/discovery/`, `product/` and planning references for the current implemented stage.

## Capability: Validate a client repository progressively

**What it does.** `scripts/validate.sh` checks whether a client repository satisfies the methodology rules appropriate to the currently implemented stage, including required structure, lock/configuration validity, discovery artifacts and reference integrity.

**Problem it solves.** As a methodology grows, separate ad-hoc validators tend to disagree. A single progressive validator gives the project one deterministic entry point for structural checks.

**Example.** Before an agent session starts, the launcher can run `validate.sh` and refuse to proceed if required discovery registries or schema-valid artifacts are missing.

**Limits.** Deterministic validation cannot prove that the client's needs were understood correctly or that a proposed solution is good.

**Technical references.** `scripts/validate.sh`, schemas, test fixtures, `tests/run-tests.sh`.

## Capability: Derive a lightweight project status view

**What it does.** The methodology includes a status script that derives a human-readable view from the project's canonical artifacts rather than requiring the user to reconstruct progress manually.

**Problem it solves.** A structured project can still become hard to navigate if the user has to open every registry and artifact to understand where discovery currently stands.

**Example.** A user can run the status command to obtain a derived view of the client project's current recorded information.

**Limits.** The status output is a projection. It does not replace the underlying client artifacts or create new state.

**Technical references.** `scripts/status.sh`.

## Capability: Smoke-test the live Claude Code integration

**What it does.** SPK-01 exercises the real CLI integration to verify that the methodology agent resolves, skills can be invoked, rules/instructions are loaded and write boundaries behave as expected.

**Problem it solves.** A deterministic unit-test suite cannot detect every breaking change introduced by a new external CLI version. The live smoke test checks the integration contract that matters to real sessions.

**Example.** After upgrading Claude Code, the user can rerun SPK-01 before trusting the new version for client work.

**Limits.** A smoke test checks the tested integration behaviors; it does not certify every possible provider behavior or future methodology stage.

**Technical references.** `scripts/spk-01-smoke-check.sh`, SPK-01 results in `README.md` and experiment reports.

## Capability: Run a deterministic methodology regression suite

**What it does.** The repository tests scripts, schemas, fixtures and scratch-client scenarios without requiring a live model for most validation.

**Problem it solves.** A methodology change can break project generation or validation even when its documentation looks correct. Automated regression tests make those structural failures visible before release.

**Example.** `tests/run-tests.sh` builds scratch projects, validates good fixtures and confirms that intentionally invalid fixtures fail for the expected reason.

**Limits.** The suite validates encoded invariants. It does not replace live integration testing where the external agent runtime itself is part of the behavior.

**Technical references.** `tests/run-tests.sh`, `tests/`, schema fixtures.

## Capability: Version and release the methodology deliberately

**What it does.** HugePlanning uses explicit versions, a changelog and tagged releases so client projects can distinguish stable methodology changes from in-progress planning.

**Problem it solves.** If methodology rules change continuously without releases, client projects cannot know what behavior they are supposed to follow or when an upgrade is intentional.

**Example.** After tests pass, a release updates `VERSION` and `CHANGELOG.md` and creates an annotated version tag; clients remain pinned until intentionally upgraded.

**Limits.** A repository commit is not automatically a released methodology version, and an available release is not automatically adopted by every client.

**Technical references.** `VERSION`, `CHANGELOG.md`, release procedure in `README.md`.

## Capability: Preserve planning provenance separately from the active runtime

**What it does.** The repository separates the released methodology runtime from the current planning corpus, immutable baseline, historical prototypes and experiment reports.

**Problem it solves.** Without clear separation, an old prototype or future plan can be mistaken for active behavior and loaded into client sessions as if it were already implemented.

**Example.** `planning/v2/` can describe future methodology stages while the root runtime and `VERSION` identify what client sessions can actually use today.

**Limits.** A planned capability is not an implemented capability merely because it has detailed documentation.

**Technical references.** root repository map in `README.md`, `planning/`, `reports/experiments/`.

## Where exact current status lives

Use `VERSION`, `CHANGELOG.md`, the runtime paths listed in the root `README.md`, and the current planning/release documentation to distinguish implemented behavior from future methodology work. This guide explains capabilities; it does not promote planned stages into the runtime.
