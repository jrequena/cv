# Mabel — generador de código PHP a partir de contratos

**Contexto:** proyecto personal · repositorio privado\
**Tipo:** experimentación y desarrollo propio (no es experiencia laboral)

> Descripción provisional: se completará cuando se revise el repositorio.

---

## Objetivo

Una herramienta local, pensada para el código, que genera componentes PHP a partir de **contratos estructurados en YAML**. Busca eliminar el código repetitivo (DTOs, Enums) y experimentar con LLMs locales como apoyo a la generación de código.

```text
Contrato YAML
      ↓
    Mabel
      ↓
PHP DTO / Enum / código
```

## Componentes

- `mabel.py`: punto de entrada.
- `core/kernel.py`: núcleo que orquesta la generación.
- `core/generator/php_dto_generator.py`: generador de DTOs PHP.
- `core/generator/php_enum_generator.py`: generador de Enums PHP.

## Stack

**Lenguaje:** Python\
**Entrada:** YAML\
**Salida:** PHP\
**IA:** LLMs locales con Ollama
