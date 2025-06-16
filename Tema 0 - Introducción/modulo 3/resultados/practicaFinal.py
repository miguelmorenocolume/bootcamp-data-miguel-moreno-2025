# Solicitar al usuario el texto y las letras
texto = input("Ingresa un texto: ").strip()
letras = []
for i in range(1, 4):
    letra = input(f"Ingrese la letra #{i}: ").strip().lower()
    while len(letra) != 1 or not letra.isalpha():
        letra = input(f"Por favor, ingrese solo una letra válida para la letra #{i}: ").strip().lower()
    letras.append(letra)

# Convertir texto a minúsculas para análisis de letras
texto_minus = texto.lower()

# Contar apariciones de cada letra
conteos = [texto_minus.count(letra) for letra in letras]

# Contar palabras
palabras = texto.split()
cantidad_palabras = len(palabras)

# Primera y última letra
primera_letra = texto[0] if texto else ""
ultima_letra = texto[-1] if texto else ""

# Invertir el orden de las palabras
palabras_invertidas = ' '.join(palabras[::-1])

# Verificar si "Python" está en el texto (ignorando mayúsculas/minúsculas)
contiene_python = "python" in texto_minus

# Mostrar resultados
print("\n--- RESULTADOS DEL ANÁLISIS ---")
for i, letra in enumerate(letras, 1):
    print(f"La letra '{letra}' aparece {conteos[i-1]} veces en el texto.")
print(f"Cantidad total de palabras: {cantidad_palabras}")
print(f"Primera letra del texto: '{primera_letra}'")
print(f"Última letra del texto: '{ultima_letra}'")
print(f"Texto con el orden de las palabras invertido:\n{palabras_invertidas}")
print(f"La palabra 'Python' {'sí' if contiene_python else 'no'} está presente en el texto.")

