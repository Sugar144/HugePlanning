---
document_id: GOV-AUD-001-CUSTODY-001
version: 0.1.0
status: PLANNED_NOT_EXECUTED
authority: AUDIT_ARTIFACT_CUSTODY_ONLY
---

# Artifact and Custody Contract

## Canonical classes

The audit root is the planning index. Future executions live under `runs/<audit-run-id>/` and reuse the repository's formal-run semantics: exact role/mode/run identity, prospective authorization, exact prompt snapshot, hashed input manifest, declared output contract, honest status, and separate evaluation evidence. Audit runs do not replace `governance/runs/`; they are audit-program instances whose manifests must link any formal governance run machinery they reuse.

| Class | Canonical location | Mutation rule |
|---|---|---|
| Program charter, plan, status | audit root | Version prospectively; never rewrite executed evidence |
| Prompt templates | `prompts/templates/` | Planning templates only; version on correction |
| Exact scaffold prompt | `prompts/GOV-AUD-PROMPT-000-audit-program-scaffold-v0.2.0.md` | Byte-exact and immutable after commit |
| Exact instantiated pass prompt | future run `prompt/` | Preserve before execution; immutable after execution |
| Pass contracts | `passes/PASS-*/contract.yaml` | Version before execution; bound snapshot in future run |
| Input evidence | future run `input/` | Complete inventory and hashes; immutable after binding |
| Outputs | future run `output/` | No placeholder output; immutable after completed execution |
| Evaluation | future run `evaluation/` | Separate from source output; independence recorded |
| Owner decisions | `decisions/` | Append-only explicit decision records; silence is not evidence |
| Corrections | new prompt/output/run version | Never overwrite completed evidence |

## Lifecycle and custody

Local prompt lifecycle states are `TEMPLATE`, `INSTANTIATED_NOT_EXECUTED`, `EXECUTED`, `EVALUATED`, and `SUPERSEDED`. They are audit-program planning states, not changes to the global prompt-custody schema. When an instantiated prompt becomes a material execution prompt, it must also satisfy canonical `HP-PROMPT-###` custody terminology and registration before or as part of the authorized work.

The scaffold prompt has local identity `GOV-AUD-PROMPT-000/0.2.0` and canonical catalogue identity `HP-PROMPT-023/0.2.0`. Its exact text SHA-256 is `7ea731bb822d88328c26bfe69b5280a84a37153bc525f963d051fb74b6033b07`.

## Future run minimum

Before any pass begins, its run manifest must bind:

- audit ID, pass ID, run ID, role, mode, and contract version;
- exact Project Owner authorization and permitted execution count;
- exact instantiated prompt identity, bytes, and SHA-256;
- complete canonical input inventory and per-member hashes;
- declared outputs, filenames, formats, required sections, status, and validation;
- model and reasoning mode when observable, without inferring unavailable values;
- starting HEAD, target branch, allowed repository effects, stop conditions, and prohibited actions;
- separate evaluation requirements and the next Owner checkpoint.

## Authority and evidence boundary

Generated is not validated; validated is not accepted; accepted is not ratified; implemented is not operational. Operational telemetry is non-authoritative. A graph or projection is derived and regenerable. Generated evidence cannot be presented as independent evidence. Chat memory cannot substitute for repository custody.

## Corrections

A material defect in an unexecuted template or contract creates a new semantic version. A correction to an immutable completed run uses a new run/version identity that links the defective evidence, bounded correction scope, new authorization, new output contract, validation, and independent evaluation. Nothing here authorizes such a correction.
