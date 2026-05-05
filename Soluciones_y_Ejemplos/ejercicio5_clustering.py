import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from neuro_utils import load_and_clean_data

df = load_and_clean_data()

# Variables para clustering (Inflamación vs Neurodegeneración)
features = ['Num_Brotes', 'MRI_Lesiones', 'MRI_Atrofia', 'VEP_Lat', 'Velocidad_Proc']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means (3 clusters: Inflamatorio, Neurodegenerativo, Mixto)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Reducción de dimensionalidad para visualizar
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set1')
plt.title("Fenotipos de EM: Clustering K-means (PCA)")
plt.savefig('ej5_clusters.png')
print("Análisis de clusters completado. Gráfico: ej5_clusters.png")
