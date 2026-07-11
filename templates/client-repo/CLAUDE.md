# Project {{PROJECT_ID}}

This repository is the source of truth. The added methodology directory is
READ-ONLY reference: never write there, never copy client data into it.

## Session start (always)

1. Read `project.yaml` (stage, approvals, profile, language) and `methodology.lock.yaml`.
2. Run the stage's entry check before doing work (latest gate record in docs/handoffs/).
3. Never overwrite artifacts with status `approved` — use change control.
4. Never write outside this repository.

## Canonical paths

Evidence `evidence/` (sanitized; never write to `evidence-raw/`) · PRD `docs/product/PRD.md`
· Content inventory `docs/product/content-inventory.yaml` · Requirements
`docs/requirements/requirements.yaml` · Context `docs/requirements/solution-context.yaml`
· Questions `docs/requirements/open-questions.yaml` · Product backlog
`docs/backlog/product-backlog.yaml` · SDD `docs/architecture/SDD.md` · Delivery
backlog `docs/backlog/delivery-backlog.yaml` · Traceability
`docs/traceability/traceability.yaml` · Gate records `docs/handoffs/` · Releases `docs/releases/`

## Project notes

(project-specific constraints added as they arise — keep short)
