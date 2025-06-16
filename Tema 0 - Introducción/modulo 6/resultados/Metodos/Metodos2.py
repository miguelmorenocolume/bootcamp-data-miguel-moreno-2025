class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        
jugador = Jugador()

print(jugador.vivo)
jugador.revivir()
print(jugador.vivo)