texto = input('Introduce una cadena de texto: ')
contador_vocales = 0
vocales = 'aeiouAEIOU'
for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

print('Número de vocales en la cadena:', contador_vocales)
