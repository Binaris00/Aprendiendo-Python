"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max_num(num1, num2):
    """Toma dos ints y devuelve el mayor a ellos
    
    Args:
        num1 (float): Primer valor para analizar
        num2 (float): Segundo valor para analizar
        
    Returns:
        String or float: Resultado de determinar el mayor, dependera de si es igual o si son diferentes num1 y num2 si devolvera un string o un float                       
    """
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    ###
    # En caso de que num1 y num2 sean iguales se pueden retornar dos cosas diferentes
    elif num1 == num2:
        return num1
    # return f"Los dos numeros son iguales, por eso es {num1}"

def max_tres(num1, num2, num3):
    """Devuelve el mayor de tres numeros int o float \n
    Ejemplo
    tenemos x y z
    x > y
    y > z
    por eso es logico pensar que x > y > z
    
    Args:
        num1 (float): primer numero
        num2 (float): segundo numero
        num3 (float): tercer numero

    Returns:
        float or string: devuelve dependiendo si todos son iguales o si son diferentes
    """
    if num1 > num2 > num3:
        return num1
    elif num2 > num1 > num3:
        return num2
    elif num3 > num2 > num1:
        return num3    
    ###
    # En caso de que num1, num2 y num3 sean iguales se pueden retornar dos cosas diferentes
    elif num1 == num2 == num3:
        return num1
    # return f"Los tres numeros son iguales, por eso es {num1}"


"""
Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def fake_len(stringg):
    """Le das una lista o un string y los cuenta y te devuelve la cantidad que tiene \n
    Caso especial: En caso de que no se quiera contar los espacios se usa replace \n
     stringg = stringg.replace(" ", "")\n \n
    Caso especial: en caso de darle a la funcion una lista sin ningun valor devolvera siempre 0
    
    Args:
        stringg (_type_): _description_

    Returns:
        _type_: _description_
    """
    cantidad = 0

    for i in stringg:
        cantidad += 1
    return cantidad


"""
Escribir una función que tome un carácter y devuelva True 
si es una vocal, de lo contrario devuelve False.
"""

def vocal_find(vocal):
    """Toma un string o cualquier texto y te devuelve true si \n
    tiene una vocal y si no tiene una vocal devolvera false \n
    tambien manda true si las vocales son mayusculas

    Args:
        vocal (string): Cade de texto que se pide

    Returns:
        Boolean: Devolvera true o false
    """
    vocal = vocal.lower()
    vocales = ["a", "e", "i", "o", "u"]
    print(vocal)
    for i in vocales:
        if i in vocal:
            return True
    return False

"""
Escribir una función sum() y una función multip() que sumen y 
multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24
"""

def fake_sum(lista):
    """Devuelve la suma de una lista de numeros

    Args:
        lista (list): Lista de numeros

    Returns:
        Float: El resultado de la suma
    """
    resultado = 0
    for i in lista:
        resultado += i
    return resultado

def fake_multip(lista):
    """Devuelve el resultado de la multiplicacion de una lista asignada \n
    Tiene resultado = 1 para no tener problemas en la multiplicacion

    Args:
        lista (list): Lista de numeros

    Returns:
        float: Resultado de la multiplicacion
    """
    resultado = 1
    
    for i in lista:
        resultado = resultado * i 
        
    return resultado


"""
 Definir una función inversa() 
 que calcule la inversión de una cadena. Por ejemplo la cadena 
 "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(texto):
    return texto[::-1]

"""
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(texto):
    """Funcion para un identificar un palindromo \n
    en caso de querer dar True aunque tenga mayusculas usar .lower()

    Args:
        texto (string): Texto para identificar

    Returns:
        boolean: valor para saber si es o no es palindromo
    """
    texto_inverso = texto[::-1]
    if texto_inverso == texto:
        return True
    else:
        return False


"""
Definir una función superposicion() que tome dos listas y 
devuelva True si tienen al menos 1 miembro en común o 
devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    """Determina si de dos listas tienen un numero o palabra similar \n
    (Esta hecho a lo rapido asi que puede que falta algo...)

    Args:
        lista1 (list): 1 lista de valores
        lista2 (list): 2 lista de valores

    Returns:
        Boolean: Devuelve true o false dependiendo si tienen un caracter igual
    """
    for i in lista1:
        for n in lista2:
            if i == n:
                return True
            else:
                pass
    return False
# listan1 = [1, 2, 3, 4, 5]
# listan2 = [6, 7, 3, 9, 10]
# print(superposicion(listan1, listan2))

"""
 Definir una función generar_n_caracteres() 
 que tome un entero n y devuelva el caracter multiplicado 
 por n. Por ejemplo: generar_n_caracteres(5, "x") 
 debería devolver "xxxxx".
"""

def generar_nc_caracteres(n, car):
    """Genera x cantidad de y palabras seleccionadas como parametros

    Args:
        n (int): Cantidad de veces que se repetira 
        car (string): Palabra que se repetira dependiendo de n

    Returns:
        string: la palabra multiplicada por esa cantidad
    """
    new_car = ""
    for i in range(0, n):
        new_car += car
    return new_car

"""
 Definir un histograma procedimiento() que tome una 
 lista de números enteros e imprima un histograma en la 
 pantalla. Ejemplo: procedimiento([4, 9, 7]) debería 
 imprimir lo siguiente:
*
***
"""
