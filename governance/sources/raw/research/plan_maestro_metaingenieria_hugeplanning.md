# Plan Maestro de Metaingeniería para HugePlanning

**Versión:** 0.1  
**Estado:** Documento rector  
**Propósito:** Guiar la investigación, planificación, construcción, validación y evolución del sistema HugePlanning sin confundir el sistema final con el proceso utilizado para crearlo.

---

## 0. Regla cardinal

> **HugePlanning no debe construirse como un conjunto acumulativo de prompts, agentes y automatizaciones. Debe construirse como un programa controlado de investigación, arquitectura, implementación y validación.**

Los agentes, Skills, workflows, loops, hooks, MCP, memorias y modelos son **instrumentos de ejecución**. No constituyen por sí mismos el plan maestro.

El orden correcto es:

```text
Qué conocimiento necesitamos
        ↓
Qué hipótesis queremos comprobar
        ↓
Qué decisión de diseño depende de ese conocimiento
        ↓
Qué capacidad del sistema debemos construir
        ↓
Cómo se implementará
        ↓
Cómo se probará
        ↓
Qué evidencia permitirá aceptarla
        ↓
Qué release la estabilizará
```

No:

```text
Elegir agentes
→ crear Skills
→ añadir loops
→ conectar memoria
→ intentar descubrir después cómo encaja todo
```

---

# 1. Qué se está construyendo realmente

HugePlanning es un **sistema de desarrollo de software por fases, impulsado al máximo razonable por inteligencia artificial**, que deberá ser capaz de producir software real mediante procesos estructurados, trazables, verificables y progresivamente automatizables.

Sin embargo, HugePlanning no aparece terminado de una vez. También debe ser:

- investigado;
- diseñado;
- especificado;
- implementado;
- probado;
- evaluado;
- corregido;
- versionado;
- y validado.

Por tanto, existen varios niveles que no deben confundirse.

## 1.1. Los cuatro niveles

```text
Nivel 3 — Metaingeniería
Cómo investigamos, diseñamos, construimos, validamos y evolucionamos HugePlanning.

Nivel 2 — HugePlanning
El sistema de desarrollo por fases impulsado por IA.

Nivel 1 — Instancia de proyecto
Un proyecto concreto ejecutado utilizando HugePlanning.

Nivel 0 — Producto
La aplicación, web, servicio o sistema de software producido.
```

Este documento pertenece al **Nivel 3**.

No describe principalmente cómo HugePlanning ejecutará un proyecto. Describe cómo debe construirse HugePlanning de forma rigurosa.

---

# 2. Las dos arquitecturas que deben mantenerse separadas

HugePlanning necesita dos arquitecturas diferentes.

## 2.1. Arquitectura del sistema

Responde a preguntas como:

- ¿Cómo funcionará HugePlanning una vez operativo?
- ¿Qué fases tendrá?
- ¿Qué artefactos producirá?
- ¿Qué agentes, Skills, workflows y herramientas utilizará?
- ¿Cómo conservará estado?
- ¿Cómo gestionará memoria, contexto y trazabilidad?
- ¿Cómo transformará una idea en software entregable?

## 2.2. Arquitectura de construcción

Responde a preguntas distintas:

- ¿Cómo se decide qué debe contener HugePlanning?
- ¿Qué capacidades se construyen primero?
- ¿Qué hipótesis deben validarse?
- ¿Qué experimentos se ejecutan?
- ¿Qué evidencia permite aceptar una capacidad?
- ¿Cómo se modifica el roadmap?
- ¿Cómo se evita que el sistema se certifique a sí mismo?
- ¿Cómo se usa IA para desarrollar HugePlanning sin perder control?

La relación entre ambas debe ser explícita:

```text
Capacidad final de HugePlanning
        ↓
Etapa que la introduce
        ↓
Hipótesis que intenta demostrar
        ↓
Implementación
        ↓
Experimento
        ↓
Evidencia
        ↓
Release que la estabiliza
```

---

# 3. La tesis principal del programa

Antes del roadmap debe existir una tesis general.

## 3.1. Tesis de trabajo

> Es posible construir un sistema de desarrollo de software por fases, dirigido por artefactos y asistido intensamente por IA, que permita ejecutar proyectos complejos con mayor rigor, trazabilidad, consistencia y autonomía, manteniendo control humano sobre las decisiones críticas.

Esta tesis no debe aceptarse por intuición. Debe descomponerse en hipótesis comprobables.

## 3.2. Hipótesis fundamentales

### H1 — Ejecución significativa por IA

La IA puede ejecutar partes sustanciales del ciclo de desarrollo sin reducir el proceso a generación improvisada de código.

### H2 — Coherencia mediante artefactos

Los artefactos estructurados pueden mantener coherencia entre fases, sesiones, agentes y modelos.

### H3 — Encapsulación de responsabilidades

Skills, agentes, scripts y workflows pueden encapsular responsabilidades sin duplicar conocimiento ni crear dependencias incontrolables.

### H4 — Continuidad externa a la conversación

El sistema puede mantener continuidad mediante repositorio, estado persistente, decisiones y artefactos, sin depender de una conversación infinita.

### H5 — Control mediante validación

Schemas, pruebas, hooks, evaluadores y gates humanos pueden reducir errores y evitar falsas finalizaciones.

### H6 — Adaptabilidad

La metodología puede adaptarse a proyectos de distintos tamaños y tipos sin requerir un sistema diferente para cada uno.

### H7 — Coste y complejidad razonables

El consumo de tokens, la complejidad operativa y la sobrecarga documental pueden mantenerse bajo control.

### H8 — Operabilidad individual

Una sola persona puede utilizar y gobernar el sistema sin necesitar un equipo de plataforma.

