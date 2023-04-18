from typing import List

from DAL.Manager import Manager
from DTO.BillDetails import BillDetails


class BillDetailsDAL(Manager):
    def __init__(self):
        super().__init__("bill_details", [
            "BILL_ID",
            "PRODUCT_ID",
            "QUANTITY"
        ])

    def convertToBillDetails(self, data: List[List[object]]) -> List[BillDetails]:
        return self.convert(data, lambda row: BillDetails(
            row['BILL_ID'],
            row['PRODUCT_ID'],
            row['QUANTITY']
        ))

    def addBillDetails(self, billDetails: BillDetails) -> int:
        try:
            return self.create(
                billDetails.getBillID(),
                billDetails.getProductID(),
                billDetails.getQuantity()
            )
        except Exception as e:
            print(f"Error occurred in BillDetailsDAL.addBillDetails(): {e}")
        return 0

    def searchBillDetails(self, *conditions: str) -> List[BillDetails]:
        try:
            return self.convertToBillDetails(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in BillDetailsDAL.searchBillDetails(): {e}")
        return []

