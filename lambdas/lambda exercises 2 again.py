"""
1-Write a lambda function to find the length of a string.

2-Write a lambda function to convert Celsius to Fahrenheit.

3-Write a lambda function to find the average of a list of numbers.

4-Write a lambda function to convert a string to uppercase.

5-Write a lambda function to concatenate two strings.

6-Write a lambda function to find the factorial of a number.

7-Write a lambda function to find the reverse of a string.

8-Write a lambda function to check if a string is a palindrome.

9-Write a lambda function to convert a list of strings to integers.

10-Write a lambda function to find the area of a circle with a given radius.
"""

#1
legth_string = lambda string: len(string)

#2
celsius_far = lambda num: (num*9/5) + 32

lista_aa = [7,12,20]

#3
average = lambda lista: (sum(lista))/len(lista_aa)

#4
upper_func = lambda string: string.upper()

#5
string_adder = lambda string1, string2: string1+string2

#6

#7
string_reverse = lambda string: string[::-1]

#8 If the string have any upper character I need to use .lower()
string_palindrome = lambda string: True if string == string[::-1] else False

#9
string_to_ints = lambda lista: [int(num) for num in lista]

#10
area_circle = lambda radius: 3.1416*(radius*radius)

