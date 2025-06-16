class Cubo:
   caras = 6

   def __init__(self, color):
      self.color = color

cubo_rojo = Cubo("rojo")
cubo_verde = Cubo("verde")
cubo_azul = Cubo("azul")



print(cubo_rojo.color, cubo_rojo.caras)
print(cubo_verde.color, cubo_verde.caras)
print(cubo_azul.color, cubo_azul.caras)