import polars as pl
import numpy as np
import json
from tabulate import tabulate

# Carga y Exploración de Datos
def cargar_datos(ruta_csv):
    try:
        df = pl.read_csv(ruta_csv)
        print("Datos cargados correctamente.")
        return df
    except Exception as e:
        print("Error al cargar los datos:", e)

def explorar_datos(df):
    print("\n=== EXPLORACIÓN DE DATOS ===")
    
    # Mostrar primeras 10 columnas y tipos
    primeras = list(zip(df.columns, df.dtypes))[:10]
    print("\nPrimeras 10 columnas y tipos de datos:")
    print(tabulate(primeras, headers=["Columna", "Tipo"], tablefmt="fancy_grid"))
    
    print(f"\n(Total de columnas: {len(df.columns)}. Mostrando las 10 primeras.)")
    
    # Porcentaje de valores nulos por columna
    nulos = df.null_count()
    total = df.height
    porcentaje_nulos = nulos.select([
        (pl.col(c) / total * 100).alias(c) for c in nulos.columns
    ])
    porcentaje_nulos_dict = porcentaje_nulos.to_dicts()[0]
    porcentaje_nulos_list = [(col, round(pct, 2)) for col, pct in porcentaje_nulos_dict.items()]
    
    print("\nPorcentaje de valores nulos por columna:")
    print(tabulate(porcentaje_nulos_list, headers=["Columna", "Porcentaje %"], tablefmt="fancy_grid"))
    
    # Separar columnas categóricas y numéricas
    categóricas = [col for col, tipo in zip(df.columns, df.dtypes) if tipo == pl.Utf8]
    numéricas = [col for col, tipo in zip(df.columns, df.dtypes) if tipo in [pl.Float64, pl.Int64]]
    
    print("\nColumnas categóricas:")
    print(tabulate([[c] for c in categóricas], headers=["Categorías"], tablefmt="fancy_grid"))
    
    print("\nColumnas numéricas:")
    print(tabulate([[n] for n in numéricas], headers=["Numéricas"], tablefmt="fancy_grid"))
    
    return categóricas, numéricas

# Limpieza de Datos
def limpiar_datos(df, categóricas, numéricas):
    for col in numéricas:
        if col in df.columns:
            media = df[col].mean()
            df = df.with_columns([
                pl.col(col).fill_null(media)
            ])
    
    for col in categóricas:
        if col in df.columns:
            try:
                moda = df[col].mode().to_series()[0]
                df = df.with_columns([
                    pl.col(col).fill_null(moda)
                ])
            except:
                pass
    
    for fecha_col in ['Release Date', 'Netflix Release Date']:
        if fecha_col in df.columns:
            df = df.with_columns([
                pl.col(fecha_col).str.strptime(pl.Date, format="%Y-%m-%d", strict=False).alias(fecha_col)
            ])
    
    return df

# Análisis Exploratorio
def analisis_exploratorio(df):
    print("\n=== ANÁLISIS EXPLORATORIO ===")

    # Película con mayor puntuación IMDb (solo la primera)
    max_imdb = df["IMDb Score"].max()
    peli_max_imdb = df.filter(pl.col("IMDb Score") == max_imdb)["Title"].to_list()
    print("\nPelícula con mayor puntuación IMDb:")
    print(tabulate([[peli_max_imdb[0]]], headers=["Título"], tablefmt="grid"))

    # Película con mayor puntuación en Rotten Tomatoes (solo la primera)
    max_rt = df["Rotten Tomatoes Score"].max()
    peli_max_rt = df.filter(pl.col("Rotten Tomatoes Score") == max_rt)["Title"].to_list()
    print("\nPelícula con mayor puntuación en Rotten Tomatoes:")
    print(tabulate([[peli_max_rt[0]]], headers=["Título"], tablefmt="grid"))
    
    pais_con_mas = (
        df.select(["Title", "Country Availability"])
          .group_by("Country Availability")
          .len()
          .sort("len", descending=True)
          .row(0)
    )
    pais, cantidad = pais_con_mas
    print(f"\nPaís con mayor disponibilidad de contenido: {pais} ({cantidad} títulos)")

    try:
        promedios_por_genero = (
            df.drop_nulls(["Genre", "IMDb Score", "Rotten Tomatoes Score", "Metacritic Score"])
            .group_by("Genre")
            .agg([
                pl.col("IMDb Score").mean().alias("Promedio IMDb"),
                pl.col("Rotten Tomatoes Score").mean().alias("Promedio RT"),
                pl.col("Metacritic Score").mean().alias("Promedio Metacritic")
            ])
            .sort("Promedio IMDb", descending=True)
        )
        print("\nPromedios de puntuaciones por género:")
        print(tabulate(promedios_por_genero.head(10).to_dict(as_series=False), headers="keys", tablefmt="fancy_grid"))
        print(f"(Mostrando las primeras 10 filas de un total de {promedios_por_genero.height})")
    except Exception as e:
        print("Error en análisis por género:", e)

    num_peliculas = df.filter(pl.col("Series or Movie") == "Movie").height
    num_series = df.filter(pl.col("Series or Movie") == "Series").height
    print(f"\nNúmero de películas: {num_peliculas}")
    print(f"Número de series: {num_series}")


