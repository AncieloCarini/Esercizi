# Exercise 1: Creating an Abstract Class with Abstract Methods

# Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then,
#  create two subclasses Circle and Rectangle that implement the area and perimeter methods.
'''
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def area (self):
        pass
    def perimeter (self):
        pass

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return math.pi * self.radius * 2
    
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 + [self.length + self.width]
    '''




# Exercise 2: Implementing Static Methods

# Create a class MathOperations with a static method add that takes two numbers and returns their sum,
#  and another static method multiply that takes two numbers and returns their product.

'''
class MathOperations:
    def add(a, b):
        return a + b
    def multiply(a, b):
        return a * b

'''


# Exercise 3: Library Management System 

# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:

#     __str__ method to return a string representation of the book.

#     @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn".
#     It means that you must use the class reference cls to create a new object of the Book class using a string.

# Example: 

# book = “La Divina Commedia, D. Alighieri, 999000666”
# divina_commedia: Book = Book.from_string(book)
# Here divina_commedia must contain an instance of the class Book with 

# title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:

#     borrow_book(book) to add a book to the borrowed_books list.

#     return_book(book) to remove a book from the borrowed_books list.

#     __str__ method to return a string representation of the member.

#     @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

# Create a Library class with the following attributes: books, members, total_books 
# (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.

# Create a script and play a bit with the classes:
# Create instances of books and members using class methods. Register members and add books to the library. 
# Lend books to members and display the state of the library before and after lending.










class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
        
        

title = 'La divina Commedia'
author = 'Dante Alighieri'
isbn = 1234567890

book = Book(title, author, isbn)
print(book)



class Member:
    def __init__(self, name: str, member_id: str, borrowed_books: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books += 1
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{self.title} is not available")
        
    def return_book(self, book):
        if not book.is_available:
            book.is_available = True
            self.borrowed_books -= 1
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{self.title} is not borrowed by {self.name}")
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {self.borrowed_books}"
    




        
name = 'Angelo'
member_id = '12345678'
borrowed_books = 'La divina Commedia'
member = Member(name, member_id, borrowed_books)
print(member)


class Librery:
    def __init__(self, books: str, members: list, total_books: list):
        self.books = books
        self.members = members
        self.total_books = total_books()
    
    def add_book(self, book):
        self.total_books.append(book)
        print(f"{book.title} has been added to the library")

    def remove_book(self, book):
        if book in self.total_books:
            self.total_books.remove(book)
            print(f"{book.title} has been removed from the library")

    def register_member(self, member):
        self.members.append(member)
        print(f"{member.name} has been registered as a member")
        



# Create a Library class with the following attributes: books, members, total_books 
# (class attribute to keep track of the total number of books)
# The library class must contain the following methods:

#     add_book(book) to add a book to the library and increment total_books.

#     remove_book(book) to remove a book from the library and decrement total_books.

#     register_member(member) to add a member to the library.

#     lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

#     __str__ method to return a string representation of the library with the list of books and members.

#     @classmethod library_statistics(cls) to print the total number of books.