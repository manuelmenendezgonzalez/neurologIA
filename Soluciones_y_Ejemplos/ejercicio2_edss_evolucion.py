import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from neuro_utils import load_and_clean_data

df = load_and_clean_data()

# Definir "Progresores" (aquellos cuyo EDSS actual es significativamente mayor al basal/estimado)
# En nuestra cohorte plana usamos el EDSS_Max como proxy de progresión histórica
df['Incremento_EDSS'] = df['EDSS_Max'] - 1.5 # 1.5 es la media basal aproximada
df['Estado_Progresion'] = df['Incremento_EDSS'].apply(lambda x: 'Progresor' if x > 1 else 'Estable')

print("ANÁLISIS DE EVOLUCIÓN TEMPORAL (EDSS)")
print("-" * 40)
print(df.groupby(['Tratamiento_Desc', 'Estado_Progresion']).size().unstack())

plt.figure(figsize=(10, 6))
sns.violinplot(x='Tratamiento_Desc', y='EDSS_Actual', hue='Estado_Progresion', data=df, split=True)
plt.title("Distribución de EDSS por Tratamiento y Estado de Progresión")
plt.savefig('ej2_edss_evolucion.png')
print("\nGráfico guardado: ej2_edss_evolucion.png")
