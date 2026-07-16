# Audit Run Custody

The completed PASS-01 source run is indexed below. Future separately authorized executions use:

```text
runs/<audit-run-id>/
├── authorization/
├── input/
├── prompt/
├── output/
├── evaluation/
└── manifest.yaml
```

The run must reuse the canonical formal-run requirements in `governance/methodology/project-operating-contract.md`: prospective authorization, exact role/mode/run identity, exact prompt, hashed inputs, declared outputs, honest status, validation, and independent import/evaluation where required. Directories are created only when real custodied evidence exists; no placeholders or fake execution artifacts are permitted.

## Registered runs

- `GOV-AUD-001-P01-R1` — PASS-01 source execution; authorization `GOV-AUD-AUTH-001` consumed exactly once.
- `GOV-AUD-001-P01-R1-C1` — bounded validation-lifecycle correction; preserves the initial `141 passed / 3 failed` evidence and leaves all four source outputs byte-unchanged.
- `GOV-AUD-001-P01-R1-C2` — bounded substantive correction; its independent review is preserved under `GOV-AUD-001-P01-C2-IER-001`.
- `GOV-AUD-001-P01-R1-C3` — bounded classification and temporal-semantics correction; `GOV-AUD-001-P01-C3-IER-001` is preserved as the exact independently confirmed result. The Project Owner accepted PASS-01 as `PASS_01_ACCEPTED_COMPLETED` in `GOV-AUD-DECISION-001`; PASS-02 remains unexecuted and unauthorized.
