/*
===================================================
SAKILA DATABASE - EJERCICIOS NIVEL AVANZADO
===================================================

Este archivo contiene ejercicios de SQL avanzado que cubren temas complejos
como CTEs, funciones de ventana, optimización de consultas y más.
*/

-- SECCIÓN 1: CTE (COMMON TABLE EXPRESSIONS)
-- ----------------------------------------

-- Ejercicio 1.1: Encuentra clientes VIP (top 10% en gastos) usando CTE

-- Ejercicio 1.2: CTE recursivo para crear una jerarquía de categorías
-- (Simulando un caso donde las categorías pudieran tener subcategorías)

-- Ejercicio 1.3: Usa CTE para encontrar películas populares que nunca se han alquilado en ciertos países

-- SECCIÓN 2: FUNCIONES DE VENTANA (WINDOW FUNCTIONS)
-- -------------------------------------------------

-- Ejercicio 2.1: Clasifica clientes por gasto total y muestra su posición dentro de su país

-- Ejercicio 2.2: Calcula la diferencia de alquileres entre meses consecutivos por tienda

-- Ejercicio 2.3: Encuentra la diferencia de tiempo entre alquileres consecutivos por cliente

-- SECCIÓN 3: SUBCONSULTAS CORRELACIONADAS Y JOINS LATERALES
-- -------------------------------------------------------

-- Ejercicio 3.1: Para cada actor, encuentra su película más alquilada usando subconsulta correlacionada

-- Ejercicio 3.2: Usa LATERAL JOIN para encontrar las 3 películas más alquiladas por categoría

-- SECCIÓN 4: PIVOTAJE Y ANÁLISIS CRUZADO
-- -------------------------------------

-- Ejercicio 4.1: Crea un informe de ingresos por categoría y mes como tabla pivote

-- Ejercicio 4.2: Crea un informe que muestre la cantidad de películas por clasificación y categoría

-- SECCIÓN 5: OPTIMIZACIÓN Y ANÁLISIS DE CONSULTAS
-- ---------------------------------------------

-- Ejercicio 5.1: Analiza y optimiza la siguiente consulta:
-- (Incluye tu análisis como comentarios y la consulta optimizada)

-- Ejercicio 5.2: Identifica y optimiza otra consulta compleja de tu elección

-- SECCIÓN 6: TRIGGERS Y PROCEDIMIENTOS ALMACENADOS AVANZADOS
-- --------------------------------------------------------

-- Ejercicio 6.1: Crea un trigger que mantenga actualizada una tabla de estadísticas de alquiler
-- Primero, creamos una tabla para estadísticas

-- Luego creamos el trigger

-- Ejercicio 6.2: Crea un procedimiento almacenado que implemente una lógica compleja de negocio

-- SECCIÓN 7: ADMINISTRACIÓN DE PERMISOS Y SEGURIDAD
-- -----------------------------------------------
-- Ejercicio 7.2: Implementa una política de acceso basada en vistas

-- SECCIÓN 8: RETO FINAL NIVEL AVANZADO
-- -----------------------------------

-- Ejercicio 8.1: Sistema completo de análisis de patrones de alquiler

-- Paso 1: Crear tabla para análisis avanzado de clientes

-- Consulta la tabla analítica

-- Ejercicio 8.2: Implementa un sistema de recomendación de películas
