numeros= []
for i in range(2):
    try:
        numberUnvalid = input('Ingrese un numero: ')
        numberValid = int(numberUnvalid)
        numeros.append(numberValid)
        
    except:
        print(Exception)
if len(numeros) == 2:
    if numeros[0] > numeros[1]:
        print(f'El numero {numeros[0]} es mayor que {numeros[1]}')
    elif numeros[0] < numeros[1]:
        print(f'El numero {numeros[0]} es menor que {numeros[1]}')
    else:
        print(f'Los numeros {numeros[0]} y {numeros[1]} son iguales')
else:
    print('Ingrese datos correctamente')    