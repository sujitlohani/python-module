class Library:
    def __init__(self):
        self.__items = {}
        self.__members = {}

    def add_item(self, item):
        self.__items[item.item_id] = item

    def register_member(self, member):
        self.__members[member.member_id] = member