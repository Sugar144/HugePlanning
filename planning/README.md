# Planning corpus

How this system was planned. Nothing here is runtime: client sessions load the
methodology from the repository root (`CLAUDE.md`, `.claude/`, `schemas/`,
`scripts/`, `templates/`), never from this directory.

```text
planning/
├── baseline/   plan_director_sistema_freelance_web_asistido_por_ia.md
│               — the original V1 baseline (v0.1, Spanish). IMMUTABLE:
│               audited in v2/16, never edited. V1 plan preserved at
│               tag `plan-v1.0`.
├── v2/         the current plan ("V2 robustness"), 22 numbered files.
│               Start at 00_final_plan_index.md — it holds the reading
│               order and the file inventory.
└── history/    claude-ai-prototypes/ — the pre-V2 Claude.ai prototype
                skills and project instructions, preserved verbatim
                (R2-36). Historical prototype: not active runtime, not
                behaviorally validated. See its README for the reuse
                assessment feeding S0b/S1.
```

## How to resolve plan references

Throughout the repository (rules, CHANGELOG, scripts' comments, reports),
plan documents are cited by their two-digit number: **`NN §m` means
`planning/v2/NN_*.md`, section m** — e.g. `02 §6` is the read-only
enforcement section of `planning/v2/02_methodology_repository_design.md`.
Decision IDs: `DEC-xx` → `v2/16` (V1, frozen) · `R2-xx` → `v2/19` (V2 log,
append-only) · stage names `S0a…S9` → `v2/13` · assurance loop → `v2/22`.

Experiment and verification reports live in `reports/`, not here.
