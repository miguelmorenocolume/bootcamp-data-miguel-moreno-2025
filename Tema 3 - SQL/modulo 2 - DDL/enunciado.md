# Enunciado

## Modificación básica a una tabla

En esta práctica tienes que hacer modificaciones esenciales a tu tabla `EMPLEADOS` creada en el módulo anterior.

Modifica la tabla de la siguiente manera:

- Añade una columna llamada `experiencia` con los valores `Junior`, `Medio` o `Senior`.
- Añade una columna llamada `telefono` con los valores de un telefono de la persona.
- Añade una columna llamada `activo` con los valores `true` o `false`.

## Crear una tabla y relacionar

Crea una tabla llamada `ASIGNACIONES` con las siguientes columnas:

- `id_empleado`
- `id_proyecto`
- `horas_asignadas`

Esta tabla debe tener una relación uno a muchos con la tabla `EMPLEADOS` y la tabla `PROYECTOS`.

- Crea una relación uno a muchos entre las dos tablas.

### Eliminar tablas completas

1. Intenta eliminar la tabla `EMPLEADOS` directamente. ¿Qué ocurre y por qué?
2. Elimina correctamente las tablas siguiendo el orden adecuado debido a las restricciones de clave foránea.
3. Utiliza la cláusula `CASCADE` para eliminar una tabla y todas sus dependencias (ten precaución con esta operación).