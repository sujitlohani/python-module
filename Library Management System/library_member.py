class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_items = []

    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @property
    def borrowed_items(self):
        return self.__borrowed_items

    def borrow_item(self, item):
        self.__borrowed_items.append(item)
    
    def return_item(self, item):
        self.__borrowed_items.remove(item)

    def display_borrowed_items(self):
        return [item.title for item in self.__borrowed_items]

