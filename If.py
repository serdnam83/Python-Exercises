def evaluacion(nota):
	valoracion = "Aprobado"
	if nota <= 3:
		valoracion = "Reprobado"
	return valoracion

print(evaluacion(5))

