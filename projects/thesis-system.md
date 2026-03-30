# Sistema de Gestión de Tesis

## Descripción General

Sistema web diseñado para gestionar el ciclo completo del proceso de tesis, incluyendo registro, seguimiento, evaluación y aprobación.

La solución fue implementada para digitalizar y optimizar procesos académicos, reduciendo la carga operativa manual y mejorando la trazabilidad de la información.

---

## Problema

El proceso de gestión de tesis presentaba múltiples limitaciones:

* Procesos manuales y descentralizados
* Falta de trazabilidad del estado de las tesis
* Manejo ineficiente de documentos
* Dificultad en la comunicación entre actores (estudiantes, evaluadores, administración)
* Riesgo de inconsistencias y pérdida de información

---

## Solución

Se diseñó e implementó una plataforma web centralizada basada en arquitectura cliente-servidor, que permite:

* Gestión completa del flujo de tesis
* Control de estados y seguimiento en tiempo real
* Administración de documentos digitales
* Control de acceso basado en roles

El sistema permitió estandarizar el proceso y mejorar significativamente la eficiencia operativa.

---

## Funcionalidades Principales

* Registro y gestión de tesis
* Flujo de trabajo configurable (registro → revisión → aprobación)
* Gestión de documentos y versiones
* Control de acceso por roles
* Seguimiento del estado en tiempo real
* Validaciones de integridad de datos

---

## Arquitectura del Sistema

Arquitectura basada en separación de responsabilidades:

* **Frontend:** Angular (SPA)
* **Backend:** PHP (API REST)
* **Base de datos:** MySQL

### Flujo de interacción

1. El cliente (Angular) consume la API REST
2. El backend procesa la lógica de negocio
3. Se interactúa con la base de datos MySQL
4. Se retorna la respuesta al cliente

### Decisión clave

Se optó por desacoplar frontend y backend para permitir:

* escalabilidad
* mantenimiento independiente
* futura integración con otros sistemas

---

## Decisiones Técnicas

### Diseño de API REST

Se implementó una API REST para:

* facilitar integraciones futuras
* mantener desacoplamiento
* permitir reutilización de servicios

---

### Modelado de Base de Datos

* Uso de relaciones normalizadas
* Implementación de índices en consultas críticas
* Optimización de queries para mejorar tiempos de respuesta

---

### Control de Acceso

Se implementó un sistema de roles:

* Estudiante
* Evaluador
* Administrador

Esto permitió:

* seguridad en el acceso
* control de acciones por usuario
* reducción de errores operativos

---

### Manejo de Documentos

* Almacenamiento estructurado de archivos
* Control de versiones
* Validación de formatos

---

## Retos Técnicos

* Gestión de múltiples roles con diferentes permisos
* Sincronización de estados en el flujo de trabajo
* Manejo eficiente de archivos
* Optimización de consultas en base de datos
* Garantizar consistencia en transacciones críticas

---

## Optimización y Rendimiento

Se aplicaron mejoras como:

* Indexación en columnas clave
* Reducción de consultas innecesarias
* Optimización de queries complejas
* Separación de lógica para evitar cuellos de botella

---

## Resultados

* Reducción significativa del trabajo manual en procesos académicos
* Mejora en la trazabilidad del estado de las tesis
* Centralización de la información
* Mayor confiabilidad del sistema

---

## Impacto

El sistema permitió:

* Digitalizar completamente el proceso de tesis
* Reducir errores administrativos
* Mejorar la eficiencia operativa
* Facilitar la toma de decisiones mediante información centralizada

---

## Aprendizajes

* Diseño de sistemas backend escalables
* Construcción de APIs REST mantenibles
* Optimización de bases de datos relacionales
* Manejo de arquitectura desacoplada
* Resolución de problemas en entornos reales

---

## Posibles Mejoras Futuras

* Implementación de notificaciones en tiempo real
* Integración con servicios externos
* Migración a arquitectura basada en microservicios
* Implementación de pruebas automatizadas
* Uso de contenedores (Docker)

---

## Stack Tecnológico

**Backend:** PHP
**Frontend:** Angular
**Base de datos:** MySQL
**Entorno:** Linux
**Control de versiones:** Git
    