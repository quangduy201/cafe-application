from typing import List

from BLL.Manager import Manager
from DAL.ReceiptDetailsDAL import ReceiptDetailsDAL
from DTO.ReceiptDetails import ReceiptDetails


class ReceiptDetailsBLL(Manager[ReceiptDetails]):
    def __init__(self):
        try:
            self.__receiptDetailsDAL = ReceiptDetailsDAL()
            self.__receiptDetailsList = self.searchReceiptDetailsDetails()
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

    def searchReceiptDetailsDetails(self, *conditions: str) -> List[ReceiptDetails]:
        return self.__receiptDetailsDAL.searchReceiptDetailsDetails(*conditions)

    def findReceiptDetailsDetailsBy(self, conditions: dict) -> list[ReceiptDetails]:
        receiptDetailsDetails = []
        for key, value in conditions.items():
            receiptDetailsDetails = super().findObjectsBy(key, value, receiptDetailsDetails)
        return receiptDetailsDetails

    def getValueByKey(self, receiptDetails: ReceiptDetails, key: str) -> object:
        return {
            "RECEIPTDETAILS_ID": receiptDetails.getReceiptDetailsID(),
            "INGREDIENT_ID": receiptDetails.getIngredientID(),
            "QUANTITY": receiptDetails.getQuantity(),
            "SUPPLIER_ID": receiptDetails.getSupplierID()
        }.get(key, None)
