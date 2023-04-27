"""
1-What is the difference between a tuple and a list in Python?

2-Define a function in Python that takes two parameters and returns their product.

3-What is the difference between a for loop and a while loop in Python?

4-Define a Python class called "Car" with the following attributes: make, model, year, and color.

5-What is inheritance in OOP and how is it implemented in Python?

6-Define a Python function that takes a list of integers as input and returns the sum of the even numbers in the list.

7-What is polymorphism in OOP and how is it implemented in Python?

8-Define a Python class called "Rectangle" with attributes length and width. Include methods to calculate the area and perimeter of the rectangle.

9-What is encapsulation in OOP and how is it implemented in Python?

10-Define a Python function that takes a string as input and returns a new string with all vowels removed.

11-What is the purpose of the "init" method in a Python class?

12-Define a Python class called "BankAccount" with attributes account number and balance. Include methods to deposit and withdraw money from the account.

13-What is the difference between a local variable and a global variable in Python?

14-Define a Python function that takes a list of strings as input and returns a new list with all the strings in uppercase.

15-What is the purpose of the "self" keyword in a Python class?
"""

# My Answer -CORRECT :D
#1 Tuple is written () and list {}
#  Tuple is not editable and static
#  List is dinamic and editable

#My Answer -CORRECT or not... ChatGPT don't like a put the funtion name "fake_sum" and he say other name
#2
def fake_sum(a, b):
    product = a + b
    return product

#My answer -A litte god and a litte bad...
#3
#Loop is a bucle finite depends about range or a list, and loop write "for i in range(1, 10):"
#While can be infinite depends about the condition, and while "while a == b:"


#4
class Car:
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        pass
#5
# Inheritance is about inherate attributes for a base class to other class, example (Use class Car):
class Ferrari(Car):
    def __init__(self, make, model, year, color, example) -> None:
        super().__init__(make, model, year, color)
        self.example = example

#6
#This task can solved easy with sum() but I make to forms to solved this task

integers_list = [1, 5, 10, 4, 3]

#First option
print(sum(integers_list))

#Second option (without sum())
def good_sum(random_list):
    result = 0
    for n in random_list:
        result += n
    return result
print(good_sum(integers_list))


#7
#Is about re-use methods definited in base class, example with Car class
class Guchi(Car):
    def info(self):
        return f"{self.make}, {self.model}, {self.year}, {self.color}"


# 8

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length*self.width
    
    def get_perimeter(self):
        return 2*self.length+2*self.width

# 9
#Its a practice in OOP abot private or restringed a variable in a class

class Car_Private:
    def __init__(self, make, model, year, private1, private2):
        self.make = make
        self.model = model
        self.year = year
        self._private1 = private1
        self.__private2 = private2
        
# 10
def hate_vowels(sentence):
    sentence = sentence.lower()
    vocals = ["a", "e", "i", "o", "u"]
    for vol in vocals:
        if vol in sentence:
            sentence = sentence.replace(vol, "")
    return sentence
print(hate_vowels("Hola"))

# 11
#__init__ means when I created a class and I create a method with the name __init__ the method run fitrs


#12

class BankAccount:
    def __init__(self, account_number, balance) -> None:
        self.account_number = account_number
        self.balance = balance
    
    def deposit_money(self, quantity):
        self.balance += quantity
        return f"now your balance is: {self.balance}"    
    
    def withdraw_money(self, quantity):
        self.balance -= quantity
        return f"now your balance is: {self.balance}"    

# 13
# Local variable is a variables used in a funtion and deleted when the funtion finishes
# Global variables can be used to change and edit in multiple funtions, and the keyword is "Global Variable"


# 14

def list_upper():
    string_list = []
    
    for i in range(10):
        string = input("New string: ")
        string = string.upper()
        string_list.append(string)
    return string_list

print(list_upper())


# 15
# self is a keyword used in OOP to used to create objects