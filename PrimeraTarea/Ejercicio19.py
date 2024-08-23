from datetime import datetime

def leer_fecha(prompt):
    while True:
        try:
            fecha_str = input(prompt)
            # Define el formato de la fecha, por ejemplo, 'dd/mm/aaaa'
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Formato de fecha inválido. Usa el formato dd/mm/aaaa.")

def main():
    print("Introduce las fechas en el formato dd/mm/aaaa.")
    fecha1 = leer_fecha("Introduce la primera fecha: ")
    fecha2 = leer_fecha("Introduce la segunda fecha: ")
    
    diferencia = abs((fecha2 - fecha1).days)
    
    print(f"El número de días entre las dos fechas es: {diferencia}")

if __name__ == "__main__":
    main()
