class BillDetails:
    def __init__(self, billID, productID, quantity):
        self.billID = billID
        self.productID = productID
        self.quantity = quantity

    def getBillID(self):
        return self.billID

    def setBillID(self, billID):
        self.billID = billID

    def getProductID(self):
        return self.productID

    def setProductID(self, productID):
        self.productID = productID

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def toString(self):
        return self.billID + " | " + self.productID + " | " + self.quantity
