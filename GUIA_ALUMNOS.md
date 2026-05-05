# Guía para Alumnos: Flujo de Trabajo con ChatGPT Plus y NeuroIA

Esta guía te ayudará a trabajar con el repositorio del curso usando **ChatGPT Plus** para generar código, resolver ejercicios y analizar datos neurológicos.

---

## Opción Principal: Proyecto de ChatGPT Compartido (Recomendada)

El profesor ha creado un **Proyecto de ChatGPT** con todo el contexto del curso cargado. Esta es la forma más sencilla de empezar.

### Acceso al Proyecto

🔗 **URL del Proyecto:** `https://chatgpt.com/g/g-p-69fa482eda308191af2c1545d6f7465e-curso-neurologia/project`

### Cómo Acceder:

1. Asegúrate de que el profesor te haya **invitado al área de trabajo** del curso
2. Inicia sesión en **chat.openai.com** con tu cuenta ChatGPT Plus
3. Navega a **Áreas de trabajo** (Workspaces) en el sidebar
4. Selecciona el área de trabajo del curso
5. Abre el proyecto **"Curso NeurologIA"**

### Ventajas del Proyecto Compartido:

- ✅ **Contexto pre-cargado**: El repo ya está indexado y disponible
- ✅ **Historial persistente**: Tus conversaciones se guardan en el proyecto
- ✅ **Colaboración**: El profesor puede ver y participar en tus chats
- ✅ **Instrucciones personalizadas**: Optimizado para ejercicios del curso
- ✅ **No necesitas clonar primero**: Puedes generar código y luego sincronizar

### Flujo de Trabajo con el Proyecto:

1. **Abre el proyecto** desde el área de trabajo compartida
2. **Pregunta directamente** sobre ejercicios: "Quiero hacer el ejercicio 3 de auditoría"
3. **Copia el código** generado a tu IDE local
4. **Prueba y depura** localmente
5. **Vuelve al proyecto** para iterar: "Me da este error..." o "Mejora la función..."

### Sincronización Local (Para usuarios del Proyecto)

Aunque uses el Proyecto de ChatGPT, necesitarás el código en tu ordenador para ejecutarlo:

```bash
# Clonar el repositorio
git clone https://github.com/manuelmenendezgonzalez/neurologIA.git
cd neurologIA

# Instalar dependencias
pip install -r requirements.txt

# Abrir en VS Code (opcional)
code .
```

**Flujo recomendado:**
1. Genera código en el Proyecto de ChatGPT compartido
2. Copia/pega el código a archivos `.py` en tu carpeta local
3. Ejecuta y prueba localmente
4. Si hay errores, comparte el error en el Proyecto de ChatGPT
5. Itera hasta que funcione

---

## Opción Alternativa: ChatGPT Individual + Repositorio

Si prefieres trabajar en tu ChatGPT personal (fuera del área de trabajo compartida):

### Paso 1: Cargar el Repositorio en ChatGPT

1. Abre **chat.openai.com** con tu cuenta Plus
2. Crea un nuevo chat
3. Pega este mensaje de carga del repositorio:

```
Voy a trabajar con el repositorio https://github.com/manuelmenendezgonzalez/neurologIA

Por favor, analiza:
1. La estructura de archivos y su propósito
2. Los ejercicios disponibles en Soluciones_y_Ejemplos/
3. El dataset base_datos_emrr.csv y sus columnas
4. Las utilidades en neuro_utils.py

Luego prepárame para el ejercicio: [indica qué ejercicio vas a hacer]
```

4. ChatGPT cargará el contexto del repositorio y podrás preguntarle sobre el código

### Paso 2: Clonar el Repositorio en Local

```bash
# Abre terminal y ejecuta:
git clone https://github.com/manuelmenendezgonzalez/neurologIA.git
cd neurologIA

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Flujo de Trabajo

1. **Lee el ejercicio** en el chat con ChatGPT
2. **Pídele que te guíe**: "Quiero hacer el ejercicio X. Explícame qué debo hacer paso a paso"
3. **Trabaja en tu IDE** favorito (VS Code, PyCharm, Jupyter)
4. **Copia/pega código** desde ChatGPT a tu editor
5. **Prueba el código** localmente
6. **Itera con ChatGPT**: "Me da error X" o "¿Cómo mejoro esta función?"

### Prompts Útiles para Ejercicios

**Para empezar un ejercicio:**
```
Estoy en el ejercicio [número]. 
El objetivo es: [describir objetivo]
¿Qué algoritmo/método recomiendas?
Dame el código paso a paso.
```

**Para depurar errores:**
```
Tengo este error: [pegar traceback]
Mi código actual:
```python
[pegar código]
```
¿Qué está mal y cómo lo arreglo?
```

**Para entender conceptos:**
```
Explica [concepto estadístico/algoritmo] aplicado a neurología
con un ejemplo del dataset EMRR
```

---

## Opción 2: VS Code + GitHub Copilot (Si tienes suscripción)

Si tienes GitHub Copilot además de ChatGPT Plus:

1. Instala VS Code: https://code.visualstudio.com
2. Activa GitHub Copilot en VS Code
3. Abre el repositorio clonado
4. Copilot sugerirá código mientras escribes
5. Usa ChatGPT Plus para explicaciones conceptuales más profundas

**Configuración:**
- Extensión GitHub Copilot (oficial)
- Extensión Python
- Extensión Jupyter (si usas notebooks)

---

## Opción 3: Jupyter Notebook + ChatGPT Plus (Análisis de Datos)

Ideal para ejercicios de análisis exploratorio:

1. Instala Jupyter:
```bash
pip install jupyter
```

2. Inicia Jupyter:
```bash
jupyter notebook
```

3. Crea un nuevo notebook en la carpeta del repositorio

4. Flujo de trabajo:
   - Copia prompts de ChatGPT al notebook
   - Pega código generado en celdas
   - Ejecuta y visualiza resultados
   - Itera con ChatGPT basándote en outputs

**Prompt útil para notebooks:**
```
Dame el código completo para un Jupyter notebook que:
1. Cargue base_datos_emrr.csv
2. Haga análisis exploratorio de [variable]
3. Visualice [gráfico específico]
4. Interprete los resultados clínicamente
```

---

## Ejemplo de Ejercicio Resuelto con ChatGPT Plus

### Escenario: Ejercicio de Auditoría de Datos

**Tú en ChatGPT:**
```
Necesito hacer el ejercicio de auditoría de calidad del dataset EMRR.

