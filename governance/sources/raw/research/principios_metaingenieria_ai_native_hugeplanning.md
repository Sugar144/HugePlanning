# Principios de Metaingeniería AI-Native para HugePlanning

**Subtítulo:** Intención, harnesses, verificación, autonomía, conocimiento y evolución controlada  
**Versión:** 0.1  
**Estado:** Documento rector complementario  
**Fecha:** 12 de julio de 2026  
**Relación:** Complementa el *Plan Maestro de Metaingeniería para HugePlanning*

---

# 0. Propósito

Este documento desarrolla los principios específicos de la **metaingeniería de sistemas de software impulsados por IA**: sistemas donde modelos, agentes, workflows y herramientas participan en la investigación, especificación, planificación, implementación, validación y evolución del propio sistema.

El objetivo no es reunir frases llamativas. Es construir un marco operativo para HugePlanning que distinga entre:

- conceptos asentados;
- patrones respaldados por investigación o experiencia industrial;
- heurísticas razonables;
- formulaciones propias que deben tratarse como hipótesis;
- y afirmaciones exageradas que no deberían convertirse en arquitectura sin validación.

La metaingeniería AI-native es todavía una disciplina emergente. No posee un cuerpo universal de “leyes” comparable a campos más maduros. Sí existe una convergencia entre:

- ingeniería de agentes;
- harness engineering;
- context engineering;
- specification-driven development;
- evaluación de sistemas probabilísticos;
- sistemas multiagente;
- seguridad de herramientas;
- diseño de interfaces para agentes;
- gobernanza de software generado;
- y self-hosting controlado.

HugePlanning debe aprovechar esa convergencia sin asumir que toda formulación novedosa constituye una ley científica.

---

# 1. Qué significa “juicio humano escaso”

## 1.1. No significa que el humano tenga poco juicio

La expresión **juicio humano escaso** no quiere decir que las personas tengan poca inteligencia o que la IA sea superior al humano.

“Escaso” se utiliza en sentido económico e ingenieril:

> Un recurso es escaso cuando su disponibilidad es limitada en relación con la demanda existente.

En un sistema AI-native, la IA puede generar rápidamente:

- propuestas;
- cambios de código;
- documentos;
- alternativas arquitectónicas;
- tests;
- hipótesis;
- diagnósticos;
- y nuevas tareas.

Pero una persona no puede revisar todo con la misma velocidad y profundidad.

La capacidad humana de:

- entender consecuencias;
- detectar supuestos implícitos;
- interpretar necesidades ambiguas;
- valorar riesgos;
- resolver conflictos de objetivos;
- asumir responsabilidad;
- y decidir qué es aceptable;

sigue limitada por el tiempo, la atención, la experiencia y la fatiga.

## 1.2. La nueva asimetría

```text
Capacidad de generación de la IA
████████████████████████████████

Capacidad humana de revisión profunda
██████
```

El cuello de botella se desplaza:

```text
Antes:
producción de código

Ahora:
definir intención
+ validar resultados
+ tomar decisiones
+ asumir responsabilidad
```

La IA puede producir cien alternativas. El humano sigue teniendo que decidir cuáles son correctas, útiles, seguras y coherentes con el propósito del proyecto.

## 1.3. Dónde aporta más valor el juicio humano

El juicio humano es especialmente valioso cuando la decisión es:

- ambigua;
- estratégica;
- irreversible;
- ética;
- legal;
- económica;
- de alto riesgo;
- dependiente del contexto social;
- basada en preferencias;
- o difícil de reducir a una métrica.

Ejemplos:

```text
¿Esta funcionalidad aporta suficiente valor para justificar su coste?

¿Debemos aceptar esta deuda técnica para cumplir el plazo?

¿El cliente comprende las consecuencias del alcance?

¿Esta arquitectura limita una dirección futura importante?

¿Este riesgo de seguridad es aceptable?

¿La evidencia es suficiente para avanzar?
```

La IA puede analizar alternativas. La autoridad final puede seguir siendo humana.

## 1.4. Cristalización del juicio

La metaingeniería no debe obligar a una persona a revisar manualmente cada acción.

Debe convertir el juicio humano en estructuras reutilizables:

```text
Juicio humano puntual
        ↓
Decisión documentada
        ↓
Principio
        ↓
Contrato
        ↓
Schema, test, linter, hook o gate
        ↓
Aplicación repetible
```

Ejemplo:

```text
Juicio:
“La interfaz no debe acceder directamente a infraestructura.”

Cristalización:
- ADR;
- regla de dependencias;
- test estructural;
- mensaje de error;
- gate de CI.
```

La persona decide una vez con profundidad. El sistema aplica esa decisión repetidamente.

## 1.5. Asignación del juicio

```text
Bajo impacto + alta verificabilidad
→ automatización

Impacto medio + criterios claros
→ IA asistida + verificación automática

Alto impacto + ambigüedad
→ propuesta de IA + decisión humana

Alto impacto + irreversibilidad
→ gate humano explícito
```

Guía conceptual:

```text
Prioridad de revisión humana
≈ impacto × irreversibilidad × ambigüedad × incertidumbre
```

