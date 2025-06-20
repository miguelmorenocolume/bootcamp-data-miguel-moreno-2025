# Ejercicio complejo Pandas + NumPy
#### Requisitos:
- pandas
- numpy
- python 3.11

#### Recursos:
- `da_centros.csv`
- `plantilla_organica_2223.csv`

---

## 1. Disponemos de dos archivos que contienen el resumen de la Plantilla Orgánica de Andalucía.

### Analiza los datasets y compréndelos: delimitadores, columnas, número de registros, etc.
### Si da problemas al cargar el csv en pandas, la codificación de los archivos puede que no sea UTF-8, esto genera problemas si no se especifica a la hora de cargar datos.


---

### a) ¿Cuántos cuerpos distintos hay en Almería?

### b) ¿Cuántas plazas de plantilla tiene el instituto Joaquín Tena Sicilia de la localidad de Abla en Almería?

### c) Crea un DataFrame llamado `df_dpto_musica` con los registros de los puestos que tengan algo que ver con música.

### d) Calcula la media de plazas disponibles con numpy en lo relacionado con la música y compárala con Física y Lengua Extranjera.  
Expresa los resultados en un DataFrame llamado `df_plazas_por_dpto` con las columnas:  
`tipo de departamento` y `media de plazas`.

### e) Añade una columna llamada `alta_empleabilidad` y dale un valor de 1 a los **5 centros** que más plazas disponibles tienen.

### f) Crea un DataFrame llamado `df_pzas_tipo_centro` que contenga el número total de plazas por tipo de centro.  
(Pista: extrae el tipo de centro a partir del campo `CENTRO` preferiblemente o a partir de `D_DENOMINA` del otro dataset).

### g) Clasifica los centros del departamento de música en rangos de percentiles según su número de plazas.

```python
sum_por_centro = df_dpto_musica.groupby('CENTRO')['PLAZAS'].sum().sort_values(ascending=False)
sum_por_centro

# Calculamos los percentiles
percentiles = np.percentile(sum_por_centro, [0, 25, 75, 100])

# Creamos una función para asignar rangos
def asignar_rango(x):
    if x <= percentiles[1]:
        return '0-25%'
    elif x <= percentiles[2]:
        return '25-75%'
    else:
        return '75-100%'

# Aplicamos la función para crear los rangos
rangos_percentiles = sum_por_centro.apply(asignar_rango)

# Convertimos a Serie de Pandas
rangos_percentiles = pd.Series(rangos_percentiles)

# Definimos todos los rangos posibles
rangos = ['0-25%', '25-75%', '75-100%']

# Creamos el DataFrame con el conteo y porcentajes, forzando todos los rangos
resumen = pd.DataFrame({
    'Número de Centros': rangos_percentiles.value_counts().reindex(rangos).fillna(0).astype(int),
    'Porcentaje (%)': rangos_percentiles.value_counts(normalize=True).reindex(rangos).fillna(0) * 100
})

print(resumen)
```

#### Si el código no funciona, este es el resultado que debería dar, no te preocupes si tu resultado no es el mismo, puede ser parecido.

```python

         Número de Centros  Porcentaje (%)
PLAZAS                                    
0-25%                 2570       92.313218
25-75%                   0        0.000000
75-100%                214        7.686782

```

### Analiza el resultado. Explica qué representa cada columna con tus palabras y reflexiona sobre el resultado.

### h) Usando numpy, ¿cuál es la relación entre el número de plazas y la alta empleabilidad? ¿es alta? ¿es una relación directa o indirectamente proporcional?

### OPCIONAL) ¿Crees que tiene sentido calcular una correlación entre una columna "original" y otra que depende de ella y hemos creado nosotros (alta_empleabilidad)? Con tus palabras.
### REFLEXIÓN) ¿Cuántos registros tiene cada dataset? ¿Y si mezclas ambos datasets? Teniendo en cuenta conceptos básicos de los modelos relacionales, ¿a qué crees que se debe, o qué conclusión puedes sacar de esto?
### REFLEXIÓN) ¿Qué ha resultado más difícil de realizar?
