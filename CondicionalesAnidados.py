print("*********")
print("CONVERSOR")
print("*********\n")

print("Menu de opciones:")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero.\n")

seleccion = int(input("Cual es tu opcion deseada?:"))

if seleccion == 1:
    print("\nConversor de numero a palabra\n")
    dato1 = int(input("Cual es el numero que quieres convertir a palabra?"))
    if dato1 <= 10:
        if dato1 == 1:
            print("El numero es 'UNO'")
        elif dato1 == 2:
            print("El numero es 'DOS'")
        elif dato1 == 3:
            print("El numero es 'TRES'")
        elif dato1 == 4:
            print("El numero es 'CUATRO'")
        elif dato1 == 5:
            print("El numero es 'CINCO'")
        elif dato1 == 6:
            print("El numero es 'SEIS'")
        elif dato1 == 7:
            print("El numero es 'SIETE'")
        elif dato1 == 8:
            print("El numero es 'OCHO'")
        elif dato1 == 9:
            print("El numero es 'NUEVE'")
        elif dato1 == 10:
            print("El numero es 'DIEZ'")
    else:
        print("Numero no registrado")
elif seleccion == 2:
    print("\nConversor de palabra a numero\n")
    dato2 = str(input("Cual es la palabra que quieres convertir a numero?"))
    if dato2 == "uno":
        print("El numero es '1'")
    elif dato2 == "dos":
        print("El numero es '2'")
    elif dato2 == "tres":
        print("El numero es '3'")
    elif dato2 == "cuatro":
        print("El numero es '4'")
    elif dato2 == "cinco":
        print("El numero es '5'")
    elif dato2 == "seis":
        print("El numero es '6'")
    elif dato2 == "siete":
        print("El numero es '7'")
    elif dato2 == "ocho":
        print("El numero es '8'")
    elif dato2 == "nueve":
        print("El numero es '9'")
    elif dato2 == "diez":
        print("El numero es '10'")
    else:
        print("El numero seleccionado no esta registrado")
    
else:
    print("Opcion no disponible")
    
print("Fin")
    
    
    
        
        
        
        
    
    
    
