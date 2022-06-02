class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self) -> str:
        return"{},{}".format(self.x,self.y)

    def Cuadrante(self,x,y):   
        self.x=x
        self.y=y

        if x>0 and y>0:
            print("El punto se encuentra en el 1er cuadrante")
        elif x>0 and y<0:
            print("El punto se encuentra en el 2do cuadrante")
        elif x<0 and y<0:
            print("El punto se encuentra en el 3er cuadrante")
        elif x<0 and y>0:
            print("El punto se encuentra en el 4to cuadrante")

a = Punto(3,5)
print(a)
a.Cuadrante(3,5)