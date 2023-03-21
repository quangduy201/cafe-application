class Ingredient:
    def __init__(self, ingredientID = "", name = "", quantity = 0, unit = "", supplierID = "", deleted = False):
        self.__ingredientID = ingredientID
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit
        self.__supplierID = supplierID
        self.__deleted = deleted

    def getIngredientID(self):
        return self.__ingredientID

    def setIngredientID(self, ingredientID):
        self.__ingredientID = ingredientID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getUnit(self):
        return self.__unit

    def setUnit(self, unit):
        self.__unit = unit

    def getSupplierID(self):
        return self.__supplierID

    def setSupplierID(self, supplierID):
        self.__supplierID = supplierID

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__ingredientID + " | " \
            + self.__name + " | " \
            + self.__quantity + " | " \
            + self.__unit + " | " \
            + self.__supplierID
