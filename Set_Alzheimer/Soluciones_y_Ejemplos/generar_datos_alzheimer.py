from pathlib import Path

import numpy as np
import pandas as pd


RNG = np.random.default_rng(42)


def _clip(value, low, high):
    return float(np.clip(value, low, high))


def _bounded_normal(mean, sd, low, high, integer=False):
    value = _clip(RNG.normal(mean, sd), low, high)
    return int(round(value)) if integer else round(value, 1)


def _choose_profile():
    return RNG.choice(
        [
            "scd_nonad",
            "preclinical_ad",
            "mci_nonad",
            "mci_ad",
            "mild_ad",
            "moderate_ad",
        ],
        p=[0.16, 0.08, 0.10, 0.26, 0.25, 0.15],
    )


def _profile_spec(profile):
    specs = {
        "scd_nonad": {
            "stage": 0,
            "amyloid": 0,
            "age_mean": 69,
            "time_mean": 1.8,
            "mmse_now": 28.8,
            "mmse_decline": 0.25,
            "cdr_now": 0.3,
            "faq": 1.5,
            "memory": 7.6,
            "fluency": 23.5,
            "executive": 15.5,
            "complaints": 7.5,
            "anosognosia": 0.02,
            "abeta42": 980,
            "ptau181": 42,
            "ttau": 230,
            "ptau217": 0.11,
            "nfl": 10.5,
            "gfap": 105,
            "hippo": 55,
            "temporal": 2.58,
            "mta": 1.0,
            "micro": 0.4,
            "fdg": 1.22,
            "centiloid": 4,
        },
        "preclinical_ad": {
            "stage": 0,
            "amyloid": 1,
            "age_mean": 71,
            "time_mean": 2.1,
            "mmse_now": 28.2,
            "mmse_decline": 0.45,
            "cdr_now": 0.5,
            "faq": 2.0,
            "memory": 6.8,
            "fluency": 22.0,
            "executive": 15.0,
            "complaints": 7.0,
            "anosognosia": 0.05,
            "abeta42": 690,
            "ptau181": 64,
            "ttau": 280,
            "ptau217": 0.20,
            "nfl": 12.0,
            "gfap": 145,
            "hippo": 42,
            "temporal": 2.48,
            "mta": 1.2,
            "micro": 0.8,
            "fdg": 1.18,
            "centiloid": 38,
        },
        "mci_nonad": {
            "stage": 1,
            "amyloid": 0,
            "age_mean": 70,
            "time_mean": 2.5,
            "mmse_now": 26.0,
            "mmse_decline": 0.85,
            "cdr_now": 1.2,
            "faq": 4.5,
            "memory": 5.8,
            "fluency": 20.0,
            "executive": 13.0,
            "complaints": 8.0,
            "anosognosia": 0.08,
            "abeta42": 930,
            "ptau181": 46,
            "ttau": 255,
            "ptau217": 0.12,
            "nfl": 11.8,
            "gfap": 118,
            "hippo": 40,
            "temporal": 2.44,
            "mta": 1.3,
            "micro": 0.6,
            "fdg": 1.17,
            "centiloid": 8,
        },
        "mci_ad": {
            "stage": 1,
            "amyloid": 1,
            "age_mean": 72,
            "time_mean": 2.8,
            "mmse_now": 25.0,
            "mmse_decline": 1.55,
            "cdr_now": 1.6,
            "faq": 6.5,
            "memory": 3.4,
            "fluency": 17.0,
            "executive": 11.0,
            "complaints": 6.2,
            "anosognosia": 0.16,
            "abeta42": 560,
            "ptau181": 82,
            "ttau": 340,
            "ptau217": 0.28,
            "nfl": 14.5,
            "gfap": 185,
            "hippo": 28,
            "temporal": 2.33,
            "mta": 2.0,
            "micro": 1.0,
            "fdg": 1.10,
            "centiloid": 67,
        },
        "mild_ad": {
            "stage": 2,
            "amyloid": 1,
            "age_mean": 74,
            "time_mean": 4.0,
            "mmse_now": 21.0,
            "mmse_decline": 2.35,
            "cdr_now": 3.0,
            "faq": 11.5,
            "memory": 2.0,
            "fluency": 13.0,
            "executive": 8.0,
            "complaints": 4.8,
            "anosognosia": 0.34,
            "abeta42": 470,
            "ptau181": 103,
            "ttau": 420,
            "ptau217": 0.35,
            "nfl": 18.0,
            "gfap": 228,
            "hippo": 16,
            "temporal": 2.18,
            "mta": 2.8,
            "micro": 1.2,
            "fdg": 1.00,
            "centiloid": 88,
        },
        "moderate_ad": {
            "stage": 3,
            "amyloid": 1,
            "age_mean": 76,
            "time_mean": 5.5,
            "mmse_now": 13.5,
            "mmse_decline": 3.10,
            "cdr_now": 5.0,
            "faq": 18.0,
            "memory": 0.8,
            "fluency": 9.0,
            "executive": 5.0,
            "complaints": 3.0,
            "anosognosia": 0.55,
            "abeta42": 410,
            "ptau181": 118,
            "ttau": 495,
            "ptau217": 0.41,
            "nfl": 22.0,
            "gfap": 268,
            "hippo": 7,
            "temporal": 2.01,
            "mta": 3.6,
            "micro": 1.5,
            "fdg": 0.91,
            "centiloid": 102,
        },
    }
    return specs[profile]


