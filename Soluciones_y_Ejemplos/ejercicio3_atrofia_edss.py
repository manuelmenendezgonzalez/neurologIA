import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from neuro_utils import load_and_clean_data

df = load_and_clean_data()

# Crear Terciles de Atrofia
ranked_atrofia = df['MRI_Atrofia'].rank(method='first')
df['Tercil_Atrofia'] = pd.qcut(ranked_atrofia, 3, labels=['Severa', 'Moderada', 'Leve'])

print("ANÁLISIS DE REGRESIÓN: IMPACTO DE LA ATROFIA")
print("-" * 50)

# Regresión Multivariable: EDSS ~ Atrofia + Edad_Debut + Num_Brotes
X = df[['MRI_Atrofia', 'Edad_Debut', 'Num_Brotes']]
X = sm.add_constant(X)
y = df['EDSS_Actual']

model = sm.OLS(y, X).fit()
print(model.summary())

plt.figure(figsize=(10, 6))
sns.boxplot(x='Tercil_Atrofia', y='EDSS_Actual', data=df, palette='Reds_r')
plt.title("Discapacidad (EDSS) según Grado de Atrofia Cortical")
plt.savefig('ej3_atrofia_edss.png')
print("\nGráfico guardado: ej3_atrofia_edss.png")
