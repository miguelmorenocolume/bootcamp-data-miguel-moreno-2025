# 📊 Ejercicio de Visualización con Seaborn y dataset de Diamantes

## 🐍 Requisitos:
- Python 3.11
- seaborn
- matplotlib
- scipy

## 🎯 Objetivo
Crear visualizaciones utilizando diferentes funcionalidades de Seaborn utilizando el dataset de `diamonds` que viene incluido en la biblioteca.

## 🐍 Configuración Inicial.
Usa este snippet para empezar.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos el dataset
diamonds = sns.load_dataset('diamonds')

# Configuramos el estilo inicial
plt.rcParams['figure.figsize'] = [10, 6]

sns.set_style("whitegrid")
sns.set_palette("muted")

diamonds.head()
diamonds = diamonds.dropna()
diamonds = diamonds.sample(2500)
```

## 📝 Ejercicios

### 1. Exploración Básica (usando solo Seaborn)
1. Visualiza la distribución del precio de los diamantes usando `displot`
2. Crea un `boxplot` del precio por corte
3. Genera un `violinplot` del precio por claridad

### 2. Distribuciones
explora un poco los parámetros en este apartado
1. Crea un `histplot` del precio con diferentes bins
2. Utiliza `kdeplot` para mostrar la densidad del quilataje (carat)
3. Compara las distribuciones de precio por corte usando `boxenplot`

### 3. Relaciones
1. Crea un `scatterplot` de quilates vs precio
2. Añade una línea de regresión usando `regplot`
3. Utiliza `jointplot` para visualizar la relación entre quilates y precio con histogramas marginales

### 4. Visualizaciones Categóricas
1. Genera un `stripplot` del precio por claridad
2. Crea un `swarmplot` del precio por corte
3. Combina un `boxplot` con un `stripplot` para el precio por color

### 5. Gráficos de Rejilla
1. Usa `FacetGrid` para crear histogramas de precio por corte
2Utiliza `JointGrid` para explorar la relación entre profundidad y precio

### 6. Visualizaciones Avanzadas
1. Crea una matriz de correlación usando `heatmap`
   - ¿Qué conclusión sacas de esta gráfica?

2. Usa el siguiente código y explica qué cambia en relación con el anterior:

```python
sns.clustermap(diamonds.select_dtypes('number').corr(), annot=True, figsize=(6, 6), linewidths=0.5, cmap='coolwarm')
```

3. Usa el siguiente código, explica qué expresa. Sinceramente, ¿crees que esta gráfica es útil?, ¿la usarías?, ¿en ese caso, en qué casos?:

```python
sns.kdeplot(diamonds.select_dtypes('number').corr())
```

## Reflexión
1. ¿Qué diferencia ves de seaborn a matplotlib? ¿crees que son excluyentes?