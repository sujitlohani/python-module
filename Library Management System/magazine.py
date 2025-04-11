from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number, publisher):
        super().__init__(item_id, title)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_details(self):
        return f"Magazine: {self.title}, Issue No: {self.issue_number}, Publisher: {self.publisher}"
