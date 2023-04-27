"""
Implement a library management system. 
Create a class for books, which contains attributes like title, author, ISBN, and available copies. 
Create another class for library, which contains a list of books and methods to add/remove books 
and check the availability of a book.
"""

class book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies

class library:

    great_gatsby = book("The Great Gatsby", "F. Scott Fitzgerald", 9780743273565, 12)
    mockingbird = book("To Kill a Mockingbird", "Harper Lee", 9780446310789, 10)
    b1984 =  book("1984", "George Orwell", 9780451524935, 15)
    pride_prejudice = book("Pride and Prejudice", "Jane Austen", 9780141439518, 8)
    lord_rings = book("The Lord of the Rings", "J.R.R. Tolkien", 9780261102361, 9)
    catcher_rye = book("The Catcher in the Rye", "J.D. Salinger", 9780140237375, 11)
    hundred_years = book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 9780060883287, 3)
    moby_dick = book("Moby-Dick", "Herman Melville", 9781501100170, 14)
    litte_women = book("Little Women", "Louisa May Alcott", 9781984820019, 7)
    huckleberry_finn = book("The Adventures of Huckleberry Finn", "Mark Twain", 9781853260095, 6)


    def add_book(self):
        book_add = int(input("Cantity of books you want to add: "))
        print(self.copies + book_add)

    def remove_book(self):
        book_remove = int(input("Cantity of books you want to delete: "))
        print(self.copies - book_remove)
    def availability_book(self):
        return print(f"Now, you can buy: {self.copies}")

if __name__ == "__main__":
    library.add_book(library.great_gatsby)
    library.remove_book(library.b1984)
    library.availability_book(library.hundred_years)