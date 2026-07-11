# Client Data Separation

## Policy

Client data may be written only inside that client's repository. The methodology
repository is read-only in client sessions and contains only fictitious examples.
Do not move client data into methodology rules, skills, knowledge, templates,
schemas, tests, logs, or prompts. Later-stage agents read sanitized evidence,
not `evidence-raw/`.

## Why

Repository-per-client isolation is the privacy, access, retention, and deletion
boundary.

## Observable violation

Client identifiers or materials outside the client repository, a write to the
methodology during client work, raw evidence consumed by an agent, or one
client's content appearing in another project.
