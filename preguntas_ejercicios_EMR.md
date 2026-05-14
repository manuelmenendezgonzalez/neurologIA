# Certificación en Prompt Engineering para Neurología (EMRR)
## Programa Integral de Ejercicios v2.3

## 🚀 Guía de Inicio Rápido para el Alumno

Para comenzar este curso, asegúrate de tener los siguientes archivos en tu carpeta de trabajo y sigue estas instrucciones:

1. **Configuración del Entorno**: Abre una terminal en tu IDE y ejecuta el siguiente comando para instalar todas las librerías necesarias:
   ```bash
   pip install -r requirements.txt
   ```
2. **Uso de Datos**: El archivo `Base_Datos_EMRR_Final.xlsx` contiene la cohorte y el **Diccionario de Variables** (códigos). Consúltalo siempre para saber qué significa cada número.
3. **El Asistente Inteligente (`neuro_utils.py`)**: Este archivo es **imprescindible**. Cuando redactes tus prompts, menciona siempre a la IA: *"Utiliza las funciones de neuro_utils.py para cargar y limpiar los datos de base_datos_emrr.csv"*. Esto evitará errores de lectura y ahorrará tiempo de programación.

---

### Infraestructura de Datos
- **Fuente**: `base_datos_emrr.csv` (SEP=;)
- **Soporte**: `neuro_utils.py` y `requirements.txt`

---

## BLOQUE 1: Fundamentos y Análisis de Datos

### 🟦 Guía Teórica: Presentaciones como Código (*Slides as Code*)

Antes de los ejercicios, el alumno debe comprender que el flujo de trabajo moderno no es "arrastrar y soltar", sino **compilar presentaciones**.

#### 1. Contexto y Herramientas
La transición de herramientas visuales (PowerPoint) hacia el ecosistema del IDE permite mantener la coherencia estética mediante CSS/Temas y el control de versiones (Git).

| Herramienta | Especialidad | Ventaja en NeuroIA |
|---|---|---|
| **Marp** | Markdown Simple | El más rápido para transformar notas en slides. |
| **Slidev** | Web / Interactividad | Permite integrar componentes interactivos. |
| **Quarto** | Data Science | **Recomendado**: Ejecuta código Python directamente en las slides. |
| **python-pptx** | Programático | Generación masiva de .pptx desde scripts de datos. |

#### 2. El Pipeline de la NeuroIA
El objetivo de este bloque es dominar el flujo:
`Prompt → Estructura → Markdown → Renderer → Slides`

---

### 📋 EJERCICIOS DEL BLOQUE 1

### Ejercicio 1: Prompt para Caso Clínico EMRR_024 (Disociación)
**Enunciado:** Redacta un prompt para analizar la disociación entre la fatiga percibida y los resultados en los tests cognitivos del paciente 24. El script debe calcular percentiles y validar si la queja subjetiva tiene base objetiva.
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejemplo_caso_clinico1.py`).

### Ejercicio 2: Evolución Temporal del EDSS (Versión Premium)
**Enunciado:** Redacta un prompt para clasificar a los pacientes en "Estables" vs "Progresores" basándose en la evolución de su EDSS y comparar el éxito según el tratamiento. El script final debe generar una **presentación ejecutiva Premium (.pptx)** con estética Gamma, incluyendo gráficos de distribución y un resumen de hallazgos clínicos.
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejercicio2_edss_evolucion.py`).

### Ejercicio 3: Prompt para Correlación Atrofia vs EDSS
**Enunciado:** Redacta un prompt para realizar una regresión multivariable que determine el impacto de la atrofia cortical en la discapacidad, dividiendo la cohorte en terciles de atrofia.
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejercicio3_atrofia_edss.py`).

### Ejercicio 4: Prompt para Predicción de Brotes (ML)
**Enunciado:** Redacta un prompt para entrenar un modelo predictivo (Random Forest) que estime el riesgo de nuevos brotes basándose en la actividad basal y la carga lesional.
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejercicio4_brotes_predictivo.py`).

### Ejercicio 5: Prompt para Clustering de Fenotipos
**Enunciado:** Redacta un prompt para realizar un Clustering K-means que identifique los 3 subtipos biológicos de EM (Inflamatoria, Neurodegenerativa y Mixta) usando PCA.
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejercicio5_clustering.py`).

### Ejercicio 6: Prompt para Eficacia en Vida Real
**Enunciado:** Redacta un prompt para analizar la eficacia de los tratamientos en entorno observacional, ajustando por el "sesgo de indicación" (confusión por actividad basal).
**Estado:** ✅ Completado (Ver `Soluciones_y_Ejemplos/ejercicio6_tratamientos_eficacia.py`).

### Ejercicio 7 a 15: Retos de Precisión y Neurofisiología
*(Continuación del programa: latencias patológicas, LCR, edad de debut y dashboards interactivos).*

---

## BLOQUE 2: Comunicación Científica (PowerPoint Avanzado)

### Ejercicio 16: Prompt para Auditoría Integral Premium
**Enunciado:** Generación de un PowerPoint ejecutivo de 15 diapositivas con estética de alta gama y análisis de la "Evaluación de la Atrofia Cortical como Marcador de Progresión Estructural". Integración de `python-pptx` para automatización total.

**Toque Premium (Opcional):** Para elevar la calidad visual, utiliza **Napkin AI** para generar figuras técnicas (estilo 3D o dibujo técnico) e intégralas en tu script. Puedes usar layouts asimétricos mediante código para un acabado de consultoría:

```python
# Ejemplo de insertar una figura de Napkin AI con diseño "Floating" y barra lateral
def add_impact_slide(prs, title, text, napkin_img_path):
    slide = prs.slides.add_slide(prs.slide_layouts[5]) # Layout en blanco
    
    # Añadir un rectángulo de color lateral para diseño asimétrico
    from pptx.util import Inches
    from pptx.dml.color import RGBColor
    shape = slide.shapes.add_shape(6, 0, 0, Inches(0.2), Inches(7.5)) # Barra lateral
    shape.fill.solid()
    shape.fill.foreground_color.rgb = RGBColor(15, 32, 60)
    
    # Título con tipografía controlada
    title_place = slide.shapes.title
    title_place.text = title
    
    # Insertar la figura técnica de Napkin AI (centrada a la derecha)
    slide.shapes.add_picture(napkin_img_path, Inches(4), Inches(1.5), width=Inches(5))
```

---

## BLOQUE 3: Investigación y Publicación de Alto Impacto

### Ejercicio 17: Del Abstract al Manuscrito Final
**Fase A**: Búsqueda bibliográfica automatizada en OpenAlex con metadatos completos.
**Fase B**: Generación de artículo científico PDF real integrando datos locales y evidencia global.
