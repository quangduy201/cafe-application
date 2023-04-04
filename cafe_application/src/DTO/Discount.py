from datetime import date


class Discount:
    def __init__(self, discountID = "", discountPercent = 0.0, startDay = date(1, 1, 1), endDay = date(1, 1, 1), status = "", deleted = False):
        self.__discountID = discountID
        self.__discountPercent = discountPercent
        self.__startDay = startDay
        self.__endDay = endDay
        self.__status = status
        self.__deleted = deleted

    def getDiscountID(self) -> str:
        return self.__discountID

    def setDiscountID(self, discountID) -> None:
        self.__discountID = discountID

    def getDiscountPercent(self) -> float:
        return self.__discountPercent

    def setDiscountPercent(self, discountPercent) -> None:
        self.__discountPercent = discountPercent

    def getStartDay(self) -> date:
        return self.__startDay

    def setStartDay(self, startDay) -> None:
        self.__startDay = startDay

    def getEndDay(self) -> date:
        return self.__endDay

    def setEndDay(self, endDay) -> None:
        self.__endDay = endDay

    def getStatus(self) -> str:
        return self.__status

    def setStatus(self, status) -> None:
        self.__status = status

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__discountID} | " \
            + f"{self.__status} | " \
            + f"{self.__discountPercent} | " \
            + f"{self.__startDay} | " \
            + f"{self.__endDay}"
