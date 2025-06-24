import seaborn as sns
import matplotlib.pyplot as plt

# Cargar y preparar datos
diamonds = sns.load_dataset('diamonds')
diamonds = diamonds.dropna().sample(2500)

# Configuración visual
plt.rcParams['figure.figsize'] = [10, 6]
sns.set_style("whitegrid")
sns.set_palette("muted")

# 1. Exploración Básica
sns.displot(diamonds['price'], kde=False, bins=30)
plt.title('Distribución del Precio')
plt.show()

sns.boxplot(x='cut', y='price', data=diamonds)
plt.title('Boxplot del Precio por Corte')
plt.show()

sns.violinplot(x='clarity', y='price', data=diamonds)
plt.title('Violinplot del Precio por Claridad')
plt.show()

# 2. Distribuciones
sns.histplot(diamonds['price'], bins=50, kde=True)
plt.title('Histograma del Precio con Más Bins')
plt.show()

sns.kdeplot(diamonds['carat'], fill=True)
plt.title('Densidad del Quilataje')
plt.show()

sns.boxenplot(x='cut', y='price', data=diamonds)
plt.title('Boxenplot del Precio por Corte')
plt.show()

# 3. Relaciones
sns.scatterplot(x='carat', y='price', data=diamonds)
plt.title('Scatterplot de Quilates vs Precio')
plt.show()

sns.regplot(x='carat', y='price', data=diamonds, scatter_kws={'alpha':0.3})
plt.title('Regplot con Línea de Regresión')
plt.show()

sns.jointplot(x='carat', y='price', data=diamonds, kind='scatter')
plt.show()

# 4. Visualizaciones Categóricas
sns.stripplot(x='clarity', y='price', data=diamonds, jitter=True)
plt.title('Stripplot Precio por Claridad')
plt.show()

sns.swarmplot(x='cut', y='price', data=diamonds)
plt.title('Swarmplot Precio por Corte')
plt.show()

sns.boxplot(x='color', y='price', data=diamonds, fliersize=0)
sns.stripplot(x='color', y='price', data=diamonds, color='black', alpha=0.3)
plt.title('Boxplot + Stripplot Precio por Color')
plt.show()

# 5. Gráficos de Rejilla
g = sns.FacetGrid(diamonds, col='cut', col_wrap=3)
g.map(sns.histplot, 'price')
plt.show()

g = sns.JointGrid(data=diamonds, x='depth', y='price')
g.plot(sns.scatterplot, sns.histplot)
plt.show()

# 6. Visualizaciones Avanzadas
corr = diamonds.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()

sns.clustermap(corr, annot=True, figsize=(6, 6), linewidths=0.5, cmap='coolwarm')
plt.show()

sns.kdeplot(corr)
plt.title("KDE de la matriz de correlación")
plt.show()
