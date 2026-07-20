<!--
Audit front matter (added at preservation time; the audit body below is
reproduced verbatim from the source and was NOT rewritten).

audit_date: 2026-07-20
repository: Sugar144/HugePlanning
tested_branch: feat/s1-discovery-interviewer
tested_head: 558431640b34dbc7738808bb055fa88d5586d923 (short 5584316)
status: read-only audit — no repository file, branch, tag, worktree or PR was
        created, modified, moved or deleted while producing it.
recommendations: NOT automatically accepted. Every recommended disposition
        below is a proposal requiring an explicit Owner decision; none was
        executed as part of the audit.
source_claude_plan: you-are-conducting-an-abstract-codd.md
preserved_by: bounded cleanup & reconciliation execution, 2026-07-20.
-->

# Auditoría de arquitectura e higiene — HugePlanning (solo lectura)

## Context

Auditoría independiente y adversarial de la arquitectura de repositorio, ramas,
worktrees y artefactos de `Sugar144/HugePlanning`. Objetivo: determinar si la
estructura actual es comprensible, consistente, mantenible, escalable a S1–S9 y
segura para agentes y humanos, e identificar material obsoleto o engañoso.

**Naturaleza del entregable.** Esta ejecución es **read-only**. No se ha creado,
modificado, movido ni borrado ningún archivo del repositorio; no se han tocado
ramas, tags, worktrees ni PRs. Este archivo de plan es el **informe de
hallazgos**. Cada disposición recomendada es una propuesta que requiere decisión
del Owner — nada se ejecuta como parte de esta auditoría.

---

## Startup verification (verificado)

