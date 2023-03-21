class Recipe:
    def __init__(self, productID = "", ingredientID = "", mass = 0, unit = "", deleted = False):
        self.__productID = productID
        self.__ingredientID = ingredientID
        self.__mass = mass
        self.__unit = unit
        self.__deleted = deleted

    def getProductID(self):
        return self.__productID

    def setProductID(self, productID):
        self.__productID = productID

    def getIngredientID(self):
        return self.__ingredientID

    def setIngredientID(self, ingredientID):
        self.__ingredientID = ingredientID

    def getMass(self):
        return self.__mass

    def setMass(self, mass):
        self.__mass = mass

    def getUnit(self):
        return self.__unit

    def setUnit(self, unit):
        self.__unit = unit

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__productID + " | " \
            + self.__ingredientID + " | " \
            + self.__mass + " | " \
            + self.__unit

