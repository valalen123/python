import os 
os.system ("cls")

base_r = float(input("ingrese la basae del rectangulo: "))
altura_r = float(input("ingrese la altura del rectangula: "))

area_r = base_r * altura_r 
perimetro_r = 2 *(base_r + altura_r)

print("el area del rectangulo es", format(area_r,".2f"))
print("el perimetro del rectangulo es",format(perimetro_r,".2f"))