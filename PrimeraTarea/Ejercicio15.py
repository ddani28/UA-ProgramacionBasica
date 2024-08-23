try:
    monto = float(input('Ingrese el monto de la compra: '))
    tasa_impuesto = float(input('Ingrese la tasa de impuesto: '))
    impuesto = monto * (tasa_impuesto * 0.01)
    total = monto + impuesto
    print(total)
except:
    print('Ingresa correctamente los datos')