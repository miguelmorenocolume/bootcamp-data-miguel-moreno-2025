import random

matriz = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for fila in matriz:
    print(' '.join(str(num) for num in fila))