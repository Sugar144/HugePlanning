# Metodología paso a paso para definir y desarrollar el Kernel de HugePlanning con IA

**Versión:** 0.1  
**Estado:** Guía operativa  
**Propósito:** Ayudar a definir, revisar, ratificar e implementar el kernel de HugePlanning de forma rigurosa, gradual y compatible con una forma de trabajo que reduzca sobrecarga cognitiva, ambigüedad y pérdida de contexto.

---

# 0. Cómo utilizar este documento

Este documento no debe leerse ni ejecutarse de una sola vez.

Está diseñado para trabajar así:

```text
Una fase
→ un objetivo
→ un artefacto
→ una revisión
→ una decisión
→ descanso o siguiente fase
```

No se recomienda mantener abiertas varias fases simultáneamente.

## Regla operativa principal

> **Nunca trabajes en más de una pregunta constitucional activa a la vez.**

Ejemplo:

```text
Pregunta activa:
¿Quién puede modificar el kernel?

No trabajar todavía en:
- modelos;
- Skills;
- loops;
- estructura de carpetas;
- permisos de producción;
- políticas de contexto.
```

## Estados permitidos para cada paso

```text
DONE
→ El resultado cumple los criterios.

BLOCKED
→ Falta información o una decisión.

REVISE
→ Existe resultado, pero necesita corrección.

DEFERRED
→ Se pospone de forma consciente.

REJECTED
→ La propuesta no se acepta.
```

No debe existir un estado ambiguo como:

```text
“Más o menos terminado”
```

---

# 1. Por qué el kernel es difícil

El kernel no es simplemente una lista de reglas.

Es la capa de mayor autoridad de HugePlanning.

Debe definir:

- quién puede decidir;
- qué información tiene autoridad;
- qué salidas de IA pueden convertirse en estado canónico;
- cómo se valida el progreso;
- cuándo debe detenerse un agente;
- cuándo se requiere aprobación humana;
- cómo puede HugePlanning modificarse a sí mismo;
- y cómo se modifica el propio kernel.

Por eso definirlo requiere juicio, pero no es necesario resolverlo todo al mismo tiempo.

## Idea tranquilizadora

No debes crear desde el inicio:

- un workflow automático;
- siete agentes;
- muchos hooks;
- una constitución perfecta;
- una política completa para todas las fases;
- ni una arquitectura definitiva.

Para la primera versión es suficiente:

```text
1 diseñador asistido por IA
1 revisor adversarial
1 revisor de enforcement
tú como autoridad de ratificación
```

Estos tres roles pueden ser **tres chats separados**.

No necesitan ser agentes permanentes dentro de HugePlanning.

---

# 2. Diferencia entre pase, rol y agente

## Pase

Una etapa de trabajo:

```text
analizar riesgos
proponer invariantes
redactar cláusulas
intentar romper cláusulas
diseñar enforcement
```

## Rol

La perspectiva adoptada durante un pase:

```text
diseñador constitucional
crítico adversarial
ingeniero de enforcement
revisor de minimalidad
```

## Agente

Una implementación concreta con:

- instrucciones;
- contexto;
- herramientas;
- modelo;
- memoria;
- límites.

## Regla

> **Todo agente ejecuta un rol, pero no todo rol necesita convertirse en un agente.**

Para la versión `v0.1` del kernel:

```text
Rol
→ chat separado

No:
Rol
→ agente permanente
```

---

# 3. Arquitectura mínima del proceso

```text
Bloque A — Descubrimiento
Bloque B — Formalización
Bloque C — Ataque y revisión
Bloque D — Enforcement y ratificación
```

## Bloque A — Descubrimiento

Produce:

```text
hazard-register.yaml
invariant-candidates.yaml
```

## Bloque B — Formalización

Produce:

```text
kernel-draft.md
kernel-clauses.yaml
```

## Bloque C — Ataque y revisión

Produce:

```text
kernel-review.md
adversarial-scenarios/
```

## Bloque D — Enforcement y ratificación

Produce:

```text
enforcement-map.yaml
kernel-v0.1.md
```

---

# 4. Organización recomendada de chats

## Chat 1 — Kernel Designer

Responsabilidades:

```text
identificar riesgos
→ derivar invariantes
→ clasificar reglas
→ redactar cláusulas candidatas
```

No debe aprobar el kernel.

## Chat 2 — Kernel Adversary

Responsabilidades:

```text
buscar contradicciones
→ encontrar ambigüedades
→ detectar gaming
→ crear escenarios de fallo
→ señalar reglas ausentes
```

