from database import DB

class User(DB):

    __purchases = []
    __invoices = []

    def __init__(self, firstName, lastName, address, phoneNumber, email, username, password):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__email = email
        self.__username = username
        self.__password = password

    def id(self):
        return DB.hash(self.__username)

    def firstName(self):
        return self.__firstName

    def lastName(self):
        return self.__lastName

    def address(self):
        return self.__address

    def email(self):
        return self.__email

    def username(self):
        return self.__username

    def password(self):
        return self.__password

    def purchases(self):
        return self.__purchases.__dict__

    def invoices(self):
        return self.__invoices.__dict__