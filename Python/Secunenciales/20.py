import os 
os.system ("cls")

dinero = int(input("ingrese la cantidad de dinero: S/. "))

billetes200 = dinero//200
billetes100 = (dinero%200)//100
billetes50 = (dinero%200)%100 //50
billetes20 = (((dinero%200)%100)%50)//20
billetes10 = ((((dinero%200)%100)%50)%20)//10
moneda5 = ((((dinero%200)%100)%50)%20)%10 //5
moneda2 = ((((((dinero%200)%100)%50)%20)%10)%5)//2
moneda1 = (((((((dinero%200)%100)%50)%20)%10)%5)%2)//1

print("billetes de 200 soles son ",billetes200)
print("billetes de 100 soles son ",billetes100)
print("billetes de 50 soles son ",billetes50)
print("billetes de 20 soles son ",billetes20)
print("billetes de 10 soles son ",billetes10)
print("monedas de 5 soles son ",moneda5)
print("monedas de 2 soles son ",moneda2)
print("monedas de 1 sol son ",moneda1)