from database import DB

class Tool(DB):

    def __init__(self, name, price, availability, date):
        self.__name = name
        self.__price = price
        self.__availability = availability
        self.__date = date

    def name(self):
        return self.__name

    def price(self):
        return self.__price

    def availability(self):
        return self.__availability

    def date(self):
        return self.__date

