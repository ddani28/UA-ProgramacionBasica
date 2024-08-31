entrada = input('Introduce una lista de números separados por espacios: ')
numeros = entrada.split()
numeros = [int(numero) for numero in numeros]
mayor = max(numeros)
menor = min(numeros)
print('El número mayor es:', mayor)
print('El número menor es:', menor)
