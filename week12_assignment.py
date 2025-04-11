from abc import ABC, abstractmethod

class Book ():
    def __init__ (self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author 

    @property
    def get_book_id(self):
        return self.__book_id
    @property
    def get_title(self):
        return self.__title
    @property
    def get_author(self):
        return self.__author

    @property
    def set_book_id(self, book_id):
        self.__book_id = book_id

    @property
    def set_title(self, title):
        self.__title = title
    @property
    def set_author(self, author):
        self.__author = author



class Library (ABC):

    def __init__(self):
        self.books = {}
        self.members

    @abstractmethod
    def add_book(self, book):
        if book.book_id in self.books:
            print ("Book already exists")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added to the library.")


    @abstractmethod
    def remove_book(self, book_id):
        if book_id in self.books:
            removed =  self.books.pop(book_id)
            print (f"Book {removed} has been removed from library")
        else:
            print ("Book not found")

    def register_member(self, member):
        if member.person_id in self.members:
            print("Member already registered.")
        else:
            self.members[member.person_id] = member
            print(f"Member '{member.name}' registered.")

    @property
    def get_book(self, book_id):
        return self.books.get(book_id, None)

    def get_member(self, member_id):
        return self.members.get(member_id, None)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                print(book)

    def display_members(self):
        if not self.members:
            print("No members registered.")
        else:
            for member in self.members.values():
                print(f"{member.person_id}: {member.name}")
