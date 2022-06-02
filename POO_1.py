class coche(): #sintaxis de la clase

	def __init__(self): #sintaxis del cosntructor

		self.__largoChasis=250  #__sintaxis de encapsulacion
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	def arrancar(self):
		self.enMarcha=True

	def estado(self):
		if (self.enMarcha):
			`

			
miCoche=coche()

print("El largo del coche es: " + miCoche.largoChasis)
print("El coche tiene " + miCoche.ruedas + "ruedas")
miCoche.arrancar()

print(miCoche.estado())
