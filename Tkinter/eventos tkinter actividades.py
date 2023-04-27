from tkinter import *

root = Tk()
root.title("Events tkinter")

"""Button(root, text="Boton 1", command = lambda : Label(root, text="Boton 1 pulsado").pack()).pack()
Button(root, text="Boton 2", command = lambda : Label(root, text="Boton 2 pulsado").pack()).pack()
Button(root, text="Boton 3", command = lambda : Label(root, text="Boton 3 pulsado").pack()).pack()
Button(root, text="Boton 4", command = lambda : Label(root, text="Boton 4 pulsado").pack()).pack()"""

Label(root, text="Nombre:").grid(row = 0, column =0)
Label(root, text="Edad:").grid(row = 1, column =0)
Label(root, text="Nacimiento:").grid(row = 2, column =0)

nombre_entry = Entry(root)
nombre_entry.grid(row = 0, column =1)
edad_entry = Entry(root)
edad_entry.grid(row = 1, column=1)
nacimiento_entry = Entry(root)
nacimiento_entry.grid(row = 2, column=1)

def nombre_edad():
    nombre_texto = nombre_entry.get()
    edad_texto = edad_entry.get()
    nacimiento_texto = nacimiento_entry.get()
    Label(root, text=f"Tu nombre es {nombre_texto}, tu edad es {edad_texto} y tu nacimiento es el {nacimiento_texto}").grid(row = 4, column =1)

Button(root, text="Presioname! :D", command= nombre_edad).grid(row = 3, column =1)
root.mainloop()