| Concepto | Valor |
|---|---|
| Repo root | `/home/sugar/Documents/Huge Planning` |
| Rama actual / HEAD | `feat/s1-discovery-interviewer` @ `5584316` |
| Upstream | `origin/feat/s1-discovery-interviewer` (alineada) |
| Worktree/staging | Limpio (sin material sin commitear en riesgo) |
| Worktrees | (1) este repo → `feat/s1-discovery-interviewer`; (2) `/home/sugar/Documents/HugePlanning-governance` → `governance/kernel-designer-revision-v0.1` (limpio, `1899a3e`) |
| Default branch | `main` |
| **`main` local vs `origin/main`** | **`main` local `538523e` está 3 commits POR DETRÁS de `origin/main` `007ce7e`** (le falta el merge del PR#4) |
| Tags | `v0.1.0` (S0a), `v0.2.0` (S0b), `plan-v1.0`, `plan-v2.0` |
| PRs | Sin `gh` CLI disponible; PR#3 y PR#4 constan como *merged* en el historial. PRs abiertos: no verificables desde aquí → decisión de Owner |

**Sin bloqueos:** ningún worktree tiene material sin commitear que peligre por
comandos de inspección. Se pudo continuar.

### Inventario de ramas (relación con `main` local: ahead/behind)

| Rama | Únicos (ahead) | Falta (behind) | Clasificación |
|---|---|---|---|
| `feat/s1-discovery-interviewer` | 12 | 3 | ACTIVE_WORKSTREAM |
| `governance/kernel-designer-revision-v0.1` | 41 | 0 | ACTIVE_WORKSTREAM (worktree adjunto, sin fusionar) |
| `governance/kernel-adversary-v0.1` | 2 | 0 | MERGED en `origin/main` vía PR#4 (local desincronizado) |
| `origin/experiment/chatgpt-s0a` (solo remoto) | 1 | 30 | **UNIQUE_WORK_REQUIRES_DISPOSITION** |
| `chore/planning-assurance-organization` | 0 | 24 | MERGED_DELETE_CANDIDATE |
| `chore/product-spec-foundation` | 0 | 18 | MERGED_DELETE_CANDIDATE |
| `docs/claude-ai-prototype-baseline` | 0 | 22 | MERGED_DELETE_CANDIDATE |
| `docs/s1-scenario-task-split` | 0 | 16 | MERGED_DELETE_CANDIDATE |
| `experiment/claude-s0a` | 0 | 28 | MERGED_DELETE_CANDIDATE (arm ganador; contenido en `main`) |
| `feat/s0b-discovery-infra` | 0 | 4 | MERGED_DELETE_CANDIDATE |
| `governance/bootstrap-v0.1` | 0 | 1 | MERGED_DELETE_CANDIDATE |
| `integration/s0a-final` | 0 | 26 | MERGED_DELETE_CANDIDATE |

---

## Findings

```yaml
finding_id: F-01
classification: VERIFIED_FACT
severity: HIGH
title: governance/ es un proyecto paralelo de facto, indocumentado en main y con substancia sin fusionar
affected_surfaces:
  - README.md (main)
  - governance/ (91 files en main; 636 en governance/kernel-designer-revision-v0.1)
  - branch governance/kernel-designer-revision-v0.1 (41 commits únicos)
repository_evidence:
  - "git ls-tree main incluye governance/ (91 archivos: GOVERNANCE_MASTER_PLAN.md, CURRENT_STATE.md, DECISION_LOG.md, ARTIFACT_REGISTRY.yaml, RUNTIME_PROJECTION_MAP.yaml, runs/KGR-00x)."
  - "git show main:README.md | grep governance → sin coincidencias: el mapa del repo no menciona governance."
  - "governance/ en la rama = 636 archivos vs 91 en main → ~545 archivos de governance viven SIN FUSIONAR en una rama de 41 commits."
root_cause: "Governance se desarrolló como un segundo ciclo de vida completo (master plan, decision log, artifact registry, estado propio) dentro del mismo repo, sin una decisión de arquitectura que declare qué ES, dónde vive canónicamente y cómo se integra. No hay fuente canónica que lo describa."
current_effect: "El README describe un repo que no coincide con el contenido de main. Un humano/agente que lea el mapa no sabe que governance/ existe ni con qué autoridad. Riesgo de confundir experimental/histórico/autoritativo."
future_effect: "A S2–S9, governance como proyección de controles (RUNTIME_PROJECTION_MAP) no tiene punto de integración definido; el desfase rama↔main crece y se vuelve inmanejable."
recommended_disposition: "Owner decide una de dos: (A) adoptar governance como producto documentado de ESTE repo — actualizar README con su capa, fijar estrategia de integración rama→main, y reconciliar; o (B) separarlo a su propio repositorio proyectando controles vía contrato (RUNTIME_PROJECTION_MAP.yaml). Recomendación: evaluar (B) porque governance ya modela proyección y tiene lifecycle propio, PERO sólo si se identifica un beneficio real de ownership/release/carga — no por pulcritud."
deletion_or_migration_risk: "Alto si se fusiona a ciegas: 545 archivos + AGENTS.md raíz alterarían la superficie de runtime del cliente. No fusionar sólo para no perder trabajo."
owner_decision_required: true
```

```yaml
finding_id: F-02
classification: VERIFIED_FACT
severity: HIGH
title: El significado de rutas y la jerarquía de instrucciones cambian según la rama
affected_surfaces:
  - governance/ (presente en main, AUSENTE en feat/s1-discovery-interviewer)
  - AGENTS.md (existe SOLO en governance/kernel-designer-revision-v0.1)
repository_evidence:
  - "git ls-tree feat/s1-discovery-interviewer → NO contiene governance/ (rama cortada antes del merge de governance)."
  - "Root instruction files por rama: feat/s1 → CLAUDE.md; main → CLAUDE.md; governance branch → AGENTS.md + CLAUDE.md."
root_cause: "Ramas de larga vida por subsistema (branch-per-subsystem) sin una política de sincronización con main. La rama de runtime activa (feat/s1) y main han divergido en su top-level."
current_effect: "Un agente cargado en feat/s1 no ve governance/; uno en la governance branch ve un AGENTS.md raíz adicional. La jerarquía de instrucciones efectiva depende de qué rama esté checked out."
future_effect: "Divergencia oculta: cuando S1 se fusione a main, colisionará con governance/ y con la doble jerarquía CLAUDE.md/AGENTS.md sin un plan de resolución."
recommended_disposition: "Definir política de integración continua rama→main para subsistemas de larga vida; decidir si AGENTS.md raíz es canónico (y entonces existir en todas las ramas de runtime) o pertenece sólo a governance. Documentar la jerarquía de instrucciones única."
deletion_or_migration_risk: "N/A (política, no borrado)."
owner_decision_required: true
```

```yaml
finding_id: F-03
classification: VERIFIED_FACT
severity: MEDIUM
title: main local está 3 commits por detrás de origin/main (baseline local obsoleto)
affected_surfaces:
  - refs/heads/main (local 538523e) vs origin/main (007ce7e)
repository_evidence:
  - "git rev-list --left-right --count main...origin/main → 0 3."
  - "origin/main incluye PR#4 (governance/kernel-adversary-v0.1) y GOV-0/GOV-3; main local no."
root_cause: "El checkout local no hace fast-forward de main tras merges remotos; se trabaja desde ramas feature sin reconciliar main."
current_effect: "Cualquier cálculo ahead/behind local (incluido este informe) usa un main desincronizado; el 'main' local no es la baseline real. Riesgo de re-derivar trabajo ya en origin/main."
future_effect: "Ramas cortadas desde main local nacen ya obsoletas; conflictos de merge evitables."
recommended_disposition: "Owner/operador: git fetch + fast-forward de main local a origin/main antes de cortar ramas nuevas. Es un FF, no reescribe historia."
deletion_or_migration_risk: "Ninguno (fast-forward)."
owner_decision_required: false
```

```yaml
finding_id: F-04
classification: VERIFIED_FACT
severity: MEDIUM
title: Los estados de tarea en backlog.yaml quedan rezagados frente al trabajo commiteado (proyección sin reconciliación)
affected_surfaces:
  - product/backlog.yaml
  - CHANGELOG.md ([Unreleased])
repository_evidence:
  - "backlog.yaml: TASK-010..013 status in_review; TASK-016..019 status ready; TASK-015 status backlog."
  - "Pero existen commits: 'record Scenario 01/03/04 RESULT (TASK-016/018/019)', 'record SPK-01 evidence', y CHANGELOG dice 'Implementation complete'."
  - "README SPK-01 log registra un run 5/5 (2026-07-12) relevante a TASK-015."
root_cause: "backlog.yaml es una proyección de estado mantenida a mano, sin mecanismo de generación/reconciliación contra los commits/CHANGELOG que son la verdad. El estado de tarea vive en dos superficies que no se sincronizan."
current_effect: "Trabajo implementado y commiteado aparece como ready/in_review/backlog. Un lector no puede confiar en el estado del backlog para saber qué está hecho."
future_effect: "A escala S2–S9 el desajuste crece; la trazabilidad task→commit se vuelve poco fiable y las métricas de avance mienten."
recommended_disposition: "Definir dueño único del estado de tarea (recomendado: derivarlo/validarlo contra commits+CHANGELOG en el suite, o reconciliar en el commit que registra el RESULT). No duplicar estado sin reconciliación."
deletion_or_migration_risk: "Bajo (edición de estados con control de cambios)."
owner_decision_required: false
```

```yaml
finding_id: F-05
classification: VERIFIED_FACT
severity: MEDIUM
title: tests/ está sobrecargado — golden-artifacts/ mezcla definiciones golden con evidencia de ejecución
affected_surfaces:
  - tests/golden-artifacts/ (golden-checklist.md = definición; RESULT.md = evidencia de ejecución)
  - tests/interview-scenarios/ (definiciones de escenario)
  - tests/schema-tests/ (74 fixtures deterministas)
repository_evidence:
  - "tests/golden-artifacts/ contiene golden-checklist.md (6) y RESULT.md (sólo 3: 01,03,04)."
  - "tres semánticas bajo tests/: fixtures deterministas, escenarios de comportamiento, y golden+resultados de ejecución."
root_cause: "tests/ acumula cuatro tipos distintos (tests de implementación deterministas, definiciones de escenarios de comportamiento, definiciones golden y RESULTADOS de ejecución) sin separar definición inmutable de evidencia de corrida."
current_effect: "Evidencia de ejecución (RESULT.md) conviven con definiciones canónicas (golden-checklist.md); sólo 3/6 escenarios tienen RESULT → el gate de comportamiento está incompleto y es difícil ver qué falta."
future_effect: "A S2–S9 (test definitions vs test execution evidence, golden por stage) tests/ se vuelve un cajón sin índice; colisión entre lo canónico y lo generado por corrida."
recommended_disposition: "Separar definición de evidencia: p.ej. tests/golden-artifacts/ sólo definiciones; los RESULT.md de corrida a un espacio de evidencia de ejecución con índice. Documentar la taxonomía de tests/."
deletion_or_migration_risk: "Medio: RESULT.md son evidencia del gate — reubicar, no borrar."
owner_decision_required: true
```

```yaml
finding_id: F-06
classification: VERIFIED_FACT
severity: MEDIUM
title: origin/experiment/chatgpt-s0a es el ÚNICO contenedor de evidencia experimental única (riesgo de pérdida)
affected_surfaces:
  - origin/experiment/chatgpt-s0a (1 commit único: "feat(s0a): implement minimal runtime bootstrap")
repository_evidence:
  - "git rev-list --left-right --count main...origin/experiment/chatgpt-s0a → 30 1."
  - "Es el arm 'ChatGPT' del experimento de bootstrap S0a; el arm 'Claude' (experiment/claude-s0a) sí está contenido en main."
  - "No hay tag apuntando a ese commit."
root_cause: "El experimento comparativo S0a conservó ambos arms como ramas; sólo el arm ganador se fusionó. El arm perdedor quedó únicamente como rama remota, sin tag ni nota de archivo."
current_effect: "El valor comparativo del experimento (por qué ganó un arm) depende de una rama remota sin respaldo referencial."
future_effect: "Si alguna limpieza de ramas borra origin/experiment/chatgpt-s0a, el commit queda huérfano y recolectable → pérdida irreversible de evidencia experimental."
recommended_disposition: "ARCHIVAL_EVIDENCE_RETAIN. Antes de cualquier limpieza de ramas: taggear el commit (p.ej. tag anotado experiment/chatgpt-s0a) o referenciarlo desde reports/experiments/s0a/. NO borrar sin archivar."
deletion_or_migration_risk: "Alto si se borra sin archivar (pérdida del único ref)."
owner_decision_required: true
```

```yaml
finding_id: F-07
classification: VERIFIED_FACT
severity: LOW
title: Ocho ramas totalmente fusionadas (0 commits únicos) — candidatas a borrado local
affected_surfaces:
  - chore/planning-assurance-organization, chore/product-spec-foundation, docs/claude-ai-prototype-baseline, docs/s1-scenario-task-split, experiment/claude-s0a, feat/s0b-discovery-infra, governance/bootstrap-v0.1, integration/s0a-final
repository_evidence:
  - "Para cada una, git rev-list main...<branch> muestra 0 commits únicos (contenidas en main)."
root_cause: "Ramas feature/experiment/integration no podadas tras su merge."
current_effect: "Ruido de ramas; dificulta distinguir workstreams activos de terminados."
future_effect: "Acumulación; el README no representa qué ramas siguen vivas."
recommended_disposition: "MERGED_DELETE_CANDIDATE. Tras verificar por rama (sin worktree sucio, sin PR abierto, contenido en main): borrar rama local; decidir por separado el borrado remoto. Distinguir borrado local vs remoto vs remoción de worktree. Requiere aprobación del Owner y no reescribe historia."
deletion_or_migration_risk: "Bajo (contenido preservado en main)."
owner_decision_required: true
```

```yaml
finding_id: F-08
classification: INFERENCE
severity: LOW
title: schemas/ mezcla schemas cliente-facing con schemas product-* internos de la metodología
affected_surfaces:
  - schemas/ (product-requirements.schema.json, product-backlog.schema.json vs project/requirements/solution-context/interview-state/handoff/open-questions)
repository_evidence:
  - "schemas/ es un directorio plano; product/README.md aclara que product-* nunca se listan en methodology.lock ni se replican al cliente — la distinción vive sólo en prosa."
root_cause: "Dos audiencias de schema (runtime del cliente vs producto interno del repo) en un mismo namespace de carpeta."
current_effect: "Un agente puede confundir un schema interno con uno cliente-facing; la frontera depende de leer product/README."
future_effect: "A S2–S9 crecen ambos conjuntos; sin separación explícita aumenta el riesgo de listar por error un schema interno en el lock del cliente."
recommended_disposition: "Considerar subcarpeta (p.ej. schemas/product/) o convención de nombres + índice explícito que marque audiencia. Retener con mejor etiquetado; no es urgente."
deletion_or_migration_risk: "Bajo (reubicación con actualización de refs)."
owner_decision_required: false
```

```yaml
finding_id: F-09
classification: VERIFIED_FACT
severity: LOW
title: Artefactos locales no versionados — auditoría previa en PDF fuera del repo
affected_surfaces:
  - "Auditoría HugePlanning.pdf" (raíz; en .git/info/exclude)
  - .venv/ (auto-ignorado por su propio .gitignore)
repository_evidence:
  - "git check-ignore: 'Auditoría HugePlanning.pdf' excluido vía .git/info/exclude:8."
  - ".venv contiene su propio .gitignore ('*') → todo su contenido aparece ignorado."
root_cause: "Salida de una auditoría previa guardada sólo en disco local; entorno virtual de Python local."
current_effect: ".venv es correcto (no debe versionarse). El PDF de auditoría previa NO tiene retención en el repo ni en historia — existe sólo en esta máquina."
future_effect: "La auditoría previa se pierde si se pierde el disco; no es citable por ID/commit."
recommended_disposition: "Si la auditoría previa tiene valor de referencia, decidir un lugar de retención (reports/ o almacenamiento de respaldo del operador). .venv: sin acción. No es evidencia de repo — no tratar como autoridad."
deletion_or_migration_risk: "Ninguno."
owner_decision_required: true
```

```yaml
finding_id: F-10
classification: INFERENCE
severity: LOW
title: planning/v2 como autoridad activa y logs append-only — mantenibles hoy (sin defecto), vigilar
affected_surfaces:
  - planning/v2/ (22 archivos), planning/baseline/ (inmutable), planning/history/
  - decision logs (v2/16 DEC congelado, v2/19 R2 append-only)
repository_evidence:
  - "planning/README documenta resolución de citas NN §m y separación baseline/history/v2; frontera canónico↔histórico explícita y consistente."
root_cause: "N/A — evaluado adversarialmente; la separación planning/v2 (activo) vs baseline (inmutable) vs history (prototipos) está bien delimitada y documentada."
current_effect: "Comprensible y consistente. Ausencia de defecto material aquí."
future_effect: "Vigilar: los logs append-only (R2-xx) pueden crecer; si superan la legibilidad, considerar índice/particionado. No es problema hoy."
recommended_disposition: "Sin acción. Registrado como conclusión de 'ausencia de defecto' donde corresponde."
deletion_or_migration_risk: "N/A."
owner_decision_required: false
```

---

## Respuesta directa a los retos adversariales

1. **¿Runtime+planning+producto+governance+evidencia juntos?** Runtime/planning/
   producto conviven de forma coherente y documentada. **Governance es la
   excepción problemática** (F-01/F-02): no está integrado ni documentado.
2. **¿Separar reduce acoplamiento o crea coordinación?** Sólo governance muestra
   un beneficio real de separación (lifecycle, master plan y registry propios).
   El resto NO — separarlo sería pulcritud sin beneficio.
3. **¿`product/` engañoso?** Riesgo real de colisión de nombre con "producto del
   cliente", pero `product/README.md` lo acota con dureza (scope S0b/S1,
   nunca cliente, nunca en el lock). Aceptable con su etiquetado actual.