### H9 — Calidad profesional

Los resultados pueden alcanzar un estándar profesional en requisitos, arquitectura, planificación, implementación, validación y entrega.

### H10 — Evolución acumulativa

Cada etapa validada puede servir de infraestructura para construir las siguientes sin volver frágil el sistema.

Estas hipótesis deben evolucionar. Pueden quedar:

- confirmadas;
- parcialmente confirmadas;
- pendientes;
- refutadas;
- o reformuladas.

---

# 4. Invariantes del sistema

Antes de diseñar componentes deben definirse propiedades que el sistema debe preservar.

## 4.1. Invariantes de información

1. El repositorio es la fuente canónica del proyecto.
2. Las conversaciones no son la memoria principal.
3. Cada concepto importante tiene una única fuente canónica.
4. Hechos, supuestos, decisiones, propuestas y preguntas deben distinguirse.
5. Toda decisión relevante debe registrar su razón.
6. Los artefactos deben ser versionables y revisables.
7. La información crítica no debe existir únicamente en resúmenes generados.

## 4.2. Invariantes de proceso

1. Cada fase tiene entradas, precondiciones, salidas y criterios de finalización.
2. Una fase no se considera completa solo porque un agente lo declare.
3. Los resultados deben verificarse mediante mecanismos adecuados.
4. Las transiciones importantes requieren evidencia.
5. Las acciones críticas deben ser observables y reversibles cuando sea posible.
6. Las decisiones irreversibles o de negocio requieren aprobación humana.
7. Ningún loop debe carecer de condición de parada.
8. Las tareas bloqueadas deben terminar como `BLOCKED`, no fingir éxito.

## 4.3. Invariantes de arquitectura de IA

1. Los modelos deben ser reemplazables.
2. Las Skills no deben contener estado específico de una instancia de proyecto.
3. La memoria persistente debe tener propósito y límites.
4. Los agentes deben recibir el contexto mínimo suficiente, no todo el proyecto.
5. Las herramientas deben concederse según responsabilidad.
6. El mismo agente no debe diseñar, implementar, evaluar y aprobar una capacidad crítica sin revisión independiente.
7. El sistema debe preferir software determinista cuando una tarea pueda resolverse de forma determinista.
8. La autonomía debe ser proporcional a la capacidad de validación.

## 4.4. Invariantes de evolución

1. Las etapas futuras son hipótesis, no contratos inmutables.
2. El roadmap debe poder cambiar mediante evidencia.
3. Cada defecto importante debe producir aprendizaje reutilizable.
4. Una versión puede ayudar a construir la siguiente, pero no redefinir sin supervisión los criterios mediante los que será aprobada.
5. La complejidad se introduce cuando resuelve un problema observado.

---

# 5. El kernel meta

Para evitar una regresión infinita del tipo “plan del plan del plan”, HugePlanning necesita un **kernel meta pequeño y estable**.

Este kernel no es otro sistema complejo. Es el conjunto mínimo de reglas que gobierna cómo se desarrolla HugePlanning.

## 5.1. Responsabilidades del kernel

Debe definir:

1. Cómo se formulan hipótesis.
2. Cómo se registran evidencias.
3. Cómo se documentan decisiones.
4. Cómo se define una etapa.
5. Cómo se especifican experimentos.
6. Cómo se clasifican defectos.
7. Cómo se valida una implementación.
8. Cómo se modifica el roadmap.
9. Cómo se aprueba un release.
10. Cómo se aplican gates humanos.
11. Cómo se versionan artefactos.
12. Cómo se conserva trazabilidad.
13. Cómo se determina que no hay progreso.
14. Cómo se interrumpe una línea de trabajo fallida.

## 5.2. Qué no debe hacer el kernel

No debe:

- especificar todos los agentes futuros;
- decidir todos los workflows;
- contener todos los prompts;
- fijar de forma permanente toda la arquitectura;
- absorber los detalles de cada etapa;
- convertirse en otro HugePlanning completo.

Su función es ofrecer gobernanza mínima estable.

---

# 6. Las unidades fundamentales del plan

La fase no debe ser la única unidad de planificación. HugePlanning debe trabajar con varias unidades conectadas.

## 6.1. Capacidad

Una capacidad describe algo que HugePlanning debe ser capaz de hacer.

Ejemplos:

- conservar estado;
- ejecutar discovery;
- generar requisitos;
- validar artefactos;
- delegar subtareas;
- seleccionar modelos;
- gestionar cambios;
- verificar implementación;
- recuperar una sesión;
- mantener trazabilidad.

## 6.2. Hipótesis

Describe por qué creemos que una capacidad o diseño funcionará.

## 6.3. Decisión

Registra qué opción se adopta, por qué y con qué consecuencias.

## 6.4. Incremento validable

Es una porción vertical del sistema que puede implementarse y evaluarse.

## 6.5. Experimento

Es el procedimiento utilizado para comprobar una hipótesis o propiedad.

## 6.6. Evidencia

Son los resultados observables que apoyan o contradicen una conclusión.

## 6.7. Release

Es el punto en el que una capacidad alcanza un nivel de estabilidad aceptado.

La cadena completa debe poder rastrearse:

```text
Capacidad
→ hipótesis
→ decisión
→ incremento
→ implementación
→ experimento
→ evidencia
→ release
```

---

# 7. Capability map de HugePlanning

La planificación debe comenzar por las capacidades, no por los agentes.

## 7.1. Gobierno y control

- gobernanza del proyecto;
- gestión de decisiones;
- gestión de versiones;
- gates humanos;
- gestión de riesgos;
- control de cambios;
- auditoría;
- recuperación ante errores.

## 7.2. Estado y memoria