def _sample_apoe4(profile):
    if profile in {"preclinical_ad", "mci_ad", "mild_ad", "moderate_ad"}:
        return int(RNG.choice([0, 1, 2], p=[0.28, 0.50, 0.22]))
    return int(RNG.choice([0, 1, 2], p=[0.58, 0.32, 0.10]))


def _sample_treatment(stage, amyloid_positive, apoe4, micro, anticoag, mmse_now):
    eligible_antiamyloid = (
        amyloid_positive == 1
        and stage in [1, 2]
        and apoe4 < 2
        and micro < 5
        and anticoag == 0
        and mmse_now >= 18
    )

    if eligible_antiamyloid and RNG.random() < 0.28:
        return int(RNG.choice([6, 7], p=[0.58, 0.42]))
    if stage == 0:
        return int(RNG.choice([0, 1], p=[0.88, 0.12]))
    if stage == 1:
        return int(RNG.choice([0, 1, 2, 3], p=[0.48, 0.28, 0.14, 0.10]))
    if stage == 2:
        return int(RNG.choice([1, 2, 3, 5], p=[0.36, 0.18, 0.14, 0.32]))
    return int(RNG.choice([4, 5], p=[0.42, 0.58]))


def generar_base_datos_alzheimer(n_pacientes=220):
    data = []

    for i in range(1, n_pacientes + 1):
        profile = _choose_profile()
        spec = _profile_spec(profile)

        edad = _bounded_normal(spec["age_mean"], 5.0, 55, 88, integer=True)
        sexo = int(RNG.choice([0, 1], p=[0.57, 0.43]))
        escolaridad = _bounded_normal(12.5 if edad < 75 else 11.0, 3.0, 4, 20, integer=True)
        apoe4 = _sample_apoe4(profile)
        tiempo_evol = round(_clip(RNG.normal(spec["time_mean"], 1.0), 0.5, 10.0), 1)
        estadio = spec["stage"]
        amyloid_positive = spec["amyloid"]

        mmse_actual = round(_clip(RNG.normal(spec["mmse_now"], 1.8), 8, 30), 1)
        declive_mmse = round(_clip(RNG.normal(spec["mmse_decline"], 0.55), 0.0, 5.5), 2)
        mmse_basal = round(_clip(mmse_actual + declive_mmse * tiempo_evol + RNG.normal(0, 0.8), mmse_actual, 30), 1)
        moca_actual = round(_clip(RNG.normal(mmse_actual - 2.2, 1.6), 4, 30), 1)

        cdr_actual = round(_clip(RNG.normal(spec["cdr_now"], 0.55), 0.0, 12.0), 1)
        cdr_increment = round(_clip(RNG.normal(0.18 + 0.18 * estadio, 0.08), 0.05, 1.8), 2)
        cdr_basal = round(_clip(cdr_actual - cdr_increment * tiempo_evol + RNG.normal(0, 0.15), 0, cdr_actual), 1)
        faq_high = 5 if estadio == 0 else 30
        faq = int(_clip(RNG.normal(spec["faq"], 2.4), 0, faq_high))

        memoria_diferida = int(_clip(RNG.normal(spec["memory"], 1.2), 0, 10))
        fluencia_sem = int(_clip(RNG.normal(spec["fluency"], 2.8), 4, 35))
        funciones_ejecutivas = int(_clip(RNG.normal(spec["executive"], 1.8), 2, 18))

        quejas_memoria = int(
            _clip(
                RNG.normal(spec["complaints"], 1.4)
                + (0.8 if estadio <= 1 and amyloid_positive == 0 else 0),
                0,
                10,
            )
        )
        anosognosia = int(RNG.random() < spec["anosognosia"])
        if estadio >= 2 and anosognosia == 1:
            quejas_memoria = int(_clip(quejas_memoria - RNG.integers(1, 4), 0, 10))

        gds15 = int(_clip(RNG.normal(4.0 if profile != "scd_nonad" else 5.0, 2.2), 0, 15))
        npi_apatia = int(_clip(RNG.normal(1.4 + 2.0 * estadio, 1.8), 0, 12))

        abeta_upper = 780 if amyloid_positive == 1 else 1300
        lcr_abeta42 = round(_clip(RNG.normal(spec["abeta42"], 70), 280, abeta_upper), 1)
        lcr_ptau181 = round(_clip(RNG.normal(spec["ptau181"], 11), 18, 160), 1)
        lcr_ttau = round(_clip(RNG.normal(spec["ttau"], 45), 120, 850), 1)

        plasma_ptau217 = round(_clip(RNG.normal(spec["ptau217"], 0.06), 0.03, 0.70), 3)
        plasma_nfl = round(_clip(RNG.normal(spec["nfl"], 2.0), 6, 45), 1)
        plasma_gfap = round(_clip(RNG.normal(spec["gfap"], 34), 45, 420), 1)

        rm_hipocampo_pctl = int(_clip(RNG.normal(spec["hippo"], 10), 1, 95))
        rm_espesor_temporal = round(_clip(RNG.normal(spec["temporal"], 0.11), 1.7, 3.1), 2)
        rm_mta = int(_clip(RNG.normal(spec["mta"], 0.6), 0, 4))

        micro_lambda = spec["micro"] + 0.45 * (apoe4 == 1) + 0.95 * (apoe4 == 2)
        rm_microhemorragias = int(_clip(RNG.poisson(micro_lambda), 0, 9))
        fdg_pet = round(_clip(RNG.normal(spec["fdg"], 0.08), 0.72, 1.45), 2)
        amyloid_centiloid = round(_clip(RNG.normal(spec["centiloid"] + 6 * apoe4, 12), -15, 135), 1)
        if amyloid_centiloid >= 25:
            lcr_abeta42 = round(min(lcr_abeta42, _clip(RNG.normal(585, 95), 280, 760)), 1)
        else:
            lcr_abeta42 = round(max(lcr_abeta42, _clip(RNG.normal(910, 85), 700, 1250)), 1)

        anticoagulacion = int(RNG.random() < np.clip(0.04 + 0.01 * (edad - 65), 0.03, 0.20))
        tratamiento = _sample_treatment(
            estadio,
            amyloid_positive,
            apoe4,
            rm_microhemorragias,
            anticoagulacion,
            mmse_actual,
        )

        if i == 24:
            edad = 68
            sexo = 1
            escolaridad = 16
            apoe4 = 1
            tiempo_evol = 2.4
            estadio = 1
            mmse_basal = 28.5
            mmse_actual = 25.2
            moca_actual = 21.0
            cdr_basal = 0.5
            cdr_actual = 1.5
            faq = 5
            memoria_diferida = 2
            fluencia_sem = 15
            funciones_ejecutivas = 10
            quejas_memoria = 3
            anosognosia = 1
            gds15 = 2
            npi_apatia = 3
            lcr_abeta42 = 470.0
            lcr_ptau181 = 86.0
            lcr_ttau = 370.0
            plasma_ptau217 = 0.31
            plasma_nfl = 14.0
            plasma_gfap = 176.0
            rm_hipocampo_pctl = 18
            rm_espesor_temporal = 2.29
            rm_mta = 2
            rm_microhemorragias = 1
            fdg_pet = 1.08
            amyloid_centiloid = 66.0
            anticoagulacion = 0
            tratamiento = 6

        data.append(
            {
                "ID": i,
                "Edad": edad,
                "Sexo": sexo,
                "Escolaridad": escolaridad,
                "APOE4_Cod": apoe4,
                "Tiempo_Evol": tiempo_evol,
                "Estadio_Cod": estadio,
                "MMSE_Basal": mmse_basal,
                "MMSE_Actual": mmse_actual,
                "MoCA_Actual": moca_actual,
                "CDR_SB_Basal": cdr_basal,
                "CDR_SB_Actual": cdr_actual,
                "FAQ_Actual": faq,
                "Memoria_Diferida": memoria_diferida,
                "Fluencia_Semantica": fluencia_sem,
                "Funciones_Ejecutivas": funciones_ejecutivas,
                "Quejas_Memoria": quejas_memoria,
                "Anosognosia_Cod": anosognosia,
                "GDS15": gds15,
                "NPI_Apatia": npi_apatia,
                "LCR_Abeta42": lcr_abeta42,
                "LCR_pTau181": lcr_ptau181,
                "LCR_tTau": lcr_ttau,
                "Plasma_pTau217": plasma_ptau217,
                "Plasma_NfL": plasma_nfl,
                "Plasma_GFAP": plasma_gfap,
                "RM_Hipocampo_Pctl": rm_hipocampo_pctl,
                "RM_Espesor_Temporal": rm_espesor_temporal,
                "RM_MTA_Score": rm_mta,
                "RM_Microhemorragias": rm_microhemorragias,
                "FDG_PET_TP_SUVR": fdg_pet,
                "PET_Amiloide_Centiloid": amyloid_centiloid,
                "Anticoagulacion": anticoagulacion,
                "Tratamiento_Cod": tratamiento,
            }
        )

    return pd.DataFrame(data)


