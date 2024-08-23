import math
medidas = []

try:
    medida = input('Ingrese una medida: ')
    medidaValid = float(medida)
    radio = (medidaValid/2)**2
    area = radio * math.pi
    print(area)
except:
    print(Exception)

