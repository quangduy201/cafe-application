from typing import List

from BLL.Manager import Manager
from DAL.ReceiptDAL import ReceiptDAL
from DTO.Receipt import Receipt


class ReceiptBLL(Manager[Receipt]):
    def __init__(self):
        try:
            self.__receiptDAL = ReceiptDAL()
            self.__receiptList = self.searchReceipts()
        except Exception:
            pass

    def getReceiptDAL(self) -> ReceiptDAL:
        return self.__receiptDAL

    def setReceiptDAL(self, receiptDAL: ReceiptDAL) -> ReceiptDAL:
        self.__receiptDAL = receiptDAL

    def getReceiptList(self) -> list:
        return self.__receiptList

    def setReceiptList(self, receiptList) -> list:
        self.__receiptList = receiptList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__receiptList)

    def addReceipt(self, receipt: Receipt) -> bool:
        self.__receiptList.append(receipt)
        return self.__receiptDAL.addReceipt(receipt) != 0

    def updateReceipt(self, receipt: Receipt) -> bool:
        self.__receiptList[self.getIndex(receipt, "RECEIPT_ID", self.__receiptList)] = receipt
        return self.__receiptDAL.updateReceipt(receipt) != 0

    def deleteReceipt(self, receipt: Receipt) -> bool:
        self.__receiptList.pop(self.getIndex(receipt, "RECEIPT_ID", self.__receiptList))
        return self.__receiptDAL.deleteReceipt(f"RECEIPT_ID = '{receipt.getReceiptID}'") != 0

    def searchReceipts(self, *conditions: str) -> List[Receipt]:
        return self.__receiptDAL.searchReceipts(*conditions)

    def findReceiptsBy(self, conditions: dict) -> list[Receipt]:
        receipts = []
        for key, value in conditions.items():
            receipts = super().findObjectsBy(key, value, receipts)
        return receipts

    def getAutoID(self) -> str:
        return super().getAutoID("REC", 3, self.__receiptList)

    def getValueByKey(self, receipt: Receipt, key: str) -> object:
        return {
            "RECEIPT_ID": receipt.getReceiptID(),
            "STAFF_ID": receipt.getStaffID(),
            "DOR": receipt.getDor(),
            "GRAND_TOTAL": receipt.getGrandTotal()
        }.get(key, None)
