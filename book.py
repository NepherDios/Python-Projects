class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        
    def describe(self):
        return f"""\tBook Description:
            Title: {self.title}
            Author: {self.author}
            Pages: {self.pages}
        """
        
class LibraryBook(Book):
    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author, pages)
        self._borrowed = False
    
    def borrow(self):
        if self.is_borrowed():
            raise Exception("Book already borrowed!")
        
        self._borrowed = True
        
        
    def return_book(self):
        if not self.isborrowed():
            raise Exception("Book is not borrowed!")
        
        self._borrowed = False
        
    def is_borrowed(self):
        return self._borrowed
        

book_1 = Book("Glaze 2", "Admin", 30)
book_2 = Book("Glaze 1", "Admin", 27)
book_3 = LibraryBook("The Blast", "Admin", 30)

print("Book 1: \n", book_1.describe())
print("Book 2: \n", book_2.describe())
print("Book 3: \n", book_3.describe())

print(f"Book 3 state: {book_3.is_borrowed()}")