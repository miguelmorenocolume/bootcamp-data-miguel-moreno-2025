import pandas as pd
import numpy as np

# Cargar archivos
df_centros = pd.read_csv("datos/da_centros.csv", sep=";", encoding="latin1")
df_plantilla = pd.read_csv("datos/plantilla_organica_2223.csv", sep=";", encoding="latin1")

# Vista general
print("Primeras filas de df_centros:\n", df_centros.head(), "\n")
print("Primeras filas de df_plantilla:\n", df_plantilla.head(), "\n")

# a) Cuerpos distintos en Almería
cuerpos_almeria = df_plantilla[df_plantilla["PROVINCIA"] == "ALMERÍA"]["CUERPO"].nunique()
print("a) Número de cuerpos distintos en Almería:", cuerpos_almeria, "\n")

# b) Plazas en el IES Joaquín Tena Sicilia de Abla
plazas_tena_sicilia = df_plantilla[
    (df_plantilla["CENTRO"].str.contains("JOAQUÍN TENA SICILIA", case=False)) &
    (df_plantilla["LOCALIDAD"].str.upper() == "ABLA") &
    (df_plantilla["PROVINCIA"].str.upper() == "ALMERÍA")
]["PLAZAS"].sum()
print("b) Número de plazas en el IES Joaquín Tena Sicilia (Abla, Almería):", plazas_tena_sicilia, "\n")

# c) DataFrame de puestos relacionados con Música
df_dpto_musica = df_plantilla[df_plantilla["PUESTO"].str.contains("MÚSICA", case=False, na=False)]
print("c) Puestos relacionados con Música (primeras filas):\n", df_dpto_musica.head(), "\n")

# d) Media de plazas en Música, Física y Lengua Extranjera
musica = df_plantilla[df_plantilla["PUESTO"].str.contains("MÚSICA", case=False, na=False)]
fisica = df_plantilla[df_plantilla["PUESTO"].str.contains("FÍSICA", case=False, na=False)]
lengua_extranjera = df_plantilla[df_plantilla["PUESTO"].str.contains("LENGUA EXTRANJERA", case=False, na=False)]

media_musica = np.mean(musica["PLAZAS"])
media_fisica = np.mean(fisica["PLAZAS"])
media_idioma = np.mean(lengua_extranjera["PLAZAS"])

df_plazas_por_dpto = pd.DataFrame({
    "tipo de departamento": ["Música", "Física", "Lengua Extranjera"],
    "media de plazas": [media_musica, media_fisica, media_idioma]
})
print("d) Media de plazas por departamento:\n", df_plazas_por_dpto, "\n")

# e) Alta empleabilidad para los 5 centros con más plazas
df_plantilla["total_plazas_por_centro"] = df_plantilla.groupby("CENTRO")["PLAZAS"].transform("sum")
top_centros = df_plantilla.sort_values("total_plazas_por_centro", ascending=False)["CENTRO"].unique()[:5]
df_plantilla["alta_empleabilidad"] = df_plantilla["CENTRO"].isin(top_centros).astype(int)

print("e) Centros con alta empleabilidad:\n", df_plantilla[df_plantilla["alta_empleabilidad"] == 1][["CENTRO", "total_plazas_por_centro"]].drop_duplicates(), "\n")

# f) Plazas totales por tipo de centro
df_plantilla["tipo_centro"] = df_plantilla["CENTRO"].str.extract(r'^[0-9]+-[.]*([A-Z\. ]+)')
df_pzas_tipo_centro = df_plantilla.groupby("tipo_centro")["PLAZAS"].sum().reset_index()
print("f) Plazas totales por tipo de centro:\n", df_pzas_tipo_centro, "\n")

# g) Clasificación de centros de música por percentiles
sum_por_centro = df_dpto_musica.groupby("CENTRO")["PLAZAS"].sum().sort_values(ascending=False)
percentiles = np.percentile(sum_por_centro, [0, 25, 75, 100])

def asignar_rango(x):
    if x <= percentiles[1]:
        return '0-25%'
    elif x <= percentiles[2]:
        return '25-75%'
    else:
        return '75-100%'

rangos_percentiles = sum_por_centro.apply(asignar_rango)
rangos = ['0-25%', '25-75%', '75-100%']

resumen = pd.DataFrame({
    'Número de Centros': rangos_percentiles.value_counts().reindex(rangos).fillna(0).astype(int),
    'Porcentaje (%)': rangos_percentiles.value_counts(normalize=True).reindex(rangos).fillna(0) * 100
})
print("g) Clasificación por percentiles de centros de música:\n", resumen, "\n")

# h) Correlación entre número de plazas y alta empleabilidad
correlacion = np.corrcoef(df_plantilla["PLAZAS"], df_plantilla["alta_empleabilidad"])[0, 1]
print("h) Correlación entre plazas y alta empleabilidad:", round(correlacion, 4))
