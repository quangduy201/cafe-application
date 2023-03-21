class DiscountDetails:
    def __init__(self, discountID = "", productID = ""):
        self.__discountID = discountID
        self.__productID = productID

    def getDiscountID(self):
        return self.__discountID

    def setDiscountID(self, discountID):
        self.__discountID = discountID

    def getProductID(self):
        return self.__productID

    def setProductID(self, productID):
        self.__productID = productID

    def __str__(self):
        return self.__discountID + " | "\
            + self.__productID