- estado persistente;
- reanudación de sesiones;
- memoria de proyecto;
- registro de decisiones;
- preguntas abiertas;
- contexto activo;
- historial de ejecuciones;
- políticas de retención.

## 7.3. Artefactos y trazabilidad

- contratos de artefactos;
- schemas;
- identificadores;
- relaciones entre artefactos;
- source of truth;
- generación de vistas;
- validación estructural;
- trazabilidad extremo a extremo.

## 7.4. Ejecución de fases

- discovery;
- requirements engineering;
- arquitectura;
- UX;
- planificación;
- descomposición de tareas;
- implementación;
- testing;
- seguridad;
- accesibilidad;
- entrega;
- mantenimiento.

## 7.5. Orquestación de IA

- selección de Skills;
- delegación;
- routing de modelos;
- gestión de herramientas;
- empaquetado de contexto;
- ejecución de subagentes;
- workflows;
- loops;
- stop conditions;
- observabilidad.

## 7.6. Validación

- pruebas deterministas;
- evaluaciones semánticas;
- revisión humana;
- comparación de modelos;
- golden scenarios;
- smoke tests;
- regresiones;
- clasificación de defectos.

## 7.7. Operación

- coste y consumo;
- monitorización;
- depuración;
- repetibilidad;
- seguridad de credenciales;
- aislamiento;
- portabilidad;
- documentación operativa.

Cada capacidad debe responder:

```text
¿Qué problema resuelve?
¿De qué depende?
¿Qué entradas utiliza?
¿Qué produce?
¿Cómo se valida?
¿Qué riesgos introduce?
¿Cuándo debe implementarse?
```

---

# 8. Roadmap dirigido por dependencias

El roadmap no debe ser una lista intuitiva de funcionalidades.

## 8.1. Regla

> Una capacidad solo debe planificarse en detalle cuando sus dependencias conceptuales, operativas y de validación estén suficientemente maduras.

Ejemplo:

```text
Estado persistente ───────┐
                          ├→ ejecución de Skills
Contratos de artefactos ──┘          ↓
                                  subagentes
                                      ↓
                                  workflows
                                      ↓
                                     loops
```

Un loop autónomo depende de:

- estado observable;
- objetivo explícito;
- criterio de éxito;
- verificación;
- límite de iteraciones;
- detección de ausencia de progreso;
- recuperación;
- registro de acciones.

Por tanto, “añadir loops” no puede ser una etapa temprana aislada.

## 8.2. Orden lógico orientativo

```text
1. Bootstrap y entorno reproducible
2. Estado y artefactos canónicos
3. Contratos y schemas
4. Ejecución manual asistida
5. Validación determinista
6. Skills especializadas
7. Delegación controlada
8. Subagentes con contexto aislado
9. Evaluación independiente
10. Workflows reproducibles
11. Loops limitados y verificables
12. Self-hosting parcial
13. Automatización avanzada
```

Este orden puede cambiar, pero las dependencias deben permanecer explícitas.

---

# 9. Planificación por ondas sucesivas

No todas las etapas deben planificarse con la misma resolución.

## 9.1. Arquitectura global, detalle local

```text
Etapa actual      → especificación completa
Etapa siguiente   → diseño suficiente para preparar su inicio
Etapa posterior   → propósito, dependencias y riesgos
Etapas lejanas    → capacidades e hipótesis provisionales
```

Representación:

```text
S1  ██████████  detalle completo
S2  ███████░░░  diseño próximo
S3  ████░░░░░░  arquitectura preliminar
S4  ██░░░░░░░░  intención y dependencias
S5  █░░░░░░░░░  dirección provisional
```

## 9.2. Qué se especifica para cada horizonte

### Etapa actual

- tareas;
- contratos;
- schemas;
- tests;
- escenarios;
- responsables;
- herramientas;
- criterios de aceptación;
- release gate.

### Etapa siguiente

- objetivo;
- hipótesis;
- dependencias;
- interfaces;
- principales riesgos;
- resultados esperados.

### Etapas lejanas

- capacidad;
- razón de existencia;
- dependencia aproximada;
- riesgo sistémico;
- preguntas pendientes.

Esto evita gastar meses diseñando componentes que los aprendizajes tempranos volverán obsoletos.

---

# 10. El contrato de etapa

Cada etapa debe definirse como un incremento experimental y no como un simple bloque de trabajo.

## 10.1. Plantilla maestra

```yaml
stage:
  id: Sx
  name: Nombre de la etapa
  status: proposed | planned | active | validating | accepted | revised | rejected

purpose:
  statement: >
    Qué capacidad pretende introducir o demostrar.

system_capabilities:
  introduced: []
  extended: []
  stabilized: []

hypotheses:
  - id: H-Sx-01
    statement: >
      Hipótesis comprobable.
    falsification_conditions: []

dependencies:
  required_stages: []
  required_artifacts: []
  required_capabilities: []

inputs:
  canonical: []
  optional: []

outputs:
  canonical: []
  generated: []
  temporary: []

implementation_scope:
  included: []
  excluded: []

experiments:
  deterministic: []
  scenario_based: []
  live: []
  comparative: []

acceptance:
  required_checks: []
  quality_thresholds: []
  unresolved_limitations_allowed: []

failure_modes:
  known: []
  blocked_conditions: []
  rollback_strategy: []

human_gates:
  - gate: architecture_approval
    required: true

release:
  target_version: ""
  evidence_required: []

possible_decisions:
  - accept
  - accept_with_limitations
  - revise
  - redesign
  - reject_hypothesis
```

## 10.2. Preguntas obligatorias antes de activar una etapa

