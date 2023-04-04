class DiscountDetails:
    def __init__(self, discountID = "", productID = ""):
        self.__discountID = discountID
        self.__productID = productID

    def getDiscountID(self) -> str:
        return self.__discountID

    def setDiscountID(self, discountID) -> None:
        self.__discountID = discountID

    def getProductID(self) -> str:
        return self.__productID

    def setProductID(self, productID) -> None:
        self.__productID = productID

    def __str__(self):
        return f"{self.__discountID} | " \
            + f"{self.__productID}"
