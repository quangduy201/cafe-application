class DiscountDetails:
    def __init__(self, discountID, productID):
        self.discountID = discountID
        self.productID = productID

    def getDiscountID(self):
        return self.discountID

    def setDiscountID(self, discountID):
        self.discountID = discountID

    def getProductID(self):
        return self.productID

    def setProductID(self, productID):
        self.productID = productID

    def toString(self):
        return self.discountID + " | " + self.productID

