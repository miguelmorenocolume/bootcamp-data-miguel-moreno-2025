def suma_absolutos(*args):
    return sum(abs(x) for x in args)

suma_absolutos = suma_absolutos(1, -2, 3)
print(suma_absolutos)