# El programa de La empresa Global Change debe realizar:

#1.	Solicitar al usuario el monto en soles (PEN) que desea cambiar

#2. Preguntar la tasa de cambio actual (por ejemplo, 1 USD = 3.85 PEN).

#3. Calcular y mostrar el equivalente en dólares (USD).

#4. Mostrar el resultado con dos decimales, indicando claramente el monto ingresado y el monto convertido

monto_soles=float(input("ingrese el monto en soles(PEN):"))
tasa_cambio=float(input("ingrese tasa de cambio actual(1 USD = ? PEN):"))
monto_dolares=monto_soles/tasa_cambio
print("\n--- Conversión en Global Change ---")
print(f"Monto en soles: S/ {monto_soles:.2f}")
print(f"Tasa de cambio: 1 USD = S/{tasa_cambio:.2f}")
print(f"Equivalente en dólares: $ {monto_dolares:.2f}")