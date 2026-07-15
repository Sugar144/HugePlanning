---
name: governance-review-packager
description: Build and inspect a bounded deterministic review bundle when material repository work is ready for review, validation evidence must travel with a change set, or a governance implementation report needs a review package. Use only within an explicit repository modification or review authorization.
---

# Governance Review Packager

Contract version: `0.1.0`.

## Workflow

1. Read all applicable repository instructions and durable status records.
2. Confirm the repository root, expected branch, base HEAD, staging expectation, authorized changed paths, output ZIP path, validation commands, dependency-version commands, and implementation/review report path. Stop if the authorization or scope is ambiguous.
3. Create or update a versioned review-bundle configuration that conforms to `governance/schemas/review-bundle-config.schema.json`. Keep phase-specific values in the configuration, never in the tool.
4. Ensure the concise implementation/review report states scope, authority limits, changed artifacts, validations, findings, bundle identity, honest status, and exact next action.
5. Run `python3 governance/tools/build_review_bundle.py --root <repository> --config <configuration> --output <external-zip>`.
6. If the command fails, inspect its reported repository, scope, path, or required-command failure. Report the failure without manufacturing success evidence.
7. If it succeeds, inspect the ZIP without extracting it into the repository. Confirm safe unique member names, sorted ordering, the configured file inventory, required command exit codes, and every `SHA256SUMS` digest.
8. Report the bundle path and SHA-256, the report path, validation results, material findings, and remaining authority gate.
9. Stop before publication unless explicit authority already covers each requested publication action.

## Output

Return a concise review handoff containing configuration, report, bundle, hash, validation status, scope status, findings, and exact next action.

## Failure handling

Treat a required validation failure, scope drift, unsafe path, repository mismatch, staging mismatch, or bundle-integrity mismatch as a failed package. Route any material defect or near miss through the repository learning contract when authorized; do not silently repair it.

## Must not

- Do not reimplement inventory, diff, ZIP, hashing, manifest, or validation execution in natural-language steps.
- Do not stage, commit, push, open a pull request, merge, release, accept risk, ratify, execute a formal run, or apply a Controller transition without separate explicit authority.
- Do not treat a generated bundle as validated, accepted, published, or operational until the corresponding evidence exists.
