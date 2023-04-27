import random
print()
def fibonacci_arr(number):
    """This function find the fibonacci serie and save in a array

    Args:
        number int: number max to find

    Returns:
        list: All fibonacci serie
    """
    array = [0, 1]
    a, b = 0, 1
    while a < number:
        a, b = b, a+b
        array.append(b)
    return array

def fibonacci_printer(number):
    """This function print the fibonacci serie 1 in 1

    Args:
        number int: number max to find
    """
    array = [0, 1]
    a, b = 0, 1
    print(0)
    print(1)
    while a < number:
        a, b = b, a+b
        array.append(b)
        print(b)
        
print(fibonacci_printer(100))