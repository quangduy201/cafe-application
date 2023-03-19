class Recipe:
    def __init__(self, productID, ingredientID, mass, unit, deleted):
        self.productID = productID
        self.ingredientID = ingredientID
        self.mass = mass
        self.unit = unit
        self.deleted = deleted

    def getProductID(self):
        return self.productID

    def setProductID(self, productID):
        self.productID = productID

    def getIngredientID(self):
        return self.ingredientID

    def setIngredientID(self, ingredientID):
        self.ingredientID = ingredientID

    def getMass(self):
        return self.mass

    def setMass(self, mass):
        self.mass = mass

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.productID + " | " + self.ingredientID + " | " + self.mass + " | " + self.unit

