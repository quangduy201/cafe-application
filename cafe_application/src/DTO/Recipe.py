class Recipe:
    def __init__(self, recipeID = "", productID = "", ingredientID = "", mass = 0.0, unit = "", deleted = False):
        self.__recipeID = recipeID
        self.__productID = productID
        self.__ingredientID = ingredientID
        self.__mass = mass
        self.__unit = unit
        self.__deleted = deleted

    def getRecipeID(self) -> str:
        return self.__recipeID

    def setRecipeID(self, recipeID) -> None:
        self.__recipeID = recipeID

    def getProductID(self) -> str:
        return self.__productID

    def setProductID(self, productID) -> None:
        self.__productID = productID

    def getIngredientID(self) -> str:
        return self.__ingredientID

    def setIngredientID(self, ingredientID) -> None:
        self.__ingredientID = ingredientID

    def getMass(self) -> float:
        return self.__mass

    def setMass(self, mass) -> None:
        self.__mass = mass

    def getUnit(self) -> str:
        return self.__unit

    def setUnit(self, unit) -> None:
        self.__unit = unit

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__recipeID} | " \
            + f"{self.__productID} | " \
            + f"{self.__ingredientID} | " \
            + f"{self.__mass} | " \
            + f"{self.__unit}"
