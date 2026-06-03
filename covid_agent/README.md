# COVID-19 Agent

Este es un agente desarrollado con **ADK** que utiliza un servidor MCP para obtener datos sobre la pandemia de COVID-19. Soporta consultas en español.

## Requisitos

- Python 3.12+
- ADK (incluido en el entorno virtual)

## Configuración

1. Asegúrate de tener tu `GOOGLE_API_KEY` en el archivo `.env`.

## Cómo Ejecutar

Para ejecutar el agente, debes activar el entorno virtual e iniciar `adk`:

```bash
# Entrar al directorio del agente
cd covid_agent

# Activar el entorno virtual
source .venv/bin/activate

# Ejecutar el agente en modo interactivo
adk run .
```

## Ejemplo de Consultas

- "¿Cuántos casos de COVID-19 hay en total?"
- "¿Cuál es la situación en México?"
- "Dame las estadísticas de vacunación en España."
