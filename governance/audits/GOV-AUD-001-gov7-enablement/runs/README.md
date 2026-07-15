# Future Audit Run Custody

No audit run exists here. A future separately authorized execution uses:

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
