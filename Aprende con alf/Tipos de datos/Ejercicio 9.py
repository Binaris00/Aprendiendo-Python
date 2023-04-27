#https://aprendeconalf.es/docencia/python/ejercicios/
#Para consultar las practicas :)
#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

#cantidad = int(input("Que cantidad deseas invertir? "))
#interes = int(input("Que porcentaje de interes tienes"))
#tiempo = int(input("Cuantos años son? "))
#inversion = 0
#contador = 0
#while contador != tiempo:
#    print("Funcionando...")
#    contador = contador +1
#    inversion = cantidad*interes/100

#print("El valor de tu inversion seria igual a:", inversion)
#Metodo que trate de usar pero que no funciono, segun yo diria que el problema fue que no supe como hacerlo en primer lugar :c

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))