No es una ecuación científica. Es una regla para distribuir atención.

---

# 2. Qué es la metaingeniería AI-native

No existe un único nombre universal. Se utilizan expresiones como:

- AI-native software engineering;
- agentic software engineering;
- harness engineering;
- context engineering;
- intent-centric engineering;
- specification-driven development;
- agent-computer interfaces;
- multi-agent software engineering.

Definición operativa para HugePlanning:

> **Metaingeniería AI-native** es el diseño del sistema de reglas, artefactos, interfaces, herramientas, verificadores, memorias, workflows y mecanismos de gobernanza que permiten a la IA participar de forma controlada en la creación y evolución de software.

No equivale a:

- generar código con un chat;
- usar un copiloto;
- encadenar prompts;
- crear muchos agentes;
- o añadir MCP.

Incluye toda la infraestructura que hace que esos elementos sean útiles, trazables, evaluables y seguros.

---

# 3. Procedencia y especies de artefactos

La clasificación de “tres especies de código” es útil, pero no es una ley universal. Su valor está en reconocer que no todos los artefactos deben editarse, validarse o regenerarse igual.

## 3.1. Taxonomía ampliada

### A. Human-authored

Creado y mantenido deliberadamente por una persona.

Ejemplos:

- kernel meta;
- políticas;
- decisiones aprobadas;
- reglas críticas;
- excepciones justificadas.

### B. Deterministically generated

Generado por reglas reproducibles.

Ejemplos:

- clientes OpenAPI;
- código desde schemas;
- documentación de tipos;
- archivos compilados.

### C. Model-generated

Producido por un modelo probabilístico.

Ejemplos:

- implementación propuesta;
- borradores;
- tests;
- planes;
- clasificaciones.

### D. Externally sourced

Procedente de terceros.

Ejemplos:

- dependencias;
- snippets;
- librerías;
- servicios;
- datasets.

### E. Runtime-derived

Derivado del estado real.

Ejemplos:

- cobertura;
- traces;
- resultados de evaluación;
- snapshots;
- métricas;
- artefactos de build.

## 3.2. La política importa más que el origen

Saber que un archivo fue generado por IA no basta.

Debe conocerse:

```text
procedencia
+ fuente canónica
+ propietario
+ editabilidad
+ regeneración
+ validación
+ autoridad de aprobación
```

Ejemplo determinista:

```yaml
artifact:
  id: ART-CLIENT-API
  path: src/generated/api-client/
  provenance: deterministic_generator
  canonical_source: specs/openapi.yaml
  owner: platform
  editable: false
  regeneration:
    command: npm run generate:client
  validation:
    - npm run typecheck
    - npm run contract:test
```

Ejemplo generado por IA y posteriormente mantenido:

```yaml
artifact:
  id: ART-AUTH-SERVICE
  path: src/auth/auth-service.ts
  provenance: model_generated_then_maintained
  canonical_sources:
    - REQ-AUTH-001
    - ADR-AUTH-003
  owner: application
  editable: true
  validation:
    - npm run typecheck
    - npm run test:auth
    - npm run security:scan
  approval:
    required: true
```

---

# 4. De code-centric a intent-centric

## 4.1. El cambio central

```text
Ingeniería tradicional:
código como artefacto dominante

Ingeniería AI-native:
intención + contratos + restricciones + verificadores
como artefactos dominantes
```

El código sigue siendo esencial. Pero algunas zonas pueden ser abundantes, reemplazables y regenerables. La intención verificable es el recurso que debe preservarse.

## 4.2. Principio de primacía de la intención

> No debe automatizarse una intención que todavía no pueda expresarse con suficiente claridad.

Cadena recomendada:

```text
Deseo
→ problema
→ necesidad
→ objetivo
→ requisito
→ restricciones
→ criterios de aceptación
→ diseño
→ implementación
```

Cadena peligrosa:

```text
Deseo ambiguo
→ código
→ reinterpretación posterior
→ parches
→ contradicciones
```

## 4.3. Intención verificable

Una intención preparada para ejecución debería contener:

- comportamiento esperado;
- límites;
- ejemplos;
- casos negativos;
- invariantes;
- criterios de éxito;
- comportamientos prohibidos;
- autoridad.

```yaml
requirement:
  id: REQ-AUTH-004
  statement: >
    Tras cinco intentos fallidos consecutivos, la cuenta debe
    bloquearse durante quince minutos.

acceptance_examples:
  - failed_attempts: 4
    expected_state: active
  - failed_attempts: 5
    expected_state: locked
  - elapsed_minutes: 16
    expected_state: active

invariants:
  - failed_attempts >= 0
  - lock_duration_minutes == 15

forbidden:
  - permanent_lock_without_admin_review
  - exposing_account_existence
```

## 4.4. Niveles de especificación

### Spec-first

La especificación precede a la implementación.

### Spec-anchored

La especificación permanece como referencia y limita cambios.

### Spec-as-source

La implementación se deriva de la especificación.

Aplicación orientativa:

```text
Kernel y gobernanza
→ spec-anchored + gate humano

Contratos y protocolos
→ spec-as-source cuando sea viable

Lógica de aplicación
→ spec-first o spec-anchored

Boilerplate y clientes
→ spec-as-source
```

