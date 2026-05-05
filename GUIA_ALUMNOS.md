# Guía para Alumnos: Flujo de Trabajo del Curso NeuroIA

Esta guía explica cómo trabajar con el curso usando **ChatGPT Plus** (como profesor virtual) y un **IDE local** (para ejecutar todos los ejercicios con automatización completa).

---

## 🎯 Arquitectura del Curso

- **ChatGPT Proyecto**: Tu "profesor virtual" con instrucciones del curso pre-configuradas
- **IDE Local**: Entorno de desarrollo para ejecutar código y generar archivos (`.pptx`, `.pdf`, etc.)
- **Repositorio GitHub**: Materiales del curso, dataset y ejercicios

---

## Paso 1: Instalar el IDE (Obligatorio)

Para ejecutar todos los ejercicios del curso (incluyendo generación de presentaciones y artículos), necesitas un IDE. Recomendamos **VS Code** (gratuito).

### Instalación de VS Code:

1. Descarga VS Code: https://code.visualstudio.com
2. Instala Python: https://www.python.org/downloads/ (versión 3.8 o superior)
3. Durante la instalación de Python, marca la opción "Add Python to PATH"

### Extensiones de VS Code (recomendadas):

- **Python** (Microsoft)
- **Jupyter** (Microsoft) - si quieres usar notebooks
- **GitLens** - para control de versiones

---

## Paso 2: Configurar el Repositorio Local

```bash
# Clonar el repositorio
git clone https://github.com/manuelmenendezgonzalez/neurologIA.git
cd neurologIA

# Instalar dependencias
pip install -r requirements.txt

# Abrir en VS Code
code .
```

---

## Paso 3: Acceder al Proyecto de ChatGPT

El profesor ha creado un **Proyecto de ChatGPT** que actúa como tu asistente del curso.

🔗 **URL del Proyecto:** `https://chatgpt.com/g/g-p-69fa482eda308191af2c1545d6f7465e-curso-neurologia/project`

### Cómo Acceder:

1. Asegúrate de que el profesor te haya **invitado al área de trabajo** del curso
2. Inicia sesión en **chat.openai.com** con tu cuenta ChatGPT Plus
3. Navega a **Áreas de trabajo** (Workspaces) en el sidebar
4. Selecciona el área de trabajo del curso
5. Abre el proyecto **"Curso NeurologIA"**

### Qué ofrece el Proyecto:

- ✅ **Contexto pre-cargado**: El repo ya está indexado
- ✅ **Instrucciones del curso**: Configurado específicamente para NeuroIA
- ✅ **Historial persistente**: Tus conversaciones se guardan
- ✅ **Supervisión**: El profesor puede ver y ayudar en tus chats

---

## Paso 4: Flujo de Trabajo (ChatGPT + IDE)

Este es el flujo estándar para todos los ejercicios del curso:

### Para Ejercicios 1-6 (Análisis de Datos):

1. **Abre el Proyecto** de ChatGPT
2. **Pregunta sobre el ejercicio**: "Quiero hacer el ejercicio 3 de regresión atrofia vs EDSS"
3. **ChatGPT genera código** optimizado para el curso
4. **Copia el código** a VS Code (crea archivo `ejercicio3.py`)
5. **Ejecuta en VS Code**: Terminal → `python ejercicio3.py`
6. **Si hay errores**: Copia el error al Proyecto de ChatGPT para ayuda
7. **Itera** hasta que funcione

### Para Ejercicio 16 (Generación de PowerPoint):

1. **Pide código** en el Proyecto: "Genera código para presentación sobre atrofia cortical"
2. **ChatGPT genera código** con `python-pptx` (layout 4:3, colores corporativos)
3. **Copia a VS Code** (crea `ejercicio16.py`)
4. **Ejecuta**: `python ejercicio16.py`
5. **Se genera** el archivo `.pptx` en tu carpeta local
6. **Abre el PowerPoint** para revisar las diapositivas

### Para Ejercicio 17 (Artículo Científico):

1. **Pide código** en el Proyecto: "Genera artículo Quarto sobre [tema]"
2. **ChatGPT genera archivo** `.qmd` con contenido científico
3. **Copia a VS Code** (crea `articulo.qmd`)
4. **Instala Quarto** (si no lo tienes): https://quarto.org
5. **Compila**: `quarto render articulo.qmd`
6. **Se genera** el PDF con formato científico

---

## 💡 Prompts Útiles

### Para empezar un ejercicio:
```
Quiero hacer el ejercicio [número]. 
Explícame qué debo hacer paso a paso y dame el código completo.
```

### Para depurar errores:
```
Me da este error al ejecutar el código:
[pegar traceback]

Mi código actual:
```python
[pegar código]
```
¿Qué está mal y cómo lo arreglo?
```

### Para entender conceptos:
```
Explica [concepto estadístico/método] aplicado a neurología
con un ejemplo del dataset EMRR.
```

---

## 📁 Estructura de Archivos en tu IDE

```
neurologIA/
├── base_datos_emrr.csv          # Dataset del curso
├── neuro_utils.py               # Utilidades (usa siempre load_and_clean_data)
├── requirements.txt             # Dependencias
├── Soluciones_y_Ejemplos/       # Ejemplos resueltos
├── ejercicio1.py                # Tu solución (crea estos archivos)
├── ejercicio2.py
├── ...
├── ejercicio16.py               # Genera PowerPoint
└── articulo.qmd                 # Para ejercicio 17
```

---

## 🔧 Comandos Útiles en VS Code

```bash
# Ejecutar un script
python ejercicio3.py

# Ver archivos generados
ls

# Actualizar el repo con cambios del profesor
git pull

# Ver cambios que has hecho
git status
```

---

## 📝 Entrega de Ejercicios

### Opción A: Archivos por email/Teams
- Envía los archivos `.py` generados
- Para Ej 16: envía el `.pptx`
- Para Ej 17: envía el `.pdf`

### Opción B: GitHub (si tienes cuenta)
- Crea tu fork del repo
- Sube tus archivos a tu fork
- Comparte el link con el profesor

---

## ❓ Soporte

- **Errores de instalación**: Consulta al profesor
- **Errores de código**: Pregunta en el Proyecto de ChatGPT
- **Dudas conceptuales**: ChatGPT es tu primer recurso
- **Problemas con el repo**: Abre un issue en GitHub

---

**¡Éxito en el curso!**

*Recuerda: ChatGPT Plus es una herramienta potente, pero la interpretación clínica y el juicio médico siempre son responsabilidad tuya como neurólogo.*
