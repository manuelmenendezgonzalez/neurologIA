# /slides — Generador de Presentaciones Clínicas Premium

**Description**: Genera presentaciones de alta gama para neurología utilizando un flujo de "Slides as Code".

### Protocolo de Ejecución:
1. **Comprensión del Contexto**: Analiza la cohorte de datos y el objetivo clínico (ej. Auditoría de Atrofia, Eficacia Terapéutica).
2. **Generación de Figuras Técnicas**:
    - Crea gráficos científicos con Seaborn/Matplotlib (estilo limpio, colores corporativos).
    - Genera una figura conceptual de alta calidad (estilo Napkin AI) usando `generate_image`.
3. **Desarrollo del Script**:
    - Crea un archivo Python que utilice `python-pptx`.
    - **LAYOUT OBLIGATORIO**: Doble columna (4.5" Texto | 4.2" Imagen) con margen de 0.6".
    - Implementa `word_wrap` y `TEXT_TO_FIT_SHAPE` para evitar desbordamientos.
4. **Capa de Calidad Lingüística**:
    - Revisa gramática, tildes y puntuación de todos los textos.
    - Usa terminología médica precisa (evita sensacionalismos).
    - Usa coma (,) para decimales.
5. **Compilación**: Ejecuta el script y verifica que el archivo .pptx se genere sin errores de permisos.

### Estética Requerida:
- Títulos en Azul Profundo (#0F203C).
- Acentos en Verde Esmeralda (#2ECC71).
- Tipografía moderna (Segoe UI / Arial).
- Barra lateral decorativa en cada slide.
