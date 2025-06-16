def suma_cuadrados(*args):
    return sum(x**2 for x in args)


resultado = suma_cuadrados(1, 2, 3)
print(resultado)