class Vehiculos():
    color = None
    longitud_metros = None
    ruedas = 4

    def arrancar(self):
        print("El vehiculo ha arrancado")

    def detener(self):
        print("El vehiculo se ha detenido")

vehiculo_1 = Vehiculos()
vehiculo_2 = Vehiculos()

vehiculo_2.material_aleron = "Fibra de carbono"
print(vehiculo_2.material_aleron)