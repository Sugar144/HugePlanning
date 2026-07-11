# {{PROJECT_ID}}

Client project repository, created {{DATE}} from `freelance-methodology`
(see `methodology.lock.yaml` for the pinned version). This repository is the
**single source of truth** for the project: evidence, canonical data,
documents, code, and releases.

## Launching a work session

From the methodology repository:

```bash
"{{METHOD_DIR}}/scripts/start-agent.sh" <this-repo-path> <agent-name>
```

The launcher checks this repository (`validate.sh`), refuses a dirty
methodology checkout, exports the required environment, and starts Claude Code
with the methodology attached read-only (`--add-dir`).

## Ground rules

- `evidence-raw/` is local-only (gitignored): recordings, originals,
  unredacted transcripts. Never commit it; back it up only to the operator's
  encrypted backup location.
- Secrets never enter Git: use `.env` (gitignored); `.env.example` holds names
  only.
- Approved artifacts change only via change control (`CR-nnn` / gate records
  in `docs/handoffs/`).

## Validation

```bash
"{{METHOD_DIR}}/scripts/validate.sh" <this-repo-path>
```

Runs the methodology's progressive validator against this repository
(structure, `project.yaml`, `methodology.lock.yaml` at S0a scope).
