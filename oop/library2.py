# book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title} by {self.author}"
        
book1 = Book("things fall apart", "chinua achebe")
book2 = Book("animal farm", "geoge owell")
book3 = Book("oliver twist", "charles dickens")
book4 = Book("great hope", "mark finely")
# print(book1)

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_book = []

    def borrowed_books(self, book):
        self.borrowed_book.append(book)


    def __str__(self):
        return f"Member: {self.name}. book borrowed: {[str(book) for book in self.borrowed_book]}"

member1 = Member("Ronald mweema")
member1.borrowed_books(book4)
# print(member1)

class Library:
    library = "Ronald's lib"
    total_books = 0
    total_members = 0

    def __init__(self, name):
        self.name = name
        self.book_obj = []
        self.member_obj = []

    def add_book(self, book):
        self.book_obj.append(book)
        Library.total_books += 1

    def add_member(self, member):
        self.member_obj.append(member)
        Library.total_members += 1

    def __str__(self):
        return f"Library: {self.name}. \nBorrowed Book: {[str(book) for book in self.book_obj]}. \nMember: {[str(member) for member in self.member_obj]}"

library1 = Library("RON'S library")
library1.add_book(book1)
library1.add_book(book3)
library1.add_member(member1)

print(library1)

        