No debe reemplazar automáticamente el kernel.

Debe entregar hallazgos.

## Chat 3 — Enforcement Engineer

Responsabilidades:

```text
asignar mecanismos de enforcement
→ detectar cláusulas imposibles de aplicar
→ separar reglas técnicas y humanas
→ proponer evidencia observable
```

## Tú — Ratification Owner

Responsabilidades:

```text
aceptar
reformular
mover a política
posponer
rechazar
ratificar
```

Tu función no es redactar todo, sino decidir si una regla representa realmente tu intención.

---

# 5. Principios de accesibilidad cognitiva

Este apartado busca reducir:

- saturación;
- parálisis por análisis;
- pérdida de hilo;
- hiperfoco excesivo;
- acumulación de decisiones abiertas;
- dificultad para reanudar;
- ambigüedad.

## 5.1. Una sola pregunta activa

Cada sesión debe tener una pregunta principal.

```text
Sesión:
Definir los peligros de autocertificación.

No:
Definir todo el kernel.
```

## 5.2. Máximo de decisiones por sesión

Recomendación:

```text
1 decisión importante
o
3 decisiones pequeñas
```

Cuando se alcance el límite:

```text
cerrar sesión
actualizar estado
descansar
```

## 5.3. Externalizar la memoria

Guardar siempre:

```text
current-state.md
decision-log.md
open-questions.md
next-action.md
```

## 5.4. Finales visibles

Cada sesión termina con:

```text
Qué se hizo
Qué se decidió
Qué queda pendiente
Cuál es el siguiente paso exacto
```

## 5.5. Trabajar por lotes

```text
Lote 1:
autoridad y autoevolución

Lote 2:
estado y trazabilidad

Lote 3:
evaluación y finalización

Lote 4:
seguridad y permisos
```

## 5.6. Separar descubrimiento y decisión

```text
Primero:
recoger opciones

Después:
comparar

Finalmente:
decidir
```

## 5.7. Stop rule personal

Detener una sesión cuando:

- ya no distingues qué regla revisas;
- comienzas a abrir temas nuevos;
- lees varias veces el mismo texto;
- quieres rehacer todo desde cero;
- aumentan las preguntas abiertas;
- la tarea se vuelve emocionalmente pesada;
- llevas demasiado tiempo sin cerrar un artefacto.

Estado recomendado:

```text
PAUSED — cognitive load
```

No es fracaso.

---

# 6. Metodología completa: KDRM

```text
K0 — Mandato
K1 — Autoridad y confianza
K2 — Peligros y fallos
K3 — Invariantes
K4 — Estratificación
K5 — Cláusulas
K6 — Enforcement
K7 — Validación adversarial
K8 — Ratificación y enmienda
```

---

# 7. K0 — Definir el mandato

## Objetivo

Definir qué es el kernel y qué autoridad tiene.

## Pregunta principal

```text
¿Qué debe gobernar el kernel de HugePlanning?
```

## La IA ayuda a

- detectar ambigüedades;
- proponer un charter;
- señalar límites;
- distinguir kernel y políticas.

## Artefacto

```text
kernel-charter.md
```

## Plantilla

```yaml
kernel:
  name: HugePlanning Meta-Kernel

  purpose: >
    Govern the design, construction, evaluation and evolution
    of HugePlanning.

  applies_to:
    - humans
    - agents
    - workflows
    - evaluation systems
    - project artifacts
    - self-hosting operations

  highest_authority_over:
    - policies
    - phase contracts
    - agent definitions
    - workflows
    - release decisions

  ultimate_owner:
    type: human
    role: project_owner

  conflict_resolution:
    rule: higher_authority_wins
```

## Criterio DONE

- El propósito cabe en un párrafo.
- Está claro a quién se aplica.
- Está clara la autoridad final.
- Está claro qué no pertenece al kernel.

## Prompt

```text
Actúa como diseñador constitucional de HugePlanning.

Tu tarea es redactar únicamente el mandato del kernel.
No redactes todavía cláusulas concretas.

Determina:
1. Qué gobierna.
2. A qué actores y componentes se aplica.
3. Qué autoridad tiene.
4. Quién conserva la autoridad final.
5. Qué queda fuera.

Entrega:
- borrador breve;
- ambigüedades;
- decisiones que necesito tomar;
- versión YAML.

No avances a riesgos, invariantes ni enforcement.
```

---

# 8. K1 — Mapear autoridad y confianza

## Objetivo

Determinar quién puede hacer qué.

