# Guia para Alumnos: Curso NeuroIA

Esta guia esta pensada para que aprendas a trabajar con Codex o con tu IDE con IA integrada. La idea no es que recibas soluciones cerradas, sino que aprendas a pedir al IDE el tipo de resultado correcto.

---

## 1. Instala el entorno base

1. Instala Python 3.11, 3.12 o 3.13 en su version estandar.
2. En Windows, durante la instalacion marca `Add Python to PATH`.
3. No uses la version free-threaded `python3.13t.exe`.
4. Instala Quarto aparte desde [quarto.org](https://quarto.org/docs/download/).

## 2. Instala dependencias del curso

Abre una terminal en la carpeta raiz del repositorio y ejecuta:

```bash
pip install -r requirements.txt
python check_env.py
```

Si `check_env.py` termina en `READY`, el entorno esta preparado.

## 3. Flujo minimo para el set de Alzheimer

La secuencia correcta es:

1. Generar o regenerar la cohorte:

```bash
python Set_Alzheimer\Soluciones_y_Ejemplos\generar_datos_alzheimer.py
```

2. Trabajar siempre sobre:

- `Set_Alzheimer/base_datos_alzheimer.csv`
- `Set_Alzheimer/alzheimer_utils.py`
- `Set_Alzheimer/preguntas_ejercicios_ALZ.md`

3. Usar `load_and_clean_data()` desde `alzheimer_utils.py` en lugar de leer el CSV a mano.

Esto es importante porque `alzheimer_utils.py` ya crea variables derivadas comunes para todos los ejercicios:

- `Amyloid_Pos`
- `Tau_Pos`
- `Neurodeg_Pos`
- `ATN_Perfil`
- `Declive_MMSE_Anual`
- `Cambio_CDRSB_Anual`
- `Estado_Progresion`
- `Candidato_Antiamiloide`

## 4. Como pedir al IDE la bibliografia automatica

No debes construir la bibliografia a mano. Debes pedirselo al IDE.

Prompt recomendado:

```text
Busca de forma automatica 12-20 referencias reales y relevantes para la Introduccion y la Discusion del articulo sobre enfermedad de Alzheimer. Usa PubMed, Crossref u OpenAlex con herramientas Python si lo necesitas. Genera o actualiza references.bib y redacta despues la Introduccion y la Discusion usando solo esas referencias y citacion Quarto [@clave]. No inventes citas.
```

Prompt reforzado para controlar el tono final:

```text
El resultado final debe parecer un paper cientifico real. No menciones que esto es un set, un ejercicio, un curso, una presentacion, una diapositiva, un alumno o un profesor. En Resultados y Conclusiones habla solo de hallazgos clinicos y cientificos.
```

Reglas importantes:

- El IDE debe citar solo referencias presentes en `references.bib`.
- La `Introduccion` y la `Discusion` no deben inventar bibliografia.
- Si falta una referencia clave, el IDE debe ampliar la busqueda y regenerar `references.bib`.
- Si el IDE necesita automatizar la busqueda, debe crear sus propios scripts auxiliares.

## 5. Regla clave entre Ejercicio 2 y Ejercicio 17

En el bloque de Alzheimer, el `Ejercicio 2` y el `Ejercicio 17` estan ligados.

- El `Ejercicio 2` genera una presentacion con apartados fijos.
- El `Ejercicio 17` debe reutilizar esos mismos apartados en el mismo orden.
- La presentacion es el esquema.
- El articulo es el desarrollo extenso y coherente de ese esquema.
- El paper final no puede hablar del curso, del set, del ejercicio, del profesor, del alumno ni del propio flujo de trabajo.

## 6. Que debes pedirle al IDE para el articulo

Prompt recomendado para el manuscrito:

```text
Redacta el articulo como un paper cientifico realista y clinicamente plausible. Usa los apartados del Ejercicio 2 como estructura. La Introduccion y la Discusion deben estar sustentadas en referencias reales. Los Resultados deben limitarse a describir hallazgos del analisis. La Discusion debe comparar esos hallazgos con la literatura. Elimina cualquier comentario metadocente o cualquier referencia a set, ejercicio, curso, presentacion, alumno o profesor.
```

## 7. Ejercicios que debes ejecutar en orden

Bloque 1:

```bash
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio1_caso_clinico_alzheimer.py
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio2_progresion_alzheimer.py
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio3_regresion_multimodal.py
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio4_clasificador_amiloide.py
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio5_clustering_alzheimer.py
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio6_efectividad_vida_real.py
```

Bloque 2:

```bash
python Set_Alzheimer\Soluciones_y_Ejemplos\ejercicio16_auditoria_alzheimer_premium.py
```

Bloque 3:

```bash
quarto render Set_Alzheimer\Soluciones_y_Ejemplos\articulo_neuroia_alzheimer.qmd
```

## 8. Nota importante para Quarto en Windows

Si Quarto intenta usar `python3.13t.exe` o falla al ejecutar celdas Python, fuerza el interprete correcto:

```powershell
$env:QUARTO_PYTHON="C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python313\python.exe"
quarto render Set_Alzheimer\Soluciones_y_Ejemplos\articulo_neuroia_alzheimer.qmd
```

## 9. Como evitar errores frecuentes en el manuscrito

- No construyas tablas muy anchas para PDF.
- Si una tabla tiene demasiadas columnas, reduce variables o dividela en dos tablas.
- No copies bullets tal cual al articulo: conviertelos en parrafos con contexto, interpretacion y limitaciones.
- La `Introduccion` y la `Discusion` deben incluir citas Quarto reales tipo `[@jack2018]`.
- El paper final no debe contener frases metadocentes ni comentarios sobre la calidad del set o del ejercicio.

## 10. Resultado esperado del set Alzheimer

Si todo esta bien instalado, deberias poder generar al menos estos archivos:

- `Set_Alzheimer/Ejercicio2_Progresion_Alzheimer.pptx`
- `Set_Alzheimer/Auditoria_Clinica_Alzheimer.pptx`
- `Set_Alzheimer/Soluciones_y_Ejemplos/articulo_neuroia_alzheimer.pdf`

## 11. Si algo falla

1. Reejecuta:

```bash
python check_env.py
```

2. Comprueba que estas usando el repo correcto y que existe `Set_Alzheimer`.
3. Si el error es de Quarto, revisa primero `QUARTO_PYTHON`.
4. Si el error es de codigo, vuelve a cargar datos usando `load_and_clean_data()`.
5. Si el error es de bibliografia, pide al IDE que revise su propia estrategia de busqueda, conectividad y formato de citas.
