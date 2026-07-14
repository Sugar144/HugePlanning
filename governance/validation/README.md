# Governance Validation Evidence

This directory defines the future custody contract for durable governance validation records. Phase 2 creates no `GOV-VAL-###` record. Controller and package test output remains transient implementation evidence until a separately authorized review decides repository custody and allocates an identifier.

## Report structure

A validation report identifies the deterministic tool and version, subject identity and hash, applied validation-profile versions, ordered diagnostics, result, and authority limitation. The versioned structural contract is `governance/schemas/governance-validation-record.schema.json`.

Durable records, when separately authorized, will use monotonic IDs of the form `GOV-VAL-###` and immutable canonical JSON. Allocation must inspect existing repository records and must not reuse an ID. No identifier is reserved by this README or by transient output.

## Authority limitations

Validation establishes only that declared deterministic checks passed for the identified bytes and profile. It does not execute a governance role, decide constitutional substance, accept risk, authorize a transition, ratify or adopt the Kernel, open Enforcement Engineering, or establish operational status.

## Transient and durable evidence

CLI stdout, temporary test reports, synthetic fixture results, and external review-bundle members are transient evidence. They may support review but are not repository-custodied validation records. A durable `GOV-VAL-###` record requires explicit authorization, schema validation, a repository path, registry treatment where applicable, and review of the exact subject and profile identities.