## Actores iniciales

- propietario humano;
- agente principal;
- subagentes;
- evaluadores;
- scripts;
- CI;
- GitHub;
- modelos;
- MCP;
- servicios externos;
- entornos.

## Artefacto

```text
authority-matrix.yaml
```

## Plantilla

```yaml
actor:
  id: implementation-agent

  may:
    - modify_branch
    - run_tests

  may_not:
    - merge_to_main
    - change_release_policy
    - modify_kernel
    - access_production

  outputs_are:
    - provisional_until_validated

  accountable_to:
    - workflow_orchestrator
    - human_gate
```

## Matriz simple

| Acción | Agente | Script | Evaluador | Humano |
|---|---:|---:|---:|---:|
| Proponer arquitectura | Sí | No | Sí | Sí |
| Aprobar arquitectura | No | No | Recomienda | Sí |
| Ejecutar tests | Sí | Sí | Sí | Sí |
| Cambiar release policy | No | No | No | Sí |
| Proponer enmienda | Sí | No | Sí | Sí |
| Aprobar enmienda | No | No | No | Sí |

## Criterio DONE

- Todos los actores críticos aparecen.
- Cada acción importante tiene autoridad definida.
- Nadie puede proponer, ejecutar, evaluar y aprobar sin control.

## Prompt

```text
A partir del kernel charter, crea un mapa de autoridad.

No diseñes agentes todavía.
Describe actores abstractos y capacidades.

Para cada actor indica:
- qué puede hacer;
- qué no puede hacer;
- qué produce;
- quién lo supervisa;
- qué resultados son provisionales;
- qué acciones requieren gate.

Detecta conflictos de intereses.
Entrega una matriz y un YAML.
```

---

# 9. K2 — Analizar peligros

## Objetivo

Descubrir cómo HugePlanning podría parecer que funciona mientras pierde control.

## Categorías

### Autoridad

- agente cambia su criterio;
- implementador elimina tests;
- workflow amplía permisos;
- cambio crítico sin gate.

### Epistemología

- inferencia registrada como hecho;
- resumen sustituye a la fuente;
- restricción perdida;
- evidencia débil tratada como definitiva.

### Estado

- dos fuentes canónicas;
- fase avanza sin precondiciones;
- `COMPLETE` en vez de `BLOCKED`;
- estado reconstruido incorrectamente.

### Autoevolución

- sistema rebaja tests;
- modifica kernel;
- acepta regresión;
- añade complejidad sin evidencia.

### Seguridad

- permisos excesivos;
- secretos expuestos;
- MCP malicioso;
- deploy accidental.

## Artefacto

```text
hazard-register.yaml
```

## Plantilla

```yaml
hazard:
  id: HAZ-AUTH-001
  title: Self-modification of acceptance criteria

  scenario: >
    An implementation agent is blocked by a release check and
    modifies the check to permit its own output.

  impact:
    - false_acceptance
    - loss_of_governance

  severity: critical

  candidate_property: >
    An executor must not modify the criteria used to evaluate
    its current execution.
```

## Criterio DONE

- Existen peligros en todas las categorías.
- Cada peligro describe escenario, impacto y propiedad candidata.
- Todavía no se han convertido todos en reglas.

## Prompt

```text
Actúa como analista de riesgos constitucionales.

Busca formas en las que HugePlanning pueda:
- parecer correcto sin serlo;
- perder intención;
- certificarse a sí mismo;
- degradar criterios;
- perder trazabilidad;
- avanzar sin evidencia;
- exceder permisos;
- ocultar bloqueos.

No propongas todavía el kernel definitivo.

Entrega peligros por:
escenario, impacto, severidad, causa y propiedad preventiva candidata.
```

---

# 10. K3 — Derivar invariantes

## Objetivo

Convertir peligros en propiedades duraderas.

```text
Procedimiento:
Ejecutar test.sh.

Invariante:
Ningún cambio se acepta sin evidencia de validación.
```

## Preguntas

1. ¿Qué propiedad impediría el peligro?
2. ¿Debe cumplirse siempre?
3. ¿Es independiente de herramientas?
4. ¿Seguiría válida con otro modelo?
5. ¿Pertenece al kernel o a una política?

## Artefacto

```text
invariant-candidates.yaml
```

## Plantilla

```yaml
invariant:
  id: INV-EVAL-001

  statement: >
    An executor cannot unilaterally control the criteria,
    mechanism and final acceptance of its own output.

  prevents:
    - HAZ-AUTH-001
    - HAZ-EVAL-003

  portability:
    model_independent: true
    tool_independent: true

  candidate_level:
    - constitutional
```

