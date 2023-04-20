from typing import List

from BLL.Manager import Manager
from DAL.ReceiptDetailsDAL import ReceiptDetailsDAL
from DTO.ReceiptDetails import ReceiptDetails


class ReceiptDetailsBLL(Manager[ReceiptDetails]):
    def __init__(self):
        try:
            self.__receiptDetailsDAL = ReceiptDetailsDAL()
            self.__receiptDetailsList = self.searchReceiptDetails()
        except Exception:
            pass

    def getReceiptDetailsDAL(self) -> ReceiptDetailsDAL:
        return self.__receiptDetailsDAL

    def setReceiptDetailsDAL(self, receiptDetailsDAL: ReceiptDetailsDAL) -> ReceiptDetailsDAL:
        self.__receiptDetailsDAL = receiptDetailsDAL

    def getReceiptDetailsList(self) -> list:
        return self.__receiptDetailsList

    def setReceiptDetailsList(self, receiptDetailsList) -> list:
        self.__receiptDetailsList = receiptDetailsList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__receiptDetailsList)

    def addReceiptDetails(self, receiptDetails: ReceiptDetails) -> bool:
        self.__receiptDetailsList.append(receiptDetails)
        return self.__receiptDetailsDAL.addReceiptDetails(receiptDetails) != 0

    def searchReceiptDetails(self, *conditions: str) -> List[ReceiptDetails]:
        return self.__receiptDetailsDAL.searchReceiptDetails(*conditions)

    def findReceiptDetailsBy(self, conditions: dict) -> list[ReceiptDetails]:
        receiptDetails = self.__receiptDetailsList
        for key, value in conditions.items():
            receiptDetails = super().findObjectsBy(key, value, receiptDetails)
        return receiptDetails

    def getValueByKey(self, receiptDetails: ReceiptDetails, key: str) -> object:
        return {
            "RECEIPT_ID": receiptDetails.getReceiptID(),
            "INGREDIENT_ID": receiptDetails.getIngredientID(),
            "QUANTITY": receiptDetails.getQuantity(),
            "SUPPLIER_ID": receiptDetails.getSupplierID()
        }.get(key, None)
