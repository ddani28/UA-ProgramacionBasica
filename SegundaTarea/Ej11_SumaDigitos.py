numero = input('Introduce un número entero: ')
suma_digitos = 0
for caracter in numero:
    if caracter.isdigit():
        suma_digitos += int(caracter)

print('La suma de los dígitos es:', suma_digitos)