1. ¿Qué capacidad concreta introduce?
2. ¿Qué hipótesis prueba?
3. ¿Qué depende de esta etapa?
4. ¿Qué evidencia permitiría refutarla?
5. ¿Qué queda fuera?
6. ¿Qué artefactos serán canónicos?
7. ¿Qué puede comprobarse con scripts?
8. ¿Qué requiere evaluación semántica?
9. ¿Qué requiere decisión humana?
10. ¿Cómo se recupera el sistema si falla?
11. ¿Qué versión estabilizará el resultado?
12. ¿Qué aprendizaje debe alimentar el roadmap?

---

# 11. El doble ciclo de desarrollo

HugePlanning debe evolucionar mediante dos ciclos conectados.

## 11.1. Ciclo de conocimiento

```text
Pregunta
→ investigación
→ evidencia
→ interpretación
→ hipótesis
→ decisión de diseño
```

## 11.2. Ciclo de construcción

```text
Decisión de diseño
→ especificación
→ implementación
→ prueba
→ evaluación
→ aprendizaje
```

## 11.3. Ciclo completo

```text
Investigación
      ↓
Hipótesis
      ↓
Arquitectura provisional
      ↓
Implementación
      ↓
Experimento
      ↓
Resultado
      ↓
Revisión de la hipótesis
      ├── confirmada
      ├── parcialmente confirmada
      ├── necesita cambios
      └── rechazada
```

## 11.4. Regla de separación

El mismo proceso de IA no debe, sin controles independientes:

- proponer la hipótesis;
- seleccionar solo evidencia favorable;
- diseñar la solución;
- implementar;
- crear los tests;
- evaluar;
- y aprobar el release.

La independencia puede conseguirse mediante:

- agentes distintos;
- prompts separados;
- modelos distintos;
- ramas separadas;
- scripts deterministas;
- revisión humana;
- ejecuciones ciegas;
- comparaciones entre implementaciones.

No siempre se necesitan agentes permanentes. Lo importante es separar funciones.

---

# 12. Pases del programa de metaingeniería

Una etapa compleja puede seguir estos pases.

## Pass 1 — Investigación y recolección

Objetivo:

- reunir evidencia;
- identificar enfoques;
- detectar límites;
- registrar desacuerdos;
- evitar decidir demasiado pronto.

Salida:

- mapa de evidencia;
- fuentes;
- preguntas abiertas;
- riesgos;
- conceptos candidatos.

## Pass 2 — Síntesis

Objetivo:

- convertir evidencia en modelos comprensibles;
- comparar alternativas;
- proponer una arquitectura provisional.

Salida:

- síntesis;
- opciones;
- trade-offs;
- propuesta.

## Pass 3 — Falsificación y crítica

Objetivo:

- buscar fallos;
- escenarios adversos;
- dependencias ocultas;
- supuestos débiles;
- riesgos de coste o complejidad.

Salida:

- objeciones;
- condiciones de falsificación;
- modificaciones necesarias.

## Pass 4 — Decisión arquitectónica

Objetivo:

- seleccionar una opción;
- registrar razones;
- definir consecuencias;
- establecer revisión futura.

Salida:

- ADR o registro de decisión.

## Pass 5 — Especificación del incremento

Objetivo:

- convertir la decisión en un contrato implementable;
- definir interfaces, artefactos, schemas y aceptación.

## Pass 6 — Implementación

Objetivo:

- realizar cambios limitados a la etapa;
- mantener trazabilidad;
- evitar expansión de alcance.

## Pass 7 — Evaluación independiente

Objetivo:

- ejecutar tests;
- escenarios;
- revisión semántica;
- análisis comparativo;
- clasificación de defectos.

## Pass 8 — Decisión de release

Objetivo:

- aceptar;
- aceptar con limitaciones;
- revisar;
- rediseñar;
- o rechazar.

---

# 13. Arquitectura de evaluación

Una capacidad no está terminada porque “parece funcionar”.

## 13.1. Capas de evaluación

### Nivel 1 — Validación estructural

- archivos presentes;
- schemas válidos;
- formatos correctos;
- referencias existentes;
- campos obligatorios;
- consistencia básica.

### Nivel 2 — Pruebas deterministas

- tests unitarios;
- integración;
- contratos;
- validadores;
- invariantes;
- regresiones.

### Nivel 3 — Escenarios controlados

- casos nominales;
- casos límite;
- información incompleta;
- contradicciones;
- cambios;
- recuperación;
- intentos adversos.

### Nivel 4 — Evaluación semántica

- calidad de razonamiento;
- cobertura;
- coherencia;
- fidelidad;
- relevancia;
- claridad;
- ausencia de invenciones.

### Nivel 5 — Ejecución real

- smoke test;
- proyecto piloto;
- interacción humana;
- restricciones reales;
- coste y duración;
- problemas operativos.

### Nivel 6 — Revisión humana

- aceptación;
- juicio profesional;
- riesgos;
- utilidad;
- confianza;
- decisión de release.

## 13.2. Golden scenarios

Deben existir escenarios estables que permitan comprobar regresiones.

Cada escenario debería tener:

```yaml
scenario:
  id: GS-001
  purpose: ""
  inputs: []
  expected_properties: []
  forbidden_behaviors: []
  review_rubric: ""
  deterministic_checks: []
```

No siempre se necesita una salida exacta. Pueden comprobarse propiedades.

## 13.3. Clasificación de defectos

```text
D1 — Error de implementación
D2 — Error de especificación
D3 — Error de arquitectura
D4 — Falta de contexto
D5 — Instrucción ambigua
D6 — Herramienta inadecuada
D7 — Modelo insuficiente
D8 — Evaluación incorrecta
D9 — Problema de coste
D10 — Problema de operabilidad
D11 — Hipótesis refutada
D12 — Limitación aceptada
```