def generar_archivos():
    root = Path(__file__).resolve().parents[1]
    df = generar_base_datos_alzheimer()
    csv_path = root / "base_datos_alzheimer.csv"
    xlsx_path = root / "Base_Datos_Alzheimer_Final.xlsx"

    df.to_csv(csv_path, index=False, sep=";")

    dictionary_rows = [
        ("ID", "Identificador del paciente"),
        ("Edad", "Edad actual, años"),
        ("Sexo", "0 mujer, 1 hombre"),
        ("Escolaridad", "Años de educación formal"),
        ("APOE4_Cod", "0 no portador, 1 heterocigoto, 2 homocigoto"),
        ("Tiempo_Evol", "Años desde inicio de síntomas"),
        ("Estadio_Cod", "0 queja subjetiva/no demencia, 1 DCL amnésico, 2 demencia leve, 3 demencia moderada"),
        ("MMSE_Basal", "MMSE estimado al inicio del seguimiento"),
        ("MMSE_Actual", "MMSE actual"),
        ("MoCA_Actual", "MoCA actual"),
        ("CDR_SB_Basal", "CDR Sum of Boxes basal"),
        ("CDR_SB_Actual", "CDR Sum of Boxes actual"),
        ("FAQ_Actual", "Functional Activities Questionnaire"),
        ("Memoria_Diferida", "Recuerdo diferido tipo lista, 0-10"),
        ("Fluencia_Semantica", "Animales por minuto"),
        ("Funciones_Ejecutivas", "Puntuación ejecutiva resumida, 0-18"),
        ("Quejas_Memoria", "Queja subjetiva de memoria, 0-10"),
        ("Anosognosia_Cod", "0 no, 1 sí"),
        ("GDS15", "Escala geriátrica de depresión, 0-15"),
        ("NPI_Apatia", "Subescala de apatía, 0-12"),
        ("LCR_Abeta42", "Aβ42 en LCR, pg/mL"),
        ("LCR_pTau181", "pTau181 en LCR, pg/mL"),
        ("LCR_tTau", "Tau total en LCR, pg/mL"),
        ("Plasma_pTau217", "pTau217 plasmática, pg/mL"),
        ("Plasma_NfL", "Neurofilamento ligero plasmático, pg/mL"),
        ("Plasma_GFAP", "GFAP plasmática, pg/mL"),
        ("RM_Hipocampo_Pctl", "Percentil de volumen hipocampal ajustado por edad"),
        ("RM_Espesor_Temporal", "Espesor cortical temporal, mm"),
        ("RM_MTA_Score", "Medial Temporal Atrophy score, 0-4"),
        ("RM_Microhemorragias", "Número de microhemorragias lobares visibles"),
        ("FDG_PET_TP_SUVR", "SUVR temporoparietal de FDG-PET"),
        ("PET_Amiloide_Centiloid", "Carga amiloide global en escala centiloid"),
        ("Anticoagulacion", "0 no, 1 sí"),
        ("Tratamiento_Cod", "0 ninguno, 1 donepezilo, 2 rivastigmina, 3 galantamina, 4 memantina, 5 donepezilo+memantina, 6 lecanemab UE, 7 donanemab UE"),
    ]
    dict_df = pd.DataFrame(dictionary_rows, columns=["Variable", "Descripcion"])

    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Cohorte", index=False)
        dict_df.to_excel(writer, sheet_name="Diccionario", index=False)

    print(f"Cohorte generada: {csv_path}")
    print(f"Workbook generado: {xlsx_path}")


if __name__ == "__main__":
    generar_archivos()
