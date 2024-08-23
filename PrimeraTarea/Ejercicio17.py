try:
    index = int(input("Introduce el índice de la serie de Fibonacci (n): "))

    if index <= 0:
        print("El índice debe ser un número entero positivo.")
    elif index == 1:
        print("El número en la posición 1 de la serie de Fibonacci es: 0")
    elif index == 2:
        print("El número en la posición 2 de la serie de Fibonacci es: 1")
    else:
        a, b = 0, 1
        for _ in range(2, index):
            a, b = b, a + b
        print(f"El número en la posición {index} de la serie de Fibonacci es: {b}")

except ValueError:
    print("Por favor, introduce un número entero válido.")
