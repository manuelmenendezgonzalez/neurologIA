import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from neuro_utils import load_and_clean_data

# Cargar base de datos coherente
df = load_and_clean_data()

# ============================================================================
# PASO 1: Extraer datos del paciente específico (ID 24)
# ============================================================================
paciente_id = 24
paciente = df[df['ID'] == paciente_id].iloc[0]

print("=" * 60)
print(f"CASO CLÍNICO: EMRR_{paciente_id:03d}")
print("=" * 60)
print(f"Edad Debut: {paciente['Edad_Debut']} años")
print(f"EDSS actual: {paciente['EDSS_Actual']}")
print(f"Tratamiento: {paciente['Tratamiento_Desc']}")
print(f"Quejas subjetivas: {paciente['Quejas_Subjetivas']}/10")
print("-" * 60)

# ============================================================================
# PASO 2: Análisis de Disociación Subjetivo-Objetiva
# ============================================================================
metricas = ['Memoria_Episodica', 'Memoria_Trabajo', 'Velocidad_Proc', 'Funciones_Ejecutivas']
percentiles = {}

print("PERFIL NEUROPSICOLÓGICO (Percentiles):")
for m in metricas:
    perc = (df[m] < paciente[m]).mean() * 100
    percentiles[m] = perc
    print(f" - {m:20}: {paciente[m]:3} (Percentil {perc:3.0f}%)")

# Detección de Disociación
if paciente['Quejas_Subjetivas'] >= 7 and percentiles['Memoria_Episodica'] > 50:
    print("\nALERTA: Disociacion Subjetivo-Objetiva DETECTADA.")
    print("El paciente refiere mala memoria, pero sus tests objetivos son NORMALES.")
    print(f"Fatiga detectada: {paciente['Fatiga']}/40")
    print(f"Ansiedad detectable: {'SI' if paciente['Ansiedad'] == 1 else 'NO'}")

# ============================================================================
# PASO 3: Visualización Radar (Paciente vs Media)
# ============================================================================
labels = np.array(['Memoria', 'Trabajo', 'Velocidad', 'Ejecución'])
stats_pac = np.array([paciente[m] for m in metricas])
stats_mean = np.array([df[m].mean() for m in metricas])

# Normalización para el gráfico
stats_pac_norm = stats_pac / stats_pac.max() * 100
stats_mean_norm = stats_mean / stats_mean.max() * 100
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

# Cerramos el radar repitiendo el primer punto al final.
labels = np.append(labels, labels[0])
stats_pac_norm = np.append(stats_pac_norm, stats_pac_norm[0])
stats_mean_norm = np.append(stats_mean_norm, stats_mean_norm[0])
angles = np.append(angles, angles[0])

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'projection': 'polar'})
ax.plot(angles, stats_pac_norm, color='#1f77b4', linewidth=2, label='Paciente 24')
ax.fill(angles, stats_pac_norm, color='#1f77b4', alpha=0.25)
ax.plot(angles, stats_mean_norm, color='#ff7f0e', linewidth=2, linestyle='--', label='Media cohorte')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1])
ax.set_yticklabels([])
ax.set_title("Perfil neuropsicologico: Paciente 24 vs Cohorte", pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.savefig("radar_paciente_24.png", dpi=300)
plt.close(fig)

print("\nVisualización generada: radar_paciente_24.png")
print("=" * 60)
print("CONCLUSIÓN: Mantener tratamiento actual. Tratar ansiedad y fatiga.")
print("=" * 60)