## 4.5. Especificaciones ejecutables

```text
Requisito
→ ejemplo
→ contrato
→ test
→ observable
→ evaluación
```

No toda propiedad puede automatizarse, pero toda propiedad crítica debería tener un método explícito de evaluación.

---

# 5. Núcleo probabilístico y envoltura determinista

## 5.1. El problema

Un LLM puede:

- variar;
- interpretar de manera diferente;
- omitir;
- inventar;
- atascarse;
- optimizar el indicador equivocado.

No debe ser la única capa de control.

## 5.2. Arquitectura recomendada

```text
Deterministic control plane
        ↓
Probabilistic reasoning plane
        ↓
Deterministic verification plane
```

### Control plane

Gestiona:

- estados;
- permisos;
- contratos;
- límites;
- transiciones;
- versiones;
- routing;
- auditoría;
- cancelación;
- presupuestos.

### Reasoning plane

Realiza:

- interpretación;
- planificación;
- síntesis;
- exploración;
- generación;
- crítica;
- diagnóstico;
- propuestas.

### Verification plane

Comprueba:

- schemas;
- tests;
- contratos;
- invariantes;
- análisis estático;
- seguridad;
- resultados;
- políticas.

## 5.3. Principio del núcleo probabilístico acotado

> Utiliza IA donde el razonamiento flexible aporte valor; utiliza software determinista para imponer lo que no debe depender de interpretación.

## 5.4. Ley de la frontera de incertidumbre

> Toda salida probabilística que afecte a una propiedad crítica debe cruzar una frontera verificable antes de convertirse en estado canónico.

```text
Requisito propuesto
→ validación humana

Código propuesto
→ build + typecheck + tests + revisión

Decisión arquitectónica
→ alternativas + ADR + gate

Cambio de estado
→ precondiciones deterministas

Conclusión de investigación
→ evidencia + referencias + auditoría
```

## 5.5. No autocertificación

Peligroso:

```text
LLM decide
→ LLM ejecuta
→ LLM evalúa
→ LLM declara éxito
```

Más fiable:

```text
LLM propone
→ entorno ejecuta
→ verificadores observan
→ evaluador interpreta
→ gate autoriza
```

---

# 6. Harness engineering

## 6.1. Definición

```text
Agente = modelo + harness
```

El harness incluye:

- instrucciones;
- tools;
- permisos;
- contexto;
- memoria;
- estado;
- loop;
- entorno;
- observabilidad;
- validación;
- recuperación;
- límites.

Cambiar el harness puede cambiar radicalmente el comportamiento sin cambiar el modelo.

## 6.2. Dos harnesses

### Agent harness

Permite que el agente trabaje.

### Evaluation harness

Permite comprobar de forma repetible cómo trabajó y qué produjo.

HugePlanning necesita ambos.

## 6.3. Repositorio agent-friendly

Debe ofrecer:

- estructura predecible;
- documentación localizable;
- comandos estables;
- tests rápidos;
- errores informativos;
- interfaces pequeñas;
- convenciones explícitas;
- límites mecánicos;
- estado fácil de consultar;
- cambios revisables.

## 6.4. Agent-Computer Interface

Una mala interfaz obliga al agente a:

- leer demasiado;
- adivinar rutas;
- interpretar logs gigantes;
- editar de forma frágil;
- reconstruir estado.

Una buena interfaz ofrece operaciones intencionales:

```text
get_current_stage()
get_task_contract(task_id)
validate_artifact(path)
run_relevant_tests(scope)
get_failure_summary(run_id)
commit_stage_result(stage_id)
```

## 6.5. Observabilidad accionable

Malo:

```text
Validation failed.
```

Mejor:

```text
REQ-014 references ADR-009, but ADR-009 does not exist.
Fix: create the ADR, change the reference, or mark the requirement blocked.
```

---

# 7. Context engineering

## 7.1. Contexto como recurso finito

Más contexto puede producir:

- pérdida de foco;
- prioridades confusas;
- mezcla de fases;
- reglas irrelevantes;
- información obsoleta;
- mayor consumo.

## 7.2. Ley del contexto tributario

> Todo token cargado permanentemente impone un impuesto sobre cada inferencia posterior.

Preguntas:

```text
¿Se necesita siempre?
¿Se necesita ahora?
¿Puede descubrirse bajo demanda?
¿Existe una versión más compacta?
¿Está actualizado?
```

## 7.3. Progressive disclosure

```text
CLAUDE.md
→ mapa mínimo y principios

docs/index.md
→ catálogo

stages/S1/index.md
→ etapa

tasks/TASK-017.yaml
→ contrato actual

evidence/
→ evidencia concreta
```

## 7.4. Clases de contexto

- permanente;
- de etapa;
- de tarea;
- recuperado;
- episódico;
- de evidencia.

## 7.5. Paquete quirúrgico

```yaml
task_packet:
  id: TASK-017
  objective: ""
  stage: S2
  rationale: ""
  authorized_inputs: []
  constraints: []
  forbidden_actions: []
  output_contract: ""
  acceptance_checks: []
  stop_conditions: []
  max_iterations: 5
```