Requisitos:
- Detectar valores faltantes
- Identificar outliers en EDSS
- Verificar consistencia de fechas
- Generar reporte de calidad

Dame el código Python completo y modular.
```

**ChatGPT te dará código como:**
```python
import pandas as pd
import numpy as np
from datetime import datetime

def auditar_dataset(ruta_csv):
    df = pd.read_csv(ruta_csv)
    
    reporte = {
        'total_registros': len(df),
        'valores_faltantes': df.isnull().sum().to_dict(),
        'duplicados': df.duplicated().sum(),
        'outliers_edss': detectar_outliers(df['EDSS']) if 'EDSS' in df.columns else None
    }
    
    return reporte

def detectar_outliers(serie):
    Q1 = serie.quantile(0.25)
    Q3 = serie.quantile(0.75)
    IQR = Q3 - Q1
    outliers = serie[(serie < Q1 - 1.5*IQR) | (serie > Q3 + 1.5*IQR)]
    return len(outliers)

# Ejecutar
if __name__ == "__main__":
    resultado = auditar_dataset('base_datos_emrr.csv')
    print(resultado)
```

**Siguiente iteración:**
```
Mejora la función para que:
1. Genere un archivo Excel con el reporte
2. Incluya visualizaciones con matplotlib
3. Detecte inconsistencias entre EDSS y subtipo_clinico
```

---

## Entregas y Proyectos

### Para Entregar Ejercicios:

1. Trabaja en tu rama local:
```bash
git checkout -b ejercicio-[tu-nombre]-[numero]
```

2. Guarda tu código en archivos separados:
   - `ejercicio_01_[tu_nombre].py`
   - `resultados_ejercicio_01.xlsx` (si aplica)

3. Comparte con el profesor:
   - Opción A: Push a tu fork y pull request
   - Opción B: Enviar archivos por email/Teams
   - Opción C: Compartir en el foro del curso

### Ejercicio Final - Presentación:

Para la presentación final con ChatGPT Plus:

1. Genera código de análisis
2. Pide a ChatGPT que te ayude a crear visualizaciones
3. Exporta gráficos (PNG/SVG)
4. Crea presentación en PowerPoint con los resultados
5. Usa ChatGPT para generar guión de presentación:
```
Ayúdame a crear un guión de 10 minutos para presentar 
mi análisis de [tema] a neurólogos. Los hallazgos principales son:
[enumerar hallazgos]
```

---

## Recursos Adicionales

### Documentación Útil
- Repositorio del curso: https://github.com/manuelmenendezgonzalez/neurologIA
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/

### Plugins de VS Code Recomendados
- Python (Microsoft)
- Python Docstring Generator
- Code Runner (ejecutar scripts rápido)
- Error Lens (ver errores en tiempo real)
- GitLens (control de versiones)

### Tips de Prompting para Código

**Específico es mejor:**
- ❌ "Hazme un análisis"
- ✅ "Crea una función que reciba un DataFrame y devuelva estadísticas de EDSS agrupadas por subtipo_clinico"

**Proporciona contexto:**
```
Estoy usando pandas 2.0 y python 3.11.
El dataset tiene estas columnas: [lista].
Necesito que el código maneje valores faltantes.
```

**Pide explicaciones:**
```
Además del código, explica:
1. Por qué elegiste este algoritmo
2. Qué significan los resultados clínicamente
3. Limitaciones del análisis
```

---

## Soporte Técnico

Si tienes problemas:

1. **Errores de instalación**: Consulta al profesor o usa el foro
2. **Errores de código**: Pega el error completo en ChatGPT
3. **Dudas conceptuales**: ChatGPT Plus es tu primer recurso
4. **Problemas con el repositorio**: Abre un issue en GitHub

---

**¡Éxito en el curso!**

*Recuerda: ChatGPT Plus es una herramienta potente, pero la interpretación clínica y el juicio médico siempre son responsabilidad tuya como neurólogo.*
