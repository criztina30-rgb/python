# Examen Final — Análisis del Costo de Vida por País (2017)

## Descripción
Este proyecto analiza un dataset con el índice de costo de vida de 167 países en el año 2017. El objetivo es realizar una revisión inicial del dataset y generar visualizaciones que permitan comparar el costo de vida entre países.

## Dataset
Archivo: `dataset_costo_vida.csv`

Columnas:
- **Countries**: nombre del país.
- **Cost of living, 2017**: índice de costo de vida.
- **Global rank**: ranking global de costo de vida (2017).
- **Available data**: rango de años con datos disponibles.
- **Continent**: continente al que pertenece el país.

## 1. Revisión inicial del dataset

| Indicador | Valor |
|---|---|
| Nro. de Filas | 167 |
| Nro. de Columnas | 5 |
| Costo de vida promedio | 82.92 |
| País con costo de vida más alto | Bermuda (225.86) |
| País con costo de vida más bajo | Egipto (27.37) |
| Costo de Vida en Perú | 83.26 |
| Ranking de Perú | 60 |

## 2. Visualizaciones

- `top10_costo_mas_alto.png`: Top 10 países con el costo de vida más alto.
- `top10_costo_mas_bajo.png`: Top 10 países con el costo de vida más bajo.
- `costo_vida_america.png`: Costo de vida de todos los países de América.

## Cómo ejecutar

```bash
pip install pandas matplotlib
python analisis.py
```

Esto imprime en consola la revisión inicial del dataset y genera los tres gráficos en formato PNG.

## Estructura del repositorio

```
├── analisis.py                  # Script principal de análisis
├── dataset_costo_vida.csv       # Dataset utilizado
├── top10_costo_mas_alto.png     # Gráfico: top 10 más caros
├── top10_costo_mas_bajo.png     # Gráfico: top 10 más baratos
├── costo_vida_america.png       # Gráfico: países de América
└── README.md
```

## Autor
Examen Final — Análisis de Datos
