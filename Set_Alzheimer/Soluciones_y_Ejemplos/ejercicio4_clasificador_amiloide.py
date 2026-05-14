import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)
from alzheimer_utils import load_and_clean_data

df = load_and_clean_data(os.path.join(ROOT, "base_datos_alzheimer.csv"))
X = df[
    [
        "Plasma_pTau217",
        "Plasma_GFAP",
        "Plasma_NfL",
        "RM_Hipocampo_Pctl",
        "RM_Espesor_Temporal",
        "FDG_PET_TP_SUVR",
        "Edad",
        "APOE4_Cod",
    ]
]
y = df["Amyloid_Pos"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = RandomForestClassifier(n_estimators=250, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

print("CLASIFICADOR DE POSITIVIDAD AMILOIDE")
print("-" * 50)
print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
print(f"ROC AUC:  {roc_auc_score(y_test, proba):.3f}")
print("\nImportancia de variables:")
print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False))
