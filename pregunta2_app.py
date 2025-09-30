# La empresa de transporte urbano MoviExpress debe implementar sistema que calcule la tarifa automaticamente:

#1. Solicitar al usuario la edad del pasajero.

#2. Usar una estructura condicional if – elif – else para determinar la tarifa correspondiente.

#3. Mostrar el precio final con un mensaje claro y formateado.

# Determinar la tarifa según la edad usando condicionales

edad = int(input("Ingrese la edad del pasajero: "))

if edad < 12:
    tarifa = 3.00
    mensaje = "Tarifa infantil"
elif edad <= 59: 
    tarifa = 5.00
    mensaje = "Tarifa regular"
else:  
    tarifa = 2.00
    mensaje = "Tarifa especial"

print(f"{mensaje}: S/ {tarifa:.2f}")