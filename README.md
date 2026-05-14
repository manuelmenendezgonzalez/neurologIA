# NeuroIA - Curso de Inteligencia Artificial para Neurologos

Repositorio de materiales y recursos del curso de formacion en Inteligencia Artificial aplicada a la Neurologia, dirigido a profesionales neurologicos que desean integrar herramientas de IA en su practica clinica e investigacion.

## Repositorio del curso

URL publica para clonar el curso:

`https://github.com/manuelmenendezgonzalez/neurologIA.git`

## Descripcion del curso

Este curso proporciona una introduccion practica a los conceptos fundamentales de la inteligencia artificial y su aplicacion especifica en neurologia. Los participantes aprenderan a utilizar herramientas de IA para analisis de datos clinicos, generacion de informes, auditoria de bases de datos y optimizacion de flujos de trabajo neurologicos.

## Contenidos del repositorio

### Archivos principales

- Ejercicios practicos: scripts de Python para analisis de datos neurologicos
- Bases de datos de ejemplo: cohortes para practicas
- Documentacion: guias y preguntas de ejercicios sobre casos clinicos
- Utilidades: funciones auxiliares para procesamiento de datos neurologicos

### Estructura

```text
.
|-- Soluciones_y_Ejemplos/   # Ejemplos resueltos y material complementario
|-- Set_Alzheimer/           # Set de ejercicios de Alzheimer
|-- base_datos_emrr.csv      # Dataset de pacientes EMRR
|-- neuro_utils.py           # Utilidades para procesamiento neurologico
|-- requirements.txt         # Dependencias de Python
|-- check_env.py             # Comprobacion automatica del entorno
```

## Requisitos tecnicos

- Python 3.8 o superior
- Dependencias Python en `requirements.txt`
- Un IDE con IA integrada o equivalente
- Quarto para renderizar archivos `.qmd`

## Instalacion

```bash
# Clonar el repositorio
git clone https://github.com/manuelmenendezgonzalez/neurologIA.git

# Entrar en la carpeta
cd neurologIA

# Instalar dependencias
pip install -r requirements.txt

# Validar entorno
python check_env.py
```

## Dependencia de sistema para Quarto

`Quarto` no es una libreria Python del `requirements.txt`, sino una herramienta externa de linea de comandos para renderizar archivos `.qmd` a PDF, HTML o Word.

Instalacion oficial:

- [Descargar Quarto](https://quarto.org/docs/download/)

Verificacion recomendada:

```bash
quarto check
quarto check jupyter
```

## Como usar este repositorio

La guia principal para los alumnos es:

- [GUIA_ALUMNOS.md](GUIA_ALUMNOS.md)

La recomendacion es leer primero esa guia y despues trabajar cada bloque con ayuda del IDE.

## Comprobacion rapida del entorno

Antes de empezar, puedes validar que Python, Jupyter, Quarto y las dependencias del curso estan disponibles con:

```bash
python check_env.py
```

Si Quarto en Windows intenta usar `python3.13t.exe` y falla al renderizar, fuerza el interprete estandar:

```powershell
$env:QUARTO_PYTHON="C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python313\python.exe"
quarto render archivo.qmd
```

## Nota sobre archivos grandes

Las presentaciones de PowerPoint (`.pptx`) no estan incluidas en el repositorio porque GitHub penaliza archivos binarios grandes. El codigo que las genera si forma parte del material del curso.

## Dirigido a

- Neurologos
- Residentes de Neurologia

## Autor

**Manuel Menendez Gonzalez**
