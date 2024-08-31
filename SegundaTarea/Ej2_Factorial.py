num = int(input('Ingrese un numero para calcular el factorial: '))
i = num
result = 1 
while i < 20 and i > 1:
   result *= i
   i -= 1

   print(result)