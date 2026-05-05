# Guía para Alumnos: Flujo de Trabajo del Curso NeuroIA

Esta guía explica cómo trabajar con el curso usando **ChatGPT Plus** (como profesor virtual) y un **IDE local** (para ejecutar todos los ejercicios con automatización completa).

---

## 🎯 Arquitectura del Curso

- **ChatGPT Proyecto**: Tu "profesor virtual" con instrucciones del curso pre-configuradas
- **IDE Local**: Entorno de desarrollo para ejecutar código y generar archivos (`.pptx`, `.pdf`, etc.)
- **Repositorio GitHub**: Materiales del curso, dataset y ejercicios

---

## Paso 1: Instalar tu IDE (Obligatorio)

Para ejecutar todos los ejercicios del curso (incluyendo generación de presentaciones y artículos), necesitas un IDE. Recomendamos estos dos gratuitos con IA integrada:

### Opción A: Windsurf (Con IA integrada gratuita)

**Windsurf** es un IDE gratuito con IA integrada (Cascade) que puede leer tus archivos locales, corregir código y generar nuevos scripts automáticamente.

1. Descarga Windsurf: https://www.windsurf.com/
2. Instala Python: https://www.python.org/downloads/ (versión 3.8 o superior)
3. Durante la instalación de Python, marca la opción "Add Python to PATH"
4. Abre Windsurf y abre la carpeta del repositorio clonado

**Ventajas de Windsurf:**
- ✅ IA integrada gratuita (pide ayuda con `Ctrl+K` o `Cmd+K`)
- ✅ Lee tus archivos locales automáticamente
- ✅ Puede editar código directamente
- ✅ Similar a VS Code, sin necesidad de extensiones adicionales

### Opción B: Antigravity (Con IA integrada gratuita)

**Antigravity** es otro IDE gratuito con IA integrada que permite trabajar con código Python de forma interactiva.

1. Descarga Antigravity: https://www.antigravity.dev/
2. Instala Python: https://www.python.org/downloads/ (versión 3.8 o superior)
3. Durante la instalación de Python, marca la opción "Add Python to PATH"
4. Abre Antigravity y abre la carpeta del repositorio clonado

**Ventajas de Antigravity:**
- ✅ IA integrada gratuita
- ✅ Interfaz amigable para principiantes
- ✅ Ejecución de código integrada
- ✅ Soporte para Python y data science

### Opción C: VS Code (Sin IA integrada)

1. Descarga VS Code: https://code.visualstudio.com
2. Instala Python: https://www.python.org/downloads/ (versión 3.8 o superior)
3. Durante la instalación de Python, marca la opción "Add Python to PATH"

### Extensiones de VS Code (recomendadas):

- **Python** (Microsoft)
- **Jupyter** (Microsoft) - si quieres usar notebooks
- **GitLens** - para control de versiones

---

## Paso 2: Abrir el Proyecto de ChatGPT (Tu Profesor Virtual)

El profesor ha creado un **Proyecto de ChatGPT** que actúa como tu profesor virtual para este curso. Contiene todo el contexto del curso pre-cargado.

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

## Paso 3: Configurar el Repositorio Local (A través del Proyecto ChatGPT)

**NO clones el repo manualmente.** En el Proyecto de ChatGPT, pide:

```
Dame el prompt exacto para que mi IDE (Windsurf) clone el repositorio del curso e instale las dependencias.
```

ChatGPT te dará un prompt optimizado para tu IDE. Por ejemplo:

```
Abre la carpeta del curso NeuroIA. Clona este repositorio:
https://github.com/manuelmenendezgonzalez/neurologIA.git

Luego instala las dependencias:
pip install -r requirements.txt

Abre el proyecto en el IDE.
```

**Copia ese prompt y pégalo en Windsurf** (o presiona `Ctrl+K` y pide que lo ejecute).

---

## Paso 4: Flujo de Trabajo Oficial del Curso

Este es el flujo estándar para todos los ejercicios:

### 1. Pide el ejercicio al Proyecto de ChatGPT

En el Proyecto, escribe:
```
Quiero hacer el ejercicio [número]. Explícame qué debo hacer y dame el código/prompt para mi IDE.
```

### 2. Ejecuta en tu IDE (Windsurf)

- Copia el código o el prompt que te dio ChatGPT
- Presiona `Ctrl+K` en Windsurf y pégalo, o crea el archivo directamente
- Pide a Windsurf que **explique y ejecute** el ejercicio paso a paso

### 3. Si hay errores, problemas o dudas:

**Tienes dos fuentes de ayuda:**

- **Windsurf (IA integrada)**: Presiona `Ctrl+K` y describe el error. La IA del IDE puede leer tus archivos locales y corregir directamente.
- **Proyecto ChatGPT**: Vuelve al chat del curso y pide ayuda. El profesor virtual tiene todo el contexto del ejercicio.

### Ejemplos por tipo de ejercicio:

**Ejercicios 1-6 (Análisis de Datos):**
- ChatGPT te da el código Python
- Windsurf ejecuta y muestra gráficos
- Itera con Windsurf o ChatGPT si hay errores

**Ejercicio 16 (Generación de PowerPoint):**
- ChatGPT genera código `python-pptx`
- Windsurf ejecuta → Se genera `.pptx` automáticamente
- Revisa las diapositivas generadas

**Ejercicio 17 (Artículo Científico):**
- ChatGPT genera archivo `.qmd`
- Windsurf compila con Quarto (si instalado) o genera el archivo
- Obtienes PDF con formato científico

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
