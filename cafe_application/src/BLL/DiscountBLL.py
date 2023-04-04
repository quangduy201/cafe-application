from typing import List

from BLL.Manager import Manager
from DAL.DiscountDAL import DiscountDAL
from DTO.Discount import Discount


class DiscountBLL(Manager[Discount]):
    def __init__(self):
        try:
            self.__discountDAL = DiscountDAL()
            self.__discountList = self.searchDiscounts()
        except Exception:
            pass

    def getDiscountDAL(self) -> DiscountDAL:
        return self.__discountDAL

    def setDiscountDAL(self, discountDAL: DiscountDAL) -> DiscountDAL:
        self.__discountDAL = discountDAL

    def getDiscountList(self) -> list:
        return self.__discountList

    def setDiscountList(self, discountList) -> list:
        self.__discountList = discountList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__discountList)

    def addDiscount(self, discount: Discount) -> bool:
        self.__discountList.append(discount)
        return self.__discountDAL.addDiscount(discount) != 0

    def updateDiscount(self, discount: Discount) -> bool:
        self.__discountList[self.getIndex(discount, "DISCOUNT_ID", self.__discountList)] = discount
        return self.__discountDAL.updateDiscount(discount) != 0

    def deleteDiscount(self, discount: Discount) -> bool:
        self.__discountList.pop(self.getIndex(discount, "DISCOUNT_ID", self.__discountList))
        return self.__discountDAL.deleteDiscount(f"DISCOUNT_ID = '{discount.getDiscountID}'") != 0

    def searchDiscounts(self, *conditions: str) -> List[Discount]:
        return self.__discountDAL.searchDiscounts(*conditions)

    def findDiscountsBy(self, conditions: dict) -> list[Discount]:
        discounts = []
        for key, value in conditions.items():
            discounts = super().findObjectsBy(key, value, discounts)
        return discounts

    def getAutoID(self) -> str:
        return super().getAutoID("DIS", 3, self.__discountList)

    def getValueByKey(self, discount: Discount, key: str) -> object:
        return {
            "CATEGORY_ID": discount.getDiscountID(),
            "DISCOUNT_PERCENT": discount.getDiscountPercent(),
            "START_DATE": discount.getStartDay(),
            "END_DATE": discount.getEndDay(),
            "STATUS": discount.getStatus()
        }.get(key, None)
