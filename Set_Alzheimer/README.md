# NeuroIA Alzheimer

Set de ejercicios sobre la enfermedad de Alzheimer y otras demencias.

## Contenido

- `base_datos_alzheimer.csv`: cohorte sintetica principal.
- `Base_Datos_Alzheimer_Final.xlsx`: cohorte + diccionario de variables.
- `alzheimer_utils.py`: funciones de carga, limpieza y variables derivadas.
- `preguntas_ejercicios_ALZ.md`: programa de ejercicios.
- `Soluciones_y_Ejemplos/`: scripts ejecutables y materiales generados.

## Flujo docente recomendado

- Ejecuta primero `python ..\check_env.py` para validar dependencias y Quarto.
- Resuelve primero el `Ejercicio 2` para producir la presentacion ejecutiva.
- Pide despues al IDE que redacte el `Ejercicio 17` como un paper cientifico real, reutilizando la estructura del `Ejercicio 2`.
- Para `Introduccion` y `Discusion`, pide al IDE que busque referencias reales y actualice `references.bib`.
- El articulo final no debe mencionar curso, set, ejercicio, presentacion, alumno ni profesor.

## Supuestos terapeuticos

La cohorte usa terapias sintomaticas habituales y anticuerpos antiamiloide con autorizacion europea.

- Sintomaticos: donepezilo, rivastigmina, galantamina, memantina y combinacion donepezilo-memantina.
- Antiamiloide: lecanemab y donanemab.

Nota docente:
Los codigos `Lecanemab_UE` y `Donanemab_UE` representan farmacos autorizados por la UE, pero su acceso real puede depender de comercializacion, precio y financiacion nacional.
