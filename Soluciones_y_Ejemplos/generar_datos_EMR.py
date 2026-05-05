import pandas as pd
import numpy as np
import random

def generar_base_datos_total(n_pacientes=200):
    print(f"Generando base de datos total y coherente para {n_pacientes} pacientes...")
    
    data = []
    for i in range(1, n_pacientes + 1):
        # 1. Metadatos
        id_pac = i
        edad_debut = random.randint(18, 55)
        sexo = random.choice([0, 1])  # 0: Mujer, 1: Hombre
        actividad_basal = random.choice([0, 1, 2])  # 0: Baja, 1: Mod, 2: Alta
        tiempo_evol = random.randint(1, 15)
        
        # 2. Clínica
        factor_progresion = (actividad_basal + 1) * (tiempo_evol / 10.0)
        edss_actual = np.clip(1.5 + factor_progresion * 2 + np.random.normal(0, 0.5), 0, 9)
        edss_max = edss_actual + random.uniform(0, 1)
        num_brotes = int(np.random.poisson(1 + actividad_basal * 1.2))
        
        # 3. Resonancia (MRI)
        mri_lesiones = int(np.random.poisson(5 + actividad_basal * 8))
        mri_atrofia = np.clip(0.95 - (factor_progresion * 0.15) + np.random.normal(0, 0.02), 0.70, 0.99)
        mri_frontal = 1 if random.random() < (0.2 + actividad_basal * 0.2) else 0
        mri_temporal = 1 if random.random() < (0.1 + actividad_basal * 0.1) else 0
        
        # 4. Laboratorio / Funcional
        ocb = 1 if actividad_basal > 0 or random.random() < 0.4 else 0
        igg_index = round(random.uniform(0.3, 0.9) + actividad_basal * 0.5, 2)
        vep_lat = round(100 + factor_progresion * 30 + np.random.normal(0, 5), 1)
        ssep_lat = round(20 + factor_progresion * 10 + np.random.normal(0, 2), 1)
        
        # 5. Neuropsicología (NUEVO: Columnas para ejercicios 1-6)
        memoria_epi = int(np.clip(30 - factor_progresion * 10 + np.random.normal(0, 3), 5, 36))
        memoria_trab = int(np.clip(25 - factor_progresion * 8 + np.random.normal(0, 2), 5, 30))
        vel_proc = int(np.clip(90 - factor_progresion * 30 + np.random.normal(0, 10), 10, 110))
        func_ejec = int(np.clip(45 - factor_progresion * 15 + np.random.normal(0, 5), 10, 50))
        
        quejas_subjetivas = random.randint(1, 10)
        fatiga = int(np.clip(10 + factor_progresion * 20, 0, 40))
        ansiedad = 1 if random.random() < 0.3 else 0
        
        # Perfiles (Codificados)
        # Perfil_Neuro: 0: Normal, 1: Subcortical, 2: Cortical
        perfil_neuro = 0
        if vel_proc < 50: perfil_neuro = 1
        if memoria_epi < 15: perfil_neuro = 2
        
        # 6. Tratamiento
        # 0: Ninguno, 1: Inmunomodulador, 2: Alta Eficacia
        trat_cod = 1 if actividad_basal < 2 else 2
        if random.random() < 0.1: trat_cod = 0
        
        # --- CASO ESPECIAL ID 24 (Ejercicio 1) ---
        if i == 24:
            edad_debut, sexo, edss_actual, num_brotes = 24, 0, 1.5, 3
            memoria_epi, memoria_trab, vel_proc, func_ejec = 34, 28, 95, 48
            quejas_subjetivas, fatiga, ansiedad = 8, 22, 1
            trat_cod, perfil_neuro = 1, 1
            
        data.append({
            'ID': id_pac, 'Edad_Debut': edad_debut, 'Sexo': sexo,
            'Actividad_Basal': actividad_basal, 'Tiempo_Evol': tiempo_evol,
            'EDSS_Actual': round(edss_actual, 1), 'EDSS_Max': round(edss_max, 1),
            'Num_Brotes': num_brotes, 'MRI_Lesiones': mri_lesiones,
            'MRI_Atrofia': round(mri_atrofia, 4), 'MRI_Frontal': mri_frontal,
            'MRI_Temporal': mri_temporal, 'OCB': ocb, 'IgG_Index': igg_index,
            'VEP_Lat': vep_lat, 'SSEP_Lat': ssep_lat,
            'Memoria_Episodica': memoria_epi, 'Memoria_Trabajo': memoria_trab,
            'Velocidad_Proc': vel_proc, 'Funciones_Ejecutivas': func_ejec,
            'Quejas_Subjetivas': quejas_subjetivas, 'Fatiga': fatiga,
            'Ansiedad': ansiedad, 'Perfil_Neuro': perfil_neuro,
            'Tratamiento_Cod': trat_cod
        })

    df = pd.DataFrame(data)
    df.to_csv('base_datos_emrr.csv', index=False, sep=';')
    print("Base de datos coherente guardada como 'base_datos_emrr.csv' (SEP=;)")
    return df

if __name__ == "__main__":
    generar_base_datos_total()
