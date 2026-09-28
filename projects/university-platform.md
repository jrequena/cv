# Plataforma universitaria de gestión académica y de investigación

**Contexto:** GNBIT\
**Mi rol:** diseño y construcción desde cero, puesta en producción, mantenimiento y, desde 2023, liderazgo técnico del equipo (3–5 desarrolladores)

---

## En cifras

| | |
|---|---|
| Módulos | **más de 10** |
| Usuarios | **más de 5.000** |
| Tesis y proyectos gestionados | **miles** |
| Registros relacionados en la base de datos | **más de 100.000** |
| Tiempo de aprobación | **de semanas a días** |

---

## Problema

La gestión de tesis y proyectos de investigación de la universidad dependía de procesos manuales y descentralizados:

- no se sabía en qué estado estaba cada tesis o proyecto;
- los documentos se gestionaban en papel, sin control de versiones;
- la comunicación entre estudiantes, investigadores, evaluadores y administración era lenta;
- los datos de docentes e investigadores estaban dispersos entre sistemas;
- el gasto de los proyectos se controlaba a mano, con riesgo de superar el presupuesto.

## Solución

Una plataforma web centralizada que cubre el ciclo de vida completo de tesis y proyectos de investigación. Entre sus más de 10 módulos están:

- **Registro de tesis y proyectos** con integrantes, investigadores y cursos.
- **Flujo de revisión, evaluación y aprobación**, con estados y asignación de evaluadores.
- **Enmiendas** a proyectos ya aprobados.
- **Gestión documental**: carga de archivos, tipos y estados de documento, versionado y documentos asociados a proyectos y enmiendas.
- **Integración con el sistema de RRHH** de la institución para mantener actualizados docentes, investigadores y estudiantes.
- **Gestión económica de proyectos**: registro de facturas de bienes y servicios y control del presupuesto asignado frente al ejecutado.
- **Control de acceso por roles** (estudiante, evaluador, administrador).

---

## Arquitectura

Arquitectura cliente-servidor con frontend y backend desacoplados:

- **Backend:** PHP. Los módulos legacy están en Zend Framework y los nuevos en Laminas / Mezzio.
- **APIs:** REST y GraphQL.
- **Frontend:** Angular + TypeScript (Signals, NG-Zorro, Apollo Client) en los módulos nuevos; jQuery en los legacy.
- **Seguridad:** OAuth2 y control de acceso basado en roles.
- **Base de datos:** MySQL / MariaDB.

### Evolución incremental

La plataforma no se reescribió de golpe. Las partes legacy y las modernas **conviven en producción**, y los módulos se migran y refactorizan de forma progresiva. Así el sistema sigue dando servicio a más de 5.000 usuarios mientras se moderniza.

---

## Decisiones técnicas

### APIs desacopladas
- API REST y GraphQL (consumida con Apollo desde Angular), independientes del frontend.
- Permiten evolucionar frontend y backend por separado e integrar otros sistemas.

### Modelo de datos
- Modelo relacional normalizado con más de 100.000 registros interrelacionados.
- Índices en las columnas que usan las consultas críticas.
- Transacciones e integridad referencial en las operaciones de aprobación y de gasto.

### Integración y calidad de datos
- Sincronización con el sistema de RRHH institucional como fuente de docentes, investigadores y estudiantes.
- Actualizaciones masivas, eliminación de duplicados y detección de registros huérfanos.

### Reglas del módulo económico
- No se aprueba un gasto si `gasto_actual + nuevo_gasto > presupuesto_total`.
- Todo gasto se clasifica obligatoriamente como bien o servicio.
- Estados de gasto: registrado → aprobado / rechazado.

---

## Resultados

- **Proceso 100% digital:** sin papel ni gestión manual.
- **Aprobaciones de semanas a días.**
- **Trazabilidad completa** del estado de cada tesis y proyecto.
- **Menos errores e incidencias** administrativas.

---

## IA en el mantenimiento del sistema

En el día a día del equipo uso agentes de IA y servidores MCP para:

- consultar la base de datos a través de servidores MCP;
- generar código nuevo siguiendo los patrones del proyecto;
- analizar y documentar módulos legacy antes de refactorizarlos.

---

## Stack

**Backend:** PHP · Zend Framework · Laminas / Mezzio\
**APIs:** REST · GraphQL · OAuth2\
**Frontend:** Angular · TypeScript · NG-Zorro · Apollo · jQuery (legacy)\
**Base de datos:** MySQL / MariaDB\
**Entorno:** Linux · Git