La clasificación importa porque cada defecto debe corregirse en la capa adecuada.

---

# 14. Sistema de aprendizaje

Cada defecto significativo debe producir una mejora trazable.

```text
Defecto observado
        ↓
Reproducción
        ↓
Causa probable
        ↓
Clasificación
        ↓
Corrección
        ↓
Nueva prueba
        ↓
Prevención de regresión
        ↓
Actualización de arquitectura o reglas
```

## 14.1. Registro recomendado

```yaml
defect:
  id: DEF-0001
  stage: Sx
  scenario: GS-001
  symptom: ""
  impact: ""
  classification: D1
  root_cause: ""
  correction: ""
  regression_test: ""
  affected_decisions: []
  roadmap_impact: ""
  status: open | fixed | accepted_limitation
```

## 14.2. Regla

No todo defecto exige añadir una regla global.

Primero debe decidirse si es:

- accidental;
- local;
- recurrente;
- sistémico;
- o una limitación inevitable.

Demasiadas reglas reactivas pueden volver el sistema rígido y contradictorio.

---

# 15. Gobernanza de decisiones

Las decisiones arquitectónicas deben sobrevivir a chats y modelos.

## 15.1. Registro de decisión

```yaml
decision:
  id: DEC-0001
  title: ""
  status: proposed | accepted | superseded | rejected
  context: ""
  decision: ""
  alternatives:
    - option: ""
      reasons_against: []
  evidence: []
  consequences:
    positive: []
    negative: []
  assumptions: []
  revisit_when: []
  affected_capabilities: []
  affected_stages: []
```

## 15.2. Qué merece una decisión formal

- cambio de source of truth;
- nuevo tipo de memoria;
- introducción de agentes;
- introducción de loops;
- cambio de modelo de artefactos;
- nueva dependencia crítica;
- cambio de release policy;
- modificación del kernel meta;
- aceptación de una limitación relevante;
- decisión difícil de revertir.

## 15.3. Qué no necesita un ADR

- nombres menores;
- reorganizaciones triviales;
- decisiones locales fácilmente reversibles;
- detalles de implementación sin impacto sistémico.

---

# 16. El papel de la IA durante la construcción

La IA puede participar en el nivel meta, pero sus roles deben distinguirse de los componentes que existirán dentro de HugePlanning.

## 16.1. Roles de IA para construir HugePlanning

- investigador;
- sintetizador;
- crítico;
- arquitecto;
- planificador;
- implementador;
- tester;
- evaluador;
- analista de defectos;
- documentador;
- revisor de coherencia;
- comparador de alternativas.

## 16.2. Componentes de IA que formarán parte de HugePlanning

- entrevistador;
- analista de requisitos;
- planificador técnico;
- generador de artefactos;
- implementador;
- revisor;
- orquestador;
- evaluador;
- gestor de cambios.

No deben confundirse.

Un agente utilizado para revisar el roadmap de HugePlanning no tiene por qué formar parte del producto final.

## 16.3. Regla de asignación

Antes de crear un agente, preguntar:

1. ¿La tarea es repetible?
2. ¿Necesita contexto aislado?
3. ¿Requiere herramientas distintas?
4. ¿Se beneficia de un modelo diferente?
5. ¿Debe ser independiente del generador?
6. ¿Produce un artefacto propio?
7. ¿Existe un criterio claro de éxito?
8. ¿No puede resolverla mejor un script?
9. ¿Su coste está justificado?

Si la mayoría de respuestas son negativas, probablemente no necesita ser un agente.

---

# 17. Cuándo introducir cada mecanismo

## 17.1. Skill

Introducir cuando:

- existe un procedimiento especializado;
- se repite;
- necesita instrucciones detalladas;
- no debe cargarse siempre;
- puede ejecutarlo el agente principal.

## 17.2. Subagente

Introducir cuando:

- la tarea llenaría el contexto principal;
- necesita independencia;
- requiere un modelo distinto;
- usa herramientas específicas;
- produce un resultado autocontenido;
- puede recibir un contrato pequeño.

## 17.3. Evaluador independiente

Introducir cuando:

- el generador tiende a aprobar su propio trabajo;
- los criterios son semánticos;
- existe riesgo alto;
- se necesita perspectiva adversarial.

## 17.4. Hook

Introducir cuando:

- una regla debe cumplirse siempre;
- no basta con confiar en instrucciones;
- existe una comprobación objetiva;
- se necesita impedir una acción;
- se necesita bloquear una finalización.

## 17.5. Workflow

Introducir cuando:

- el proceso debe repetirse;
- tiene ramas o pasos claros;
- intervienen varios ejecutores;
- importa mantener resultados intermedios fuera del contexto;
- la reproducibilidad compensa la complejidad.

## 17.6. Loop

Introducir únicamente cuando:

- el objetivo es verificable;
- existe progreso medible;
- hay límite de iteraciones;
- se detecta estancamiento;
- existe condición de bloqueo;
- el coste está controlado.

## 17.7. Memoria persistente

Introducir cuando:

- existe información reutilizable entre sesiones;
- tiene dueño y política;
- puede revisarse;
- no duplica el estado canónico;
- se conoce cuándo debe actualizarse o eliminarse.

---

# 18. Incrementos verticales

HugePlanning debe construirse verticalmente.

Un incremento vertical incluye:

```text
Capacidad
+ estado
+ artefactos
+ ejecución
+ validación
+ experimentos
+ documentación
```

Ejemplo:

```text
Existe una tarea de discovery
→ el runtime la activa
→ se ejecuta la entrevista
→ se conserva el estado
→ se produce el artefacto
→ se valida
→ se detectan defectos
→ puede reanudarse
→ puede cerrarse correctamente
```

