print("***********")
print("CALCULADORA")
print("***********\n")


print("MENU DE OPCIONES")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division Entera")
print("6. Exponente")
print("7. Modulo o Resto\n")

opcion = int(input("Digite el numero de la operacion a realizar: "))

if opcion == 1:
    print("\nHa elegido Suma\n")
    numero = int(input("\nDigite el primer valor: "))
    numero += int(input("\nDigite el segundo valor: "))
    print("\nEl resultado de la suma es " + str(numero))
elif opcion == 2:
    print("\nHa elegido Resta\n")
    numero = int(input("\nDigite el primer valor"))
    numero -= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la resta es " + str(numero))
elif opcion == 3:
    print("\nHa elegido Multiplicacion\n")
    numero = int(input("\nDigite el primer valor"))
    numero *= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la multiplicacion es " + str(numero))
elif opcion == 4:
    print("\nHa elegido Division\n")
    numero = int(input("\nDigite el primer valor"))
    numero /= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la division es " + str(numero))
elif opcion == 5:
    print("\nHa elegido Division Entera\n")
    numero = int(input("\nDigite el primer valor"))
    numero //= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la division entera es " + str(numero))
elif opcion == 6:
    print("\nHa elegido Exponente\n")
    numero = int(input("\nDigite el primer valor"))
    numero **= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la multiplicacion exponencial es " + str(numero))
elif opcion == 7:
    print("\nHa elegido Modulo o Resto\n")
    numero = int(input("\nDigite el primer valor"))
    numero %= int(input("\nDigite el segundo valor"))
    print("\nEl resultado de la modulo o resto es " + str(numero))

else:
    print("Opcion no disponible")
print("")
print("Fin")
    
    


