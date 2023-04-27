class American_Motocicletas():
    estado_de_uso = "Nuevo"
    motor = False #Detenido

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_de_fabricacion, velocidad_punta, peso, precio):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_de_fabricacion = fecha_de_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.precio = precio
    def arrancar(motor):
        if motor is False:
            print("El motor ha arrancado.")
    def detener(motor):
        if motor is True:
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba encendido")
cliente = American_Motocicletas("rojo", "123483461904", 10, 2, "american motos", "modelo rojo vino", "11/23/00", 1, "1283kg")
cliente_1 = American_Motocicletas(
    matricula= "123123214",
    combustible_litros=0,
    color="Negra",
    marca="Si",
    modelo="fa",
    peso=121312321,
    fecha_de_fabricacion="12/4/22012",
    velocidad_punta=21394,
    numero_ruedas=9,
    precio=1797788,
)
print(f"El precio de la motocicleta {cliente_1.marca}{cliente_1.modelo}tiene un precio de {cliente_1.precio}")
cliente_1.precio = 1243
cliente_1.detener()