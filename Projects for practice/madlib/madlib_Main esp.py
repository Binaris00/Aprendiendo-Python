import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print
print("Bienvenido a mi juego madlib, he cambiado algunas cosas del juego original para que sea mas comodo c:\n Primero, necesito unos pequeños datos sobre ti\n")
print("")
name = input("Cual es tu nombre? ")
objetive = input("Selecciona tu objetivo en el castillo\n Rescatar a la princesa\n Explorar el castillo\n Estas perdido y quieres buscar un lugar para dormir")
luck = input("Super importante, crees que eres alguien con suerte (Si/No)? ")


print(f"{name} entra al castillo y se sorprende de lo grande que es")
print("Se encuentra con que al inicio tiene varias habitaciones a las que puede ir a buscar a alguien")
hab = input()
