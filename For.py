print("******************************")
print("PROGRAMA PARA VERIFICAR E-MAIL")
print("******************************\n")

email = str(input("Ingrese su e-mail: "))

condicion = False

for i in email:
	if i == "@":
		condicion = True

if condicion == True:
	print("\nEl e-mail es correcto")

else:
	print("\nEl e-mail es incorrecto")

mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio'] 
for nombre in mi_lista: 
    print(nombre)


for i in range (2001, 2010):
    	print("Informes del anio " + str(i))


for i in range (5, 50, 5):
	print("El valor de la variable i es " + str(i))

