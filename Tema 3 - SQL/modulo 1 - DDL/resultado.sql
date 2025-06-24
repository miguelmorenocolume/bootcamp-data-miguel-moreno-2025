CREATE TABLE MMC_EMPLEADOS (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_contratacion DATE NOT NULL,
    salario DECIMAL(15,2) NOT NULL,
    id_departamento INT NOT NULL,
    telefono VARCHAR(20),
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    experiencia VARCHAR(10) NOT NULL CHECK (experiencia IN ('Junior', 'Medio', 'Senior'))
);