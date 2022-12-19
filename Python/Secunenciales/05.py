import os
os.system ("cls")

gigabytes = int(input("ingrese capacidad de disco en GB: "))

megabytes = gigabytes * 1024
kilobytes = megabytes * 1024
cbytes = kilobytes * 1024

print("la capacidad del disco duro es", gigabytes,"GB")
print("en megabyteses",megabytes,"MB")
print("en kilobytes es",kilobytes,"KB")
print("en bytes es",cbytes,"B")