from ast import If
from email import message
from gettext import install
from re import I
from select import select
import sys
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox
root=Tk()
root.title("Mi Editor")

ruta=""

def nuevo():
    mensaje.set("Nuevo fichero")
    texto.delete(1.0,END)  #el primer parametro es un salto

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta=FileDialog.askopenfilename(initialdir=".",
        filetypes=(("Ficheros de texto","*.txt"),),
        title="Abrir un fichero"
    )

    if ruta != "":
        fichero=open(ruta,"r")
        contenido=fichero.read()
        texto.delete(1.0,END)
        texto.insert("insert",contenido)
        fichero.close()
        root.title(ruta+" Mi Editor")
    root.title("Mi Editor")
    ruta=""

def guardar():
    global ruta

    if ruta !="":        
        contenido=texto.get(1.0,"end")
        fichero=open(ruta,"w+")
        fichero.write(contenido)
        fichero.close
        mensaje.set("Fichero guardado con exito")
    
    else:
        guardarComo()

def guardarComo():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero=FileDialog.asksaveasfile(title="Guardar fichero", 
    mode="w",defaultextension=".txt")

    if fichero is not None:
        ruta=fichero.name
        contenido=texto.get(1.0,"end-1c")
        fichero=open(ruta,"w+")
        fichero.write(contenido)
        fichero.close
        mensaje.set("Fichero guardado con exito")
    
    else:
        mensaje.set("Guardado cancelado")
        ruta=""

def salir():
    global ruta
        
    if ruta != "":
        sys.exit()
    
    else:
        resultado=messagebox.askquestion("Salir",
        "Desea guardar los cambios antes de salir?")

        if resultado == "yes":
            guardar()
            sys.exit()

def copiar():
    root.clipboard_clear()
    root.clipboard_append(texto.get(1.0,END))

def cortar():
    root.clipboard_clear()
    root.clipboard_append(texto.get(1.0,END))
    texto.delete(1.0,END)

def pegar():
    paste=root.clipboard_get()
    texto.insert("insert",paste)

#Menu superior
menubar=Menu(root)  #creamos la barra de menu
filemenu=Menu(menubar)  #creamos un submenu
menubar.add_cascade(label="Archivo",menu=filemenu)  #le damos nombre al submenu
filemenu.add_command(label="Nuevo",command=nuevo)  #agregamos comandos al submenu
filemenu.add_command(label="Abrir",command=abrir)
filemenu.add_command(label="Guardar",command=guardar)
filemenu.add_command(label="Guardar como",command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=salir)

editmenu=Menu(menubar)
menubar.add_cascade(label="Editar",menu=editmenu)
editmenu.add_command(label="Copiar",command=copiar)
editmenu.add_command(label="Cortar",command=cortar)
editmenu.add_command(label="Pegar",command=pegar)

helpmenu=Menu(menubar)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Ayuda")
helpmenu.add_command(label="Acerca de...")

#Caja de texto central
texto=Text(root)
texto.pack(fill="both", expand=1)
texto.config(padx=6, pady=6, bd=0, font=("Consoloas", 12))

#Monitor inferior
mensaje=StringVar()
mensaje.set("Bienvenido a Mi Editor")
monitor=Label(root, justify="left", textvar=mensaje)
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()



