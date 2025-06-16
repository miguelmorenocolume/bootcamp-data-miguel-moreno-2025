def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

resultado = numeros_persona("Miguel", 1, 2, 3, 4, 5)
print(resultado)