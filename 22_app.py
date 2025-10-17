def calcular_precio_final(monto, porcentaje_descuento):

  # Calcula el descuento

  descuento = monto * (porcentaje_descuento / 100)

  # Calcula el precio final

  precio_final = monto - descuento

  return precio_final



# Ejemplo de uso

monto = float(input("Ingrese el monto del producto: "))

porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

precio_final = calcular_precio_final(monto, porcentaje_descuento)



print(f"El monto a pagar es: {precio_final}")