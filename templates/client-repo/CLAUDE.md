# Project {{PROJECT_ID}}

This repository is the source of truth. The added methodology directory is
READ-ONLY reference: never write there and never copy client data into it.

## Session start

1. Read `project.yaml` and `methodology.lock.yaml`.
2. Check the current stage and its latest gate record under `docs/handoffs/`.
3. Never overwrite an approved artifact; use change control.
4. Never write outside this repository.

## Canonical S0a paths

- Sanitized evidence: `evidence/`
- Raw local evidence: `evidence-raw/` (agents must not read or write it)
- Engagement: `docs/product/engagement.md`
- Open questions: `docs/requirements/open-questions.yaml`
- Gate records: `docs/handoffs/`

Later-stage canonical paths are introduced only when their implementing stage
lands. Do not invent missing S0b-or-later artifacts.

## Project notes

Keep project-specific constraints short and evidence-linked.
