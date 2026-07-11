# Rule: evidence-policy (always loaded)

**Policy.** Evidence is append-only. Every recorded fact, requirement, or
classification carries a `source_refs` entry resolving to evidence (e.g.
`interview:client-discovery-01#turn-24`). Corrections are new turns or new
records — existing evidence is never rewritten retroactively. PII is minimized:
only what a requirement needs is recorded.

**Raw/sanitized split (R2-03).** Raw sensitive evidence (recordings, original
attachments and email exports, unredacted transcripts) lives only in the
gitignored `evidence-raw/` directory of the client repo — never committed,
backed up only to the operator's encrypted backup location. Committed evidence
in `evidence/` is sanitized: identifiers are aliased or removed (third-party
names → roles, contact data removed), statements are **never paraphrased**, and
turn numbering is identical to the raw counterpart so `#turn-nnn` anchors
resolve. Sanitized files carry `raw_ref` plus the SHA-256 of their raw
counterpart. Agents consume sanitized evidence only; reading raw evidence is a
manual, operator-only act.

**Why.** Traceability requires anchors that resolve; privacy law (erasure)
forbids raw PII in Git history; paraphrase would silently distort what the
client actually said.

**Observable violation.** A fact without `source_refs`; an edit that changes
the text of an existing evidence file; personal contact data, recordings, or
unredacted transcripts inside a committed path; a sanitized transcript whose
turn numbering differs from its raw counterpart; an agent-generated artifact
citing `evidence-raw/`.
