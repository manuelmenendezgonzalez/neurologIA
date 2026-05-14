# NeuroIA - Curso de Inteligencia Artificial para Neurólogos

Repositorio de materiales y recursos del curso de formación en Inteligencia Artificial aplicada a la Neurología, dirigido a profesionales neurológicos que desean integrar herramientas de IA en su práctica clínica e investigación.

## Descripción del Curso

Este curso proporciona una introducción práctica a los conceptos fundamentales de la inteligencia artificial y su aplicación específica en el campo de la neurología. Los participantes aprenderán a utilizar herramientas de IA para análisis de datos clínicos, generación de informes, auditoría de bases de datos y optimización de flujos de trabajo neurológicos.

## Contenidos del Repositorio

### Archivos Principales
- **Ejercicios prácticos**: Scripts de Python para análisis de datos neurológicos
- **Base de datos de ejemplo**: Dataset de Esclerosis Múltiple Remitente Recurrente (EMRR) para prácticas
- **Documentación**: Guías y preguntas de ejercicios sobre casos clínicos
- **Utilidades**: Funciones auxiliares para procesamiento de datos neurológicos

### Estructura
```
.
├── Soluciones_y_Ejemplos/   # Ejemplos resueltos y material complementario
├── base_datos_emrr.csv      # Dataset de pacientes EMRR
├── neuro_utils.py           # Utilidades para procesamiento neurológico
├── ejercicio16_auditoria_premium.py  # Script de auditoría clínica
└── requirements.txt         # Dependencias de Python
```

## Requisitos Técnicos

- Python 3.8 o superior
- Bibliotecas: pandas, matplotlib, numpy (ver `requirements.txt`)
- Entorno de desarrollo: VS Code, PyCharm, **Windsurf** o **Antigravity** (gratuitos con IA integrada) o similar

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/manuelmenendezgonzalez/neurologIA.git

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencia de sistema para Quarto

`Quarto` no es una librería Python del `requirements.txt`, sino una herramienta externa de línea de comandos para renderizar archivos `.qmd` a PDF, HTML o Word.

Instalación oficial:
- [Descargar Quarto](https://quarto.org/docs/download/)

Verificación recomendada:

```bash
quarto check
quarto check jupyter
```

## Cómo Usar Este Repositorio

📚 **[Guía para Alumnos](GUIA_ALUMNOS.md)** - Instrucciones completas para trabajar con el curso usando **ChatGPT Plus** y un **IDE local** (VS Code o **Windsurf**, gratuito con IA integrada), incluyendo:
- Cómo acceder al Proyecto de ChatGPT compartido
- Flujo de trabajo con IDE + ChatGPT Proyecto
- Ejemplos de prompts para ejercicios
- Cómo entregar tareas

**Recomendación:** Lee la guía de alumnos antes de empezar los ejercicios.

### Comprobación rápida del entorno

Antes de empezar, puedes validar que Python, Jupyter, Quarto y las dependencias del curso están disponibles con:

```bash
python check_env.py
```

Si Quarto en Windows intenta usar `python3.13t.exe` y falla al renderizar, fuerza el intérprete estándar:

```bash
$env:QUARTO_PYTHON="C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python313\python.exe"
quarto render archivo.qmd
```

## Nota sobre Archivos Grandes

Las presentaciones de PowerPoint (`.pptx`) no están incluidas en este repositorio debido a restricciones de tamaño de GitHub. Estos materiales se proporcionan por canales alternativos durante el curso.

## Dirigido a

- Neurólogos 
- Residentes de Neurología

## Autor

**Manuel Menéndez González**

---
