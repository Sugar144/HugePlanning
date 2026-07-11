# {{PROJECT_ID}}

This private repository contains all project-specific evidence, canonical data,
documents, source, and tests. The methodology at `{{METHOD_DIR}}` is read-only.

## Validate

```bash
"{{METHOD_DIR}}/scripts/validate.sh" .
```

## Launch

```bash
"{{METHOD_DIR}}/scripts/start-agent.sh" . spk-01-fixture
```

Before G0 approval, complete `docs/product/engagement.md`, replace onboarding
defaults in `project.yaml`, configure a private remote with protected `main`,
run validation, and execute the launch smoke check.
