entrada = input('Introduce una lista de números separados por espacios: ')
numeros = entrada.split()
suma_total = 0
for numero in numeros:
    suma_total += int(numero)

print('La suma es: ', suma_total)
