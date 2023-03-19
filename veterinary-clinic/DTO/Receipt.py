class Receipt:
    def __init__(self, receiptID, staffID, dor, grandTotal, deleted):
        self.receiptID = receiptID
        self.staffID = staffID
        self.dor = dor
        self.grandTotal = grandTotal
        self.deleted = deleted

    def getReceiptID(self):
        return self.receiptID

    def setReceiptID(self, receiptID):
        self.receiptID = receiptID

    def getStaffID(self):
        return self.staffID

    def setStaffID(self, staffID):
        self.staffID = staffID

    def getDor(self):
        return self.dor

    def setDor(self, dor):
        self.dor = dor

    def getGrandTotal(self):
        return self.grandTotal

    def setGrandTotal(self, grandTotal):
        self.grandTotal = grandTotal

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.receiptID + "  | " + self.staffID + "  | " + self.dor + "  | " + self.grandTotal