## 18.1. Qué evitar

No construir por separado:

```text
primero todos los agentes
después todos los schemas
después toda la memoria
después todos los workflows
y al final probar si encajan
```

Eso produce integración tardía y arquitectura especulativa.

---

# 19. Self-hosting controlado

HugePlanning puede utilizar gradualmente sus propias capacidades para construirse.

## 19.1. Etapa 1 — Construcción externa

Se utilizan:

- prompts;
- chats;
- Claude Code;
- repositorio;
- documentos;
- revisión humana;
- scripts manuales.

HugePlanning todavía no gestiona su propia evolución.

## 19.2. Etapa 2 — Self-hosting parcial

Las capacidades ya validadas ayudan a construir las siguientes.

Ejemplos:

- el runtime validado gestiona etapas nuevas;
- el sistema de tareas genera task packets;
- la trazabilidad existente conecta nuevas decisiones;
- el sistema de evaluación revisa nuevos incrementos.

## 19.3. Etapa 3 — Self-hosting controlado

HugePlanning puede:

- descubrir una nueva capacidad;
- generar especificación;
- planificar;
- delegar;
- implementar;
- ejecutar pruebas;
- generar una evaluación.

Pero debe mantenerse esta regla:

> Una versión de HugePlanning puede ayudar a construir la siguiente, pero no debe poder redefinir sin supervisión los criterios mediante los que será aprobada.

## 19.4. Áreas que deben permanecer especialmente protegidas

- kernel meta;
- política de releases;
- criterios de seguridad;
- permisos;
- gates humanos;
- definición de evidencia suficiente;
- cambios irreversibles;
- aceptación de riesgos.

---

# 20. Control del contexto en el nivel meta

El desarrollo de HugePlanning también puede sufrir context rot.

## 20.1. Qué debe vivir fuera de la conversación

- estado actual;
- decisiones;
- roadmap;
- hipótesis;
- resultados experimentales;
- defectos;
- artefactos;
- criterios de aceptación;
- tareas activas;
- preguntas abiertas.

## 20.2. Paquete mínimo para una tarea de metaingeniería

```text
Objetivo
+ etapa
+ hipótesis
+ artefactos autorizados
+ decisión relevante
+ restricciones
+ entregable
+ criterios de aceptación
+ condición de parada
```

## 20.3. Resultado mínimo de un subproceso

```json
{
  "status": "complete",
  "artifact": "path/to/output",
  "findings": [],
  "risks": [],
  "blocked_by": [],
  "recommended_next_action": ""
}
```

Los detalles extensos deben permanecer en artefactos.

---

# 21. Arquitectura documental mínima

No es necesario mantener decenas de documentos con información duplicada.

## 21.1. Columna vertebral recomendada

```text
00-meta-charter.md
01-capability-map.md
02-roadmap-and-stage-registry.md
03-meta-kernel-and-governance.md
04-evaluation-architecture.md
05-decision-log.md
06-experiment-registry.md
07-defect-and-learning-log.md
```

También pueden existir carpetas:

```text
stages/
decisions/
experiments/
evidence/
defects/
releases/
```

## 21.2. Función de cada documento

### `00-meta-charter.md`

- visión;
- tesis;
- alcance;
- no alcance;
- invariantes;
- definición de éxito.

### `01-capability-map.md`

- capacidades;
- dependencias;
- estado de madurez;
- etapa prevista.

### `02-roadmap-and-stage-registry.md`

- etapas;
- objetivos;
- dependencias;
- estado;
- release target.

### `03-meta-kernel-and-governance.md`

- reglas del programa;
- gates;
- control de cambios;
- roles;
- autoridad.

### `04-evaluation-architecture.md`

- capas de evaluación;
- escenarios;
- métricas;
- criterios de aceptación.

### `05-decision-log.md`

Índice de decisiones y enlaces a registros detallados.

### `06-experiment-registry.md`

Experimentos planificados, ejecutados y resultados.

### `07-defect-and-learning-log.md`

Defectos, causas, correcciones y aprendizaje.

## 21.3. Regla de unicidad

Cada concepto debe tener una única fuente canónica.

Ejemplo:

- la etapa vive en el stage registry;
- la decisión vive en su ADR;
- el resultado vive en el experimento;
- el estado de un defecto vive en el defect log.

Los resúmenes pueden enlazar, pero no reescribir la verdad completa.

---

# 22. Matriz maestra de trazabilidad

Debe poder mantenerse una tabla como esta:

| Capacidad | Hipótesis | Decisión | Etapa | Implementación | Experimento | Evidencia | Release | Estado |
|---|---|---|---|---|---|---|---|---|
| Estado persistente | H-001 | DEC-004 | S0b | runtime/state | EXP-003 | EV-010 | v0.x | estable |
| Discovery | H-012 | DEC-018 | S1 | discovery module | EXP-021 | EV-034 | v0.x | validando |
| Requirements | H-020 | pendiente | S2 | pendiente | pendiente | pendiente | futura | propuesta |

Esta matriz conecta:

- el sistema que se quiere terminar;
- el programa mediante el que se construye;
- la evidencia que justifica el avance.

---

# 23. Métricas del programa

No debe medirse solo cuántas funciones se implementan.

## 23.1. Métricas de calidad

- tasa de escenarios superados;
- defectos por etapa;
- regresiones;
- coherencia entre artefactos;
- cobertura de trazabilidad;
- errores detectados antes del release;
- falsos positivos de validación.

## 23.2. Métricas de operabilidad

