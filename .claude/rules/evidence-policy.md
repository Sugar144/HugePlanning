# Evidence Policy

## Policy

Evidence is append-only. Client-derived facts need resolvable `source_refs`.
Raw recordings, originals, unredacted transcripts, and contact data stay in the
gitignored `evidence-raw/`; agents consume only minimized, sanitized material in
`evidence/`. Sanitization may alias or remove identifiers but must not paraphrase
the client's statement. Corrections are new evidence events.

## Why

This preserves auditability while limiting personal data in permanent Git
history.

## Observable violation

A client fact without a source, edited historical evidence, raw evidence tracked
by Git, different raw/sanitized turn numbering, or a paraphrase presented as a
verbatim statement.
