# freelance-methodology — invariants

This directory is the **methodology repository**: it defines *how* work is done.
It is loaded read-only into client sessions via `--add-dir`. It contains zero
client data, ever. (Full design: `02_methodology_repository_design.md`.)

## Invariants (never violated)

1. **Git is truth.** Anything not committed to a repository does not exist.
2. **Four information layers, strict precedence:** evidence → canonical data →
   human documents → operational views; on conflict the higher layer wins and
   the conflict is recorded, never resolved silently.
3. **Never convert inference to fact.** Unconfirmed statements stay marked as
   assumptions or open questions with their source; only evidence or explicit
   approval upgrades them.
4. **Stable IDs, never renumbered.** Every identified item keeps its ID forever;
   IDs are never reused, renamed, or compacted.
5. **Agents draft, humans approve.** No gate is auto-approved; agents produce
   `draft` statuses and stop at their completion criteria.
6. **No client data outside the client repository.** The methodology repo and
   its examples contain fictitious material only.
7. **The methodology is read-only in client sessions.** Never write here, never
   take this path as a write target of any script run in a client session.
8. **Consult `knowledge/INDEX.md` before improvising method.** If a procedure or
   reference exists, use it; do not invent parallel method on the fly.
9. **Validate structured artifacts against `schemas/` before declaring done.**
   A structured artifact that does not pass its locked schema is not finished.
10. **Approved artifacts change only via change control.** Supersede, don't
    rewrite; append-only records keep history.

Anything longer than these invariants belongs in `.claude/rules/`, skills, or
knowledge — not here.
