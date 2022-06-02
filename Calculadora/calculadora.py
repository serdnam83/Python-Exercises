# funciones backend
def borrar():
	n1.set("")
	n2.set("")
	r.set("")
	

def sumar():
	r.set(float(n1.get())+float(n2.get()))
	

def restar():
	r.set(float(n1.get())-float(n2.get()))

def multiplicar():
	r.set(float(n1.get())*float(n2.get()))

def dividir():
	r.set(float(n1.get())/float(n2.get()))


# estuctura del formulario
from cgitb import text
from textwrap import fill
from tkinter import *
from tokenize import Floatnumber
root = Tk()
root.title("Calculadora")
root.resizable(1,1)

miFrame = Frame(root, bg="#6CABDD", borderwidth=2, relief="raised", padx=10, pady=10)
miFrame.pack(fill='both')

n1=StringVar()
n2=StringVar()
r=StringVar()
labelN1 = Label(miFrame, justify="center", text="NUMERO 1")
labelN1.grid(row=0, column=2, padx=5, pady=5)

inN1 = Entry(miFrame, justify = "center", textvariable = n1)
inN1.grid(row = 1, column = 2, padx = 5, pady = 5)

labelN2 = Label(miFrame, justify="center", text="NUMERO 2")
labelN2.grid(row=2, column=2, padx=5, pady=5)

inN2 = Entry(miFrame, justify = "center", textvariable = n2)
inN2.grid(row = 3, column = 2, padx = 5, pady = 5)

labelR = Label(miFrame, justify="center", text="RESULTADO")
labelR.grid(row=4, column=2, padx=5, pady=5)

inR = Entry(miFrame, state="disabled", justify = "center", textvariable = r)
inR.grid(row = 5, column = 2, padx = 5, pady = 5)

Button(miFrame, text="Sumar", command=sumar).grid(row=6, column=1)
Button(miFrame, text="Restar", command=restar).grid(row=6, column=2)
Button(miFrame, text="multiplicar", command=multiplicar).grid(row=6, column=3)
Button(miFrame, text="Dividir", command=dividir).grid(row=6, column=4)
Button(miFrame, text="Borrar", command=borrar).grid(row=6, column=5)


root.mainloop()


