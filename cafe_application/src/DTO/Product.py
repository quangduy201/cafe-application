class Product:
    def __init__(self, productID  = "", name = "", categoryID = "", sized = "", cost = 0.0, image = "", deleted = False):
        self.__productID = productID
        self.__name = name
        self.__categoryID = categoryID
        self.__sized = sized
        self.__cost = cost
        self.__image = image
        self.__deleted = deleted

    def getProductID(self) -> str:
        return self.__productID

    def setProductID(self, productID) -> None:
        self.__productID = productID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def getCategoryID(self) -> str:
        return self.__categoryID

    def setCategoryID(self, categoryID) -> None:
        self.__categoryID = categoryID

    def getSized(self) -> str:
        return self.__sized

    def setSized(self, sized) -> None:
        self.__sized = sized

    def getCost(self) -> float:
        return self.__cost

    def setCost(self, cost) -> None:
        self.__cost = cost

    def getImage(self) -> str:
        return self.__image

    def setImage(self, image) -> None:
        self.__image = image

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__productID} | " \
            + f"{self.__name} | " \
            + f"{self.__categoryID} | " \
            + f"{self.__sized} | " \
            + f"{self.__cost}"
