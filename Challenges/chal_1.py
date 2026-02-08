class Book:
    def __init__(self, title: str, author: str, pages: int, isbn: str):
        self.title = title
        self.author = author
        self.pages = pages
        self._isbn = isbn
        self._borrowed = False
        
    def get_isbn(self):
        return self._isbn
    
class Library:
    def __init__(self, name: str):
        self.name = name
        self._books_list = []
        
    def get_book_by_isbn(self, isbn: str) -> Book | None:
        for book in self._books_list:
            if book.get_isbn() == isbn:
                return book
        return None
        
    def store_book(self, book: Book):
        if book in self._books_list:
            raise BookAlreadyStoredError()
        
        self._books_list.append(book)
        print("Book successfully stored!\n")
        
    def remove_book(self, isbn: str):
        book = self.get_book_by_isbn(isbn)
        
        if not book:
            raise BookNotStoredError()
        
        if book.get_book_state():
            raise BookCurrentlyBorrowedError()
        
        self._books_list.remove(book)
        print("Book successfully removed!\n")
                
        
    def borrow_book(self, isbn: str):
        book = self.get_book_by_isbn(isbn)
        
        if not book:
            raise BookNotStoredError()
        
        if book.get_book_state():
            raise BookAlreadyBorrowedError()
        
        book._borrowed = True
        print("Book borrowed successfully!\n")
        
    def return_book(self, isbn: str):
        book = self.get_book_by_isbn(isbn)
        
        if not book:
            raise BookNotStoredError()
        
        if not book.get_book_state():
            raise BookNotBorrowedError()
        
        book._borrowed = False
        print("Book returned successfully!\n")

        
class LibraryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class BookNotStoredError(LibraryError):
    def __init__(self):
        super().__init__("The mentioned book is not stored!\n")
        
class BookCurrentlyBorrowedError(LibraryError):
    def __init__(self):
        super().__init__("The book is currently borrowed!\nPlease wait until it's returned.\n")
        
class BookAlreadyStoredError(LibraryError):
    def __init__(self):
        super().__init__("The mentioned book is already stored!\n")

class BookAlreadyBorrowedError(LibraryError):
    def __init__(self):
        super().__init__("The mentioned book was already borrowed!\n")
        
class BookNotBorrowedError(LibraryError):
    def __init__(self):
        super().__init__("The mentioned book was not borrowed!")