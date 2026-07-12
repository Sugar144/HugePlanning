# TASK-015 — Execute scenario validation, bounded corrections, live SPK-01, S1 release

Epic: EP-002 (S1) · Implements: FR-019, FR-020 · Depends on: TASK-014

## Goal
S1's behavioural gate: all six scenarios pass their goldens, the live smoke
check passes against the production agent, and the release is tagged with its
evidence.

## Procedure (per 22 §1, full weight — agent runtime surface changed)
1. Run scenarios per FR-019-AC-03 protocol (contradictory + PII live-assisted;
   clear, non-technical, LITE, trigger-escalation in import mode).
2. Score each against its golden checklist — coverage and non-invention, never
   wording.
3. Classify every failing check (CODE/TEST/CONTRACT/PROCESS/ENVIRONMENT)
   before fixing; max 2 correction cycles per defect class, then re-examine
   the design contract (04), not the output.
4. Deterministic suite green twice; live SPK-01 5/5 on the installed CLI
   (record version in README log).
5. Release: CHANGELOG entry with the 22 §7 evidence set (tested commit, suite
   totals, SPK result + CLI version, clean tree, known limitations), VERSION
   bump, annotated tag (version per R2-38 sequence), push with tags.

## Acceptance criteria (verbatim)
- FR-019-AC-01/02/03/04 · FR-020-AC-01

## Validation commands
`tests/run-tests.sh` (×2) · `scripts/spk-01-smoke-check.sh <scratch-client>` ·
scenario sessions via `scripts/start-agent.sh <scratch-client> client-discovery`

## Effort note
Behavioural validation dominates (plan 13 S1: BV 10–14 fh) — budget the two
live sittings ≈1–1.5 h each plus scoring; import-mode runs are cheaper and
repeatable.

## Out of scope
S2 work of any kind; knowledge research (RES-01 blocks the first real paid
interview, not this fictitious-scenario gate — R2-32).
