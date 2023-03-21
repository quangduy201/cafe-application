class ReceiptDetails:
    def __init__(self, receiptID = "", ingredientID = "", quantity = 0, supplierID = ""):
        self.__receiptID = receiptID
        self.__ingredientID = ingredientID
        self.__quantity = quantity
        self.__supplierID = supplierID

    def getReceiptID(self):
        return self.__receiptID

    def setReceiptID(self, receiptID):
        self.__receiptID = receiptID

    def getIngredientID(self):
        return self.__ingredientID

    def setIngredientID(self, ingredientID):
        self.__ingredientID = ingredientID

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getSupplierID(self):
        return self.__supplierID

    def setSupplierID(self, supplierID):
        self.__supplierID = supplierID

    def __str__(self):
        return self.__receiptID + " | " \
            + self.__ingredientID + " | " \
            + self.__quantity + " | " \
            + self.__supplierID

