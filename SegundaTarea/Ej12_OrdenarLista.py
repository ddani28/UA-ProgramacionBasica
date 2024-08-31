entrada = input('Introduce una lista de números separados por espacios: ')
numeros = entrada.split()
numeros = [int(numero) for numero in numeros] 
numeros.sort()
print('Lista ordenada de menor a mayor:', numeros)
