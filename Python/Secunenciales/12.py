import os
os.system ("cls")

num_segundos = int(input("digite un numero expresado en segundos: "))

dias = ((num_segundos//60)//60)//24

hora = ((num_segundos//60)//60)%24

minutos = (num_segundos//60)%60

segundos = num_segundos%60

print = ("Dias: ",dias)
print = ("Horas: ",hora)
print = ("Minutos: ",minutos)
print = ("Segundos: ",segundos)
print = ("")