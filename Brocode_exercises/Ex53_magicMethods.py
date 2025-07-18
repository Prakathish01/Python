"""
Magic methods - Dunder methods (double underscore) __init__,__str__,__eq__
                They are automatically called by many of Python's built-in operations
                They allow developers to define or customise the behaviour of objects
"""

class Book:

    def __init__(self,author,book_name,pages):
        self.author = author
        self.book_name = book_name
        self.pages = pages
    def __str__(self):
        return f"{self.author}'s - {self.book_name}"
    def __eq__(self, other):
        return self.author == other.author
    def __lt__(self, other):
        return self.pages < other.pages
    def __gt__(self, other):
        return self.pages > other.pages
    def __add__(self, other):
        return self.pages + other.pages
    def __getitem__(self, item):
        if item == "author":
            return self.author
        elif item == "book_name":
            return self.book_name
        elif item == "pages":
            return self.pages
        else:
            return 0
    def __contains__(self, item):
        return item in self.author or item in self.book_name

book1 = Book("Kumararamy","Kumar's kanavu",69)
book2 = Book("Thiruvaluvar","thirukural",1130)


print("Kumar's kanavu" in book1)