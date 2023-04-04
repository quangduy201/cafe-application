from typing import List

from DAL.Manager import Manager
from DTO.DiscountDetails import DiscountDetails


class DiscountDetailsDAL(Manager):
    def __init__(self):
        super().__init__("discount_details", [
            "DISCOUNT_ID",
            "PRODUCT_ID"
        ])

    def convertToDiscountDetailss(self, data: List[List[object]]) -> List[DiscountDetails]:
        return self.convert(data, lambda row: DiscountDetails(
            row['DISCOUNT_ID'],
            row['PRODUCT_ID']
        ))

    def addDiscountDetails(self, discountDetails: DiscountDetails) -> int:
        try:
            return self.create(
                discountDetails.getDiscountID(),
                discountDetails.getProductID()
            ) # discountDetails khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in DiscountDetailsDAL.addDiscountDetails(): {e}")
        return 0

    def searchDiscountDetailss(self, *conditions: str) -> List[DiscountDetails]:
        try:
            return self.convertToDiscountDetailss(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in DiscountDetailsDAL.searchDiscountDetailss(): {e}")
        return []
