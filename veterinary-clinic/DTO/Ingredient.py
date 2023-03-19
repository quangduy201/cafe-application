class Ingredient:
    def __init__(self, ingredientID, name, quantity, unit, supplierID, deleted):
        self.ingredientID = ingredientID
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.supplierID = supplierID
        self.deleted = deleted

    def getIngredientID(self):
        return self.ingredientID

    def setIngredientID(self, ingredientID):
        self.ingredientID = ingredientID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getUnit(self):
        return self.unit

    def setUnit(self, unit):
        self.unit = unit

    def getSupplierID(self):
        return self.supplierID

    def setSupplierID(self, supplierID):
        self.supplierID = supplierID

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.ingredientID + " | " + self.name + " | " + self.quantity + " | " + self.unit + " | " + self.supplierID
