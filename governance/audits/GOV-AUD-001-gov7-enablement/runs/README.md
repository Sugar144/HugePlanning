# Audit Run Custody

The completed PASS-01 and executed, validated, unaccepted PASS-02 source runs are indexed below. Future separately authorized executions use:

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
- `GOV-AUD-001-P01-R1-C3` — bounded classification and temporal-semantics correction; `GOV-AUD-001-P01-C3-IER-001` is preserved as the exact independently confirmed result. The Project Owner accepted PASS-01 as `PASS_01_ACCEPTED_COMPLETED` in `GOV-AUD-DECISION-001`.
- `GOV-AUD-001-P02-R1` — PASS-02 source execution under `GOV-AUD-AUTH-002` and exact amended prompt `GOV-AUD-PROMPT-021` / `HP-PROMPT-029`; its immutable outputs were independently reviewed in `GOV-AUD-001-P02-IER-002` with result `PASS_02_R1_CONFIRMED`. The Project Owner accepted PASS-02 and approved CHECKPOINT-A in `GOV-AUD-DECISION-003/0.1.0`.
- `GOV-AUD-001-P03-R1` — PASS-03 source execution under `GOV-AUD-AUTH-003` and exact prompt `GOV-AUD-PROMPT-031` / `HP-PROMPT-035`; nine requirements outputs are deterministically validated and an immutable review package is prepared. `GOV-AUD-001-P03-AR-001` provides prepared review execution custody only. The run is not accepted or completed, its independent adversarial review has not executed, and the review opportunity is unconsumed. PASS-04 remains unauthorized and unexecuted.
