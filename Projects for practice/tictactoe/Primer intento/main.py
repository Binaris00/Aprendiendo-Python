import time as tm
import random as rd

print("Bienvenido! este juego fue hecho con el proposito de ser SOLO UNA PRACTICA AAAAAAAAAAAAAAAAA")

jugadores = ["Jugador", "Robot"]
lineas = "---------------"
cuadro_1 = "# * #"
cuadro_2 = "# * #"
cuadro_3 = "# * #"
cuadro_4 = "# * #"
cuadro_5 = "# * #"
cuadro_6 = "# * #"
cuadro_7 = "# * #"
cuadro_8 = "# * #"
cuadro_9 = "# * #"

def aleatorio():
    print("Veamos quien empieza primero...")
    global seleccion_aleatoria
    seleccion_aleatoria = rd.choice(jugadores)
    print(f"Empieza primero el {seleccion_aleatoria}")
aleatorio()

def tablero():
    global cuadro_1
    global cuadro_2
    global cuadro_3
    global cuadro_4
    global cuadro_5
    global cuadro_6
    global cuadro_7
    global cuadro_8
    global cuadro_9

    if respuesta_cuadro == "1j":
        cuadro_1 = "# X #"
    elif respuesta_cuadro == "2j":
        cuadro_2 = " X #"
    elif respuesta_cuadro == "3j":
        cuadro_3 = " X #"
    elif respuesta_cuadro == "4j":
        cuadro_4 = "# X #"
    elif respuesta_cuadro == "5j":
        cuadro_5 = " X #"
    elif respuesta_cuadro == "6j":
        cuadro_6 = " X #"
    elif respuesta_cuadro == "7j":
        cuadro_7 = "# X #"
    elif respuesta_cuadro == "8j":
        cuadro_8 = " X #"
    elif respuesta_cuadro == "9j":
        cuadro_9 = " X #"
    elif respuesta_cuadro == "1r":
        cuadro_1 = "# O #"
    elif respuesta_cuadro == "2r":
        cuadro_2 = " O #"
    elif respuesta_cuadro == "3r":
        cuadro_3 = " O #"
    elif respuesta_cuadro == "4r":
        cuadro_4 = "# O #"
    elif respuesta_cuadro == "5r":
        cuadro_5 = " O #"
    elif respuesta_cuadro == "6r":
        cuadro_6 = " O #"
    elif respuesta_cuadro == "7r":
        cuadro_7 = "# O #"
    elif respuesta_cuadro == "8r":
        cuadro_8 = " O #"
    elif respuesta_cuadro == "9r":
        cuadro_9 = " O #"
 
def revisar_victoria():
    global victoria
    if cuadro_1 == "# X #" and cuadro_2 == "# X #" and cuadro_3 == "# X #":
        victoria = "Jugador"
    elif cuadro_4 == "# X #" and cuadro_5 == "# X #" and cuadro_6 == "# X #":
        victoria = "Jugador"
    elif cuadro_7 == "# X #" and cuadro_8 == "# X #" and cuadro_9 == "# X #":
        victoria = "Jugador"
    elif cuadro_1 == "# X #" and cuadro_4 == "# X #" and cuadro_7 == "# X #":
        victoria = "Jugador"
    elif cuadro_2 == "# X #" and cuadro_5 == "# X #" and cuadro_8 == "# X #":
        victoria = "Jugador"
    elif cuadro_3 == "# X #" and cuadro_6 == "# X #" and cuadro_9 == "# X #":
        victoria = "Jugador"
    elif cuadro_1 == "# X #" and cuadro_5 == "# X #" and cuadro_9 == "# X #":
        victoria = "Jugador"
    elif cuadro_3 == "# X #" and cuadro_5 == "# X #" and cuadro_7 == "# X #":
        victoria = "Jugador"

    if cuadro_1 == "# O #" and cuadro_2 == "# O #" and cuadro_3 == "# O #":
        victoria = "Robot"
    elif cuadro_4 == "# O #" and cuadro_5 == "# O #" and cuadro_6 == "# O #":
        victoria = "Robot"
    elif cuadro_7 == "# O #" and cuadro_8 == "# O #" and cuadro_9 == "# O #":
        victoria = "Robot"
    elif cuadro_1 == "# O #" and cuadro_4 == "# O #" and cuadro_7 == "# O #":
        victoria = "Robot"
    elif cuadro_2 == "# O #" and cuadro_5 == "# O #" and cuadro_8 == "# O #":
        victoria = "Robot"
    elif cuadro_3 == "# O #" and cuadro_6 == "# O #" and cuadro_9 == "# O #":
        victoria = "Robot"
    elif cuadro_1 == "# O #" and cuadro_5 == "# O #" and cuadro_9 == "# O #":
        victoria = "Robot"
    elif cuadro_3 == "# O #" and cuadro_5 == "# O #" and cuadro_7 == "# O #":
        victoria = "Robot"

def juego():
    victoria =None
    turnos_contador = 1
    global respuesta_cuadro
    if seleccion_aleatoria == "Jugador":
        while victoria != "Jugador" or victoria != "Robot":
            print("Tu turno!")
            print(f"Turno {turnos_contador}")
            print(f"{lineas}\n{cuadro_1}{cuadro_2}{cuadro_3}\n{cuadro_4}{cuadro_5}{cuadro_6}\n{cuadro_7}{cuadro_8}{cuadro_9}")
            respuesta_cuadro = str(input("Que cuadro deseas seleccionar? \n"))
            respuesta_cuadro = respuesta_cuadro + "j"
            turnos_contador = turnos_contador +1
            tablero()
            revisar_victoria()

            print("Turno del robot")
            print(f"Turno {turnos_contador}")
            print(f"{lineas}\n{cuadro_1}{cuadro_2}{cuadro_3}\n{cuadro_4}{cuadro_5}{cuadro_6}\n{cuadro_7}{cuadro_8}{cuadro_9}")
            print("Que opcion eligira el robot? mmmm")
            tm.sleep(2)
            respuesta_cuadro = str(rd.randint(1,9))
            respuesta_cuadro = respuesta_cuadro + "r"
            turnos_contador = turnos_contador +1
            tablero()
            revisar_victoria()
        if victoria == "Jugador":
            print("Felicidades has ganado!!!")
        else:
            print("Lo lamento, mejor suerte para la proxima.")
    if seleccion_aleatoria == "Robot":
        while victoria != "Jugador" or victoria != "Robot":
            print("Turno del robot")
            print(f"Turno {turnos_contador}")
            print(f"{lineas}\n{cuadro_1}{cuadro_2}{cuadro_3}\n{cuadro_4}{cuadro_5}{cuadro_6}\n{cuadro_7}{cuadro_8}{cuadro_9}")
            print("Que opcion eligira el robot? mmmm")
            tm.sleep(2)
            respuesta_cuadro = str(rd.randint(1,9))
            respuesta_cuadro = respuesta_cuadro + "r"
            turnos_contador = turnos_contador +1
            tablero()

            print("Tu turno!")
            print(f"Turno {turnos_contador}")
            print(f"{lineas}\n{cuadro_1}{cuadro_2}{cuadro_3}\n{cuadro_4}{cuadro_5}{cuadro_6}\n{cuadro_7}{cuadro_8}{cuadro_9}")
            respuesta_cuadro = str(input("Que cuadro deseas seleccionar? \n"))
            respuesta_cuadro = respuesta_cuadro + "j"
            turnos_contador = turnos_contador +1
            tablero()

juego()