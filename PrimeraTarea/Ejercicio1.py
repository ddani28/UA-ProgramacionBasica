#Calculo de promedio de tres digitos
suma = 0
totalNumeros = 0
for i in range(3):
    try:
        numberUnvalid = input('Ingrese un numero ')
        numberValid = float(numberUnvalid)
        suma += numberValid
        totalNumeros += 1
        
    except:
        print(Exception)
if totalNumeros > 0:
    promedio = (suma / totalNumeros)
    print(f'Su promedio es de:  + {promedio}')
else:
    print('Ingrese datos correctos')