# library_system.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
        else:
            raise ValueError("The book must be an instance of Book, EBook, or PrintBook")

    def list_books(self):
        for book in self.books:
            print(book)




