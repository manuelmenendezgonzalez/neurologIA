import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from neuro_utils import load_and_clean_data

df = load_and_clean_data()

print("ANÁLISIS DE EFICACIA (VIDA REAL)")
print("-" * 40)

# Comparar EDSS Final ajustando por Actividad Basal
resumen = df.groupby(['Actividad_Basal', 'Tratamiento_Desc'])['EDSS_Actual'].mean().unstack()
print("EDSS Medio (Fila: Actividad Basal | Col: Tratamiento):")
print(resumen)

plt.figure(figsize=(10, 6))
sns.barplot(x='Actividad_Basal', y='EDSS_Actual', hue='Tratamiento_Desc', data=df)
plt.title("Eficacia Terapéutica Ajustada por Actividad Basal")
plt.savefig('ej6_eficacia.png')
print("\nGráfico guardado: ej6_eficacia.png")
