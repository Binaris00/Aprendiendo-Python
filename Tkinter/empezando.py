import tkinter
from turtle import fillcolor

ventana = tkinter.Tk() #Para ya tener la ventana
# "ventana.geometry("1000x600")" en caso de que quiera ponerle un espacio en especifico

#etiqueta = tkinter.Label(ventana, text = "Ola", bg = "blue")
#etiqueta.pack(fill= tkinter.BOTH, expand = True)
#ventana.mainloop()
#Una etiqueta sin funciones
def saludo():
    print("Ola")

#boton = tkinter.Button(ventana, text = "Presiona :O", padx = 40, pady = 50, command = saludo)
#boton.pack()

Texto = tkinter.Entry(ventana, font = "Helvetica 50")
Texto.pack()

etiqueta2 = tkinter.Label(ventana)
etiqueta2.pack()

def texto_guardado():
    texto20 = Texto.get()
    print(texto20)
    etiqueta2["text"] = texto20

boton1 = tkinter.Button(ventana, text = "Click", command = texto_guardado)
boton1.pack()
ventana.mainloop()