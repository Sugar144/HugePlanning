# Rule: traceability (always loaded)

**Policy.** Every identified item uses the ID grammar defined in the
`id-and-status-conventions` rule. No artifact may reference an ID that does not
exist (**no dangling references**). Trace links are updated at defined moments,
not continuously: requirement creation (source_refs), backlog derivation
(implements/acceptance_criteria), task merge (implementation refs), release
verification (test evidence). Layer-3 documents cite layer-2 IDs; they never
restate a requirement in new normative words. `traceability.yaml` (from S6)
stores only ID-to-ID links, never text.

**Why.** The chain evidence → requirement → story/task → code → test → release
is the system's audit spine; one dangling or duplicated reference silently
breaks impact analysis and verification derivation.

**Observable violation.** A reference to a nonexistent ID; a requirement with
no `source_refs`; a document introducing a normative statement with no ID; a
merged task with no linked requirement or acceptance criterion; two artifacts
authoring the same fact in different words.
