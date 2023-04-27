"""
Create a class called Product that has 
attributes name, price, and description, 
and methods print_info() that prints all of the attributes.
"""

class Product:
    """Basic class for create products"""
    def __init__(self, name, price, description) -> None:
        self.name = name
        self.price = price
        self.description = description
    
    
    def print_info(self):
        pass

"""
Create a subclass of Product called Book that has an additional 
attribute author and methods print_info() and get_author() that 
print the book's information and return the author's name, respectively.
"""

class Book(Product):
    """Base Class for create books

    Args:
        Product (class): Class base for create products
    """
    def __init__(self, name, price, description, author) -> None:
        super().__init__(name, price, description)
        self.author = author
    
    def print_info(self):
        print(f"Book Name: {self.name}, Price: {self.price}, Description: {self.description}")
    
    def get_author(self):
        return f"Author: {self.author}"

"""
Create a subclass of Product called Movie that has additional attributes director and 
duration, and methods print_info() and get_duration() that print the movie's 
information and return the duration, respectively.
"""

class Movie(Product):
    def __init__(self, name, price, description, director, duration) -> None:
        super().__init__(name, price, description)
        self.director = director
        self._duration = duration
        
    def print_info(self):
        print(f"Movie Name: {self.name}, Price: {self.price}, Description: {self.description}")
    
    def get_duration(self):
        return f"{self._duration}"

movie = Movie("Una pelicula", "0 pesos", "Una pelicula muy pelicula", "Yo", "1 segundo")
movie.print_info()
print(movie.get_duration())