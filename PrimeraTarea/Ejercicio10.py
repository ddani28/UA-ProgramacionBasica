valores = []
for i in range(3):
    try:
        valor = input('Ingrese un valor: ')
        valorValido = float(valor)
        valores.append(valorValido)
    except:
        print(Exception)

if len(valores) == 3:
    discriminante = (valores[1]**2) - 4 * (valores[0] * valores[2])
    print(f'El resultado del discriminante es: {discriminante}')
else:
    print('Ingrese los datos correctamente')