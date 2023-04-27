"""
Classes and Objects:
a. Create a class to represent a real-world object, like a bank account, car, or person.
b. Implement the init method to initialize the object's attributes.
c. Add methods to perform actions with the object.
d. Create multiple objects of the same class and manipulate them.
"""

class Planet:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
        
    def information(self):
        return f"{self.name}, {self.color}, {self.size}"
    
    def pretty(self):
        return f"{self.name} pretty!!"
    
earth = Planet("Earth", "Green, Blue", 128.2)
mars = Planet("Mars", "Red", 1124)
venus = Planet("Venus", "Blue", 1212)

print(earth.pretty(), earth.information())

"""
    def change_size(self, quantity):
        self.size -= quantity

print(mars.pretty(), mars.information())
print(venus.pretty(), venus.information())
print(earth.change_size(10))
"""