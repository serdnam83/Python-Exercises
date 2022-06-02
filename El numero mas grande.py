print("*****************************")
print("CUAL ES EL NUMERO MAS GRANDE?")
print("*****************************\n")

numero_1 = int(input("Digite el primer numero: "))
numero_2 = int(input("Digite el segundo numero: "))
numero_3 = int(input("Digite el tercer numero: "))
print("")

if numero_1 > numero_2 and numero_1 > numero_3:
    print("El numero " + str(numero_1) + " es el mas grande de los tres")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("El numero " + str(numero_2) + " es el mas grande de los tres")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print("El numero " + str(numero_3) + " es el mas grande de los tres")
else:
    print("Datos invalidos")

print("")
print("Fin")
