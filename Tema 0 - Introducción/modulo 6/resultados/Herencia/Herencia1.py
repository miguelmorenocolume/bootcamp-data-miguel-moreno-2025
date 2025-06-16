class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

alumno_1 = Alumno("Miguel", 21)

print(alumno_1.nombre, alumno_1.edad)