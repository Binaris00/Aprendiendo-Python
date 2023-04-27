"""
Polymorphism:
a. Create multiple methods with the same name but different implementations in different classes.
b. Use function or method overloading to automatically call the correct method based on arguments.
c. Use polymorphism to write generic code that works with objects of different classes.
"""

class Person:
    """Class for a Person base
    """
    def accion(self):
        pass

    def birthday(self):
        pass

    def work(self):
        pass

class Man(Person):
    """Class for Man based in Person Class

    Args:
        Person (Class): Base class to make genders or other things I don't know jajajsja
    """
    def __init__(self, name, birthday, work):
        self.name = name
        self.birthday = birthday
        self.work = work
        
    def accion(self):
        return f"Play football :)"

    def birthday(self):
        return f"{self.name} is {self.birthday}"


    def work(self):
        return f"Work: {self.work}"

class Woman(Person):
    def __init__(self, name, birthday, work):
        self.name = name
        self.birthday = birthday
        self.work = work
        
    def accion(self):
        return f"Its time to cook!"

    def birthday(self):
        return f"Omg, is my birthday ({self.birthday})"
    
    def work(self):
        return f"Work: {self.work}"

carlos = Man("Carlos", "13-2-2000", "Astronaut")
maria = Woman("Maria", "23-5-1999", "Mother")

print(carlos.work, carlos.birthday, carlos.accion)