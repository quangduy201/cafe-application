class ReceiptDetails:
    def __init__(self, receiptID = "", ingredientID = "", quantity = 0.0, supplierID = ""):
        self.__receiptID = receiptID
        self.__ingredientID = ingredientID
        self.__quantity = quantity
        self.__supplierID = supplierID

    def getReceiptID(self) -> str:
        return self.__receiptID

    def setReceiptID(self, receiptID) -> None:
        self.__receiptID = receiptID

    def getIngredientID(self) -> str:
        return self.__ingredientID

    def setIngredientID(self, ingredientID) -> None:
        self.__ingredientID = ingredientID

    def getQuantity(self) -> float:
        return self.__quantity

    def setQuantity(self, quantity) -> None:
        self.__quantity = quantity

    def getSupplierID(self) -> str:
        return self.__supplierID

    def setSupplierID(self, supplierID) -> None:
        self.__supplierID = supplierID

    def __str__(self):
        return f"{self.__receiptID} | " \
            + f"{self.__ingredientID} | " \
            + f"{self.__quantity} | " \
            + f"{self.__supplierID}"
