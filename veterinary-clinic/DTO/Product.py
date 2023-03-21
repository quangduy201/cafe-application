class Product:
    def __init__(self, productID  = "", name = "", categoryID = "", size = "", cost = 0, deleted = False):
        self.__productID = productID
        self.__name = name
        self.__categoryID = categoryID
        self.__size = size
        self.__cost = cost
        self.__deleted = deleted

    def getProductID(self):
        return self.__productID

    def setProductID(self, productID):
        self.__productID = productID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getCategoryID(self):
        return self.__categoryID

    def setCategoryID(self, categoryID):
        self.__categoryID = categoryID

    def getSize(self):
        return self.__size

    def setSize(self, size):
        self.__size = size

    def getCost(self):
        return self.__cost

    def setCost(self, cost):
        self.__cost = cost

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__productID + " | " \
            + self.__name + " | " \
            + self.__categoryID + " | " \
            + self.__size + " | " \
            + self.__cost