- tiempo de preparación de una etapa;
- tiempo de reanudación;
- número de pasos manuales;
- dificultad de depuración;
- claridad del estado;
- facilidad de revisión humana.

## 23.3. Métricas de IA

- tokens por capacidad;
- número de iteraciones;
- porcentaje de trabajo repetido;
- contexto medio;
- tasa de tareas bloqueadas correctamente;
- diferencias entre modelos;
- frecuencia de correcciones humanas.

## 23.4. Métricas de arquitectura

- duplicación documental;
- número de componentes por capacidad;
- dependencias circulares;
- estabilidad de interfaces;
- cantidad de reglas globales;
- cambios de roadmap derivados de evidencia.

## 23.5. Métrica decisiva

> ¿La nueva complejidad mejora de forma demostrable la calidad, control, coste o velocidad?

Si no, debe reconsiderarse.

---

# 24. Gates del plan maestro

## Gate 1 — Claridad de la tesis

- ¿Está claro qué se intenta demostrar?
- ¿Las hipótesis son comprobables?
- ¿Existe una definición de éxito?

## Gate 2 — Capacidad

- ¿La capacidad resuelve un problema real?
- ¿Está diferenciada de otras?
- ¿Tiene dependencias identificadas?

## Gate 3 — Arquitectura

- ¿Se han comparado alternativas?
- ¿La decisión está registrada?
- ¿La complejidad está justificada?

## Gate 4 — Especificación

- ¿La etapa tiene contrato?
- ¿Entradas y salidas son explícitas?
- ¿Existe estrategia de recuperación?

## Gate 5 — Implementación

- ¿El alcance está controlado?
- ¿Existe trazabilidad con la decisión?
- ¿Las interfaces se respetan?

## Gate 6 — Validación

- ¿Se ejecutaron pruebas deterministas?
- ¿Se completaron escenarios?
- ¿Se clasificaron defectos?
- ¿Se repitieron casos corregidos?

## Gate 7 — Release

- ¿La evidencia es suficiente?
- ¿Las limitaciones están documentadas?
- ¿La persona responsable aprueba?
- ¿La siguiente etapa puede apoyarse en esta?

---

# 25. Antipatrones que deben evitarse

## 25.1. Diseñar agentes antes que capacidades

Síntoma:

- lista de agentes;
- responsabilidades solapadas;
- entradas y salidas difusas.

Corrección:

- volver al capability map;
- definir contratos;
- asignar ejecutores después.

## 25.2. Mega-prompt como arquitectura

Síntoma:

- instrucciones de decenas de páginas;
- reglas contradictorias;
- consumo elevado;
- difícil mantenimiento.

Corrección:

```text
principios → instrucciones base
procedimientos → Skills
estado → archivos
datos → schemas
validación → scripts/hooks
orquestación → workflows
```

## 25.3. Planificación total anticipada

Síntoma:

- detalle extremo en etapas lejanas;
- grandes reescrituras;
- sensación de no empezar nunca.

Corrección:

- rolling-wave planning;
- arquitectura global;
- detalle solo en el horizonte próximo.

## 25.4. Automatización sin verificación

Síntoma:

- el agente declara éxito;
- no existen tests;
- no se conoce el estado real.

Corrección:

- criterios observables;
- validadores;
- gates;
- stop conditions.

## 25.5. Autocertificación

Síntoma:

- el mismo agente propone, implementa, revisa y aprueba.

Corrección:

- separar funciones;
- usar revisión independiente;
- introducir controles deterministas;
- gate humano.

## 25.6. Memoria sin gobernanza

Síntoma:

- archivos crecientes;
- hechos antiguos;
- contradicciones;
- duplicación.

Corrección:

- propósito;
- dueño;
- tamaño;
- revisión;
- caducidad;
- fuente canónica.

## 25.7. Complejidad por moda

Síntoma:

- GraphRAG, multiagentes, loops o MCP sin necesidad demostrada.

Corrección:

- introducir cada mecanismo únicamente para resolver un fallo observado.

## 25.8. Confundir self-hosting con autonomía total

Síntoma:

- HugePlanning modifica sus criterios;
- aprueba sus propios cambios;
- elimina gates.

Corrección:

- proteger kernel, releases y seguridad;
- mantener autoridad humana.

---

# 26. Proceso operativo para planificar una nueva etapa

## Paso 1 — Identificar la capacidad

```text
¿Qué debe ser capaz de hacer HugePlanning que hoy no puede hacer?
```

## Paso 2 — Justificarla

```text
¿Qué problema resuelve?
¿Qué ocurre si no existe?
```

## Paso 3 — Formular hipótesis

```text
¿Qué creemos que funcionará?
¿Qué observación demostraría que estamos equivocados?
```

## Paso 4 — Revisar dependencias

```text
¿Qué capacidades previas necesita?
¿Están realmente estables?
```

## Paso 5 — Investigar solo lo necesario

```text
¿Qué decisiones no pueden tomarse todavía por falta de conocimiento?
```

## Paso 6 — Comparar alternativas

```text
¿Qué opciones existen?
¿Cuáles son sus trade-offs?
```

## Paso 7 — Registrar decisión

```text
¿Qué se elige?
¿Por qué?
¿Qué consecuencias se aceptan?
```

## Paso 8 — Crear contrato de etapa

- alcance;
- interfaces;
- artefactos;
- pruebas;
- riesgos;
- gates;
- release.

## Paso 9 — Diseñar experimentos antes de implementar

```text
¿Cómo sabremos que funciona?
```

## Paso 10 — Implementar un incremento vertical

No construir infraestructura genérica sin demostrarla en una capacidad real.

## Paso 11 — Evaluar

- scripts;
- tests;
- escenarios;
- revisión;
- coste;
- operabilidad.

