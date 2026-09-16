# Examen Final - Costo de Vida por País
# Se usa pandas para el analisis y matplotlib para los graficos

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("dataset_costo_vida.csv", index_col=0)

# Ver las primeras filas para entender los datos
print(df.head())
print()

# 1. Revision inicial del dataset
print("=" * 50)
print("REVISION INICIAL DEL DATASET")
print("=" * 50)

# Numero de filas y columnas
print(f"Nro. de Filas: {df.shape[0]}")
print(f"Nro. de Columnas: {df.shape[1]}")

# Costo de vida promedio
promedio = df["Cost of living, 2017"].mean()
print(f"Costo de vida promedio: {round(promedio, 2)}")

# Pais con costo mas alto
idx_max = df["Cost of living, 2017"].idxmax()
pais_max = df.loc[idx_max]
print(f"Pais con costo de vida mas alto: {pais_max['Countries']} ({pais_max['Cost of living, 2017']})")

# Pais con costo mas bajo
idx_min = df["Cost of living, 2017"].idxmin()
pais_min = df.loc[idx_min]
print(f"Pais con costo de vida mas bajo: {pais_min['Countries']} ({pais_min['Cost of living, 2017']})")

# Datos de Peru
peru = df[df["Countries"] == "Peru"]
print(f"Costo de Vida en Peru: {peru['Cost of living, 2017'].values[0]}")
print(f"Ranking de Peru: {peru['Global rank'].values[0]}")

print()

# 2. Visualizaciones

# Grafico 1: Top 10 paises con costo de vida mas alto
top10_alto = df.sort_values("Cost of living, 2017", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10_alto["Countries"][::-1], top10_alto["Cost of living, 2017"][::-1], color="firebrick")
plt.xlabel("Indice de Costo de Vida")
plt.title("Top 10 paises con el costo de vida mas alto (2017)")
plt.tight_layout()
plt.savefig("top10_costo_mas_alto.png")
plt.show()

# Grafico 2: Top 10 paises con costo de vida mas bajo
top10_bajo = df.sort_values("Cost of living, 2017").head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10_bajo["Countries"][::-1], top10_bajo["Cost of living, 2017"][::-1], color="steelblue")
plt.xlabel("Indice de Costo de Vida")
plt.title("Top 10 paises con el costo de vida mas bajo (2017)")
plt.tight_layout()
plt.savefig("top10_costo_mas_bajo.png")
plt.show()

# Grafico 3: Paises de America
america = df[df["Continent"] == "America"].sort_values("Cost of living, 2017", ascending=False)

plt.figure(figsize=(10, 10))
plt.barh(america["Countries"][::-1], america["Cost of living, 2017"][::-1], color="darkgreen")
plt.xlabel("Indice de Costo de Vida")
plt.title("Costo de vida en paises de America (2017)")
plt.tight_layout()
plt.savefig("costo_vida_america.png")
plt.show()

print("Listo, los graficos se guardaron como PNG")