## Criterio DONE

- Cada invariante evita uno o más peligros.
- Está formulado como propiedad.
- Se ha clasificado provisionalmente.

## Prompt

```text
A partir del hazard register, deriva invariantes.

Para cada uno:
- escribe una propiedad estable;
- indica qué peligros previene;
- explica si es independiente de modelos y herramientas;
- clasifícalo como kernel, política o procedimiento candidato.

No redactes todavía lenguaje MUST/SHOULD.
```

---

# 11. K4 — Estratificar reglas

## Niveles

### A — Constitución

Muy estable.

### B — Políticas

Generales, revisables.

### C — Estándares

Formatos comunes.

### D — Procedimientos

Pasos operativos.

### E — Configuración

Valores concretos.

## Ejemplo

```text
Kernel:
Todo loop DEBE tener límites.

Política:
Los loops deben limitarse por turnos,
progreso y presupuesto.

Configuración:
Máximo de 6 iteraciones.
```

## Artefacto

```text
rule-classification.yaml
```

## Test de clasificación

Una regla es candidata a kernel si:

- protege una propiedad esencial;
- afecta muchas fases;
- sobrevive a cambios tecnológicos;
- define autoridad, verdad, seguridad o legitimidad;
- no es configuración;
- no es preferencia;
- no debería cambiar durante una tarea ordinaria.

## Criterio DONE

- Ninguna configuración está en el kernel.
- Las políticas están separadas.
- El kernel candidato sigue pequeño.

## Prompt

```text
Clasifica cada invariante en:
A Constitución
B Política
C Estándar
D Procedimiento
E Configuración

Explica:
- por qué;
- el riesgo de colocarlo demasiado alto;
- el riesgo de colocarlo demasiado bajo.

Sé estricto: el kernel debe ser mínimo.
```

---

# 12. K5 — Redactar cláusulas

## Objetivo

Convertir invariantes aceptados en reglas normativas.

## Lenguaje

- `DEBE`;
- `NO DEBE`;
- `DEBERÍA`;
- `PUEDE`.

## Plantilla

```yaml
kernel_clause:
  id: K-EVAL-001
  title: Separation of evaluation

  normative_statement: >
    An executor MUST NOT unilaterally control the criteria,
    mechanism and final acceptance of its own critical output.

  rationale: >
    Self-evaluation can reproduce the assumptions and incentives
    of the generator.

  scope:
    - critical_outputs
    - release_decisions

  protected_properties:
    - independent_validation
    - non_self_certification

  violations:
    severity: constitutional
    effect: block

  exceptions:
    allowed: false
```

## Test de calidad

Una cláusula debe ser:

- breve;
- normativa;
- portable;
- observable;
- justificada;
- difícil de explotar literalmente;
- sin detalles tecnológicos temporales.

## Criterio DONE

- Cada cláusula tiene ID.
- Tiene rationale.
- Tiene alcance.
- Tiene severidad.
- El kernel inicial contiene aproximadamente 10–20 cláusulas.

## Prompt

```text
Convierte únicamente los invariantes constitucionales
en cláusulas normativas.

Usa DEBE, NO DEBE, DEBERÍA o PUEDE.

Incluye:
- ID;
- título;
- declaración normativa;
- rationale;
- alcance;
- propiedad protegida;
- severidad;
- excepciones.

No añadas ideas nuevas sin marcarlas como propuestas.
```


# 13. K6 — Diseñar enforcement

## Objetivo

Definir cómo se aplica o detecta cada cláusula.

## Tipos

### Hard

La acción es imposible.

### Blocking

Puede intentarse, pero no aceptarse.

### Detective

Se detecta y registra.

### Advisory

Se advierte.

### Human

Requiere decisión humana.

## Matriz

| Regla | Mecanismo |
|---|---|
| Formato | Schema |
| Dependencia | Architecture test |
| Permiso | Sandbox |
| Estado | State machine |
| Release | CI gate |
| Independencia | Workflow separation |
| Decisión estratégica | Human gate |
| Trazabilidad | IDs + Git |

## Artefacto

```text
enforcement-map.yaml
```

## Plantilla

```yaml
enforcement:
  clause: K-EVAL-001

  controls:
    - type: workflow_separation
      strength: blocking

    - type: human_gate
      applies_when:
        severity: critical

  evidence:
    - evaluator_run_id
    - approval_record

  failure_effect:
    - block_acceptance
```

