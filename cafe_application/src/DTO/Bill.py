from datetime import date


class Bill:
    def __init__(self, billID = "", customerID = "", staffID = "", dateOfPurchase = date(0,0,0), total = 0, deleted = False):
        self.__billID = billID
        self.__customerID = customerID
        self.__staffID = staffID
        self.__dateOfPurchase = dateOfPurchase
        self.__total = total
        self.__deleted = deleted

    def getBillID(self):
        return self.__billID

    def setBillID(self, billID):
        self.__billID = billID

    def getCustomerID(self):
        return self.__customerID

    def setCustomerID(self, customerID):
        self.__customerID = customerID

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, staffID):
        self.__staffID = staffID

    def getDateOfPurchase(self):
        return self.__dateOfPurchase

    def setDateOfPurchase(self, dateOfPurchase):
        self.__dateOfPurchase = dateOfPurchase

    def getTotal(self):
        return self.__total

    def setTotal(self, total):
        self.__total = total

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__billID + " | " \
            + self.__customerID + " | " \
            + self.__staffID + " | " \
            + self.__dateOfPurchase + " | " \
            + self.__total

