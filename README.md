# HugePlanning — Freelance Methodology Runtime

This repository is the versioned methodology for AI-assisted freelance web
development. S0a provides only the minimal runtime bootstrap: conventions, two
core schemas, a client-repository template, deterministic launch/validation
scripts, and the SPK-01 distribution smoke check. The V2 planning documents at
the repository root remain the design authority.

## Prerequisites

- Bash 4+
- Git 2.28+
- Python 3 with PyYAML (`python3 -c 'import yaml'`)
- Claude Code only for the live SPK-01 check and real agent sessions

## Create and validate a client repository

```bash
./scripts/new-client.sh "$HOME/Clients/Acme Web" ACME-WEB
./scripts/validate.sh "$HOME/Clients/Acme Web"
```

The target must be absent or empty. The bootstrap creates a `main` branch and
one initial commit, substitutes the project and methodology placeholders, and
prints the remaining G0 actions. It never overwrites a non-empty directory.

Before approving G0, replace onboarding placeholders in `project.yaml` and
`docs/product/engagement.md`, create the private GitHub repository, protect
`main`, and record the approval. The S0a validator checks the local structural
and schema prerequisites; it does not pretend to verify remote settings or
human/commercial facts.

## Launch an agent

```bash
./scripts/start-agent.sh "$HOME/Clients/Acme Web" spk-01-fixture
```

The launcher validates the client, refuses a dirty or lock-mismatched
methodology checkout, exports
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`, and passes this repository via
`--add-dir`. It checks the methodology again after the session.

## Run S0a tests

```bash
./tests/run-s0a-tests.sh
```

The suite checks shell syntax, schema fixtures, validator failure modes,
placeholder substitution, paths with spaces, Git initialization, overwrite
protection, dirty-methodology detection, and launcher preconditions.

## SPK-01 live smoke check

Claude Code is required. From a clean released checkout:

```bash
./scripts/new-client.sh "/tmp/SPK 01 Client" SPK-01-CLIENT
./tests/spk-01/run.sh "/tmp/SPK 01 Client"
```

Inside the launched session ask the fixture agent to execute its checklist.
Confirm all four results:

1. `SPK01_AGENT_RESOLVED` is reported.
2. The `spk-01-smoke` skill creates `spk-01-skill-marker.txt` in the client.
3. The agent states the Git-truth invariant and `<TYPE>-<NNN>` grammar without
   explicitly reading the methodology instruction files.
4. Its attempted methodology write is denied and the checkout stays clean.

Record the installed CLI version and result in the experiment/release notes.
Re-run this smoke check after every Claude Code upgrade.

## Scope and version

The current methodology version is in `VERSION`; release changes are in
`CHANGELOG.md`. S0b and later schemas, production agents, CI/CD, discovery,
requirements, design, backlog, deployment, and operations pipelines are not
implemented in this stage.
