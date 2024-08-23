

try:
    cap_inicial = float(input('Ingrese el capital inicial: '))
    interes_anual = float(input('Ingrese el interes anual: ')) 
    num_años = int(input('Ingrese el numero de años: '))

    interes = cap_inicial * interes_anual * num_años
    monto_total = interes + cap_inicial

    print(f'El monto total es de: {monto_total}')
except:
    print('Ingrese los datos correctamente')