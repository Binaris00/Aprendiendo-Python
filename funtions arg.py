#Aprendiendo a usar *arg en una funcion

def suma_arg(*arg):
    print("Loading...")
    
    try:
        resultado = sum(arg)
    except:
        print("Please put the numbers again")
    
question = list(input("What numbers you want to sum? "))

if __name__ == "__main__":
    suma_arg(question)
