from typing import List

from BLL.Manager import Manager
from DAL.DiscountDetailsDAL import DiscountDetailsDAL
from DTO.DiscountDetails import DiscountDetails


class DiscountDetailsBLL(Manager[DiscountDetails]):
    def __init__(self):
        try:
            self.__discountDetailsDAL = DiscountDetailsDAL()
            self.__discountDetailsList = self.searchDiscountDetailsDetails()
        except Exception:
            pass

    def getDiscountDetailsDAL(self) -> DiscountDetailsDAL:
        return self.__discountDetailsDAL

    def setDiscountDetailsDAL(self, discountDetailsDAL: DiscountDetailsDAL) -> DiscountDetailsDAL:
        self.__discountDetailsDAL = discountDetailsDAL

    def getDiscountDetailsList(self) -> list:
        return self.__discountDetailsList

    def setDiscountDetailsList(self, discountDetailsList) -> list:
        self.__discountDetailsList = discountDetailsList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__discountDetailsList)

    def addDiscountDetails(self, discountDetails: DiscountDetails) -> bool:
        self.__discountDetailsList.append(discountDetails)
        return self.__discountDetailsDAL.addDiscountDetails(discountDetails) != 0

    def searchDiscountDetailsDetails(self, *conditions: str) -> List[DiscountDetails]:
        return self.__discountDetailsDAL.searchDiscountDetailsDetails(*conditions)

    def findDiscountDetailsDetailsBy(self, conditions: dict) -> list[DiscountDetails]:
        discountDetailsDetails = []
        for key, value in conditions.items():
            discountDetailsDetails = super().findObjectsBy(key, value, discountDetailsDetails)
        return discountDetailsDetails

    def getValueByKey(self, discountDetails: DiscountDetails, key: str) -> object:
        return {
            "DISCOUNT_ID": discountDetails.getDiscountDetailsID(),
            "PRODUCT_ID": discountDetails.getProductID()
        }.get(key, None)
