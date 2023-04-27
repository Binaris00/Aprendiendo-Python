"""
1-Create a class called Rectangle that has a constructor which takes two 
arguments width and height. The class should have a method called area which returns the area of the rectangle.

2-Create a subclass called Square that inherits from the Rectangle class. 
The Square class should have a constructor that takes a single argument side, 
which is used to set both the width and height of the square. The Square class 
should also override the area method to correctly calculate the area of a square.

3-Create a class called Person that has a constructor which takes 
two arguments name and age. The class should have a method called 
introduction which prints a message introducing the person by name and age.

4-Create a class called Student that inherits from the Person class. 
The Student class should have a constructor that takes three arguments: 
name, age, and student_id. The Student class should override the introduction method to 
include the student's ID in the introduction message.

5-Create a class called BankAccount that has a constructor which takes a 
single argument balance. The class should have methods called deposit and 
withdraw which allow deposits and withdrawals to the account. The class 
should also have a __str__ method that returns a string representation of the account balance.
"""


#-1
class rectangle():
    """Class for find the area and with tho parameters
    """
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        """find the area

        Returns:
            float: area
        """
        return self.width*self.height

#-2
class square(rectangle):
    def __init__(self, side: float) -> None:
        self.side = side
    
    def area(self):
        return self.side*self.side

#-3
class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def introduce_yourself(self):
        return f"Hi my name is {self.name} and my age is {self.age}"

#-4 
class student(Person):
    def __init__(self, name, age, student_id) -> None:
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce_yourself(self):
        return f"Hi, I am a student, my name is {self.name}, my age is {self.age} and my student id is {self.student_id}"

#-5
class balance():
    def __init__(self, balance) -> None:
        self.balance = balance
    
    def withdraw(self, quantity):
        self.balance -= quantity
        return self.balance
    
    def deposit(self, quantity):
        self.balance += quantity
        return self.balance
    def __str__(self) -> str:
        return f"My balance is {self.balance}"