# Análisis Numérico con NumPy
def analisis_numpy(df):
    print("\n=== ANÁLISIS NUMÉRICO (NumPy) ===")
    try:
        imdb = df["IMDb Score"].to_numpy()
        rt = df["Rotten Tomatoes Score"].to_numpy()
        meta = df["Metacritic Score"].to_numpy()

        matriz = np.stack([imdb, rt, meta])
        correlacion = np.corrcoef(matriz)
        print("\nMatriz de correlación:")
        print(tabulate(correlacion, headers=["IMDb", "RT", "Metacritic"], showindex=["IMDb", "RT", "Metacritic"], tablefmt="fancy_grid"))

        desviaciones = {
            "IMDb": np.std(imdb),
            "Rotten Tomatoes": np.std(rt),
            "Metacritic": np.std(meta)
        }
        print("\nDesviación estándar de las puntuaciones:")
        print(tabulate(desviaciones.items(), headers=["Puntuación", "Desviación estándar"], tablefmt="grid"))

        hist, bins = np.histogram(imdb, bins=10)
        print("\nHistograma de puntuaciones IMDb:")
        hist_data = [[f"{bins[i]:.1f} - {bins[i+1]:.1f}", hist[i]] for i in range(len(hist))]
        print(tabulate(hist_data, headers=["Rango", "Cantidad"], tablefmt="grid"))

    except Exception as e:
        print("Error en análisis con NumPy:", e)

# Exportación
def exportar_resultados(df, salida_csv, salida_json):
    df = df.with_columns([
        (
            (pl.col("IMDb Score") + pl.col("Rotten Tomatoes Score") + pl.col("Metacritic Score")) / 3
        ).alias("Overall Score")
    ])

    df.write_csv(salida_csv)
    print("\nArchivo CSV exportado como:", salida_csv)

    resumen = {
        "Máxima IMDb Score": df["IMDb Score"].max(),
        "Máxima Rotten Tomatoes Score": df["Rotten Tomatoes Score"].max(),
        "Máxima Metacritic Score": df["Metacritic Score"].max(),
        "Películas totales": df.filter(pl.col("Series or Movie") == "Movie").height,
        "Series totales": df.filter(pl.col("Series or Movie") == "Series").height
    }

    with open(salida_json, "w") as f:
        json.dump(resumen, f, indent=4)
    print("Resumen exportado como:", salida_json)

# Ejecución Principal
def main():
    archivo_csv = "Netflix_Dataset.csv"
    salida_csv = "Netflix_Dataset_Limpio.csv"
    salida_json = "Resumen_Netflix.json"
    
    df = cargar_datos(archivo_csv)
    categ, num = explorar_datos(df)
    df = limpiar_datos(df, categ, num)
    analisis_exploratorio(df)
    analisis_numpy(df)
    exportar_resultados(df, salida_csv, salida_json)

if __name__ == "__main__":
    main()
