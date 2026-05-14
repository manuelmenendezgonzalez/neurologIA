# Certificacion en Prompt Engineering para Neurologia
## Programa de Ejercicios: Enfermedad de Alzheimer

## Guia de inicio rapido

1. Instala dependencias con `pip install -r ..\requirements.txt`.
2. Valida el entorno con `python ..\check_env.py`.
3. Genera o regenera la cohorte con `python Soluciones_y_Ejemplos\generar_datos_alzheimer.py`.
4. Usa siempre `alzheimer_utils.py` para cargar datos y crear variables derivadas.
5. Resuelve primero el `Ejercicio 2` y usa despues esa estructura para el `Ejercicio 17`.
6. Para `Introduccion` y `Discusion`, no hagas la bibliografia a mano: pide al IDE que la busque y la cite automaticamente.

### Infraestructura de datos

- Fuente: `base_datos_alzheimer.csv` (SEP=`;`)
- Soporte: `alzheimer_utils.py`
- Diccionario: `Base_Datos_Alzheimer_Final.xlsx`
- Derivadas comunes creadas por `alzheimer_utils.py`: `ATN_Perfil`, `Declive_MMSE_Anual`, `Cambio_CDRSB_Anual`, `Estado_Progresion`, `Candidato_Antiamiloide`

## Nota tecnica para Windows

Si Quarto intenta usar `python3.13t.exe`, fija antes el interprete estandar:

```powershell
$env:QUARTO_PYTHON="C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python313\python.exe"
```

## Nota terapeutica

Este set utiliza tratamientos sintomaticos aprobados y anticuerpos antiamiloide con autorizacion europea.

- `Leqembi` (`lecanemab`): autorizacion UE emitida el **15 de abril de 2025**.
- `Kisunla` (`donanemab`): autorizacion UE emitida el **24 de septiembre de 2025**.
- `Aduhelm` (`aducanumab`): solicitud retirada en la UE el **20 de abril de 2022**.

Los codigos antiamiloide representan autorizacion regulatoria europea; no implican disponibilidad homogenea en cada pais.

---

## BLOQUE 1: Analisis de datos que Codex puede resolver end-to-end

### Ejercicio 1: Caso clinico ALZ_024 (anosognosia biomarcador-concordante)
**Enunciado:** Analiza al paciente 24 como caso de DCL amnesico/EA prodromica. Integra neuropsicologia, queja subjetiva, anosognosia, LCR, plasma, RM, FDG-PET y PET de amiloide. El script debe calcular percentiles y concluir si el patron es compatible con enfermedad de Alzheimer temprana.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio1_caso_clinico_alzheimer.py`).

### Ejercicio 2: Progresion cognitiva anual y presentacion ejecutiva
**Enunciado:** Clasifica a los pacientes en `progresores rapidos` frente a `progresores lentos/estables` segun el declive anualizado de MMSE y el cambio de CDR-SB. El script debe generar una presentacion `.pptx` con una estructura fija que luego servira como esqueleto del manuscrito.
**Apartados obligatorios de la presentacion:**
- `Resumen clinico`
- `Cohorte y estratificacion`
- `Progresion cognitiva anual`
- `Progresion funcional anual`
- `Biomarcadores y ritmo de progresion`
- `Tratamiento y sesgo de indicacion`
- `Elegibilidad antiamiloide`
- `Interpretacion clinica y limitaciones`
- `Conclusiones`
**Regla docente:** estos titulos no son decorativos; el manuscrito del `Ejercicio 17` debe reutilizarlos en el mismo orden.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio2_progresion_alzheimer.py`).

### Ejercicio 3: Regresion multimodal de discapacidad
**Enunciado:** Modeliza el impacto independiente de la volumetria hipocampal, el FDG-PET y los biomarcadores tau sobre `CDR_SB_Actual`.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio3_regresion_multimodal.py`).

### Ejercicio 4: Clasificador de positividad amiloide
**Enunciado:** Entrena un clasificador para predecir positividad amiloide (`PET_Amiloide_Centiloid >= 25`) a partir de biomarcadores plasmaticos y RM, y resume la importancia de variables.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio4_clasificador_amiloide.py`).

