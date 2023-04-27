"""
1-Create a decorator that measures the execution time of a function and prints it out. 
Use the time module to calculate the time.

2-Create a decorator that counts the number of times a function has been called and 
prints it out. Use a dictionary to store the counts.

3-Create a decorator that logs the arguments and return values of a function. 
Write the log to a file.

4-Create a decorator that validates the arguments of a function. If the arguments 
are not valid, raise an exception.

5-Create a decorator that retries a function a certain number of times if it fails. 
If the function still fails after the retries, raise an exception.

6-Create a decorator that memoizes a function's output. Use a dictionary to store 
the function's input-output pairs.

7-Create a decorator that limits the rate at which a function can be called. 
Use the time module to calculate the time between calls.

8-Create a decorator that wraps a function in a try-except block. 
If the function raises an exception, print the exception and return a default value.

9-Create a decorator that caches a function's output to disk. Use the pickle module to store the function's input-output pairs.

10-Create a decorator that logs the execution time of a function to a database. Use the sqlite3 module to store the data.
"""


#1-Create a decorator that measures the execution time of a function and prints it out. 
#Use the time module to calculate the time.

import time

def timer(function):
    def wrapper(*args, **kwargs):
        begin = time.time()
        
        func = function(*args, **kwargs)
        print("Example:\n[Late time](Function name) is running correctly")
        
        end = time.time()
        return f"[{begin-end}]{function.__name__} is running correctly"
    return wrapper

@timer
def simple_sum(num_1, num_2):
    return num_1 + num_2

#2-Create a decorator that counts the number of times a function has been called and 
#prints it out. Use a dictionary to store the counts.
def counter(function):
    dictionary = {}
    def wrapper(*args, **kwargs):
        if function.__name__ not in dictionary:
            dictionary[function.__name__] = 1
        else:
            dictionary[function.__name__] += 1
        print(f"{function.__name__} executed {dictionary[function.__name__]} times")
        return function(*args, **kwargs)
    return wrapper

@counter
def resta(num_1, num_2):
    return num_1 - num_2

#3-Create a decorator that logs the arguments and return values of a function. 
#Write the log to a file.

def log_creator(function):
    def wrapper(*args, **kwargs):
        
        file = open("logs.txt", "a")
        func = function(*args, **kwargs)
        log = f"[{time.time()}]{function.__name__} has been executed\nOutput: {func}\n"
        
        file.write(log)
        file.close()
        return log
    return wrapper

@log_creator        
def hello_world():
    return "Hello world"

#4-Create a decorator that validates the arguments of a function. If the arguments 
#are not valid, raise an exception.

def confirmator(function):
    def wrapper(*args, **kwargs):
        if type(function(*args, **kwargs)) != int:
            raise TypeError("You can only add int values")
        else:
            return function(*args, **kwargs)
    return wrapper

@confirmator
def suma_dos(num_1, num_2):
    return num_1 + num_2

print(suma_dos(1, 1))