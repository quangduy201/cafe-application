class BillDetails:
    def __init__(self, billID = "", productID = "", quantity = 0):
        self.__billID = billID
        self.__productID = productID
        self.__quantity = quantity

    def getBillID(self):
        return self.__billID

    def setBillID(self, billID):
        self.__billID = billID

    def getProductID(self):
        return self.__productID

    def setProductID(self, productID):
        self.__productID = productID

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return self.__billID + " | " \
            + self.__productID + " | " \
            + self.__quantity
