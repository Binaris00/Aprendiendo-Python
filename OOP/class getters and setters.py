"""
This is a god menu about dogs because I don't have imagination for thing another idea for this program :)
"""

class menu_dog:
    def __init__(self, name, age, created):
        self.__name = name
        self.__age = age
        self.__created = created

    #@Getter
    def get_name(self):
        return self.__name

    #@Setter
    def set_created(self, new_created):
        self.__created = new_created
        return new_created

strange_dog = menu_dog("Hi", 1, "God")
print(strange_dog.get_name())
print(strange_dog.set_created("My"))