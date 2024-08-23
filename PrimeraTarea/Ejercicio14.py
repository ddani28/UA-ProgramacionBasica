valores = []
for i in range(5):
    try:
        valor = float(input('Ingrese un dato: '))
        valores.append(valor)
    except:
        print('Ingrese correctament los datos')

if len(valores) == 5:
    resul =((valores[0] + valores[1]) * (valores[2] - valores[3]))/ valores[4]
    print(f'El resultado es: {resul}')
else:
    print('Ingresse correctamente los datos')