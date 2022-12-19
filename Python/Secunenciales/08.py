import os 
os.system ("cls")

r = float(input("ingrese el radio del cilindro: "))
h = float(input("ingrese la altura del cilindro: "))

area_base = 3.1416 *(r**2)
area_lateral = 2 * 3.1416 * r * h
area_total = 2 * area_base * area_lateral

print("el area del cilindro es",format(area_base,".2f"))
print("el area lateral del cilindro es",format(area_lateral,".2f"))
print("el area total del cilindro es",format(area_total,".2f"))