from typing import List

from DAL.Manager import Manager
from DTO.Receipt import Receipt


class ReceiptDAL(Manager):
    def __init__(self):
        super().__init__("receipt", [
            "RECEIPT_ID",
            "STAFF_ID",
            "DOR",
            "GRAND_TOTAL",
            "DELETED"
        ])

    def convertToReceipts(self, data: List[List[object]]) -> List[Receipt]:
        return self.convert(data, lambda row: Receipt(
            row['RECEIPT_ID'],
            row['STAFF_ID'],
            row['DOR'],
            row['GRAND_TOTAL'],
            bool(row['DELETED'])
        ))

    def insertReceipt(self, receipt: Receipt) -> int:
        try:
            return self.create(
                receipt.getReceiptID(),
                receipt.getStaffID(),
                receipt.getDor(),
                receipt.getGrandTotal(),
                False
            ) # Receipt khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in ReceiptDAL.insertReceipt(): {e}")
        return 0

    def updateReceipt(self, receipt: Receipt) -> int:
        try:
            updateValues = [
                receipt.getReceiptID(),
                receipt.getStaffID(),
                receipt.getDor(),
                receipt.getGrandTotal(),
                Receipt.isDeleted()
            ]
            return self.update(updateValues, f"RECEIPT_ID = {Receipt.getReceiptID()}")
        except Exception as e:
            print(f"Error occurred in ReceiptDAL.updateReceipt(): {e}")
        return 0

    def removeReceipt(self, *conditions: str) -> int:
        try:
            updateValues = [1]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in ReceiptDAL.deleteReceipt(): {e}")
        return 0

    def searchReceipts(self, *conditions: str) -> List[Receipt]:
        try:
            return self.convertToReceipts(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in ReceiptDAL.searchReceipts(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("REC", 3)
        except Exception as e:
            print(f"Error occurred in ReceiptDAL.getAutoID(): {e}")
        return ""