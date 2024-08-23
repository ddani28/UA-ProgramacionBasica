try:
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))

    if a == 0:
        print("El valor de a no puede ser 0, ya que no se puede dividir entre 0.")
    else:
        # Calcula el valor de x usando la fórmula x = -b / a
        x = -b / a
        print(f"El valor de x que satisface la ecuación {a}x + {b} = 0 es: {x}")

except ValueError:
    print("Por favor, introduce valores numéricos válidos.")