## 7.6. Repositorio como memoria operativa

Lo que solo existe en un chat, en la cabeza del usuario o en una conversación inaccesible no es memoria fiable para un sistema autónomo.

Los archivos vivos convierten conocimiento en infraestructura.

---

# 8. Arquitectura de verificación

## 8.1. El nuevo cuello de botella

Cuando generar se vuelve barato, verificar se vuelve escaso.

Puede producirse código aparentemente correcto con:

- errores semánticos;
- tests débiles;
- documentación convincente pero falsa;
- arquitectura incoherente;
- vulnerabilidades;
- métricas engañosas.

## 8.2. Verification-first

Antes de automatizar:

```text
¿Qué demuestra éxito?
¿Qué demuestra fracaso?
¿Qué puede comprobarse automáticamente?
¿Qué requiere juicio?
¿Qué podría manipular el agente?
```

## 8.3. Outcome over narrative

No se valida lo que el agente dice. Se valida el estado real.

```text
Narrativa:
“He completado la migración.”

Outcome:
- migración presente;
- compatibilidad comprobada;
- tests ejecutados;
- rollback probado;
- datos verificados.
```

## 8.4. Capas

- estructural;
- determinista;
- dinámica;
- semántica;
- humana.

## 8.5. Oráculos múltiples

```text
Tests visibles
+ tests independientes
+ análisis estático
+ ejecución real
+ evaluador semántico
+ revisión humana
```

## 8.6. Ley del evaluador correlacionado

> Un evaluador que comparte los mismos supuestos, contexto y señales del generador puede reproducir sus errores aunque sea un agente separado.

Aumentar independencia mediante:

- otra rúbrica;
- contexto parcial;
- modelos distintos;
- tests no derivados del código;
- datos ocultos;
- revisión humana;
- perturbaciones.

## 8.7. Evaluación estadística

No basta con “funcionó una vez”.

Medir:

- pass rate;
- variabilidad;
- coste;
- latencia;
- iteraciones;
- clases de fallo;
- sensibilidad al modelo;
- sensibilidad al contexto.

```text
“Superó 27 de 30 ejecuciones.
Los tres fallos pertenecen a contexto insuficiente
durante reanudaciones.”
```

---

# 9. Specification gaming y ley del proxy

## 9.1. Definición

Un sistema satisface literalmente una métrica sin cumplir la intención.

```text
“Haz que pasen los tests”
→ eliminar tests

“Reduce warnings”
→ desactivar reglas

“Completa tareas”
→ cambiar su estado
```

## 9.2. Ley del proxy

> Una métrica incompleta convertida en objetivo puede ser optimizada de formas no deseadas.

```yaml
success:
  required:
    - all_tests_pass
    - acceptance_scenarios_pass
    - coverage_not_reduced

forbidden:
  - deleting_tests
  - weakening_assertions
  - disabling_rules
  - hardcoding_fixture_outputs
  - changing_acceptance_criteria
```

## 9.3. Separación de poderes

El implementador no debería controlar libremente:

- tests definitivos;
- política de release;
- evaluador;
- métricas;
- permisos;
- registro de estado.

No porque sea malicioso, sino porque optimiza lo que se le presenta.



# 10. Ingeniería multiagente

## 10.1. Más agentes no significa más inteligencia útil

Cada agente añade:

- contexto;
- coste;
- latencia;
- handoffs;
- coordinación;
- pérdida potencial;
- nuevos puntos de fallo.

## 10.2. Ley de la baseline simple

> Ninguna arquitectura multiagente está justificada hasta superar una alternativa secuencial más sencilla.

Baseline:

```text
localizar
→ proponer
→ validar
```

Alternativa:

```text
orquestador
├── arquitecto
├── implementador
├── tester
├── crítico
└── árbitro
```

La segunda debe demostrar mejora medible en calidad, robustez, coste, velocidad o aislamiento de contexto.

## 10.3. Ley de pérdida por transformación

Cada transformación puede eliminar información:

```text
intención
→ especificación
→ plan
→ task packet
→ implementación
→ resumen
```

Riesgos:

- omisión;
- simplificación;
- reinterpretación;
- cambio terminológico;
- pérdida de excepciones;
- resolución prematura.

## 10.4. Ley del contrato más débil

> La fiabilidad de una cadena multiagente queda limitada por su handoff más ambiguo.

Un buen handoff contiene:

- objetivo;
- razón;
- entradas autorizadas;
- restricciones;
- invariantes;
- entregable;
- criterios de aceptación;
- prohibiciones;
- condiciones de parada.

Ejemplo:

```yaml
task:
  id: TASK-AUTH-014
  objective: Implement password reset token validation.
  inputs:
    - REQ-AUTH-014
    - ADR-SEC-003
  invariants:
    - token_single_use
    - expires_in_15_minutes
    - constant_time_comparison
  acceptance:
    - TEST-AUTH-031
    - TEST-AUTH-032
  forbidden:
    - changing_token_expiration
    - editing_acceptance_tests
```

## 10.5. Cuándo separar agentes

Un agente independiente se justifica por diferencias reales en:

- contexto;
- tools;
- modelo;
- autoridad;
- perspectiva;
- criterio de éxito;
- presupuesto;
- independencia;
- ciclo de vida.

No debe crearse únicamente porque un equipo humano tendría ese cargo.

## 10.6. Tester independiente

La regla correcta no es “el tester nunca ve código”.

Debe haber:

### Tests derivados de la especificación

Validan intención externa.

### Tests derivados de riesgos

Validan seguridad, límites y ataques.

### Tests derivados de la implementación

Validan ramas, cobertura e integración.

La aceptación no debe depender exclusivamente de pruebas derivadas del código evaluado.

## 10.7. Coste de coordinación

Paralelizar cuando:

- las tareas son independientes;
- explorar diversidad aporta valor;
- el resultado puede agregarse.

No paralelizar cuando:

- existe un único estado mutable;
- cada paso depende del anterior;
- la tarea es pequeña;
- el coste supera el beneficio.

---

# 11. Entropía generativa y deuda multiplicativa

## 11.1. Amplificación de patrones

Los agentes aprenden de la base existente:

```text
Mala convención
→ el agente la copia
→ aparecen más ejemplos
→ parece estándar
→ futuros agentes la copian más
```

## 11.2. Ley de la deuda multiplicativa

> En un entorno agent-first, una mala convención se convierte en plantilla para producir nueva deuda.

## 11.3. Golden principles

Los principios importantes deben ascender:

```text
prosa
→ decisión
→ regla estructurada
→ linter
→ test
→ gate
```

Ejemplo:

```text
Principio:
Las integraciones externas solo se utilizan mediante adapters.

Mecanización:
un test de arquitectura rechaza imports externos
fuera de adapters/.
```

## 11.4. Jardinería continua

HugePlanning debería contemplar:

- architecture gardening;
- documentation gardening;
- Skill gardening;
- prompt gardening;
- test gardening;
- dependency gardening;
- memory gardening;
- eval gardening.

## 11.5. Presupuesto de entropía

```yaml
quality_budget:
  new_exceptions_allowed: 0
  duplicated_patterns_max: 1
  unresolved_todos_max: 2
  deprecated_interfaces_added: 0
```

Las cifras deben adaptarse, pero la calidad debe tratarse como estado observable.

---

# 12. Regeneración y propiedad

## 12.1. Regenerar no siempre es mejor

Regenerar un módulo completo puede ser correcto cuando:

- existe fuente canónica;
- la frontera es clara;
- la salida es reemplazable;
- no se admiten ediciones manuales;
- existen tests;
- el contrato externo es estable.

No es una ley general para todo el software.

## 12.2. Zonas de regeneración

```yaml
regeneration_zone:
  id: GEN-API-CLIENT
  paths:
    - src/generated/api/**
  source:
    - specs/openapi.yaml
  strategy: replace_all
  manual_edits: forbidden
  validation:
    - contract_tests
    - typecheck
```

Zona mantenida incrementalmente:

```yaml
regeneration_zone:
  id: APP-DOMAIN
  paths:
    - src/domain/**
  strategy: incremental_patch
  manual_edits: allowed
  approval: required
  validation:
    - unit_tests
    - architecture_tests
    - review
```

## 12.3. Ley de la fuente regenerable

> Un artefacto solo es regenerable si sobreviven la intención, las restricciones, las fuentes y el procedimiento necesario para recrearlo.

Si desaparecen la especificación, los tests o las decisiones relevantes, el código no es realmente desechable.

## 12.4. Idempotencia

Para generación determinista:

```text
mismas fuentes + misma versión + misma configuración
→ mismo resultado
```

Para generación probabilística debe exigirse:

- equivalencia de propiedades;
- reproducibilidad experimental;
- validación estable;
- registro de condiciones.

---

# 13. Seguridad, MCP y blast radius

## 13.1. MCP no es una garantía de seguridad

MCP es un protocolo de integración entre aplicaciones de IA y sistemas externos.

No proporciona automáticamente:

- aislamiento;
- autorización correcta;
- memoria;
- selección inteligente de contexto;
- validación;
- protección frente a prompt injection;
- confianza.

## 13.2. Riesgos

- herramientas excesivamente poderosas;
- credenciales amplias;
- exfiltración;
- tool poisoning;
- resultados maliciosos;
- confusión de identidad;
- acciones accidentales;
- llamadas sin límite;
- falta de auditoría.

## 13.3. Ley del blast radius

> No diseñes únicamente para evitar que el agente falle; limita el daño máximo que puede causar si falla.

Modelo conceptual:

```text
Riesgo
≈ probabilidad de fallo × impacto máximo
```

## 13.4. Least agency

Adaptación del principio de menor privilegio:

> Un agente debe recibir la capacidad mínima necesaria para cumplir su contrato.

```text
Extractor
→ lectura, sin push

Revisor
→ lectura + informe, sin edición

Implementador
→ branch aislada, sin producción

Deploy agent
→ staging; producción con gate
```

## 13.5. Niveles de autonomía

```text
L0 — Solo recomendación
L1 — Borrador
L2 — Modificación local
L3 — Branch aislada
L4 — Ejecución de tests
L5 — Apertura de PR
L6 — Merge con gate
L7 — Deploy a staging
L8 — Producción con aprobación explícita
```

