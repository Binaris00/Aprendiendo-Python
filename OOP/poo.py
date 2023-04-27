class computadoras():
    monitor = "Monitor DELL 1928k"
    teclado = "Teclado DELL 1928k"
    mouse = "Mouse DELL 1928k"
    def __init__(self, procesador, tarjeta_grafica, fuente_poder, gabinete):
        self.procesador = procesador
        self.tarjeta_grafica = tarjeta_grafica
        self.fuente_poder = fuente_poder
        self.gabinete = gabinete


cliente = computadoras(
    tarjeta_grafica = "GTX199999",
    procesador = "Ryzen 9870k",
    gabinete = "gigaearth 65",
    fuente_poder = "FullPower12 blue",
)
