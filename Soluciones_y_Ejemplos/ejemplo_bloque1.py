import pandas as pd
from neuro_utils import load_and_clean_data

# Carga de datos unificada
df = load_and_clean_data()

print("PLANTILLA BLOQUE 1: Estadísticas Descriptivas")
print("-" * 50)
print(f"Total de pacientes: {len(df)}")
print(f"Edad media al debut: {df['Edad_Debut'].mean():.1f} años")
print(f"Distribución por Sexo (0=M, 1=H):\n{df['Sexo'].value_counts(normalize=True)*100}")
print(f"\nEDSS Actual Medio: {df['EDSS_Actual'].mean():.2f}")
