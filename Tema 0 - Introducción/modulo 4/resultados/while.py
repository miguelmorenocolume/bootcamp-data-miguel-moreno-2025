while True:
    entrada = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("Saliendo del programa")
        break
    invertida = entrada[::-1]
    print("Invertido:", invertida)