def funtion_upper(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

def spliter(function):
    def wrapper():
        func = function()
        splited = func.split()
        return splited
    return wrapper

@spliter
@funtion_upper
def printer():
    return "Hi brother!"

print(printer())
