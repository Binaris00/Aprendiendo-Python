numbers = [1, 2, 3, 4, 5]

strings = ["hello", "world", "python"]

start = 1
end = 20

list_comprehesion_square = [x*x for x in numbers]
"""Write a list comprehension that squares each element of a list of numbers."""

list_comprehesion_odd = [x+x for x in numbers]
"""Write a list comprehension that filters out all the odd numbers from a list of numbers."""

list_comprehesion_upper = [x.upper() for x in strings]
"""Write a list comprehension that takes a list of strings and returns a new list with all strings converted to uppercase."""

list_comprehesion_create = [x for x in range(start, end)]
"""Write a list comprehension that creates a list of prime numbers from a given range of numbers."""