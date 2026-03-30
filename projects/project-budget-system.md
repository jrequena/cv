# Sistema de Gestión Económica de Proyectos Universitarios

## Descripción General

Sistema backend diseñado para la gestión y control del presupuesto de proyectos universitarios, permitiendo registrar, validar y rendir gastos a través de facturas asociadas a bienes y servicios.

El sistema garantiza la correcta administración de los recursos financieros y asegura la trazabilidad de cada gasto dentro del presupuesto asignado.

---

## Problema

La gestión económica de proyectos presentaba múltiples dificultades:

* Falta de control sobre el uso del presupuesto asignado
* Registro manual de facturas y gastos
* Dificultad para validar gastos según categorías (bienes y servicios)
* Riesgo de inconsistencias financieras
* Baja trazabilidad en la rendición de cuentas

---

## Solución

Se implementó un sistema backend centralizado que permite:

* Registrar facturas asociadas a bienes y servicios
* Controlar el presupuesto disponible en tiempo real
* Validar reglas de negocio antes de aprobar gastos
* Mantener trazabilidad completa de las operaciones

El sistema asegura consistencia financiera y facilita la rendición de cuentas.

---

## Funcionalidades Principales

* Registro de facturas
* Clasificación de gastos (bienes / servicios)
* Control de presupuesto asignado vs ejecutado
* Validación de reglas de negocio
* Seguimiento de estados (registrado, aprobado, rechazado)
* Reportes básicos de ejecución presupuestaria

---

## Arquitectura del Sistema

Arquitectura orientada a backend desacoplado:

* **Backend:** PHP (API REST)
* **Base de datos:** MySQL
* **Clientes consumidores:** aplicaciones web o servicios externos

### Flujo de operación

1. Registro de factura
2. Validación de datos y reglas de negocio
3. Verificación de disponibilidad presupuestaria
4. Persistencia en base de datos
5. Actualización del estado del presupuesto

---

## Decisiones Técnicas

### Validación de Reglas de Negocio

Se implementaron validaciones como:

* No exceder el presupuesto asignado
* Clasificación obligatoria del gasto
* Validación de montos y formatos

---

### Control de Consistencia

* Uso de transacciones en operaciones críticas
* Validación antes de persistencia
* Integridad referencial en base de datos

---

### Modelado de Datos

* Relación entre proyectos, presupuestos y facturas
* Separación entre bienes y servicios
* Normalización para evitar redundancia

---

### API REST

* Endpoints estructurados para operaciones CRUD
* Diseño orientado a integración con otros sistemas
* Separación clara entre lógica de negocio y acceso a datos

---

## Retos Técnicos

* Control de consistencia en operaciones financieras
* Validación de reglas de negocio complejas
* Manejo de estados en el flujo de aprobación
* Optimización de consultas para reportes

---

## Optimización y Rendimiento

* Indexación en campos clave (proyecto, estado, fechas)
* Optimización de consultas agregadas
* Reducción de operaciones redundantes
* Manejo eficiente de transacciones

---

## Ejemplo de Lógica de Negocio

Validación de presupuesto:

* Si (gasto_actual + nuevo_gasto) > presupuesto_total
  → rechazar operación

Esto garantiza que no se exceda el presupuesto asignado.

---

## Resultados

* Mayor control sobre el uso del presupuesto
* Reducción de errores en la rendición de gastos
* Mejora en la trazabilidad financiera
* Automatización de validaciones clave

---

## Impacto

El sistema permitió:

* Mejorar la transparencia en la gestión económica
* Facilitar auditorías y revisiones
* Reducir inconsistencias financieras
* Aumentar la eficiencia administrativa

---

## Aprendizajes

* Diseño de sistemas financieros backend
* Implementación de validaciones complejas
* Manejo de transacciones en bases de datos
* Modelado de datos para sistemas contables
* Construcción de APIs robustas

---

## Posibles Mejoras Futuras

* Integración con sistemas contables externos
* Generación de reportes avanzados
* Implementación de auditoría de cambios (logs)
* Autenticación y autorización avanzada (JWT)
* Uso de microservicios para escalabilidad

---

## Stack Tecnológico

**Backend:** PHP
**Base de datos:** MySQL
**Arquitectura:** API REST
**Entorno:** Linux
**Control de versiones:** Git