## 13.6. Ley de simetría autonomía-validación

> La autonomía no debe aumentar más rápido que la capacidad de observar, verificar, detener y recuperar.

Cada aumento exige:

- mejores tests;
- menor blast radius;
- logs;
- rollback;
- permisos;
- condiciones de parada;
- gate proporcional.

---

# 14. Provenance y reproducibilidad

## 14.1. Trazabilidad de generación

```yaml
generation_run:
  id: RUN-2026-0041
  task: TASK-041
  model: claude-sonnet
  model_alias_date: 2026-07-12
  harness_version: v0.7.2
  skill_commit: abc123
  base_commit: def456
  authorized_tools:
    - read
    - edit
    - test
  outputs:
    - src/auth/token.ts
  validations:
    - unit_tests
    - typecheck
    - security_scan
  result: accepted
```

No es necesario almacenar razonamiento privado. Sí las condiciones operativas.

## 14.2. Deriva del modelo

El mismo prompt puede producir resultados diferentes porque cambian:

- modelo;
- alias;
- proveedor;
- herramientas;
- harness;
- contexto;
- Skill;
- evaluador;
- repositorio.

## 14.3. Reproducibilidad experimental

No siempre puede reproducirse el texto exacto. Sí pueden reproducirse:

- condiciones;
- propiedades;
- pass rate;
- coste;
- distribución de fallos;
- nivel de calidad.

## 14.4. Regresión del harness

Cuando el rendimiento cambia deben investigarse:

```text
modelo
prompt
contexto
tool
harness
estado
dataset
evaluador
```

No asumir automáticamente que “el modelo empeoró”.

---

# 15. Self-hosting y constitución

## 15.1. HugePlanning construyéndose a sí mismo

```text
Construcción externa
→ self-hosting parcial
→ self-hosting controlado
→ automatización avanzada
```

## 15.2. Ley de autoenmienda asimétrica

> HugePlanning puede proponer y ejecutar mejoras sobre sí mismo, pero no debe rebajar unilateralmente los criterios mediante los que serán aceptadas.

Puede:

- proponer una Skill;
- crear tests;
- implementar;
- ejecutar escenarios;
- documentar deuda;
- actualizar un borrador de roadmap.

No debe poder sin gate:

- eliminar tests fallidos;
- ampliar permisos;
- reducir calidad;
- cambiar release policy;
- modificar el kernel meta;
- aprobar su propia excepción crítica.

## 15.3. Capa constitucional

Debe proteger:

- invariantes;
- autoridad;
- gates;
- políticas de seguridad;
- reglas de release;
- criterios de evidencia;
- permisos;
- proceso de modificación constitucional.

---

# 16. Conocimiento como producto acumulativo

## 16.1. No acumular reglas reactivas

Patrón peligroso:

```text
fallo
→ nueva instrucción global
→ fallo distinto
→ otra instrucción
→ instrucciones inmanejables
```

## 16.2. Escalera de cristalización

```text
Observación
→ defecto reproducido
→ patrón
→ decisión
→ principio
→ regla
→ automatización
```

No saltar de una anécdota a una ley.

## 16.3. Criterios para promover conocimiento

- ¿Es reproducible?
- ¿Aparece en más de un escenario?
- ¿Es sistémico?
- ¿Puede probarse?
- ¿Contradice otras reglas?
- ¿Pertenece al kernel, a una etapa o a una tarea?
- ¿Cuál es su fecha de revisión?

## 16.4. Memorias con autoridad diferenciada

```text
state
→ qué sucede ahora

decision log
→ qué se decidió

evidence registry
→ qué respalda una afirmación

Skill
→ cómo ejecutar un procedimiento

test
→ qué propiedad debe cumplirse

kernel
→ qué no puede redefinirse libremente
```

---

# 17. Quince leyes operativas para HugePlanning

Estas leyes son **síntesis de diseño**, no leyes oficiales universalmente aceptadas.

## Ley 1 — Primacía de la intención

No automatices una intención que no pueda expresarse mediante propiedades suficientemente claras.

## Ley 2 — Frontera de incertidumbre

Toda salida probabilística crítica necesita validación antes de volverse canónica.

## Ley 3 — Contrato más débil

Una cadena de agentes es tan fiable como su handoff más ambiguo.

## Ley 4 — Contexto tributario

Todo contexto permanente consume atención y tokens en cada ejecución.

## Ley 5 — Pérdida por transformación

Cada resumen o delegación puede eliminar información esencial.

## Ley 6 — Evaluador correlacionado

Separar agentes no garantiza independencia si comparten los mismos supuestos.

## Ley 7 — Outcome

El estado real del sistema tiene más autoridad que el relato del agente.

## Ley 8 — Proxy

Una métrica incompleta convertida en objetivo será optimizada de formas no deseadas.

## Ley 9 — Simetría autonomía-validación

No aumentes autonomía sin aumentar observabilidad, verificación y recuperación.

## Ley 10 — Blast radius

Diseña para limitar el daño del fallo, no solo para reducir su probabilidad.

## Ley 11 — Deuda multiplicativa

