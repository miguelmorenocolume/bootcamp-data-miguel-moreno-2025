a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a == b and b == c:
    print("Los tres números son iguales.")

if a != b and b != c and a != c:
    print("Los tres números son diferentes.")

if a == b or b == c or a == c:
    print("Al menos dos números son iguales.")

if a > 100 or b > 100 or c > 100:
    print("Al menos uno de los números es mayor que 100.")

if (0 <= a <= 50) and (0 <= b <= 50) and (0 <= c <= 50):
    print("Los tres números están en el rango de 0 a 50 (inclusive).")