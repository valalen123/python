import os
os.system ("cls")

num1 = int(input("ingrese el primero numero: "))
num2 = int(input("ingrese el segundo numero: "))

num1_c1 = num1//100
num1_c2 = (num1%100)//10
num1_c3 = num1%10

num2_c1 = num2//100
num2_c2 = (num2%100)//10
num2_c3 = num2%10

print("---numeros intercambiados---")
print("primer numero: ",(num2_c3*100)+(num1_c2*10)+(num2_c1))
print("segundo numero: ",(num1_c3*100)+(num2_c2*10)+(num1_c1))