import random
n = int(input('Introduce la cantidad de números aleatorios: '))
if n <= 0:
    print('Por favor, ingresa un número positivo.')
else:
    numeros_aleatorios = [random.randint(1, 100) for _ in range(n)]
    print('Lista de números aleatorios:', numeros_aleatorios)
