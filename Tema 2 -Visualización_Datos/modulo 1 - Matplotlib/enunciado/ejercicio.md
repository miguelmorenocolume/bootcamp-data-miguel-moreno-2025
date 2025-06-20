# Ejercicio: Visualización de Resultados con Polars, NumPy y Matplotlib

## Objetivo
El objetivo de este ejercicio es analizar y visualizar datos del dataset de Netflix utilizando `polars` para la manipulación de datos, `numpy` para cálculos numéricos y `matplotlib` para la generación de gráficos.

<hr>

## Instrucciones

### Carga y Limpieza de Datos

1. **Carga de Datos**  
   - Carga el archivo `Netflix_Dataset.csv` utilizando `polars`. Puedes situarlo en la raiz del proyecto para facilitar su carga.
   - Filtra el dataframe para incluir solo las columnas relevantes: `Title`, `Genre`, `IMDb Score`, `Rotten Tomatoes Score`, `Metacritic Score`, `Runtime`, `Release Date`, `Netflix Release Date` y `Series or Movie`.

2. **Limpieza de Datos**  
   - Rellena los valores nulos en las columnas numéricas (`IMDb Score`, `Rotten Tomatoes Score`, `Metacritic Score`) con la media de cada columna.
   - Para las columnas categóricas como `Genre`, rellena los valores nulos con la categoria `Unknown`.
   - Convierte las columnas de fechas (`Release Date`, `Netflix Release Date`) al formato de fecha de `polars`.
   - Estandariza la columna (`Runtime`) para que todas las duraciones estén en minutos. Por ejemplo, si la duración está en horas y minutos, conviértela a minutos. Si la duración es solo en minutos, asegúrate de que esté en el formato correcto. Si existen valores nulos, rellénalos con un 0.

<hr>

### Análisis y Visualización

#### Parte 1: Promedio de Puntuaciones por Género
- **Análisis**: Calcula el promedio de puntuaciones (`IMDb Score`, `Rotten Tomatoes Score`) por género (`Genre`) y selecciona los 10 géneros más populares.
- **Visualización**: Genera un gráfico de barras que muestre el promedio de puntuaciones por género.

#### Parte 2: Relación entre Puntuaciones
- **Análisis**: Analiza la relación entre las puntuaciones de `IMDb Score` y `Rotten Tomatoes Score`.
- **Visualización**: Genera un gráfico de dispersión que muestre esta relación, asegurándote de incluir etiquetas y una línea de tendencia.

#### Parte 3: Distribución de Puntuaciones de IMDb
- **Análisis**: Calcula la distribución de las puntuaciones de `IMDb Score` utilizando `numpy`.
- **Visualización**: Genera un histograma que muestre la distribución de las puntuaciones.

#### Parte 4: Análisis Temporal
- **Análisis**: Agrupa los datos por año de lanzamiento (`Release Date`) y calcula el número de películas y series lanzadas por año.
- **Visualización**: Genera un gráfico de líneas que muestre la evolución del número de películas y series lanzadas por año, con líneas separadas para cada tipo (`Series or Movie`).

<hr>

### Exportación de Resultados

1. **Exportación de Gráficos**  
    - Guarda cada gráfico generado en formato PNG con nombres descriptivos (por ejemplo, `promedio_puntuaciones_por_genero.png`, `relacion_puntuaciones.png`, etc.).
    - Junta todos los gráficos en un PDF para una presentación clara y limpia.
    - Asegúrate de que el PDF tenga un índice y cada gráfico esté acompañado de una breve descripción de lo que representa.
    - Responde al final del PDF a las siguientes preguntas:
        - ¿Crees que los gráficos utilizados son los más adecuados para el análisis realizado? ¿Cuales cambiarías y por qué?
        - ¿Qué información adicional incluirías en los gráficos?
        - ¿Qué otros análisis realizarías con los datos disponibles?


2. **Exportación de Datos Procesados**  
   - Guarda un nuevo archivo CSV con 20 registros aleatorios del dataset final.

<hr>

## Pistas y Requisitos Técnicos
- Usa `polars` para todas las operaciones de manipulación de datos.
- Usa `numpy` para cálculos estadísticos y matemáticos, como la media, la desviación estándar y la correlación entre variables.
- Usa `matplotlib` para todas las visualizaciones.
- Asegúrate de que las visualizaciones sean claras, con etiquetas, títulos y leyendas adecuadas.
- Documenta cada paso del proceso con comentarios claros en el código.


<hr>

## Entregables
- Un script en Python (`.py`) o un notebook de Jupyter (`.ipynb`) con el código completo.
- Imágenes de los gráficos generados en un PDF.
- Un archivo CSV con los datos procesados.

