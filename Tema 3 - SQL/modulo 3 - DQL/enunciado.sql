/*
===================================================
SAKILA DATABASE - EJERCICIOS NIVEL BÁSICO
===================================================

Este archivo contiene ejercicios de SQL básico para familiarizarse
con la estructura de la base de datos Sakila y operaciones fundamentales.
*/

-- SECCIÓN 1: CONSULTAS BÁSICAS
-- ----------------------------

-- Ejercicio 1.1: Selecciona todos los actores de la tabla actor
-- Tip: Examina la estructura de la tabla primero

-- Ejercicio 1.2: Selecciona solo nombre y apellido de los actores

-- Ejercicio 1.3: Cuenta el número total de actores

-- SECCIÓN 2: FILTRADO CON WHERE
-- -----------------------------

-- Ejercicio 2.1: Encuentra todas las películas con clasificación 'PG-13'

-- Ejercicio 2.2: Encuentra todas las películas con duración mayor a 120 minutos

-- Ejercicio 2.3: Encuentra todas las películas con la palabra "DINOSAUR" en el título

-- SECCIÓN 3: ORDENACIÓN Y LÍMITES
-- -------------------------------

-- Ejercicio 3.1: Muestra los 10 títulos de películas más largas (por duración)

-- Ejercicio 3.2: Lista los actores ordenados por apellido y luego por nombre
-- [ESCRIBE TU RESPUESTA AQUÍ]

-- SECCIÓN 4: FUNCIONES DE AGREGACIÓN
-- ----------------------------------

-- Ejercicio 4.1: Calcula la duración promedio de todas las películas

-- Ejercicio 4.2: Encuentra la película más cara de alquilar

-- Ejercicio 4.3: Calcula la suma total de todos los pagos realizados

-- SECCIÓN 5: AGRUPAMIENTO BÁSICO
-- ------------------------------

-- Ejercicio 5.1: Cuenta cuántas películas hay de cada clasificación (rating)

-- Ejercicio 5.2: Calcula el precio de alquiler promedio por categoría

-- SECCIÓN 6: JOINS SIMPLES
-- -----------------------

-- Ejercicio 6.1: Lista de películas con el nombre de su categoría

-- Ejercicio 6.2: Muestra los actores que aparecen en la película "ACADEMY DINOSAUR"

-- Ejercicio 6.3: Encuentra todos los clientes que viven en "London"

-- SECCIÓN 7: OPERACIONES BÁSICAS DE DATOS
-- --------------------------------------

-- Ejercicio 7.1: Inserta un nuevo actor en la tabla actor
-- IMPORTANTE: Ejecuta dentro de una transacción para poder revertir

-- Verifica la inserción
-- Si quieres mantener el cambio: COMMIT;
-- Si quieres revertir el cambio: ROLLBACK;
ROLLBACK;

-- Ejercicio 7.2: Actualiza el nombre de un actor específico

-- SECCIÓN 8: RETO FINAL NIVEL BÁSICO
-- ----------------------------------

-- Ejercicio 8.1: Encuentra los clientes que han gastado más de $150 en alquileres
-- Muestra su nombre, apellido y la suma total que han gastado

-- Ejercicio 8.2: Lista las 5 categorías con mayor número de alquileres
-- Incluye el recuento de alquileres por categoría