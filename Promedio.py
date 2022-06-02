nombre = input("Ingresa tu nombre ")
matematicas = float((input(nombre + " cual es tu calificacion en matematicas?")))
quimica = float((input(nombre + " cual es tu calificacion en quimica?")))
biologia = float((input(nombre + " cual es tu calificacion en biologia?")))

promedio = (matematicas + quimica + biologia)/3

if promedio >= 3:
    print("Felicitaciones " + nombre + " has aprobado con un promedio de " + str(promedio))
else :
    print("Lo siento " + nombre + " no has aprobado, tu promedio fue " + str(promedio))

    

print("Fin")

    

    
