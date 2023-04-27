"""
7-Write a list comprehension to create a list of the first letter of each word in a given sentence.

8-Write a generator expression to generate the squares of numbers from 1 to 10.

9-Write a list comprehension to create a list of all the vowels in a given word.

10-Write a generator expression to generate the running total of numbers from 1 to 10.
"""

def generator_printer(function):
   def wrapper(*args, **kwargs):
      func = function(*args, **kwargs)
      for i in func:
         print(i)
   wrapper()

lista = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

list_comprehension_square = [x*x for x in lista]
"""1-Write a list comprehension to create a list of squares of even numbers from 1 to 10."""

def multiples_3_5():
   """2-Write a generator expression to generate the first 5 multiples of 3."""
   for i in lista:
      if i%3 == 0 or i%5 == 0:
         yield i

# 5 
list_comprehension_multiples_5 = [x for x in range(1, 51) if x%5 == 0]
"""3-Write a list comprehension to create a list of all numbers from 1 to 50 that are divisible by 3 or 5."""

@generator_printer
def fibonacci():
   """4-Write a generator expression to generate the first 10 Fibonacci numbers."""
   count = 1
   
   temp1 = 1
   temp2 = 1
   print("1\n1")
   while count <= 9:
      
      temp1, temp2 = temp2, temp1+temp2
      
      count += 1
      yield temp2

list_comprehension_square_list = [[n, n*n] for n in range(1, 11)]
print(list_comprehension_square_list)

@generator_printer
def up_to_100():
   """6-Write a generator expression to generate all the prime numbers up to 100."""
   for i in range(1, 101):
      yield i

