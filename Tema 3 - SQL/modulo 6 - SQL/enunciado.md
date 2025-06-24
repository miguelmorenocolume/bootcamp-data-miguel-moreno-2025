## ¿En qué consisten las consultas de ventana y en qué se pueden diferenciar de las demás?

## Comprueba las siguientes consultas y comenta qué podría mejorar.

```sql
use sakila;
select * from payment where payment.amount > 10;
```

```sql
use NYCtaxi;
SELECT * FROM nyc_yellow_taxi_trip_records_from_Jan_to_Aug WHERE fare_amount > 2;
```

## ¿Cómo optimizarías las anteriores consulta? ¿Qué técnicas SQL se pueden usar para optimizarla?

## Busca en internet en qué consiste materializar un cálculo o una consulta en SQL y explícalo brevemente.

## ¿Qué son las common table expressions y qué sentido tienen?

## Prueba el argumento EXPLAIN en SQL y explica brevemente qué hace.

## Crea una vista que represente este resultado
ten en cienta que tienes permisos para crear vistas en esta base de datos

```sql
use NYCtaxi;
SELECT * FROM nyc_yellow_taxi_trip_records_from_Jan_to_Aug WHERE fare_amount > 2;
```

## REFLEXIÓN) ¿Qué conclusiones sacas de este ejercicio?¿Ves diferencias entre la consulta original y la vista en cuanto a rendimiento?

## REFLEXIÓN) Si fuese necesario ejecutar la anterior consulta recurrentemente, ¿Qué ideas se te ocurren para optimizar esta tarea?

## ¿Explica brevemente en qué consisten "HAVING COUNT()", "MOD()" Y "COALESCE()"?
