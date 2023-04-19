from typing import List

from BLL.Manager import Manager
from DAL.BillDetailsDAL import BillDetailsDAL
from DTO.BillDetails import BillDetails


class BillDetailsBLL(Manager[BillDetails]):
    def __init__(self):
        try:
            self.__billDetailsDAL = BillDetailsDAL()
            self.__billDetailsList = self.searchBillDetails()
        except Exception:
            pass

    def getBillDetailsDAL(self) -> BillDetailsDAL:
        return self.__billDetailsDAL

    def setBillDetailsDAL(self, billDetailsDAL: BillDetailsDAL) -> BillDetailsDAL:
        self.__billDetailsDAL = billDetailsDAL

    def getBillDetailsList(self) -> list:
        return self.__billDetailsList

    def setBillDetailsList(self, billDetailsList) -> list:
        self.__billDetailsList = billDetailsList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__billDetailsList)

    def addBillDetails(self, billDetails: BillDetails) -> bool:
        self.__billDetailsList.append(billDetails)
        return self.__billDetailsDAL.addBillDetails(billDetails) != 0

    def searchBillDetails(self, *conditions: str) -> List[BillDetails]:
        return self.__billDetailsDAL.searchBillDetails(*conditions)

    def findBillDetailsBy(self, conditions: dict) -> list[BillDetails]:
        billDetails = self.__billDetailsList
        for key, value in conditions.items():
            billDetails = super().findObjectsBy(key, value, billDetails)
        return billDetails

    def getValueByKey(self, billDetails: BillDetails, key: str) -> object:
        return {
            "BILL_ID": billDetails.getBillID(),
            "PRODUCT_ID": billDetails.getProductID(),
            "QUANTITY": billDetails.getQuantity()
        }.get(key, None)
