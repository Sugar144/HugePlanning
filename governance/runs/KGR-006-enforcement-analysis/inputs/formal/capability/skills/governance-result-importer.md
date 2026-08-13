---
name: governance-result-importer
description: Validate and import one completed formal governance result, then dry-run and optionally apply one explicitly authorized Controller transition. Use when Codex must bind an exact run, role, mode, protocol, loop, completed-output package, declared result, custody destination, counters, guards, and authority boundary without fabricating outputs, changing Kernel substance, creating a successor run, ratifying, or activating enforcement.
---

# Governance Result Importer

Contract version: `0.1.0`.

## Bind authority and identity

1. Read applicable instructions, the project operating contract, durable state and registry, run manifest, input envelope, exact run prompt, protocol, loop snapshot, package contract, and current Controller history.
2. Require explicit authority separately for import, one Controller transition, repository updates, commit, and push. Never infer approval, acceptance, ratification, risk acceptance, activation, or publication beyond named actions.
3. Record repository, branch, expected HEAD, clean-start requirement, run, role, mode, protocol/version, loop/version, package path/hash, declared result, import root, and authorization reference.
4. Stop on dirty or mismatched repository state, package drift, diagnostics, ambiguity, missing authority, conflicting durable state, exhausted guards, indeterminate counters, required semantic change, or scope drift.

## Validate before writing

Run the repository validator at `output` stage with the exact envelope, prompt, and loop snapshot:

```text
python3 governance/tools/validate_run_package.py --stage output --role <role> --package <zip> --envelope <envelope> --prompt-snapshot <prompt> --loop-snapshot <loop> --json
```

Require zero diagnostics. Use its exact inventory, SHA-256, ZIP-safety, UTF-8, strict-YAML, schema, run/role/mode/protocol/loop, result, finding, and Markdown/YAML declaration-parity facts. Never edit a completed member to make validation pass.

## Import immutable outputs

1. Copy only the exact validated members to the canonical output root without transforming bytes. Preserve existing historical artifacts and refuse an occupied formal-output target.
2. Run the same tool at `import` stage with `--import-root <canonical-output-root>` and require zero diagnostics.
3. Preserve durable validation evidence containing the package hash, inventory and member hashes, identity bindings, result, diagnostics, authority limit, and byte-identity result. Validation is not acceptance, transition, ratification, or operation.

## Dry-run and apply at most one transition

1. Create a deterministic Controller import request that references the validated package evidence, exact imported role result, current active-state evidence, and blocking-finding facts. Do not invent an execution event or use synthetic fixture fields.
2. Run `apply_loop_transition.py import` without `--apply`. Compare the zero-diagnostic proposal against `GOV-PROTOCOL-002`, `GOV-LOOP-001`, replayed Controller history, current state, declared result, counters, limits, guards, and constitutional authority boundaries.
3. Apply only when the dry-run is unambiguous, follows directly from the result, changes no methodology or Kernel semantics, and explicit authority names the transition. Invoke the same command once with `--apply --authorization-ref <reference>`.
4. Validate the created immutable transition record, replay the resulting history, and confirm exactly one source-run record. Never apply more than one transition or create a successor run.

## Reconcile durable evidence

Update only authorized prospective run status, registry/index entries, current state, plan status, validation evidence, generated views, prompt custody, and review evidence. Preserve the distinctions among completed role output, validated package, imported custody, Controller transition, acceptance, ratification, and operation.

Keep Kernel status `PROPOSED_NOT_RATIFIED`, human ratification unchanged, and Enforcement Engineering closed unless an existing contract and separate competent authorization explicitly produce another state. This skill cannot modify Kernel substance, accept risk, ratify, activate Enforcement Engineering, open a pull request, merge, tag, release, or deploy.

## Report

Return a concise completion or blocker report with repository identity; package and import validation; declared result; dry-run and applied transition facts; counters and guards before/after; durable statuses; validation; learning/session review; review bundle; publication state; and exact next action.
