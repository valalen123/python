import os
os.system ("cls")

cant_producto = int(input("ingrese a cantidad adquirida: "))
precio_producto = float(input("ingrese el precio de articulo: "))

importe_compra = precio_producto * cant_producto
descuento1 = importe_compra - (importe_compra * 0.15)
importepagar = descuento1 - (descuento1 * 0.15)

print("el importe de compra S/.", format(importe_compra, ".2f"))
print("el primer descuento fue de S/.", format(importe_compra * 0.15, ".2f"))
print("el segundo descuento fue de S/.", format(descuento1 * 0.15, ".2f"))
print("el importe a pagar es de S/.", format(importepagar, ".2f"))