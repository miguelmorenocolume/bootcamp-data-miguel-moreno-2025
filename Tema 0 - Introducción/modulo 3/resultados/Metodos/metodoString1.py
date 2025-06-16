lista_palabras = ["Si", "la", "implementación", "es", "difícil", "de", "explicar,", "puede", "que", "sea", "una", "mala", "idea"]

frase = " ".join(lista_palabras)
frase_mayus = frase.upper()
print(frase_mayus)

frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")
print(frase_modificada)