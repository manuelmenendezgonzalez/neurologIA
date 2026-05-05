import pandas as pd

def load_and_clean_data(path="base_datos_emrr.csv"):
    """Carga la base de datos científica refactorizada."""
    df = pd.read_csv(path, sep=';')
    
    # Añadimos algunas etiquetas de conveniencia para visualización
    # pero mantenemos los números para el análisis
    mapping_trat = {0: 'Ninguno', 1: 'Inmunomodulador', 2: 'Alta Eficacia'}
    df['Tratamiento_Desc'] = df['Tratamiento_Cod'].map(mapping_trat)
    
    mapping_sexo = {0: 'Mujer', 1: 'Hombre'}
    df['Sexo_Desc'] = df['Sexo'].map(mapping_sexo)
    
    # Flags de normalidad
    df['VEP_Patologico'] = (df['VEP_Lat'] > 110).astype(int)
    df['MRI_Atrofia_Severa'] = (df['MRI_Atrofia'] < 0.80).astype(int)
    
    return df

def get_patient_data(df, patient_id_num):
    """Extrae los datos de un paciente por su ID numérico."""
    return df[df['ID'] == patient_id_num].iloc[0]