## Criterio DONE

- Cada cláusula tiene enforcement o auditoría.
- Las cláusulas no verificables se reformulan o mueven.
- Las críticas tienen controles bloqueantes o humanos.

## Prompt

```text
Actúa como ingeniero de enforcement.

Para cada cláusula:
- determina qué puede imponerse por código;
- qué requiere permisos;
- qué necesita test;
- qué necesita auditoría;
- qué exige gate humano;
- qué no es verificable.

No cambies el sentido de las cláusulas.
Marca las que sean demasiado vagas.
```

---

# 14. K7 — Revisión adversarial

## Objetivo

Intentar romper el kernel.

## Pruebas

### Ambigüedad

Dos interpretaciones diferentes.

### Conflicto

Dos cláusulas ordenan cosas incompatibles.

### Gaming

Cumplir literalmente y violar la intención.

### Crisis

Fallo de CI, pérdida de contexto, secretos, estado corrupto.

### Self-hosting

El sistema intenta modificar la regla que lo bloquea.

### Minimalidad

Eliminar una cláusula y observar si realmente era necesaria.

### Estabilidad

Cambiar modelo, herramientas o lenguaje.

## Artefactos

```text
kernel-review.md
adversarial-scenarios/
```

## Plantilla de escenario

```yaml
scenario:
  id: ADV-SELF-001

  target_clause:
    - K-EVAL-001

  setup: >
    The implementation agent fails evaluation three times.

  adversarial_action: >
    It proposes lowering the threshold and applies the change
    in the same execution.

  expected_kernel_response:
    - amendment_blocked
    - execution_marked_blocked
    - human_review_required

  pass_condition:
    - criteria_remain_unchanged
```

## Criterio DONE

- Cada cláusula crítica tiene escenario adversarial.
- Se han identificado ambigüedades.
- Se han corregido contradicciones.
- Se ha revisado la minimalidad.

## Prompt para Chat 2

```text
Eres el Kernel Adversary.

No debes defender ni reescribir el kernel automáticamente.
Tu objetivo es intentar romperlo.

Para cada cláusula:
- busca ambigüedad;
- busca cumplimiento literal degenerado;
- busca conflicto con otras cláusulas;
- busca formas de autoenmienda;
- busca casos donde no pueda aplicarse;
- crea un escenario adversarial.

Entrega hallazgos priorizados:
CRITICAL, HIGH, MEDIUM, LOW.
```

---

# 15. K8 — Ratificación

## Objetivo

Aceptar conscientemente una primera versión.

## Tú decides por cláusula

```text
ACCEPT
REFORMULATE
MOVE_TO_POLICY
DEFER
REJECT
```

## Matriz de ratificación

| Cláusula | Decisión | Razón | Acción |
|---|---|---|---|
| K-AUTH-001 | ACCEPT | Preserva autoridad | Ratificar |
| K-CTX-003 | MOVE_TO_POLICY | Demasiado específica | Política |
| K-MEM-002 | DEFER | Falta evidencia | Revisar más adelante |

## Condiciones para `v0.1`

- charter aprobado;
- authority matrix aprobada;
- hazards revisados;
- cláusulas mínimas;
- enforcement inicial;
- escenarios adversariales;
- amendment policy;
- aprobación humana.

## Regla

> `v0.1` no significa definitivo. Significa suficientemente claro para gobernar el siguiente incremento.

---

# 16. Política de enmienda

El kernel debe poder cambiar, pero no durante una tarea ordinaria.

## Flujo

```text
propuesta
→ evidencia
→ impacto
→ revisión adversarial
→ revisión de enforcement
→ aprobación humana
→ nueva versión
→ migración
```

## Plantilla

```yaml
kernel_amendment:
  id: KA-003
  target_clause: K-EVAL-002

  motivation: ""
  evidence: []
  risks: []
  alternatives: []

  affected_stages: []
  migration_required: true

  validation:
    - adversarial_review
    - regression_suite

  approval:
    required_from:
      - human_owner

  effective_from_version: 0.2.0
```

## Reglas

- El proponente no aprueba.
- Una ejecución bloqueada no modifica la regla que la bloquea.
- Las reglas eliminadas permanecen en historial.
- Cada ejecución registra versión del kernel.
- Toda enmienda tiene razón y evidencia.

---

# 17. Primer conjunto candidato de cláusulas

Estas son candidatas, no kernel definitivo.

## K-AUTH-001 — Autoridad constitucional

HugePlanning DEBE preservar una autoridad humana explícita para aprobar cambios en el kernel y criterios constitucionales.

