#In this example we save a funtion in a variable

def suma(number_1, number_2):
    return number_1 + number_2

variable = suma
print(variable(1, 1))

def operacion(x):
    def mucha_suma(y):
        return x+y
    return mucha_suma

operacion_variable = operacion(1)
print(operacion_variable(1))


#Now in this example we use a decorator to view the "effiency for any funtion"
import time
def efficiency_viewer(funtion):
    def wrapper(*args, **kwargs):
        begin = time.time()
        
        result = funtion(*args, **kwargs)
        
        end = time.time()
        
        print(f"The funtion called: {funtion.__name__} late {begin-end} to run")
        return result
    return wrapper

@efficiency_viewer
def calculator(num1, num2):
    result = num1 + num2
    return result

print(calculator(1, 1))