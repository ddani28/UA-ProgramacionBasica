try:
    print('Ingrese una temperatura')
    tempUnvalid = input()
    tempValid = int(tempUnvalid)

    tempFahren = ((tempValid * 9)/5) + 32
    print(tempFahren)
except:
    print(Exception)