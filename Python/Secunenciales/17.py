import os
os.system ("cls")

donación = float(input("ingrese el monto de la donación: "))

centro_de_salud = donación * 0.25
comedor_infantil = donación * 0.35
escuela_infantil = donación * 0.25
asilo_ancianos = donación * 0.15

print("el centro de salud recibe S/.", format(centro_de_salud, ".2f"))
print("el comedor infantil recibe S/.", format(comedor_infantil, ".2f"))
print("la escuela intantil recibe S/", format(escuela_infantil, ".2f"))
print("el asilo de ancianos recibe S/", format(asilo_ancianos, ".2f"))