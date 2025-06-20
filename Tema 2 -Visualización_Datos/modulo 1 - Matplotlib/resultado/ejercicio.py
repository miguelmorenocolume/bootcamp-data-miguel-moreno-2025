import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

#1. Carga y limpieza de datos

df = pl.read_csv("datos/Netflix_Dataset.csv")

cols_relevantes = [
    "Title", "Genre", "IMDb Score", "Rotten Tomatoes Score", "Metacritic Score",
    "Runtime", "Release Date", "Netflix Release Date", "Series or Movie"
]
df = df.select(cols_relevantes)

# Rellenar valores nulos en columnas numéricas con la media
df = df.with_columns([
    pl.col("IMDb Score").fill_null(pl.col("IMDb Score").mean()),
    pl.col("Rotten Tomatoes Score").fill_null(pl.col("Rotten Tomatoes Score").mean()),
    pl.col("Metacritic Score").fill_null(pl.col("Metacritic Score").mean()),
])

# Rellenar valores nulos en 'Genre' con "Unknown"
df = df.with_columns(
    pl.col("Genre").fill_null("Unknown")
)

# Convertir columnas de fecha a tipo fecha
df = df.with_columns([
    pl.col("Release Date").str.strptime(pl.Date, "%Y-%m-%d", strict=False),
    pl.col("Netflix Release Date").str.strptime(pl.Date, "%Y-%m-%d", strict=False),
])

# Función para convertir runtime a minutos
def runtime_to_minutes(runtime: str):
    if runtime is None or runtime == "" or runtime.lower() == "nan":
        return 0
    runtime = runtime.strip()
    try:
        if "<" in runtime:
            return int(''.join(filter(str.isdigit, runtime)))
        
        if "minutes" in runtime.lower():
            return int(''.join(filter(str.isdigit, runtime)))
        
        if "minute" in runtime.lower():
            return int(''.join(filter(str.isdigit, runtime)))
        
        if "hr" in runtime or "hour" in runtime or "h" in runtime:
            parts = runtime.lower().replace("hours", "h").replace("hour", "h").replace("hr", "h").split()
            total_min = 0
            for part in parts:
                if "h" in part:
                    h = int(''.join(filter(str.isdigit, part)))
                    total_min += h * 60
                elif "m" in part or "min" in part:
                    m = int(''.join(filter(str.isdigit, part)))
                    total_min += m
            if total_min == 0:
                nums = [int(s) for s in runtime.split() if s.isdigit()]
                if nums:
                    total_min = nums[0]*60
            return total_min

        if runtime.isdigit():
            return int(runtime)
    except Exception:
        return 0
    return 0

# Aplicar la función runtime_to_minutes a la columna Runtime
df = df.with_columns([
    pl.when(pl.col("Runtime").str.contains("hour"))
      .then(
          pl.col("Runtime").str.extract(r"(\d+)").cast(pl.Int32) * 60
      )
      .when(pl.col("Runtime").str.contains("minute"))
      .then(
          pl.col("Runtime").str.extract(r"(\d+)").cast(pl.Int32)
      )
      .otherwise(0)
      .alias("Runtime_min")
])


#2. Análisis y Visualización

# Parte 1: Promedio de puntuaciones por género

# Explode de géneros en filas separadas
df_expanded = df.with_columns(
    pl.col("Genre").str.split(",").alias("GenreList")
).explode("GenreList").with_columns(
    pl.col("GenreList").str.strip_chars().alias("Genre_clean")
)

# Calcular promedio de puntuaciones por género
promedio_por_genero = df_expanded.group_by("Genre_clean").agg([
    pl.col("IMDb Score").mean().alias("IMDb Score Promedio"),
    pl.col("Rotten Tomatoes Score").mean().alias("RT Score Promedio"),
    pl.len().alias("Conteo") 
]).sort("Conteo", descending=True)


# Seleccionar los 10 géneros más populares (por conteo)
top10_generos = promedio_por_genero.head(10)

