from typing import List

from DAL.Manager import Manager
from DTO.ReceiptDetails import ReceiptDetails


class ReceiptDetailsDAL(Manager):
    def __init__(self):
        super().__init__("receipt_details", [
            "RECEIPT_ID",
            "INGREDIENT_ID",
            "QUANTITY",
            "SUPPLIER_ID"
        ])

    def convertToReceiptDetails(self, data: List[List[object]]) -> List[ReceiptDetails]:
        return self.convert(data, lambda row: ReceiptDetails(
            row['RECEIPT_ID'],
            row['INGREDIENT_ID'],
            row['QUANTITY'],
            row['SUPPLIER_ID']
        ))

    def addReceiptDetails(self, receiptDetails: ReceiptDetails) -> int:
        try:
            return self.create(
                receiptDetails.getReceiptID(),
                receiptDetails.getIngredientID(),
                receiptDetails.getQuantity(),
                receiptDetails.getSupplierID()
            ) # receiptDetails khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in ReceiptDetailsDAL.addReceiptDetails(): {e}")
        return 0

    def searchReceiptDetails(self, *conditions: str) -> List[ReceiptDetails]:
        try:
            return self.convertToReceiptDetails(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in ReceiptDetailsDAL.searchReceiptDetailss(): {e}")
        return []