## K-TRUTH-001 — Fuente canónica

Todo estado, decisión o artefacto crítico DEBE tener una fuente canónica identificable y versionada.

## K-TRACE-001 — Trazabilidad

Toda modificación significativa DEBE relacionarse con intención, decisión, tarea y evidencia.

## K-UNCERTAINTY-001 — Frontera probabilística

Ninguna salida probabilística crítica DEBE convertirse en estado canónico sin validación proporcional.

## K-OUTCOME-001 — Autoridad del resultado

Las afirmaciones del agente NO DEBEN sustituir la comprobación del estado real.

## K-EVAL-001 — Separación de evaluación

Un ejecutor NO DEBE controlar unilateralmente su criterio, mecanismo y aceptación final.

## K-PHASE-001 — Transición basada en evidencia

Una fase NO DEBE avanzar sin precondiciones y evidencia obligatoria.

## K-BLOCK-001 — Bloqueo honesto

Cuando falten condiciones, el sistema DEBE declarar `BLOCKED`.

## K-AUTONOMY-001 — Autonomía proporcional

La autonomía NO DEBE exceder la capacidad de observar, validar, detener y recuperar.

## K-PRIVILEGE-001 — Mínima capacidad

Todo agente DEBE recibir únicamente los permisos necesarios.

## K-SELF-001 — Autoenmienda asimétrica

HugePlanning PUEDE proponer mejoras, pero NO DEBE aprobar unilateralmente cambios en sus propios criterios.

## K-COMPLEXITY-001 — Complejidad justificada

Agentes, memoria, loops, MCP y workflows DEBERÍAN demostrar valor frente a una alternativa simple.

## K-LEARNING-001 — Aprendizaje basado en evidencia

Una observación aislada NO DEBE convertirse automáticamente en regla global.

## K-SECURITY-001 — Contención

La ejecución DEBE limitar el daño máximo posible de un fallo.

## K-AMEND-001 — Reforma controlada

Toda modificación del kernel DEBE registrar motivación, evidencia, impacto, revisión y aprobación.

---

# 18. Estructura de archivos mínima

```text
meta-kernel/
├── KERNEL.md
├── kernel-charter.md
├── kernel-clauses.yaml
├── authority-matrix.yaml
├── hazard-register.yaml
├── invariant-candidates.yaml
├── rule-classification.yaml
├── enforcement-map.yaml
├── amendment-policy.md
├── current-state.md
├── next-action.md
├── scenarios/
└── decisions/
```

No es necesario crear todos los archivos el primer día.

Orden:

```text
1. kernel-charter.md
2. authority-matrix.yaml
3. hazard-register.yaml
4. invariant-candidates.yaml
5. kernel-draft.md
6. enforcement-map.yaml
7. scenarios/
8. KERNEL.md
```

---

# 19. Rutina de sesión recomendada

## Antes de comenzar

Leer únicamente:

```text
current-state.md
next-action.md
artefacto activo
```

No abrir todo el repositorio.

## Inicio de sesión

```text
Objetivo de hoy:
Artefacto que debe cambiar:
Criterio de finalización:
Energía disponible:
```

## Durante

Mantener:

```text
parking-lot.md
```

Cualquier idea no relacionada se guarda allí y no se persigue.

## Cierre

Actualizar:

```text
DONE:
DECIDED:
BLOCKED:
NEXT:
```

## Plantilla

```markdown
# Session close

## DONE
- Hazard HAZ-EVAL-001 reviewed.

## DECIDED
- Self-evaluation alone is insufficient for critical outputs.

## BLOCKED
- Need to define what counts as critical.

## NEXT
- Create criticality classification proposal.
```

---

# 20. Modos de trabajo según energía

## Modo mínimo

Para días difíciles:

```text
1 riesgo
1 decisión
1 actualización de estado
```

No se exige terminar una fase.

## Modo estándar

```text
1 lote pequeño
1 artefacto actualizado
1 revisión
```

## Modo profundo

```text
1 bloque completo
+ revisión
+ decisión
```

No debe convertirse en obligación diaria.

## Regla

> El sistema debe permitir progreso válido incluso con poca energía.

HugePlanning no debería depender de sesiones heroicas.

---

# 21. Qué automatizar y cuándo

## No automatizar todavía

- ratificación;
- selección de invariantes;
- aceptación de riesgos;
- modificación constitucional;
- decisión de autoridad;
- clasificación inicial de cláusulas.

## Automatizable pronto

