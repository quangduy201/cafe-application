class Supplier:
    def __init__(self, supplierID = "", name = "", phone = "", address = "", email = "", price = 0, deleted = False):
        self.__supplierID = supplierID
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__email = email
        self.__price = price
        self.__deleted = deleted

    def getSupplierID(self):
        return self.__supplierID

    def setSupplierID(self, supplierID):
        self.__supplierID = supplierID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__supplierID + " | " \
            + self.__name + " | " \
            + self.__phone + " | " \
            + self.__address + " | " \
            + self.__email + " | " \
            + self.__price


