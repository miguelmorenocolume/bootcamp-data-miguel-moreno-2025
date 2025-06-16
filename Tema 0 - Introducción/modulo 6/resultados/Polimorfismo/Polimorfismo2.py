class Arquero:
    def atacar(self):
        print("El arquero dispara una flecha.")

class Mago:
    def atacar(self):
        print("El mago lanza un hechizo.")

class Guerrero:
    def atacar(self):
        print("El guerrero ataca con su espada.")

arquero = Arquero()
mago = Mago()
guerrero = Guerrero()

personajes = [arquero, mago, guerrero]

for personaje in personajes:
    personaje.atacar()