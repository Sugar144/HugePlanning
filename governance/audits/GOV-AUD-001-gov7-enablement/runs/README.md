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

- `GOV-AUD-001-P01-R1` — PASS-01, `EXECUTED_VALIDATED_PENDING_PROJECT_OWNER_DISPOSITION`; authorization `GOV-AUD-AUTH-001` consumed exactly once; PASS-02 remains unexecuted and unauthorized.
