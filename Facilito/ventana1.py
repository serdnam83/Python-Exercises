#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk 

class Aplicacion():

    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x200")
        self.root.configure(bg="#6CABDD")
        self.root.resizable(width=False,height=False)
        self.root.title("Facilitador de tramites de transito")
        self.root.mainloop()

def main():
    miApp=Aplicacion()
    return 0

if __name__=="__main__":
    main()


