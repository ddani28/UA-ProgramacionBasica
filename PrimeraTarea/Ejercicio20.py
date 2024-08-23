try:
    a = float(input("Introduce la longitud del primer lado: "))
    b = float(input("Introduce la longitud del segundo lado: "))
    c = float(input("Introduce la longitud del tercer lado: "))

    # Verifica si las longitudes proporcionadas forman un triángulo válido
    if a <= 0 or b <= 0 or c <= 0:
        print("Las longitudes de los lados deben ser números positivos.")
    elif a + b > c and a + c > b and b + c > a:
        # Determina el tipo de triángulo
        if a == b == c:
            print("El triángulo es equilátero.")
        elif a == b or b == c or a == c:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")
    else:
        print("Las longitudes proporcionadas no forman un triángulo válido.")
except ValueError:
    print("Por favor, introduce valores numéricos válidos.")