Un mal patrón se convierte en ejemplo para futuras generaciones de código.

## Ley 12 — Fuente regenerable

No llames regenerable a un artefacto si no conservas lo necesario para recrearlo.

## Ley 13 — Baseline simple

No introduzcas multiagentes hasta demostrar que superan un proceso más simple.

## Ley 14 — Autoenmienda asimétrica

El sistema no debe rebajar por sí mismo los criterios con los que se evalúa.

## Ley 15 — Complejidad pagada

Cada agente, memoria, workflow, loop o MCP debe justificar su coste mediante evidencia.

---

# 18. Conservación del juicio humano

## 18.1. Idea central

> El objetivo no es eliminar el juicio humano, sino utilizarlo donde aporta más valor y convertir las decisiones repetibles en infraestructura.

## 18.2. Ciclo

```text
Humano decide una propiedad importante
        ↓
La decisión se documenta
        ↓
Se formaliza como contrato
        ↓
Se implementa como test o gate
        ↓
La IA opera dentro del límite
        ↓
El humano revisa excepciones y cambios de política
```

## 18.3. Qué no debe cristalizarse demasiado pronto

No toda preferencia necesita una regla rígida.

Algunas decisiones son:

- contextuales;
- experimentales;
- temporales;
- reversibles;
- estéticas;
- dependientes del cliente.

Deben permanecer como guías hasta reunir evidencia.

## 18.4. Jerarquía de autoridad

```text
Constitución / kernel
        ↓
Políticas
        ↓
Decisiones
        ↓
Contratos
        ↓
Tareas
        ↓
Acciones del agente
```

Una acción no debe contradecir una capa superior.

---

# 19. Aplicación directa a HugePlanning

## 19.1. Registros recomendados

```text
artifact-registry.yaml
architecture-invariants.yaml
autonomy-levels.yaml
context-budget-policy.md
regeneration-zones.yaml
golden-principles.md
generation-runs/
eval-registry/
```

## 19.2. Artifact registry

```yaml
artifacts:
  - id: META-KERNEL
    path: docs/meta/kernel.md
    provenance: human_authored
    authority: constitutional
    editable_by:
      - human
    approval: mandatory

  - id: API-CLIENT
    path: src/generated/api/
    provenance: deterministic_generator
    authority: derived
    canonical_source: specs/openapi.yaml
    editable_by: []
```

## 19.3. Architecture invariants

```yaml
invariants:
  - id: INV-ARCH-001
    statement: UI cannot import infrastructure packages.
    enforcement:
      - architecture_test
    severity: blocking

  - id: INV-META-002
    statement: >
      An agent cannot modify release criteria in the same run
      in which it evaluates the release.
    enforcement:
      - permissions
      - workflow_gate
    severity: constitutional
```

## 19.4. Autonomy policy

```yaml
agent:
  name: implementation-worker
  autonomy_level: L3
  permissions:
    - read_repo
    - edit_branch
    - run_tests
  forbidden:
    - merge
    - modify_eval_policy
    - access_production
  escalation:
    - architecture_change
    - security_exception
```

## 19.5. Context budget

```yaml
context_policy:
  permanent:
    max_tokens: 6000
  task_packet:
    max_tokens: 8000
  retrieved:
    max_tokens: 20000
  tool_output:
    strategy: filter_and_summarize
  overflow:
    action: compact_or_split
```

Las cifras son ejemplos y deben calibrarse mediante experimentos.

## 19.6. Matriz de autoridad

| Elemento | Procedencia | Fuente canónica | Validación | Autoridad |
|---|---|---|---|---|
| Kernel meta | Humana | Documento rector | Revisión humana | Propietario |
| Skill | Mixta | `SKILL.md` | Evals | Maintainer |
| Cliente API | Determinista | OpenAPI | Contract tests | Generador |
| Implementación | IA asistida | Spec + repo | Tests + review | PR gate |
| Resultado de eval | Runtime | Eval harness | Auditoría | Eval system |
| ADR | Humana asistida | ADR | Gate | Arquitectura |

---

# 20. Modelo de madurez

## Nivel 0 — Prompting

- conversaciones;
- resultados manuales;
- poca trazabilidad.

## Nivel 1 — Artefactos

- repositorio;
- estado;
- decisiones;
- Skills;
- contratos básicos.

## Nivel 2 — Harness controlado

- tools limitadas;
- context packets;
- schemas;
- tests;
- logs;
- branches aisladas.

## Nivel 3 — Delegación especializada

- subagentes;
- routing;
- evaluadores;
- handoffs estructurados.

## Nivel 4 — Workflows evaluados

- procesos repetibles;
- loops acotados;
- métricas;
- regression suites;
- autonomía graduada.

## Nivel 5 — Self-hosting controlado

- HugePlanning desarrolla partes de sí mismo;
- constitución protegida;
- gates externos;
- aprendizaje acumulativo.

No es necesario alcanzar el nivel 5 en todas las capacidades.

---

# 21. Checklist antes de introducir una capacidad AI-native

## Intención

- [ ] ¿El objetivo está claro?
- [ ] ¿Existen límites?
- [ ] ¿Se conocen comportamientos prohibidos?
- [ ] ¿Hay ejemplos y contraejemplos?