4. **¿`tests/` con demasiados significados?** Sí (F-05).
5. **¿`planning/v2` sigue siendo autoridad apropiada?** Sí (F-10).
6. **¿Logs append-only inmanejables?** Todavía no (F-10, vigilar).
7. **¿Estado activo duplicado?** Sí: estado de tarea (F-04) y estado de
   governance (F-01) duplicados sin reconciliación.
8. **¿Branch-per-subsystem creó divergencia oculta?** Sí (F-02, governance 41
   commits; main local 3 detrás F-03).
9. **¿El README representa cada rama activa?** No — omite governance por completo
   (F-01).
10. **¿Se optimizó auditabilidad a costa de comprensión/entrega?** Parcialmente:
    la disciplina de trazabilidad es fuerte, pero governance sin documentar y el
    backlog rezagado dañan la comprensión.

---

## Prioridad de disposiciones (para decisión del Owner)

1. **F-01 / F-02 (HIGH)** — Resolver la identidad y la estrategia de integración
   de `governance/`. Es el defecto estructural dominante.
2. **F-06 (MEDIUM, seguridad)** — Archivar/taggear `experiment/chatgpt-s0a`
   ANTES de cualquier limpieza de ramas.
3. **F-03 (MEDIUM)** — Fast-forward de `main` local a `origin/main`.
4. **F-04 / F-05 (MEDIUM)** — Reconciliar estado de backlog; separar definición
   de evidencia en `tests/`.
5. **F-07 (LOW)** — Podar las 8 ramas ya fusionadas (local, luego remoto).
6. **F-08 / F-09 / F-10 (LOW)** — Etiquetado de schemas; retención de la
   auditoría previa; vigilancia de logs.

## Verification (cómo confirmar estos hallazgos de forma independiente)

- Divergencia main: `git rev-list --left-right --count main...origin/main`.
- Governance indocumentado: `git show main:README.md | grep -i governance`;
  `git ls-tree main -- governance/ | wc -l` vs la governance branch.
- Path por rama: `git ls-tree feat/s1-discovery-interviewer` (sin governance/).
- Backlog rezagado: `grep -nE 'id:|status:' product/backlog.yaml` vs
  `git log --oneline main..feat/s1-discovery-interviewer`.
- tests/ mezcla: `git ls-tree -r --name-only HEAD -- tests/golden-artifacts/`.
- Rama única: `git rev-list --left-right --count main...origin/experiment/chatgpt-s0a`.
- Ramas fusionadas: por cada rama, `git rev-list --count main..<branch>` = 0.
