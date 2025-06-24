# Ejercicio: Análisis y Manipulación de Datos de Netflix

## Objetivo
El objetivo de este ejercicio es realizar un análisis exhaustivo del dataset de Netflix utilizando Polars y NumPy. Implementarás operaciones avanzadas de manipulación de datos, cálculos estadísticos y visualización de resultados.

## Instrucciones
### Carga y Exploración de Datos

- Carga el archivo Netflix_Dataset.csv utilizando Polars.
- Verifica si hay valores nulos en el dataset y calcula el porcentaje de valores faltantes por columna.
- Identifica las columnas con valores categóricos y las columnas con valores numéricos.

### Limpieza de Datos

- Rellena los valores nulos en las columnas numéricas con la media de cada columna.
- Para las columnas categóricas, rellena los valores nulos con la moda (valor más frecuente).
- Convierte las columnas de fechas (Release Date y Netflix Release Date) al formato de fecha de Polars.

### Análisis Exploratorio

#### Calcula las siguientes estadísticas:
- Película con la mayor puntuación de IMDb.
- Película con la mayor puntuación de Rotten Tomatoes.
- País con mayor disponibilidad de contenido.
- Agrupa los datos por género (Genre) y calcula el promedio de las puntuaciones (IMDb Score, Rotten Tomatoes Score, Metacritic Score) para cada género.
- Encuentra el número de películas y series disponibles en el dataset.

### Análisis Numérico con NumPy

#### Usa NumPy para calcular:
- La correlación entre las puntuaciones (IMDb Score, Rotten Tomatoes Score, Metacritic Score).
- La desviación estándar de las puntuaciones.
- Genera un histograma de las puntuaciones de IMDb utilizando NumPy.

### Exportación de Resultados

- Guarda un nuevo archivo CSV con las columnas originales más una nueva columna llamada Overall Score, que será el promedio ponderado de las puntuaciones (IMDb Score, Rotten Tomatoes Score, Metacritic Score).
- Exporta un resumen en formato JSON con las estadísticas clave calculadas.

## Pistas y Requisitos Técnicos
- Usa Polars para todas las operaciones de manipulación de datos.
- Usa NumPy para cálculos numéricos avanzados.
- Asegúrate de manejar excepciones para evitar errores en caso de datos faltantes o formatos inesperados.
- Usa funciones para estructurar tu código y hacerlo modular.
- Documenta cada paso del proceso con comentarios claros.

