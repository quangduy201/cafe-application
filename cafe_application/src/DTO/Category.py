class Category:
    def __init__(self, categoryID = "", name = "", quantity = 0, deleted = False):
        self.__categoryID = categoryID
        self.__name = name
        self.__quantity = quantity
        self.__deleted = deleted

    def getCategoryID(self) -> str:
        return self.__categoryID

    def setCategoryID(self, categoryID) -> None:
        self.__categoryID = categoryID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def getQuantity(self) -> int:
        return self.__quantity

    def setQuantity(self, quantity) -> None:
        self.__quantity = quantity

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__categoryID} | " \
            + f"{self.__name} | " \
            + f"{self.__quantity}"