## Paso 12 — Clasificar resultados

- éxito;
- éxito parcial;
- limitación;
- defecto;
- hipótesis refutada.

## Paso 13 — Actualizar el sistema de conocimiento

- decisiones;
- roadmap;
- defectos;
- pruebas;
- documentación.

## Paso 14 — Aprobar o rechazar release

No avanzar solo por cansancio o inercia.

---

# 27. Checklist de uso permanente

Antes de añadir una nueva pieza, preguntar:

## Sobre el problema

- [ ] ¿Qué problema real resuelve?
- [ ] ¿Se ha observado o solo se imagina?
- [ ] ¿Existe una solución más simple?

## Sobre la arquitectura

- [ ] ¿Qué capacidad representa?
- [ ] ¿De qué depende?
- [ ] ¿Qué interfaz modifica?
- [ ] ¿Está registrada la decisión?

## Sobre IA

- [ ] ¿Necesita un agente?
- [ ] ¿Basta una Skill?
- [ ] ¿Puede ser un script?
- [ ] ¿Necesita memoria?
- [ ] ¿Qué modelo es suficiente?
- [ ] ¿Qué contexto mínimo necesita?
- [ ] ¿Qué herramientas puede usar?

## Sobre control

- [ ] ¿Qué significa terminar?
- [ ] ¿Cómo se valida?
- [ ] ¿Cuál es el máximo de iteraciones?
- [ ] ¿Cómo se detecta ausencia de progreso?
- [ ] ¿Cómo se representa `BLOCKED`?
- [ ] ¿Qué gate humano existe?

## Sobre evidencia

- [ ] ¿Qué experimento lo demuestra?
- [ ] ¿Qué resultado lo refutaría?
- [ ] ¿Cómo se evita la autocertificación?
- [ ] ¿Cómo se previene una regresión?

## Sobre evolución

- [ ] ¿La etapa futura necesita modificarse?
- [ ] ¿Se ha actualizado la trazabilidad?
- [ ] ¿Se ha documentado el aprendizaje?
- [ ] ¿La complejidad añadida está justificada?

---

# 28. Principios que deben recordarse siempre

1. **Planificar HugePlanning no es lo mismo que usar HugePlanning.**
2. **La arquitectura de construcción es distinta de la arquitectura del sistema final.**
3. **Los agentes son instrumentos, no el punto de partida.**
4. **Las capacidades y dependencias determinan el roadmap.**
5. **Cada etapa debe ser un incremento vertical validable.**
6. **Toda hipótesis debe poder fallar.**
7. **Toda finalización importante debe verificarse.**
8. **El repositorio y los artefactos son la memoria canónica.**
9. **La planificación debe tener resolución progresiva.**
10. **Las fases lejanas son provisionales.**
11. **La IA no debe certificar sin controles el sistema que ella misma diseñó.**
12. **Los errores deben transformarse en pruebas o aprendizaje.**
13. **La autonomía crece solo cuando la validación puede soportarla.**
14. **El self-hosting debe ser gradual y gobernado.**
15. **La complejidad debe pagar su coste.**
16. **Un script es mejor que un agente para una comprobación determinista.**
17. **Un buen sistema conserva decisiones, no conversaciones infinitas.**
18. **Una versión puede construir la siguiente, pero no redefinir sola la vara con la que será medida.**
19. **El objetivo no es escribir el plan perfecto, sino construir una máquina controlada de aprendizaje y evolución.**
20. **El siguiente paso debe depender de evidencia, no de entusiasmo.**

---

# 29. Definición final del plan maestro

HugePlanning debe desarrollarse como un programa de I+D e ingeniería de sistemas:

```text
Visión relativamente estable
        ↓
Tesis e hipótesis
        ↓
Capability map
        ↓
Dependencias
        ↓
Arquitectura provisional
        ↓
Etapa de alta resolución
        ↓
Incremento vertical
        ↓
Experimento
        ↓
Evidencia
        ↓
Decisión
        ↓
Release
        ↓
Aprendizaje
        ↓
Roadmap revisado
```

El resultado buscado no es solamente un sistema capaz de producir software.

El resultado buscado es:

> **Un sistema capaz de evolucionar de forma controlada, aprender de sus ejecuciones, conservar trazabilidad, utilizar IA de manera intensiva sin delegar ciegamente el juicio, y demostrar progresivamente que sus capacidades funcionan.**

Ese es el auténtico plan del plan.

---

# 30. Resumen ejecutivo de una página

## Qué se construye

Un sistema de desarrollo de software por fases impulsado por IA.

## Qué planifica este documento

Cómo investigar, diseñar, construir, validar y evolucionar ese sistema.

## Punto de partida

```text
tesis
→ hipótesis
→ capacidades
→ dependencias
```

## Unidad de progreso

```text
incremento vertical validable
```

## Unidad de verdad

```text
artefactos versionados en el repositorio
```

## Unidad de decisión

```text
decisión registrada con evidencia y consecuencias
```

## Unidad de validación

```text
experimento + criterios de aceptación + gate
```

## Estrategia temporal

```text
arquitectura global
+ detalle profundo solo en la etapa actual
```

## Papel de la IA

```text
investigar, proponer, implementar, evaluar y documentar
sin monopolizar la aprobación ni redefinir sola las reglas
```

## Regla de autonomía

```text
más autonomía solo cuando exista más capacidad de observación,
validación, parada y recuperación
```

## Regla de complejidad

```text
no introducir agentes, workflows, loops, memoria o grafos
hasta que resuelvan un problema observado
```

## Objetivo final

Construir HugePlanning y, al mismo tiempo, construir un proceso fiable para que HugePlanning pueda continuar evolucionando sin perder control.
