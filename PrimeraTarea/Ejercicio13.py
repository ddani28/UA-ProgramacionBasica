import math
try:
    radio = float(input('Ingrese el radio de la esfera: '))
    area = (4*math.pi)* radio**2
    volumen = (4* math.pi * radio**3) / 3
    print(f'El area de la esfera es: {area}')
    print(f'El volumen de la esfera es: {volumen}')
except:
    print('Ingresa correctamente los datos') 