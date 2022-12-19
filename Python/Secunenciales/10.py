import os 
os.system ("cls")

numero = int(input("ingrese el numero: "))

c1 = numero//1000
c2 = (numero%1000)//100
c3 = (((numero%1000)%100)//10)
c4 = numero%10

print("el numero al reves es",(c4 * 1000)+(c3 * 100)+(c2 * 10)+ c1)