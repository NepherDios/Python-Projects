class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        
    def describe(self):
        print(f"""\tBook Description:
            Title: {self.title}
            Author: {self.author}
            Pages: {self.pages}
        """)
        
class LibraryBook(Book):
    def borrow(self):
        self.borrowed = True
        
        
    def return_book(self):
        self.borrowed = False
        
    def book_state(self):
        return self.borrowed
        

book_1 = Book("Glaze 2", "Admin", 30)
book_2 = Book("Glaze 1", "Admin", 27)
book_3 = LibraryBook("The Blast", "Admin", 30)

print(f"Book 1: {book_1.describe()}")
print(f"Book 2: {book_2.describe()}")
print(f"Book 3: {book_3.describe()}")