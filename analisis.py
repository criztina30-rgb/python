"""
Examen Final - Análisis del Costo de Vida por País (2017)
------------------------------------------------------------
Este script realiza:
1. Revisión inicial del dataset (filas, columnas, estadísticas clave).
2. Visualizaciones:
   - Top 10 países con el costo de vida más alto.
   - Top 10 países con el costo de vida más bajo.
   - Costo de vida de los países de América.

Dataset: dataset_costo_vida.csv
Columnas: Countries, Cost of living 2017, Global rank, Available data, Continent
"""

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Carga del dataset
# ------------------------------------------------------------------
df = pd.read_csv("dataset_costo_vida.csv", index_col=0)

COL_COSTO = "Cost of living, 2017"
COL_RANK = "Global rank"

# ------------------------------------------------------------------
# 2. Revisión inicial del dataset
# ------------------------------------------------------------------
n_filas, n_columnas = df.shape
costo_promedio = df[COL_COSTO].mean()

fila_max = df.loc[df[COL_COSTO].idxmax()]
fila_min = df.loc[df[COL_COSTO].idxmin()]

peru = df[df["Countries"].str.contains("Peru", case=False, na=False)].iloc[0]

print("=" * 60)
print("1. REVISIÓN INICIAL DEL DATASET")
print("=" * 60)
print(f"Nro. de Filas: {n_filas}")
print(f"Nro. de Columnas: {n_columnas}")
print(f"Costo de vida promedio: {costo_promedio:.2f}")
print(f"País con costo de vida más alto: {fila_max['Countries']} ({fila_max[COL_COSTO]})")
print(f"País con costo de vida más bajo: {fila_min['Countries']} ({fila_min[COL_COSTO]})")
print(f"Costo de Vida en Perú: {peru[COL_COSTO]}")
print(f"Ranking de Perú: {peru[COL_RANK]}")
print()

# ------------------------------------------------------------------
# 3. Visualizaciones
# ------------------------------------------------------------------

# --- 3.1 Top 10 países con el costo de vida más alto ---
top10_alto = df.sort_values(COL_COSTO, ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10_alto["Countries"][::-1], top10_alto[COL_COSTO][::-1], color="firebrick")
plt.xlabel("Índice de Costo de Vida")
plt.title("Top 10 países con el costo de vida más alto (2017)")
plt.tight_layout()
plt.savefig("top10_costo_mas_alto.png", dpi=150)
plt.close()

# --- 3.2 Top 10 países con el costo de vida más bajo ---
top10_bajo = df.sort_values(COL_COSTO, ascending=True).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10_bajo["Countries"][::-1], top10_bajo[COL_COSTO][::-1], color="steelblue")
plt.xlabel("Índice de Costo de Vida")
plt.title("Top 10 países con el costo de vida más bajo (2017)")
plt.tight_layout()
plt.savefig("top10_costo_mas_bajo.png", dpi=150)
plt.close()

# --- 3.3 Costo de vida de los países de América ---
america = df[df["Continent"] == "America"].sort_values(COL_COSTO, ascending=False)

plt.figure(figsize=(10, 10))
plt.barh(america["Countries"][::-1], america[COL_COSTO][::-1], color="darkgreen")
plt.xlabel("Índice de Costo de Vida")
plt.title("Costo de vida de los países de América (2017)")
plt.tight_layout()
plt.savefig("costo_vida_america.png", dpi=150)
plt.close()

print("Gráficos generados:")
print(" - top10_costo_mas_alto.png")
print(" - top10_costo_mas_bajo.png")
print(" - costo_vida_america.png")
