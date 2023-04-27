"""
This is a simple practice about iterables in python, I 
learn about iter(), __iter__, __next__ and how to use them, I didn't create a for loop because I now know how to use them.
"""

name = "Albert"
name_iterable = iter(name)

print(next(name_iterable))
print(next(name_iterable))
print(next(name_iterable))
print(next(name_iterable))
print(next(name_iterable))
print(next(name_iterable))

class names():
    def __iter__(self):
        self.number = 1
        return self
    
    def __next__(self):
        x = self.number
        self.number += 1
        return x

object_variable = names()
object_iterable = iter(object_variable)

print(next(object_iterable))
print(next(object_iterable))
print(next(object_iterable))
print(next(object_iterable))
print(next(object_iterable))