### Ejercicio 5: Clustering de fenotipos biologicos
**Enunciado:** Aplica `K-means` sobre variables cognitivas y biomarcadores para identificar perfiles como amiloide-dominante temprano, Alzheimer neurodegenerativo establecido y comparadores biomarcador-negativos.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio5_clustering_alzheimer.py`).

### Ejercicio 6: Efectividad observacional y sesgo de indicacion
**Enunciado:** Compara el declive cognitivo anual entre terapias, ajustando descriptivamente por estadio clinico y carga amiloide basal.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio6_efectividad_vida_real.py`).

---

## BLOQUE 2: Comunicacion cientifica

### Ejercicio 16: Auditoria de biomarcadores
**Enunciado:** Genera un PowerPoint ejecutivo de 15 diapositivas sobre `Seleccion de candidatos a tratamiento antiamiloide basada en biomarcadores multimodales`, con estilo consultoria y figuras derivadas de la cohorte local.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/ejercicio16_auditoria_alzheimer_premium.py`).

---

## BLOQUE 3: Investigacion y publicacion

### Ejercicio 17: Del dataset al manuscrito reproducible
**Enunciado:** Genera un articulo cientifico `.qmd` con analisis ejecutables y salida PDF sobre la asociacion entre biomarcadores de Alzheimer y deterioro cognitivo/funcional.
**Flujo obligatorio con el IDE:**
- Antes de redactar, pide al IDE que busque automaticamente referencias reales para `Introduccion` y `Discusion`.
- El IDE puede usar PubMed, Crossref, OpenAlex y herramientas Python para construir o actualizar `references.bib`.
- La `Introduccion` y la `Discusion` deben escribirse usando solo referencias contenidas en `references.bib`.
- El formato de citacion dentro del `.qmd` debe ser Quarto/Pandoc: `[@clave]`.
**Prompt recomendado para el IDE:**

```text
Redacta el articulo como un paper cientifico realista y clinicamente plausible. Busca de forma automatica referencias reales para la Introduccion y la Discusion, genera o actualiza references.bib y cita solo con formato Quarto [@clave]. Usa los apartados del Ejercicio 2 como estructura. No menciones que esto es un set, un ejercicio, un curso, una presentacion, una diapositiva, un alumno o un profesor. En Resultados y Conclusiones habla solo de hallazgos clinicos y cientificos.
```

**Reglas obligatorias de redaccion:**
- El articulo debe expandir todos los apartados de la presentacion del `Ejercicio 2`.
- Cada diapositiva de contenido del `Ejercicio 2` debe convertirse en una seccion o subseccion del manuscrito.
- El orden de las secciones del articulo debe ser el mismo que el orden de las diapositivas.
- La redaccion del articulo debe ser mas extensa que la de la presentacion: no basta con copiar bullets.
- Cada seccion debe anadir contexto clinico, interpretacion de resultados, transiciones narrativas y limitaciones cuando proceda.
- Si una diapositiva resume un hallazgo, el articulo debe desarrollarlo en varios parrafos y, cuando aporte valor, con tabla o figura propia.
- Si una tabla queda demasiado ancha para PDF, debe simplificarse o dividirse; no se considera obligatorio mantener una tabla unica si compromete la legibilidad.
- La `Introduccion` y la `Discusion` no deben contener referencias inventadas ni afirmaciones factuales sin cita.
- El articulo final no debe contener comentarios metadocentes ni referencias al curso, al set, al ejercicio o al flujo de trabajo.
**Formula practica para el alumno:** `presentacion = esquema`; `articulo = desarrollo cientifico del mismo esquema`.
**Estado:** Completado (ver `Soluciones_y_Ejemplos/articulo_neuroia_alzheimer.qmd`).
