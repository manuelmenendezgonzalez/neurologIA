# /paper — Elaboración de Manuscritos Científicos de Alto Impacto

**Description**: Transforma análisis de datos y abstracts en manuscritos científicos listos para publicación.

### Protocolo de Ejecución:
1. **Búsqueda de Evidencia**: Realiza búsquedas bibliográficas automatizadas (ej. OpenAlex) para contextualizar los hallazgos con metadatos completos.
2. **Integración de Datos Locales**: Procesa la cohorte local para extraer estadísticos clave, p-values y métricas de efecto.
3. **Redacción Estructural**:
    - Genera el contenido siguiendo la estructura IMRyD (Introducción, Métodos, Resultados y Discusión).
    - Mantiene un tono clínico formal y riguroso.
4. **Capa de Calidad Lingüística**:
    - Corrección ortotipográfica exhaustiva (tildes, signos de puntuación, gramática).
    - Conversión de decimales al estándar español (comas).
5. **Generación de Salida**:
    - Crea el manuscrito en formato Quarto (.qmd) o LaTeX para exportación a PDF real.
    - Asegura que las citas bibliográficas estén correctamente formateadas (ej. estilo Vancouver o APA).

### Reglas de Estilo:
- Evitar adjetivos innecesarios; priorizar la objetividad.
- Integrar tablas y leyendas de figuras de forma coherente.
- El manuscrito debe ser "self-contained" y listo para revisión por pares.
