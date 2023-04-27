#Key: d4820958aeb9e75a743277386d34a784
#Pagina: https://api.openweathermap.org/data/2.5/weather?q={city name}
from tkinter import *
import requests
def clima(ciudad):
    API_KEY = "d4820958aeb9e75a743277386d34a784"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_key, "q": ciudad, "units": "metric"}
    response = .requests.get(URL, params = parametros)
    print(response.json()) 
ventana = Tk()
ventana.geometry("350x350")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener clima")
obtener_clima.pack

mostrar_clima = Label(text = "weather", font = ("Courier", 20, "normal"))

ventana.mainloop()