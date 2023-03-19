class Category:
    def __init__(self, categoryID, name, quantity, deleted):
        self.categoryID = categoryID
        self.name = name
        self.quantity = quantity
        self.deleted = deleted

    def getCategoryID(self):
        return self.categoryID

    def setCategoryID(self, categoryID):
        self.categoryID = categoryID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
         return self.categoryID + " | " + self.name + " | " + self.quantity

