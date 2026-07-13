# Open Import Questions

These questions concern repository bootstrap provenance only. They do not block preservation or KGR-003 preparation.

## IMP-Q-001 — Complete original Intake prompt

The supplied Intake prompt says its recoverable source ended during Stage 12 and that later material was reconstructed from the execution and outputs. Is a more complete byte-exact original execution prompt available?

Impact: if found, preserve it as a new raw source and register its relationship without silently replacing the current reconstructed canonical prompt.

## IMP-Q-002 — Historical execution metadata

No execution records establish the Intake platform/model/reasoning mode or the actual Designer model/reasoning setting, start times, interaction counts, or token usage.

Impact: manifests retain `unknown` or explicitly distinguish prompt intent from verified execution.

## IMP-Q-003 — Intake summary filename alias

The Designer basis records receipt of `07-intake-summary(1).md`, while the supplied Intake package and extracted source use `07-intake-summary.md`. Content authority is unambiguous, but the suffixed historical filename is not independently preserved.

Impact: the discrepancy remains a provenance note; no duplicate content is fabricated.

## IMP-Q-004 — Research-to-run linkage

Three research/process documents were supplied with the bootstrap inputs, but no execution manifest proves which Intake or Designer conversation received them directly.

Impact: they remain supporting research sources and are not asserted as run inputs.
