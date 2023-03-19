class Bill:
    def __init__(self, billID, customerID, staffID, dateOfPurchase, total, deleted):
        self.billID = billID
        self.customerID = customerID
        self.staffID = staffID
        self.dateOfPurchase = dateOfPurchase
        self.total = total
        self.deleted = deleted

    def getBillID(self):
        return self.billID

    def setBillID(self, billID):
        self.billID = billID

    def getCustomerID(self):
        return self.customerID

    def setCustomerID(self, customerID):
        self.customerID = customerID

    def getStaffID(self):
        return self.staffID

    def setStaffID(self, staffID):
        self.staffID = staffID

    def getDateOfPurchase(self):
        return self.dateOfPurchase

    def setDateOfPurchase(self, dateOfPurchase):
        self.dateOfPurchase = dateOfPurchase

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.billID + " | " + self.customerID + " | " + self.staffID + " | " + self.dateOfPurchase + " | " + self.total

