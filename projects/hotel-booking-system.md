# Sistema de Gestión de Reservas de Hotel

## Descripción General

Sistema web diseñado para la gestión de reservas hoteleras, permitiendo administrar disponibilidad de habitaciones, registro de clientes y control de reservas en tiempo real.

El sistema fue desarrollado para optimizar la ocupación hotelera, reducir conflictos de reservas y mejorar la experiencia de gestión administrativa.

---

## Problema

En sistemas tradicionales o procesos manuales, se presentan varios problemas:

* Doble reserva de habitaciones (overbooking)
* Falta de control en disponibilidad en tiempo real
* Dificultad para gestionar cambios o cancelaciones
* Procesos manuales propensos a errores
* Baja visibilidad del estado de ocupación

---

## Solución

Se implementó una plataforma centralizada que permite:

* Consultar disponibilidad en tiempo real
* Registrar y gestionar reservas
* Evitar conflictos mediante validaciones de concurrencia
* Gestionar clientes y estados de reserva

El sistema asegura consistencia en la asignación de habitaciones y mejora la eficiencia operativa.

---

## Funcionalidades Principales

* Registro de reservas con validación de fechas
* Control de disponibilidad por rango de fechas
* Gestión de habitaciones y tipos de habitación
* Registro y gestión de clientes
* Cancelación y modificación de reservas
* Control de estados (pendiente, confirmada, cancelada)

---

## Arquitectura del Sistema

Arquitectura cliente-servidor desacoplada:

* **Frontend:** Angular
* **Backend:** PHP (API REST)
* **Base de datos:** MySQL

### Flujo de reservas

1. Usuario consulta disponibilidad
2. El sistema valida fechas y ocupación
3. Se verifica que no existan conflictos
4. Se registra la reserva
5. Se actualiza disponibilidad

---

## Decisiones Técnicas

### Control de Concurrencia

Para evitar doble reserva (overbooking), se implementaron:

* Validaciones de disponibilidad antes de confirmar
* Restricciones a nivel de base de datos
* Manejo controlado de transacciones

---

### Modelado de Datos

* Relación entre habitaciones, reservas y clientes
* Uso de rangos de fechas para validar disponibilidad
* Normalización de datos para evitar redundancia

---

### Validación de Fechas

Se implementaron reglas para:

* Evitar solapamiento de reservas
* Validar rangos de entrada y salida
* Controlar disponibilidad dinámica

---

### API REST

Permite:

* Integración con otros sistemas (ej: portales de reservas)
* Separación entre frontend y backend
* Escalabilidad futura

---

## Retos Técnicos

* Manejo de concurrencia en reservas simultáneas
* Validación eficiente de disponibilidad por fechas
* Optimización de consultas en base de datos
* Gestión de estados de reserva

---

## Optimización y Rendimiento

* Indexación en campos clave (fechas, habitación)
* Consultas optimizadas para validación de disponibilidad
* Reducción de operaciones innecesarias
* Uso eficiente de joins en MySQL

---

## Ejemplo de Lógica de Negocio

Validación de disponibilidad:

* Verificar si existe alguna reserva activa donde:

  * fecha_inicio < nueva_fecha_fin
  * fecha_fin > nueva_fecha_inicio

Esto evita solapamientos y garantiza consistencia.

---

## Resultados

* Eliminación de conflictos de reservas
* Mejora en la gestión de disponibilidad
* Reducción de errores manuales
* Mayor control del estado del hotel

---

## Impacto

El sistema permitió:

* Mejorar la ocupación de habitaciones
* Optimizar procesos administrativos
* Reducir incidencias operativas
* Aumentar la confiabilidad del sistema

---

## Aprendizajes

* Manejo de lógica compleja de fechas
* Control de concurrencia en sistemas reales
* Diseño de APIs robustas
* Optimización de consultas SQL
* Modelado de datos para sistemas transaccionales

---

## Posibles Mejoras Futuras

* Integración con pasarelas de pago
* Notificaciones automáticas (email / SMS)
* Panel de reportes y analítica
* Implementación de cache para consultas frecuentes
* Uso de contenedores (Docker)

---

## Stack Tecnológico

**Backend:** PHP
**Frontend:** Angular
**Base de datos:** MySQL
**Entorno:** Linux
**Control de versiones:** Git
