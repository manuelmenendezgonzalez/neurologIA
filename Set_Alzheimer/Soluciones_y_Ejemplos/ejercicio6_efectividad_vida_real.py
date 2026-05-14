import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from alzheimer_utils import load_and_clean_data

df = load_and_clean_data(os.path.join(ROOT, "base_datos_alzheimer.csv"))

resumen = (
    df.groupby(["Estadio_Desc", "Tratamiento_Desc"])["Declive_MMSE_Anual"]
    .mean()
    .unstack()
    .round(2)
)

print("EFECTIVIDAD OBSERVACIONAL Y SESGO DE INDICACION")
print("-" * 60)
print("Declive anualizado medio de MMSE por estadio y tratamiento:")
print(resumen)

plt.figure(figsize=(10, 6))
sns.barplot(
    x="Estadio_Desc",
    y="Declive_MMSE_Anual",
    hue="Tratamiento_Desc",
    data=df,
)
plt.xticks(rotation=15)
plt.tight_layout()
plot_path = os.path.join(ROOT, "ej6_efectividad_alzheimer.png")
plt.savefig(plot_path, dpi=300)
plt.close()
print(f"Grafico guardado: {plot_path}")
