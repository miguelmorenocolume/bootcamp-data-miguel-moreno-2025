import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza de números!")
    nombre = input("Por favor, ingresa tu nombre: ")
    numero_secreto = random.randint(1, 100)
    intentos_maximos = 8
    print(f"\nHola, {nombre}. He pensado en un número entre 1 y 100.")
    print(f"Tienes {intentos_maximos} intentos para adivinarlo.\n")

    for intento in range(1, intentos_maximos + 1):
        try:
            entrada = input(f"Intento {intento}: Ingresa un número entre 1 y 100: ")
            numero = int(entrada)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero < 1 or numero > 100:
            print("Has elegido un número no permitido. Debe estar entre 1 y 100.")
            continue

        if numero < numero_secreto:
            print("El número elegido es menor al número secreto.\n")
        elif numero > numero_secreto:
            print("El número elegido es mayor al número secreto.\n")
        else:
            print(f"¡Felicidades, {nombre}! Has adivinado el número en {intento} intento(s).")
            break
    else:
        print(f"\nPerdiste, {nombre}. No has adivinado el número en {intentos_maximos} intentos.")
        print(f"El número secreto era: {numero_secreto}")

if __name__ == "__main__":
    juego_adivinanza()