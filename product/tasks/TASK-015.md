# TASK-015 — Aggregate scenario results, bounded corrections, live SPK-01, S1 release

Epic: EP-002 (S1) · Implements: FR-019, FR-020
Depends on: TASK-016, TASK-017, TASK-018, TASK-019, TASK-020, TASK-021

## Goal
S1's behavioural gate: the six scenario tasks have each passed their golden,
cross-scenario defects are resolved within bounded cycles, the live smoke
check passes against the production agent, and the release is tagged with its
evidence.

## Procedure (per 22 §1, full weight — agent runtime surface changed)
1. Collect the six per-scenario evidence results (TASK-016..021); confirm each
   golden passed and each surfaced defect was classified and dispositioned.
2. Resolve cross-scenario defect classes (a failure mode seen in more than one
   scenario is one defect class, not N): max 2 correction cycles per class,
   then re-examine the design contract (04), not the output. Re-run only the
   scenarios a fix touches.
3. Classify every failing check (CODE/TEST/CONTRACT/PROCESS/ENVIRONMENT)
   before fixing.
4. Deterministic suite green twice; live SPK-01 5/5 on the installed CLI
   (record version in README log).
5. Release: CHANGELOG entry with the 22 §7 evidence set (tested commit, suite
   totals, per-scenario golden results, SPK result + CLI version, clean tree,
   known limitations), VERSION bump, annotated tag (version per R2-38
   sequence), push with tags.

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
