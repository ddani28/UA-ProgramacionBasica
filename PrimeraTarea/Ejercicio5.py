medidas = []
for i in range(2):
    try:
        medida = input('Ingrese una medida: ')
        medidaValid = float(medida)
        medidas.append(medidaValid)
    except:
        print(Exception)

if len(medidas) == 2:
    area = (medidas[0] * medidas[1])/2
    print(area)
else:
    print('Ingrese correctamente los datos')