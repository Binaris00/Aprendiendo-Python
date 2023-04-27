class Vehiculos():

    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas
    def arrancar(self):
        print("El vehiculo ha arrancado")

    def detener(self):
        print("El vehiculo se ha detenido")


vehiculo_1 = None
vehiculo_1 = Vehiculos("azul", 4, 4)