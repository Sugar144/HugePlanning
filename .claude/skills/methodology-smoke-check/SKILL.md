---
name: methodology-smoke-check
description: SPK-01 fixture — confirms that methodology skills load from the --add-dir directory in a client session. Invoke when running the SPK-01 launch smoke check (02 §5, check b) or after a Claude Code upgrade.
---

# methodology-smoke-check (SPK-01 fixture)

**Purpose.** Prove skill invocation from the methodology directory (SPK-01
check b). This skill carries no methodology procedure; production skills land
at S1+ per plan `14` §3.

**Trigger.** The SPK-01 smoke check (`scripts/spk-01-smoke-check.sh`) or an
operator verifying methodology loading after a Claude Code CLI upgrade.

**Preconditions.** Running in a client-repository session launched with
`--add-dir <methodology>`; the methodology `VERSION` file is readable.

**Inputs.** None.

**Procedure.**
1. Read the `VERSION` file at the root of the added methodology directory.
2. Print, on its own line: `SPK01-SKILL-OK <contents of VERSION>`
   (e.g. `SPK01-SKILL-OK v0.1.0`).
3. Stop. Do not write any file.

**Outputs.** The sentinel line above, in the session transcript only.

**Self-checks.** The printed version matches the methodology checkout in use.

**Failure modes.** `VERSION` unreadable → print `SPK01-SKILL-FAIL` and report
the path attempted.

**Must not:** write or edit files; modify anything in the methodology
directory; be used as evidence of anything beyond skill loading.
