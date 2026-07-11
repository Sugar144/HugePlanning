# Rule: client-data-separation (always loaded)

**Policy.** All client data — evidence, requirements, documents, code, secrets,
identities — lives exclusively in that client's repository. The methodology
repository contains zero client data, ever; its examples and fixtures use
fictitious clients only. In client sessions the methodology directory is
**read-only**: never write there, never copy client material into it, and never
pass the methodology path as a write target to any script or subprocess
(deny rules do not bind arbitrary subprocesses — `02` §6). Secrets are never
committed anywhere: local `.env` (gitignored) + `.env.example` with names only.

**Why.** Privacy, retention, and deletion obligations are per-client and
enforceable only if the client repo is the single container; the methodology is
a versioned shared product that would leak data across clients otherwise.

**Observable violation.** A client name, transcript, requirement, or secret in
any methodology path; a write (or attempted write) to the methodology directory
during a client session; a dirty methodology `git status` after a client
session; a committed `.env` or credential value in any repository.
