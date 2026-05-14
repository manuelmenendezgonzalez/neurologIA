import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from alzheimer_utils import load_and_clean_data

df = load_and_clean_data(os.path.join(ROOT, "base_datos_alzheimer.csv"))
features = [
    "Memoria_Diferida",
    "FAQ_Actual",
    "Plasma_pTau217",
    "LCR_Abeta42",
    "RM_Hipocampo_Pctl",
    "FDG_PET_TP_SUVR",
    "PET_Amiloide_Centiloid",
]

X = df[features]
X_scaled = StandardScaler().fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=20)
df["Cluster"] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df["PCA1"] = X_pca[:, 0]
df["PCA2"] = X_pca[:, 1]

plt.figure(figsize=(9, 6))
sns.scatterplot(x="PCA1", y="PCA2", hue="Cluster", data=df, palette="Set1")
plt.title("Clustering de fenotipos biologicos en Alzheimer")
plt.tight_layout()
plot_path = os.path.join(ROOT, "ej5_clusters_alzheimer.png")
plt.savefig(plot_path, dpi=300)
plt.close()

print(f"Clustering completado. Grafico: {plot_path}")
print(df.groupby("Cluster")[features].mean().round(2))
