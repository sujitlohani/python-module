from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display_details(self):
        return f"Book: {self.title}, Author: {self.author},"
    
    