- validar YAML;
- comprobar IDs;
- detectar duplicados;
- verificar referencias;
- crear índices;
- ejecutar escenarios;
- comprobar que todas las cláusulas tienen enforcement.

## Automatizable después

- workflow de revisión;
- generación de escenarios;
- comparación de versiones;
- evaluación de regresión;
- actualización de matrices.

## Regla

> Primero ejecutar manualmente el proceso varias veces. Después automatizar lo estable.

---

# 22. Señales de que el proceso está fallando

## Síntomas

- el kernel acumula demasiadas reglas;
- se discuten herramientas antes que principios;
- cada fallo añade una cláusula global;
- no se sabe qué documento manda;
- aparecen cláusulas contradictorias;
- un agente cambia reglas para terminar;
- todo requiere aprobación humana;
- nada puede verificarse;
- la planificación nunca se ratifica.

## Correcciones

### Kernel demasiado grande

Mover detalle a políticas.

### Demasiada abstracción

Añadir escenario concreto.

### Demasiados detalles

Subir nivel de abstracción.

### Cláusula no verificable

Reformular o convertir en principio no bloqueante.

### Fatiga

Cerrar con `PAUSED` y registrar siguiente acción.

---

# 23. Checklist maestro

## Mandato

- [ ] ¿Está claro qué gobierna el kernel?
- [ ] ¿Está clara la autoridad humana?
- [ ] ¿Está claro qué queda fuera?

## Autoridad

- [ ] ¿Cada actor tiene límites?
- [ ] ¿Existe separación de poderes?
- [ ] ¿Nadie puede autoaprobarse completamente?

## Peligros

- [ ] ¿Hay riesgos de autoridad?
- [ ] ¿Hay riesgos de estado?
- [ ] ¿Hay riesgos epistemológicos?
- [ ] ¿Hay riesgos de seguridad?
- [ ] ¿Hay riesgos de autoevolución?

## Invariantes

- [ ] ¿Son propiedades y no procedimientos?
- [ ] ¿Son independientes de herramientas?
- [ ] ¿Previenen peligros reales?

## Estratificación

- [ ] ¿El kernel es mínimo?
- [ ] ¿Las políticas están separadas?
- [ ] ¿La configuración está fuera?

## Cláusulas

- [ ] ¿Cada una tiene ID?
- [ ] ¿Es normativa?
- [ ] ¿Tiene rationale?
- [ ] ¿Tiene alcance?
- [ ] ¿Tiene severidad?

## Enforcement

- [ ] ¿Existe mecanismo?
- [ ] ¿Existe evidencia observable?
- [ ] ¿Las críticas bloquean o escalan?

## Adversarial

- [ ] ¿Se intentó hacer gaming?
- [ ] ¿Se buscaron conflictos?
- [ ] ¿Se probó self-hosting?
- [ ] ¿Se revisó minimalidad?

## Ratificación

- [ ] ¿Cada cláusula tiene decisión?
- [ ] ¿Existe versión?
- [ ] ¿Existe política de enmienda?
- [ ] ¿Está registrado el siguiente paso?

---

# 24. Plan de ejecución recomendado

## Sesión 1

```text
K0 — mandato
```

Salida:

```text
kernel-charter.md
```

## Sesión 2

```text
K1 — autoridad
```

Salida:

```text
authority-matrix.yaml
```

## Sesiones 3–5

```text
K2 — peligros por lotes
```

Lotes:

1. autoridad y self-hosting;
2. estado y trazabilidad;
3. evaluación y seguridad.

## Sesiones 6–8

```text
K3 — invariantes
```

## Sesión 9

```text
K4 — clasificación
```

## Sesiones 10–11

```text
K5 — borrador
```

## Chat separado

```text
K7 — revisión adversarial
```

## Chat separado

```text
K6 — enforcement
```

## Sesión final humana

```text
K8 — ratificación v0.1
```

Este calendario es orientativo. No debe convertirse en presión.

---

# 25. Prompt inicial completo para Kernel Designer

