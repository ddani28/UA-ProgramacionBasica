texto = input('Introduce una cadena de texto: ')
caracter = input('Introduce el carácter a contar: ')
if len(caracter) != 1:
    print('Ingresa solo un carácter')
else:
    conteo = texto.count(caracter)
    print(f'El carácter ' + {caracter}+ ' aparece {conteo} veces en la cadena.')
