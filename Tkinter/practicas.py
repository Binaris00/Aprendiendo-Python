from tkinter import *
root = Tk()
entrada = Entry(root, width=35)
entrada.grid(row=0)

def envia_boton():
   ventana_nueva1 = Toplevel()
   ventana_nueva1.geometry("400x200")
   ventana_nueva1.title("Ventana secundaria")
   valor_entrada = entrada.get()
   etiqueta = Label(ventana_nueva1,
                    text="El valor introducido en la ventana principal es: " + valor_entrada).grid(row=0)

envia = Button(root, text="Enviar", command=envia_boton).grid(row=1)
root.mainloop()