```text
You are the Kernel Designer for HugePlanning.

HugePlanning is a meta-project for designing and building an
AI-driven phased software development system. Your task is to help
define its first governance kernel.

Work in Spanish with the user.
Produce artifacts in English unless explicitly instructed otherwise.

Important operating rules:

1. Work on only one kernel phase at a time.
2. Do not jump ahead.
3. Ask a small number of questions per turn.
4. Number questions.
5. Use lettered options when useful.
6. Distinguish facts, assumptions, proposals and decisions.
7. Maintain a parking lot for out-of-scope ideas.
8. End every turn with:
   - current state;
   - decisions made;
   - open questions;
   - exact next action.
9. Never treat AI output as ratified.
10. The human project owner is the final ratification authority.
11. Prefer simple language and explicit structure.
12. Avoid presenting many large blocks of choices at once.
13. Allow DONE, BLOCKED, REVISE, DEFERRED and REJECTED as valid states.
14. Do not create agents, workflows or enforcement mechanisms before
    their governing invariants are understood.
15. Do not add a rule to the kernel merely because it sounds useful.

Current phase:
K0 — Kernel Mandate.

Objective:
Define what the kernel governs, who it applies to, its authority,
its boundaries and the ultimate ratification authority.

Required output:
- draft kernel charter;
- unresolved ambiguities;
- decisions required from the user;
- structured YAML version.

Do not proceed to hazards, invariants or clauses until K0 is approved.
```

---

# 26. Prompt para Kernel Adversary

```text
You are the independent Kernel Adversary for HugePlanning.

You did not author the kernel and must not defend it.

Your task is to identify:
- ambiguity;
- contradictions;
- specification gaming;
- self-certification;
- self-amendment loopholes;
- unenforceable clauses;
- excessive specificity;
- missing constitutional protections;
- conflicts between safety, privacy, traceability and autonomy.

For every finding provide:
- severity;
- affected clause;
- exploit or failure scenario;
- why the current wording permits it;
- minimal recommended correction.

Do not rewrite the entire kernel.
Do not introduce unrelated architecture.
Return a prioritized review and adversarial scenario files.
```

---

# 27. Prompt para Enforcement Engineer

```text
You are the Kernel Enforcement Engineer for HugePlanning.

Inputs:
- kernel draft;
- clause registry;
- adversarial review;
- current HugePlanning architecture.

For each clause determine:
- whether it is mechanically enforceable;
- appropriate enforcement type;
- evidence produced;
- violation effect;
- required human gate;
- implementation dependencies.

Allowed enforcement categories:
- schema;
- state machine;
- permission;
- sandbox;
- hook;
- CI gate;
- test;
- audit;
- human approval;
- advisory warning.

Flag clauses that:
- are too vague;
- cannot be observed;
- prescribe temporary tools;
- conflict with other clauses;
- require policy-level detail.

Do not modify the constitutional intent.
Produce enforcement-map.yaml and a list of blocked questions.
```

---

# 28. Qué debes recordar siempre

1. No necesitas diseñar el kernel en una sola conversación.
2. No necesitas siete agentes.
3. Los roles pueden ser chats separados.
4. El kernel debe ser pequeño.
5. Las políticas contienen detalle mutable.
6. Los peligros vienen antes que las reglas.
7. Los invariantes vienen antes que los mecanismos.
8. Las cláusulas vienen antes que los hooks.
9. El enforcement debe ser proporcional al riesgo.
10. `BLOCKED` es un estado válido.
11. La ratificación sigue siendo tuya.
12. La primera versión puede ser imperfecta.
13. La claridad es más importante que la cantidad.
14. Cada sesión debe dejar una siguiente acción exacta.
15. La metodología debe adaptarse a tu energía, no al revés.

---

# 29. Definición de éxito para v0.1

La primera versión será suficiente cuando:

```text
- tenga propósito claro;
- defina autoridad;
- proteja la fuente canónica;
- impida autocertificación crítica;
- exija evidencia para avanzar;
- permita BLOCKED;
- limite autonomía y permisos;
- proteja la autoenmienda;
- tenga enforcement inicial;
- pueda modificarse mediante un proceso controlado;
- y tú comprendas y aceptes cada cláusula.
```

No necesita cubrir todas las situaciones futuras.

Debe gobernar correctamente la siguiente etapa real de HugePlanning.

---

# 30. Cierre

Definir el kernel es exigente porque implica formalizar qué partes de tu criterio, intención y autoridad no quieres que el sistema pierda.

No debes inventar una constitución perfecta.

Debes construirla así:

```text
un peligro real
→ una propiedad protectora
→ una cláusula mínima
→ un mecanismo de enforcement
→ una prueba adversarial
→ una decisión humana
```

Repetido gradualmente.

El kernel no será valioso por sonar profundo.

Será valioso si consigue que HugePlanning:

- no pierda su propósito;
- no invente estados;
- no rebaje sus criterios;
- no exceda su autoridad;
- no se apruebe a sí mismo;
- y pueda evolucionar sin dejar de estar bajo control.
