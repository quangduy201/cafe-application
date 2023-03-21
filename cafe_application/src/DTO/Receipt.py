from datetime import date


class Receipt:
    def __init__(self, receiptID = "", staffID = "", dor = date(0,0,0), grandTotal = 0, deleted = False):
        self.__receiptID = receiptID
        self.__staffID = staffID
        self.__dor = dor
        self.__grandTotal = grandTotal
        self.__deleted = deleted

    def getReceiptID(self):
        return self.__receiptID

    def setReceiptID(self, receiptID):
        self.__receiptID = receiptID

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, staffID):
        self.__staffID = staffID

    def getDor(self):
        return self.__dor

    def setDor(self, dor):
        self.__dor = dor

    def getGrandTotal(self):
        return self.__grandTotal

    def setGrandTotal(self, grandTotal):
        self.__grandTotal = grandTotal

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__receiptID + "  | " \
            + self.__staffID + "  | " \
            + self.__dor + "  | " \
            + self.__grandTotal

