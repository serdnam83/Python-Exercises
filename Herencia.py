class vehiculos(object):
	"""docstring for vehiculos"""
	def __init__(self, marca, modelo):
		
		self.marca = marca  #self. siempre dentro del constructor
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False	
		
	def arrancar(self):
		self.enMarcha = True

	def acelerar(self):
		self.acelera = True

	def frena(self):
		self.frena = True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
			"\nEn Marcha: ", self.enMarcha, "\nAcelerar: ", self.acelera,
			"\nFrenar: ", self.frena)
		

class Moto(vehiculos):

	hcaballito = ""
	
	def caballito(self):
		self.hcaballito = "Voy haciendo caballito"
	
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, 
			"\nEn Marcha: ", self.enMarcha, "\nAcelerar: ", self.acelera,
			"\nFrenar: ", self.frena, "\nHaciendo caballito: ", self.hcaballito)
				


class furgoneta(vehiculos):

	def cargar(self, cargado):
		self.carga = cargado
		if (self.carga):
			return "La furgoneta esta caargada"

		else:
			return "La furgoneta esta descargada"

		

miCarro = vehiculos("Volkswagen", "Golf")
miCarro.estado()

print("\n")

miMoto = Moto("Honda", "CBR")
miMoto.estado()	

print("\n")

miFurgoneta = furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.cargar("cargado"))





	