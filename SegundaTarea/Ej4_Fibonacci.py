n = int(input('Introduce un número: '))
if n < 1 or n > 50:
    print('El número debe estar entre 1 y 50.')
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  