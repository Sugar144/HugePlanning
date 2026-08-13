# Claude Code L4 Adapter

This adapter is the Claude Code execution binding for the reusable governance
core. It contains no normative governance content. Its renderer resolves the
same HugePlanning-owned configuration used by the Codex adapter and emits an
ephemeral Markdown context for an individual Claude Code session.

Use `python3 governance/tools/render_g6_b08_claude_context.py --output <dir>`.
The optional `--l7-projection <file>` accepts a B-07 projection only when its
bounded token measurement is valid. The command does not modify `CLAUDE.md`,
`.claude/`, the reusable core, adopter configuration, or canonical L5 evidence.

This is an L4 binding, not an active-instruction change. Live Claude runtime
validation passed in a post-closure addendum session; see
`../../audits/GOV-GEN-AUD-001-governance-generalization/G6/B-08/B-08-live-claude-runtime-validation-report.yaml`.
