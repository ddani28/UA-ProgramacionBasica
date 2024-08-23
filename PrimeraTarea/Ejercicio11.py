valores = []
for i in range(3):
    try:
        valor = input('Ingrese un valor: ')
        valorValidado = float(valor)
        valores.append(valorValidado)
    except:
        print(Exception)

if len(valores) == 3:
    area = ((valores[0] + valores[1]) * valores[2])/2
    print(f'El area es: {area}')
else:
    print('Ingrese correctamente los datos')