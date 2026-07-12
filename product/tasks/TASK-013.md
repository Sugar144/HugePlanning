# TASK-013 — client-discovery agent (replaces stub) + SPK oracle update + close templates

Epic: EP-002 (S1) · Implements: FR-013, FR-020, FR-021
Depends on: TASK-011, TASK-012

## Goal
The production interviewer replaces the S0a stub — the single runtime switch
of S1 — with its verification oracle and close artifacts updated in the same
change.

## Files
- `.claude/agents/client-discovery.md` (full 04 §1 contract; frontmatter
  model/tools/skills per 14 §2 row 1)
- `scripts/spk-01-smoke-check.sh` (check (a) semantic evidence updated to the
  production agent's output; TEST-class change per 22 §5)
- `tests/run-tests.sh` (T12 fake-runtime oracle cases updated in the same
  commit)
- `templates/discovery/completion-report.template.md`,
  `templates/discovery/consent-record.template.md`

## Acceptance criteria (verbatim)
- FR-013-AC-01/02/03 (content rules; DoD-gated closure refusal;
  trigger→flagged upgrade)
- FR-020-AC-01 (oracle cases green against production output; live SPK-01 5/5
  before tag — executed in TASK-015)
- FR-021-AC-01 (completion-report sections per 04 §12; consent record wired to
  M0)

## Contract sources
`04` (whole file — the behavioural architecture) · `14` §2 (contract row) ·
`02` §4.3 (agents carry no procedures) · CON-003 (S1 boundary).

## Validation
Deterministic: suite green incl. updated T12 oracle cases. Behavioural:
TASK-014/015 scenarios. The stub's SPK sentinel line is retained or replaced
consciously — whichever the oracle update decides, recorded in the commit.

## Out of scope
requirements-normalization invocation at close (S2 skill; the agent's close
writes state/report only per CON-003 at S1 — the 04 §1 note that
normalization "typically runs in the same session" activates at S2).
