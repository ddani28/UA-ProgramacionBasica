try:
    añoUnvalid = input('Ingrese el año: ')
    añoValid = int(añoUnvalid)

    if (añoValid % 4) == 0 and añoValid % 100 != 0 or (añoValid % 4) == 0 and añoValid % 400:
        print(f'El año {añoValid} es bisiesto')
    else:
        print(f'El año {añoValid} no es bisiesto')
except:
    print(Exception)