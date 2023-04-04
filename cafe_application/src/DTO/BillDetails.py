class BillDetails:
    def __init__(self, billID = "", productID = "", quantity = 0):
        self.__billID = billID
        self.__productID = productID
        self.__quantity = quantity

    def getBillID(self) -> str:
        return self.__billID

    def setBillID(self, billID) -> None:
        self.__billID = billID

    def getProductID(self) -> str:
        return self.__productID

    def setProductID(self, productID) -> None:
        self.__productID = productID

    def getQuantity(self) -> int:
        return self.__quantity

    def setQuantity(self, quantity) -> None:
        self.__quantity = quantity

    def __str__(self):
        return f"{self.__billID} | " \
            + f"{self.__productID} | " \
            + f"{self.__quantity}"
