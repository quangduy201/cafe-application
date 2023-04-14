from typing import List

from DAL.Manager import Manager
from DTO.Discount import Discount


class DiscountDAL(Manager):
    def __init__(self):
        super().__init__("discount", [
            "DISCOUNT_ID",
            "DISCOUNT_PERCENT",
            "START_DATE",
            "END_DATE",
            "STATUS",
            "DELETED"
        ])

    def convertToDiscounts(self, data: List[List[object]]) -> List[Discount]:
        return self.convert(data, lambda row: Discount(
            row['DISCOUNT_ID'],
            row['DISCOUNT_PERCENT'],
            row['START_DATE'],
            row['END_DATE'],
            row['STATUS'],
            bool(row['DELETED'])
        ))

    def addDiscount(self, discount: Discount) -> int:
        try:
            return self.create(
                discount.getDiscountID(),
                discount.getDiscountPercent(),
                discount.getStartDay(),
                discount.getEndDay(),
                discount.getStatus(),
                False
            ) # discount khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in DiscountDAL.addDiscount(): {e}")
        return 0

    def updateDiscount(self, discount: Discount) -> int:
        try:
            updateValues = [
                discount.getDiscountID(),
                discount.getDiscountPercent(),
                discount.getStartDay(),
                discount.getEndDay(),
                discount.getStatus(),
                discount.isDeleted()
            ]
            return self.update(updateValues, f"DISCOUNT_ID = '{discount.getDiscountID()}'")
        except Exception as e:
            print(f"Error occurred in DiscountDAL.updateDiscount(): {e}")
        return 0

    def deleteDiscount(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in DiscountDAL.deleteDiscount(): {e}")
        return 0

    def searchDiscounts(self, *conditions: str) -> List[Discount]:
        try:
            return self.convertToDiscounts(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in DiscountDAL.searchDiscounts(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("DIS", 3)
        except Exception as e:
            print(f"Error occurred in DiscountDAL.getAutoID(): {e}")
        return ""
