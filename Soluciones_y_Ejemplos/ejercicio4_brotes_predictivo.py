import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from neuro_utils import load_and_clean_data

df = load_and_clean_data()

# Objetivo: Predecir Num_Brotes basado en actividad basal y MRI
X = df[['Actividad_Basal', 'MRI_Lesiones', 'OCB', 'IgG_Index']]
y = df['Num_Brotes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)

print("MODELO PREDICTIVO: CARGA DE BROTES")
print("-" * 40)
print(f"Mean Absolute Error: {mae:.2f} brotes")

# Importancia de variables
importancias = pd.Series(model.feature_importances_, index=X.columns)
print("\nImportancia de las variables predictoras:")
print(importancias.sort_values(ascending=False))
