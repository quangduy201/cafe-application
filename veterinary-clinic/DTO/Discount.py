class Discount:
    def __init__(self, discountID, discountPercent, startDay, endDay, status, deleted):
        self.discountID = discountID
        self.discountPercent = discountPercent
        self.startDay = startDay
        self.endDay = endDay
        self.status = status
        self.deleted = deleted

    def getDiscountID(self):
        return self.discountID

    def setDiscountID(self, discountID):
        self.discountID = discountID

    def getDiscountPercent(self):
        return self.discountPercent

    def setDiscountPercent(self, discountPercent):
        self.discountPercent = discountPercent

    def getStartDay(self):
        return self.startDay

    def setStartDay(self, startDay):
        self.startDay = startDay

    def getEndDay(self):
        return self.endDay

    def setEndDay(self, endDay):
        self.endDay = endDay

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.discountID + " | " + self.status + " | " + self.discountPercent + " | " +self. startDay + " | " + self.endDay
