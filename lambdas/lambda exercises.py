"""
1-Write a lambda function to add two numbers:

2-Write a lambda function to find the square of a number:

3-Write a lambda function to multiply two numbers:

4-Write a lambda function to check if a number is even:

5-Write a lambda function to sort a list of tuples based on the second item:

6-Write a lambda function to filter a list of numbers to only include the even ones:

7-Write a lambda function to map a list of numbers to their squares:

8-Write a lambda function to reduce a list of numbers to their sum:

9-Write a lambda function to find the maximum of a list of numbers:

10-Write a lambda function to find the minimum of a list of numbers:
"""

lista = [1, 2, 3, 4, 5]

#1
add_numbers = lambda num1, num2: num1+num2

#2
square_finder = lambda num: num*num

#3
multiply_numbers = lambda num1, num2: num1*num2

#4
checker_even = lambda num: True if (num%2 == 0) else False

#5
sorted_list = sorted(lista, key=lambda x: x[1])

#6
filter_list = list(filter(lambda num: num%2 == 0, lista))

#7
map_list = list(map(lambda num: num*num, lista))

#8
sum_list = lambda lista: sum(lista)

#9
maximun_number = lambda lista: max(lista)

#10
minimun_number = lambda lista: min(lista)
