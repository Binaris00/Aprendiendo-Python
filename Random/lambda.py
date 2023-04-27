#lambda es basicamente una funcion con una sola linea de codigo, esto sirve para no tener tantas funciones que no sean tan cortas
#Ejemplo
def multiplicacion(numero1, numero2):
    return numero1 * numero2
#Esta funcion seria mejor hacerla con un lambda
#Y daria el mismo resultado
lambda numero1, numero2 : numero1 * numero2

(lambda nombre : print("Hola", nombre))("Albert")