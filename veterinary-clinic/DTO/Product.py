class Product:
    def __init__(self, productID, name, categoryID, size, cost, deleted):
        self.productID = productID
        self.name = name
        self.categoryID = categoryID
        self.size = size
        self.cost = cost
        self.deleted = deleted

    def getProductID(self):
        return self.productID

    def setProductID(self, productID):
        self.productID = productID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCategoryID(self):
        return self.categoryID

    def setCategoryID(self, categoryID):
        self.categoryID = categoryID

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.productID + " | " + self.name + " | " + self.categoryID + " | " + self.size + " | " + self.cost
