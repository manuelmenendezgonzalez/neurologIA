import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from alzheimer_utils import load_and_clean_data

df = load_and_clean_data(os.path.join(ROOT, "base_datos_alzheimer.csv"))
df["Tercil_Hipocampo"] = pd.qcut(
    df["RM_Hipocampo_Pctl"].rank(method="first"),
    3,
    labels=["Muy bajo", "Intermedio", "Conservado"],
)

X = df[["RM_Hipocampo_Pctl", "FDG_PET_TP_SUVR", "LCR_pTau181", "Plasma_pTau217", "Edad"]]
X = sm.add_constant(X)
y = df["CDR_SB_Actual"]
model = sm.OLS(y, X).fit()

print("REGRESION MULTIMODAL SOBRE CDR-SB")
print("-" * 60)
print(model.summary())

plt.figure(figsize=(9, 6))
sns.boxplot(x="Tercil_Hipocampo", y="CDR_SB_Actual", data=df, hue="Tercil_Hipocampo", palette="Blues", legend=False)
plt.title("CDR-SB segun volumetria hipocampal")
plt.tight_layout()
plot_path = os.path.join(ROOT, "ej3_regresion_multimodal.png")
plt.savefig(plot_path, dpi=300)
plt.close()
print(f"Grafico guardado: {plot_path}")
