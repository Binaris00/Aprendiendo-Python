#Esto fue para aprender a usar bucles y al final hice un programa medio largo xd
import os

list_pokemon = ["venasaur", "squirtle", "blastoice", "Mew", "Snorlax"]
global respuestas_correctas
respuestas_correctas = 0

for pokemon in list_pokemon:
    print(f"Tu siguiente pokemon sera {pokemon}")
    respuesta = input(f"{pokemon} es debil contra el tipo fuego? S/N \n")

    if pokemon == "venasaur" and respuesta == "S":
        print("Felicidades! has acertado la respuesta")
        respuestas_correctas = respuestas_correctas + 1
    elif pokemon == "squirtle" and respuesta == "N":
        print("Felicidades! has acertado la respuesta")
        respuestas_correctas = respuestas_correctas + 1
    elif pokemon == "blastoice" and respuesta == "N":
        print("Felicidades! has acertado la respuesta")
        respuestas_correctas = respuestas_correctas + 1
    elif pokemon == "Mew" and respuesta == "N":
        print("Felicidades! has acertado la respuesta")
        respuestas_correctas = respuestas_correctas + 1
    elif pokemon == "Snorlax" and respuesta == "N":
        print("Felicidades! has acertado la respuesta")
        respuestas_correctas = respuestas_correctas + 1
    else:
        print("Lo siento, tal vez deberias estudiar un poco mas...")

os.system ("cls")
print("Perfecto! ahora que has acabado el examen vamos a ver cuantas respuestas correctas has tenido...")
if respuestas_correctas >= 3:
    print(f"Felicidades! has aprobado el examen con una nota de {respuestas_correctas}/5")
else:
    print(f"Lo siento... Al parecer debes estudiar mas sobre pokemon nota={respuestas_correctas}/5")
os.getcwd()