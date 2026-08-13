# Codex L4 Adapter

This adapter is the OpenAI Codex execution binding for the reusable governance
core. It has no normative governance content. Its renderer resolves the core
through the HugePlanning-owned configuration and emits an ephemeral JSON
context for a Codex repository session.

Use `python3 governance/tools/render_g6_b08_codex_context.py --output <dir>`.
The optional `--l7-projection <file>` accepts a B-07-generated projection and
preserves its bounded token measurement. The command does not modify the core,
the adopter configuration, or canonical L5 evidence.

This is an L4 binding, not an active-instruction change. Root `AGENTS.md` and
`CLAUDE.md` remain outside this adapter.