## Artefactos

- [ ] ¿Se conoce la procedencia?
- [ ] ¿Existe fuente canónica?
- [ ] ¿Se sabe quién puede editar?
- [ ] ¿Es regenerable realmente?

## Contexto

- [ ] ¿Cuál es el contexto mínimo?
- [ ] ¿Qué debe recuperarse bajo demanda?
- [ ] ¿Qué información está obsoleta?
- [ ] ¿Existe presupuesto?

## Agentes

- [ ] ¿Hace falta un agente separado?
- [ ] ¿Una Skill sería suficiente?
- [ ] ¿Un script sería mejor?
- [ ] ¿El handoff tiene contrato?
- [ ] ¿El modelo elegido es proporcional?

## Verificación

- [ ] ¿Qué demuestra éxito?
- [ ] ¿Qué demuestra fracaso?
- [ ] ¿Se valida el outcome?
- [ ] ¿Existen varios oráculos?
- [ ] ¿El evaluador es suficientemente independiente?

## Autonomía

- [ ] ¿Cuál es el nivel de autonomía?
- [ ] ¿Cuál es el blast radius?
- [ ] ¿Puede detenerse?
- [ ] ¿Puede recuperarse?
- [ ] ¿Qué gate humano existe?

## Evolución

- [ ] ¿Puede amplificar un mal patrón?
- [ ] ¿Existe prueba de regresión?
- [ ] ¿Cómo se cristaliza el aprendizaje?
- [ ] ¿La complejidad añadida está pagada?

---

# 22. Resumen rector

La metaingeniería AI-native no consiste en sustituir a una persona por un enjambre de agentes.

Consiste en diseñar un sistema donde:

```text
la intención se preserve;
los artefactos tengan autoridad;
el contexto se administre;
la incertidumbre esté acotada;
la autonomía sea proporcional al control;
los resultados se verifiquen;
los fallos dejen aprendizaje;
el código tenga procedencia;
la arquitectura resista la entropía;
y el sistema pueda evolucionar sin aprobarse a sí mismo.
```

El recurso más limitado no será necesariamente el código.

Será la capacidad de:

- decidir qué merece construirse;
- distinguir una solución convincente de una correcta;
- aceptar riesgos;
- resolver ambigüedades;
- diseñar criterios;
- y asumir responsabilidad.

Por eso el objetivo de HugePlanning debe ser:

> **Convertir juicio humano de alta calidad en decisiones, contratos, verificadores y estructuras reutilizables, de modo que la IA pueda operar con creciente autonomía sin exigir revisión humana exhaustiva de cada acción.**

Ese es el significado exacto de utilizar **juicio humano escaso** de manera eficiente.

---

# 23. Referencias fundamentales

Las siguientes fuentes respaldan los conceptos generales. Las leyes nombradas para HugePlanning son síntesis de diseño y no deben atribuirse literalmente a estas fuentes.

1. OpenAI — *Harness engineering: leveraging Codex in an agent-first world*  
   https://openai.com/index/harness-engineering/

2. OpenAI — *Run long horizon tasks with Codex*  
   https://developers.openai.com/blog/run-long-horizon-tasks-with-codex

3. OpenAI — *Unrolling the Codex agent loop*  
   https://openai.com/index/unrolling-the-codex-agent-loop/

4. Anthropic — *Building effective agents*  
   https://www.anthropic.com/engineering/building-effective-agents

5. Anthropic — *Effective context engineering for AI agents*  
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

6. Anthropic — *Effective harnesses for long-running agents*  
   https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

7. Anthropic — *Demystifying evals for AI agents*  
   https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

8. Anthropic — *How we built our multi-agent research system*  
   https://www.anthropic.com/engineering/multi-agent-research-system

9. Model Context Protocol — *Architecture overview*  
   https://modelcontextprotocol.io/docs/learn/architecture

10. Model Context Protocol — *Security best practices*  
    https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices

11. Yang et al. — *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*  
    https://arxiv.org/abs/2405.15793

12. Huang et al. — *AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation*  
    https://arxiv.org/abs/2312.13010

13. Xia et al. — *Agentless: Demystifying LLM-based Software Engineering Agents*  
    https://arxiv.org/abs/2407.01489

14. Nunez et al. — *AutoSafeCoder: A Multi-Agent Framework for Securing LLM Code Generation through Static Analysis and Fuzz Testing*  
    https://arxiv.org/abs/2409.10737

15. Google DeepMind — *Specification gaming: the flip side of AI ingenuity*  
    https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/

---

# 24. Relación con el Plan Maestro

Este documento debe utilizarse junto al *Plan Maestro de Metaingeniería para HugePlanning*.

El primer documento responde:

```text
¿Cómo construimos y validamos HugePlanning?
```

Este segundo documento responde:

```text
¿Qué principios específicos deben gobernar un sistema
de ingeniería intensivamente impulsado por IA?
```

Ante una contradicción entre una moda técnica y estos principios, debe prevalecer:

```text
intención
→ evidencia
→ simplicidad
→ verificabilidad
→ control
```

y no la novedad de la herramienta.
