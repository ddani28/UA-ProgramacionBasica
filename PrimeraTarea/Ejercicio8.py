

try:
    horas = input('Ingrese las horas a convertir: ')
    horasValid = int(horas)
    minutos = horasValid * 60
    print(f'Las horas ingresadas equivalen a {minutos} minutos')
except:
    print(Exception)