# Parte 2: Relación entre IMDb Score y Rotten Tomatoes Score
imdb_scores = df["IMDb Score"].to_numpy()
rt_scores = df["Rotten Tomatoes Score"].to_numpy()

# Calcular línea de tendencia (regresión lineal)
coef = np.polyfit(imdb_scores, rt_scores, 1)  # grado 1
poly1d_fn = np.poly1d(coef)

# Parte 3: Distribución de puntuaciones IMDb
imdb_scores_np = imdb_scores  # ya numpy

# Parte 4: Análisis temporal - número de títulos por año y tipo (Serie o Película)
df = df.with_columns(
    pl.col("Release Date").dt.year().alias("Year")
)

conteo_por_anio_tipo = df.group_by(["Year", "Series or Movie"]).agg(
    pl.len().alias("Conteo")
).sort("Year")

#3. Visualización y guardado

with PdfPages("resultados_netflix.pdf") as pdf:

    # Gráfico 1: Promedio puntuaciones por género (barras)
    fig, ax = plt.subplots(figsize=(10,6))
    x = top10_generos["Genre_clean"].to_list()
    y_imdb = top10_generos["IMDb Score Promedio"].to_list()
    y_rt = top10_generos["RT Score Promedio"].to_list()

    width = 0.35
    ax.bar(np.arange(len(x)) - width/2, y_imdb, width, label="IMDb Score")
    ax.bar(np.arange(len(x)) + width/2, y_rt, width, label="Rotten Tomatoes Score")

    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x, rotation=45, ha="right")
    ax.set_ylabel("Puntuación Promedio")
    ax.set_title("Promedio de Puntuaciones por Género (Top 10)")
    ax.legend()
    plt.tight_layout()
    plt.savefig("promedio_puntuaciones_por_genero.png")
    pdf.savefig(fig)
    plt.close()

    # Gráfico 2: Relación IMDb vs Rotten Tomatoes
    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(imdb_scores, rt_scores, alpha=0.6, label="Títulos")
    ax.plot(imdb_scores, poly1d_fn(imdb_scores), color='red', label="Tendencia lineal")
    ax.set_xlabel("IMDb Score")
    ax.set_ylabel("Rotten Tomatoes Score")
    ax.set_title("Relación entre IMDb Score y Rotten Tomatoes Score")
    ax.legend()
    plt.tight_layout()
    plt.savefig("relacion_puntuaciones.png")
    pdf.savefig(fig)
    plt.close()

    # Gráfico 3: Histograma distribución puntuaciones IMDb
    fig, ax = plt.subplots(figsize=(8,6))
    ax.hist(imdb_scores_np, bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel("IMDb Score")
    ax.set_ylabel("Cantidad de Títulos")
    ax.set_title("Distribución de Puntuaciones IMDb")
    plt.tight_layout()
    plt.savefig("distribucion_imdb.png")
    pdf.savefig(fig)
    plt.close()

    # Gráfico 4: Evolución número de títulos por año y tipo
    fig, ax = plt.subplots(figsize=(10,6))

    for tipo in ["Series", "Movie"]:
        df_tipo = conteo_por_anio_tipo.filter(pl.col("Series or Movie") == tipo)
        ax.plot(df_tipo["Year"], df_tipo["Conteo"], label=tipo)

    ax.set_xlabel("Año de Lanzamiento")
    ax.set_ylabel("Cantidad de Títulos")
    ax.set_title("Número de Películas y Series Lanzadas por Año")
    ax.legend()
    plt.tight_layout()
    plt.savefig("evolucion_titulos_por_anio.png")
    pdf.savefig(fig)
    plt.close()


#4. Exportación datos procesados (20 registros aleatorios)

df_sample = df.sample(20)
df_sample.write_csv("netflix_dataset_sample.csv")

print("Proceso terminado. Gráficos guardados, PDF generado y CSV exportado.")
