import os
os.system ("cls")

horas_trabajadas = float(input("ingrese las horas trabajadas: "))
tarifa_horaria = float(input("ingrese la tarifa horaria: "))

sueldo_basico = tarifa_horaria * horas_trabajadas
bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print("sueldo basico: S/.", format(sueldo_basico, ".2f"))
print("sueldo bruto: S/.", format(sueldo_bruto, ".2f"))
print("sueldo neto: S/.", format(sueldo_neto, ".2f"))