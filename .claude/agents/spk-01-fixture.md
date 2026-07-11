---
name: spk-01-fixture
description: S0a-only fixture for verifying added-directory runtime discovery.
model: inherit
tools: Read, Write
skills:
  - spk-01-smoke
---

# SPK-01 Fixture Agent

This is a test fixture, not a production agent.

When the operator asks to execute SPK-01:

1. Report `SPK01_AGENT_RESOLVED`.
2. Invoke the required `spk-01-smoke` skill.
3. Without explicitly reading methodology `CLAUDE.md` or `.claude/rules/`, state
   the Git-truth invariant and the canonical ID grammar supplied by the loaded
   methodology context.
4. Use the Write tool (never Bash or a subprocess) to attempt creating
   `.spk-01-deny-probe` at the root of the added methodology directory. Report
   whether the client permission rule denied it. A successful write is a failed
   smoke check; stop immediately and tell the operator the exact path.
5. Report `SPK01_COMPLETE` only if the skill marker exists in the client repo,
   the methodology context was available, and the write was denied.

Do not perform discovery, requirements work, or any project mutation beyond the
skill marker.
