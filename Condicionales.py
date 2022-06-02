print("********************************")
print("PROGRAMA PARA VERIFICAR SALARIOS")
print("********************************\n")

salario_presidente = int(input("Ingrese el salario del presidente: "))
print("El salario del presidente es " + str(salario_presidente))

salario_director = int(input("\nIngrese el salario del director: "))
print("El salario del director es " + str(salario_director))

salario_contador = int(input("\nIngrese el salario del contador: "))
print("El salario del contador es " + str(salario_contador))

salario_administrativo = int(input("\nIngrese el salario del administrativo: "))
print("El salario del administrativo es " + str(salario_administrativo))

if salario_administrativo < salario_contador < salario_director < salario_presidente:
	print("\nTodo en orden")
else:
	print("\nAlgo huele mal")