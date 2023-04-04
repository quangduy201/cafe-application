class Ingredient:
    def __init__(self, ingredientID = "", name = "", quantity = 0.0, unit = "", supplierID = "", deleted = False):
        self.__ingredientID = ingredientID
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit
        self.__supplierID = supplierID
        self.__deleted = deleted

    def getIngredientID(self) -> str:
        return self.__ingredientID

    def setIngredientID(self, ingredientID) -> None:
        self.__ingredientID = ingredientID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def getQuantity(self) -> float:
        return self.__quantity

    def setQuantity(self, quantity) -> None:
        self.__quantity = quantity

    def getUnit(self) -> str:
        return self.__unit

    def setUnit(self, unit) -> None:
        self.__unit = unit

    def getSupplierID(self) -> str:
        return self.__supplierID

    def setSupplierID(self, supplierID) -> None:
        self.__supplierID = supplierID

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__ingredientID} | " \
            + f"{self.__name} | " \
            + f"{self.__quantity} | " \
            + f"{self.__unit} | " \
            + f"{self.__supplierID}"
