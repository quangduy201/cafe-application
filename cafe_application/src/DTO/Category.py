class Category:
    def __init__(self, categoryID = "", name = "", quantity = 0, deleted = False):
        self.__categoryID = categoryID
        self.__name = name
        self.__quantity = quantity
        self.__deleted = deleted

    def getCategoryID(self):
        return self.__categoryID

    def setCategoryID(self, categoryID):
        self.__categoryID = categoryID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
         return self.__categoryID + " | " \
            + self.__name + " | " \
            + self.__quantity

