# Guia para Alumnos: Primeros Pasos con Codex

Esta guia esta escrita para medicos que no han usado antes un IDE. No necesitas saber programar, ni saber que es un repositorio, ni instalar cosas manualmente una por una. La idea es que le pidas a Codex que lo haga por ti dentro del IDE a partir del repositorio publico del curso.

---

## Objetivo de la sesion

No vamos a aprender a programar.

Vamos a aprender a:

- abrir un IDE
- pedir bien a Codex lo que queremos
- dejar que Codex prepare el entorno
- ejecutar ejercicios clinicos
- revisar si el resultado tiene sentido medico

## 1. Abre el IDE

Abre tu IDE con IA integrada, por ejemplo Codex, Windsurf o equivalente.

No crees archivos a mano. No abras terminales por tu cuenta salvo que el IDE te las abra automaticamente.

## 2. Primera instruccion que debes darle a Codex

Nada mas abrir el IDE, copia y pega esto:

```text
Clona en mi equipo el repositorio publico del curso https://github.com/manuelmenendezgonzalez/neurologIA.git dentro de un directorio local llamado "Curso NeuroIA" y trabaja desde ahi. Quiero que prepares todo el entorno desde cero para este curso. Antes de hacer cambios, dime en 3-5 lineas que pasos vas a seguir.
```

Si el IDE necesita una formulacion todavia mas simple, usa esta alternativa:

```text
Descarga en mi ordenador el repositorio publico del curso desde https://github.com/manuelmenendezgonzalez/neurologIA.git dentro de una carpeta llamada "Curso NeuroIA". Despues trabaja desde esa carpeta y prepara todo para empezar.
```

## 3. Segunda instruccion: que lea los documentos correctos

Cuando Codex te confirme que ya ha clonado el repositorio y esta trabajando en la carpeta `Curso NeuroIA`, copia y pega esto:

```text
Lee los documentos principales del curso para orientarte antes de hacer nada mas: GUIA_ALUMNOS.md, README.md, requirements.txt, check_env.py, Set_Alzheimer/README.md y Set_Alzheimer/preguntas_ejercicios_ALZ.md. Despues instala lo necesario y deja el entorno listo para trabajar.
```

## 4. Tercera instruccion: que prepare el entorno por ti

Ahora copia y pega esto:

```text
Instala todas las dependencias del curso y ejecuta la comprobacion del entorno con python check_env.py. Si encuentras errores, resuelvelos tu y vuelve a ejecutar la comprobacion hasta que el entorno quede listo. Despues dime solo si el estado final es READY o que problema concreto queda pendiente.
```

Tu objetivo aqui no es entender la instalacion. Tu objetivo es aprender a pedirle al IDE que la resuelva.

## 5. Cuarta instruccion: preparar el set Alzheimer

Cuando Codex te diga que el entorno esta listo, copia y pega esto:

```text
Prepara el set de Alzheimer para trabajar. Genera o regenera la cohorte si hace falta, revisa que existe el archivo base_datos_alzheimer.csv y usa siempre alzheimer_utils.py para cargar y limpiar los datos. No programes nada nuevo todavia; solo deja todo listo y dime que ya puedo empezar con los ejercicios.
```

## 6. Como empezar un ejercicio

No le pidas codigo suelto. Pidele a Codex que haga el ejercicio de principio a fin.

### Para el primer ejercicio

Usa este prompt:

```text
Resuelve el Ejercicio 1 del set Alzheimer como si fueras un alumno. Lee primero el enunciado en Set_Alzheimer/preguntas_ejercicios_ALZ.md, usa alzheimer_utils.py para cargar el dataset y ejecuta el analisis completo. No me des solo codigo: haz el trabajo, ejecútalo y resume el resultado con criterio clinico.
```

### Para cualquier ejercicio posterior

Usa este esquema:

```text
Resuelve el Ejercicio [numero] del set Alzheimer como si fueras un alumno. Lee el enunciado, decide que archivos necesitas, ejecuta el trabajo completo en el IDE y ensename solo el resultado final y la interpretacion clinica.
```

## 7. Como trabajar el articulo sin programar

Cuando llegues al articulo, no debes redactarlo ni buscar bibliografia a mano. Debes pedirselo a Codex.

Usa este prompt:

```text
Redacta el articulo del Ejercicio 17 como un paper cientifico realista y clinicamente plausible. Usa la estructura del Ejercicio 2. Busca referencias reales para Introduccion y Discusion, actualiza references.bib si hace falta y cita solo con formato Quarto [@clave]. No menciones curso, ejercicio, set, presentacion, diapositivas, alumno ni profesor. En Resultados y Conclusiones habla solo de hallazgos clinicos y cientificos.
```

## 8. Como corregir un mal resultado

Si el resultado no te convence, no digas solo “esta mal”. Dale a Codex una correccion concreta.

Ejemplos:

```text
La interpretacion clinica no me convence. Revisa si los hallazgos tienen sentido para enfermedad de Alzheimer temprana y corrige el analisis.
```

```text
El texto suena a instrucciones de curso y no a paper cientifico. Reescribelo con tono de articulo biomedico real.
```

```text
La tabla es demasiado ancha para un PDF. Simplificala o dividela en dos tablas mas legibles.
```

## 9. Que no debes hacer

- No programes a mano salvo que el profesor te lo pida expresamente.
- No abras archivos para editarlos tu mismo si Codex puede hacerlo.
- No copies y pegues bibliografia inventada.
- No aceptes un resultado solo porque “ha salido”.
- No asumas que un grafico es correcto si clinicamente no tiene sentido.

## 10. Que si debes hacer

- Pedir instrucciones claras.
- Dejar que Codex ejecute el trabajo.
- Revisar si el resultado tiene sentido neurologico.
- Corregir el prompt si la salida no es buena.
- Pedir una segunda version si el tono, la clinica o la estructura no son adecuados.

## 11. Frase clave de trabajo

La forma correcta de trabajar en este curso es:

```text
No quiero solo codigo. Quiero que hagas el trabajo completo en el IDE, lo ejecutes y me devuelvas un resultado final clinicamente coherente.
```

## 12. Si algo falla al principio

Si ni siquiera puedes arrancar, usa este prompt:

```text
No tengo conocimientos tecnicos. Quiero que clones en mi ordenador el repositorio publico https://github.com/manuelmenendezgonzalez/neurologIA.git dentro de una carpeta llamada Curso NeuroIA, leas los documentos del curso, instales todo lo necesario, ejecutes python check_env.py y soluciones cualquier problema inicial. Explicame solo lo imprescindible y dime cuando pueda empezar con el Ejercicio 1.
```
