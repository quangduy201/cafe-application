from datetime import date


class Discount:
    def __init__(self, discountID = "", discountPercent = 0, startDay = date(0,0,0), endDay = date(0,0,0), status = "", deleted = False):
        self.__discountID = discountID
        self.__discountPercent = discountPercent
        self.__startDay = startDay
        self.__endDay = endDay
        self.__status = status
        self.__deleted = deleted

    def getDiscountID(self):
        return self.__discountID

    def setDiscountID(self, discountID):
        self.__discountID = discountID

    def getDiscountPercent(self):
        return self.__discountPercent

    def setDiscountPercent(self, discountPercent):
        self.__discountPercent = discountPercent

    def getStartDay(self):
        return self.__startDay

    def setStartDay(self, startDay):
        self.__startDay = startDay

    def getEndDay(self):
        return self.__endDay

    def setEndDay(self, endDay):
        self.__endDay = endDay

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__discountID + " | " \
            + self.__status + " | " \
            + self.__discountPercent + " | " \
            + self.__startDay + " | " \
            + self.__endDay
