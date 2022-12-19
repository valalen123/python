import os
os.system ("cls")

dinero_juan = float(input("dinero de juan: $"))
dinero_rosa = float(input("dinero de rosa: $"))
dinero_daniel = float(input("dinero de daniel: S/."))

dolares_daniel = dinero_daniel/3
capital_total = dinero_juan + dinero_rosa + dolares_daniel
porcentaje_juan = (dinero_juan*100)/capital_total
porcentaje_rosa = (dinero_rosa*100)/capital_total
porcentaje_daniel = (dolares_daniel*100)/capital_total

print("el capital total es: $",capital_total)
print("juan dio el",porcentaje_juan,"%")
print("rosa dio el",porcentaje_rosa,"%")
print("daniel dio el",porcentaje_daniel,"%")