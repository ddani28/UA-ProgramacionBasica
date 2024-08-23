try:
    medidaUnvalid = input('Ingrese una longitud: ')
    medidaValid = float(medidaUnvalid)
    pulgadas = medidaValid /2.54
    print(pulgadas)
except:
    print(Exception)