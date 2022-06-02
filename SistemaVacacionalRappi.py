print("***************************")
print("SISTEMA VACACIONAL DE RAPPI")
print("***************************\n")

nombre = input("Bienvenido, ingrese su nombre:")

print("\n1. Atencion al cliente")
print("2. Logistica")
print("3. Gerencia")
clave = int(input("Digite el numero del area a la cual pertenece:"))
if clave == 1:
    area = "atencion al cliente"
elif clave == 2:
    area = "logistica"
elif clave == 3:
    area = "gerencia"
else:
    print("Opcion no disponible")

edad = int(input("\nDigite su tiempo de servicio en anos:"))
print("")

if clave == 1 and edad == 1 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 6 dias de vacaciones")
elif clave == 1 and edad <=6 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 14 dias de vacaciones")
elif clave == 1 and edad >=7 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 20 dias de vacaciones")
elif clave == 2 and edad == 1 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 7 dias de vacaciones")
elif clave == 2 and edad <= 6 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 15 dias de vacaciones")
elif clave == 2 and edad >= 7 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 22 dias de vacaciones")
elif clave == 3 and edad == 1 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 10 dias de vacaciones")
elif clave == 3 and edad <= 6 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 20 dias de vacaciones")
elif clave == 3 and edad >= 7 :
    print(nombre + " quien trabaja en el area de " + area + " Usted tiene derecho a 30 dias de vacaciones")

print("")

print("Fin")





