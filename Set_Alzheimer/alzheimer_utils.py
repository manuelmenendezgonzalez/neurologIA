from pathlib import Path

import pandas as pd


TRATAMIENTO_MAP = {
    0: "Ninguno",
    1: "Donepezilo",
    2: "Rivastigmina",
    3: "Galantamina",
    4: "Memantina",
    5: "Donepezilo_Memantina",
    6: "Lecanemab_UE",
    7: "Donanemab_UE",
}

ESTADIO_MAP = {
    0: "Queja subjetiva / No demencia",
    1: "DCL amnésico",
    2: "Demencia leve",
    3: "Demencia moderada",
}

SEXO_MAP = {0: "Mujer", 1: "Hombre"}
APOE4_MAP = {0: "No portador", 1: "Heterocigoto", 2: "Homocigoto"}

STAGE_ORDER = [
    "Queja subjetiva / No demencia",
    "DCL amnésico",
    "Demencia leve",
    "Demencia moderada",
]

EJ2_PRESENTATION_SECTIONS = [
    "Resumen clinico",
    "Cohorte y estratificacion",
    "Progresion cognitiva anual",
    "Progresion funcional anual",
    "Biomarcadores y ritmo de progresion",
    "Tratamiento y sesgo de indicacion",
    "Elegibilidad antiamiloide",
    "Interpretacion clinica y limitaciones",
    "Conclusiones",
]

FAST_MMSE_THRESHOLD = 2.0
FAST_CDRSB_THRESHOLD = 0.9


def _normalize_path(path):
    return Path(path)


def compute_progression_state(
    df,
    mmse_threshold=FAST_MMSE_THRESHOLD,
    cdrsb_threshold=FAST_CDRSB_THRESHOLD,
):
    return (
        (df["Declive_MMSE_Anual"] >= mmse_threshold)
        | (df["Cambio_CDRSB_Anual"] >= cdrsb_threshold)
    ).map({True: "Progresor rapido", False: "Lento/estable"})


def summarize_stage_table(df):
    return (
        df.groupby("Estadio_Desc", observed=False)
        .agg(
            n=("ID", "count"),
            mmse_mediana=("MMSE_Actual", "median"),
            cdrsb_mediana=("CDR_SB_Actual", "median"),
            faq_mediana=("FAQ_Actual", "median"),
            declive_mmse=("Declive_MMSE_Anual", "median"),
            cambio_cdrsb=("Cambio_CDRSB_Anual", "median"),
        )
        .reindex(STAGE_ORDER)
        .round(2)
    )


def get_exercise2_sections():
    return EJ2_PRESENTATION_SECTIONS.copy()


def load_and_clean_data(path="base_datos_alzheimer.csv"):
    csv_path = _normalize_path(path)
    df = pd.read_csv(csv_path, sep=";")
    df["Tratamiento_Desc"] = df["Tratamiento_Cod"].map(TRATAMIENTO_MAP)
    df["Estadio_Desc"] = df["Estadio_Cod"].map(ESTADIO_MAP)
    df["Estadio_Desc"] = pd.Categorical(df["Estadio_Desc"], categories=STAGE_ORDER, ordered=True)
    df["Sexo_Desc"] = df["Sexo"].map(SEXO_MAP)
    df["APOE4_Desc"] = df["APOE4_Cod"].map(APOE4_MAP)

    df["Amyloid_Pos"] = (df["PET_Amiloide_Centiloid"] >= 25).astype(int)
    df["Tau_Pos"] = (
        (df["LCR_pTau181"] >= 60)
        | (df["Plasma_pTau217"] >= 0.28)
    ).astype(int)
    df["Neurodeg_Pos"] = (
        (df["RM_Hipocampo_Pctl"] <= 15)
        | (df["FDG_PET_TP_SUVR"] <= 1.05)
        | (df["LCR_tTau"] >= 350)
    ).astype(int)
    df["ATN_Perfil"] = (
        "A"
        + df["Amyloid_Pos"].astype(str)
        + "T"
        + df["Tau_Pos"].astype(str)
        + "N"
        + df["Neurodeg_Pos"].astype(str)
    )

    df["Declive_MMSE_Anual"] = (
        (df["MMSE_Basal"] - df["MMSE_Actual"]) / df["Tiempo_Evol"]
    ).round(2)
    df["Cambio_CDRSB_Anual"] = (
        (df["CDR_SB_Actual"] - df["CDR_SB_Basal"]) / df["Tiempo_Evol"]
    ).round(2)
    df["Estado_Progresion"] = compute_progression_state(df)
    df["Candidato_Antiamiloide"] = (
        (df["Amyloid_Pos"] == 1)
        & (df["Estadio_Cod"].isin([1, 2]))
        & (df["APOE4_Cod"] < 2)
        & (df["RM_Microhemorragias"] < 5)
        & (df["Anticoagulacion"] == 0)
    ).astype(int)

    return df


def get_patient_data(df, patient_id_num):
    return df[df["ID"] == patient_id_num].iloc[0]
