# Examen Final - Costo de Vida por País (2017)

## Descripción
Analisis del costo de vida en 167 paises usando un dataset del 2017. Se hace una revision del dataset y se crean graficos para comparar los paises.

## Dataset
El archivo `dataset_costo_vida.csv` tiene las siguientes columnas:
- Countries: nombre del pais
- Cost of living, 2017: indice de costo de vida
- Global rank: ranking global
- Available data: años con datos disponibles
- Continent: continente

## Resultados

| Dato | Resultado |
|---|---|
| Nro. de Filas | 167 |
| Nro. de Columnas | 5 |
| Costo de vida promedio | 82.92 |
| Pais mas caro | Bermuda (225.86) |
| Pais mas barato | Egypt (27.37) |
| Costo de vida en Peru | 83.26 |
| Ranking de Peru | 60 |

## Graficos generados
- Top 10 paises mas caros
- Top 10 paises mas baratos
- Paises de America

## Como ejecutar
```
pip install pandas matplotlib
python analisis.py
```
