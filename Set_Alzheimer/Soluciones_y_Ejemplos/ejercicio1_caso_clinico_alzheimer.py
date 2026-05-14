import matplotlib.pyplot as plt
import numpy as np
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from alzheimer_utils import get_patient_data, load_and_clean_data


df = load_and_clean_data(os.path.join(ROOT, "base_datos_alzheimer.csv"))
paciente = get_patient_data(df, 24)

metricas = [
    "Memoria_Diferida",
    "Fluencia_Semantica",
    "Funciones_Ejecutivas",
    "MMSE_Actual",
]
percentiles = {}

print("=" * 70)
print("CASO CLINICO ALZ_024")
print("=" * 70)
print(f"Edad: {paciente['Edad']} anos")
print(f"Estadio: {paciente['Estadio_Desc']}")
print(f"Tratamiento: {paciente['Tratamiento_Desc']}")
print(f"Perfil ATN: {paciente['ATN_Perfil']}")
print(f"Queja subjetiva: {paciente['Quejas_Memoria']}/10")
print(f"Anosognosia: {'SI' if paciente['Anosognosia_Cod'] == 1 else 'NO'}")
print("-" * 70)

for m in metricas:
    percentiles[m] = (df[m] < paciente[m]).mean() * 100
    print(f"{m:22}: {paciente[m]:>6} | Percentil {percentiles[m]:5.1f}")

print("-" * 70)
print(f"LCR Abeta42: {paciente['LCR_Abeta42']} pg/mL")
print(f"LCR pTau181: {paciente['LCR_pTau181']} pg/mL")
print(f"Plasma pTau217: {paciente['Plasma_pTau217']} pg/mL")
print(f"RM hipocampo pctl: {paciente['RM_Hipocampo_Pctl']}")
print(f"FDG-PET TP SUVR: {paciente['FDG_PET_TP_SUVR']}")
print(f"PET amiloide (centiloid): {paciente['PET_Amiloide_Centiloid']}")

labels = np.array(["Memoria", "Fluencia", "Ejecutivo", "MMSE"])
vals_pac = np.array([paciente[m] for m in metricas], dtype=float)
vals_mean = np.array([df[m].mean() for m in metricas], dtype=float)
vals_pac = vals_pac / vals_pac.max() * 100
vals_mean = vals_mean / vals_mean.max() * 100
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
labels = np.append(labels, labels[0])
vals_pac = np.append(vals_pac, vals_pac[0])
vals_mean = np.append(vals_mean, vals_mean[0])
angles = np.append(angles, angles[0])

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
ax.plot(angles, vals_pac, linewidth=2, label="Paciente 24")
ax.fill(angles, vals_pac, alpha=0.25)
ax.plot(angles, vals_mean, linewidth=2, linestyle="--", label="Media cohorte")
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1])
ax.set_yticklabels([])
ax.set_title("Perfil cognitivo multimodal: ALZ_024", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.savefig(os.path.join(ROOT, "radar_alz_024.png"), dpi=300)
plt.close(fig)

print("=" * 70)
print("CONCLUSION")
print("Patron compatible con enfermedad de Alzheimer temprana biomarcador-concordante,")
print("con anosognosia relativa y perfil ATN positivo. Caso razonable para discusion")
print("de estrategia antiamiloide si se mantiene elegibilidad clinico-radiologica.")
print("=" * 70)
