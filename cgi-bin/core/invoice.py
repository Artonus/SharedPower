from database import DB

class Invoice(DB):

    def __init__(self, firstName, lastName, address, purchases):
        self.__id = DB.uuid
        self.__firstName = firstName
        self.__lastName = lastName 
        self.__address = address
        self.__purchases = purchases

    def id(self):
        return self.__id

    def firstName(self):
        return self.__firstName

    def lastName(self):
        return self.__lastName

    def address(self):
        return self.__address

    def purchases(self):
        return self.__purchases.__dict__