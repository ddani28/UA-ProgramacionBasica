medidas = []
for i in range(2):
    try:
        medida = input('Ingrese una medida: ')
        medidaValid = float(medida)
        medidas.append(medidaValid)
    except:
        print(Exception)

if len(medidas) == 2:
    area = (medidas[0] * medidas[1])
    perimetro = (medidas[0] * 2) + (medidas[1] * 2)
    print(f'El area es: {area}')
    print(f'El perimetro es: {perimetro}')
else:
    print('Ingrese correctamente los datos')