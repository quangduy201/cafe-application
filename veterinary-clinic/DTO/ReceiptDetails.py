class ReceiptDetails:
    def __init__(self, receiptID, ingredientID, quantity, supplierID):
        self.receiptID = receiptID
        self.ingredientID = ingredientID
        self.quantity = quantity
        self.supplierID = supplierID

    def getReceiptID(self):
        return self.receiptID

    def setReceiptID(self, receiptID):
        self.receiptID = receiptID

    def getIngredientID(self):
        return self.ingredientID

    def setIngredientID(self, ingredientID):
        self.ingredientID = ingredientID

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getSupplierID(self):
        return self.supplierID

    def setSupplierID(self, supplierID):
        self.supplierID = supplierID

    def toString(self):
        return self.receiptID + " | " + self.ingredientID + " | " + self.quantity + " | " + self.supplierID

