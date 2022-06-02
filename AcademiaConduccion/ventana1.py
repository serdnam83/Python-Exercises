from tkinter  import *
root = Tk()
root.title("FACILITO")
root.iconbitmap()
root.resizable(0,0) 
root.config(bg = "blue")

frame = Frame(root, bg = "#6CABDD", width = 800, height = 600) 
frame.pack() 
frame.config(cursor = "arrow")

label1 = Label(root, text = "BIENVENIDO A NUESTRO FACILITADOR EN LINEA")
label1.pack()
#label1.grid(row = 0, column = 2, sticky = "w")
label1.config(bg = "#6CABDD", fg = "white",font = ("Calibri", 24))

nombre = StringVar()
apellido = StringVar()
documento = StringVar()

labelNombre = Label(frame, text = "Nombre")
labelNombre.grid(row = 2, column = 0, sticky = "w", padx = 5, pady = 5)

entryNombre = Entry(frame, justify = "center", textvariable = nombre)
entryNombre.grid(row = 2, column = 1, sticky = "w", padx = 5, pady = 5)


labelApellido = Label(frame, text = "Apellido")
labelApellido.grid(row = 4, column = 0, sticky = "w", padx = 5, pady = 5)

entryApellido = Entry(frame, justify = "center", textvariable = apellido)
entryApellido.grid(row = 4, column = 1, sticky = "w", padx = 5, pady = 5)

labelDocumento = Label(frame, text = "N° de documento")
labelDocumento.grid(row = 6, column = 0, sticky = "w", padx = 5, pady = 5)

entryDocumento = Entry(frame, justify = "center", textvariable = documento)
entryDocumento.grid(row = 6, column = 1, sticky = "w", padx = 5, pady = 5)

def ingresar():
	pass

botonIngresar = Button(frame, text = "Ingresar", font = ("Calibri", 18))
botonIngresar.grid(row = 8, column = 1, padx = 5, pady = 5)

root.mainloop() 
