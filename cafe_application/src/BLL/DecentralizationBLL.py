from typing import List

from BLL.Manager import Manager
from DAL.DecentralizationDAL import DecentralizationDAL
from DTO.Decentralization import Decentralization


class DecentralizationBLL(Manager[Decentralization]):
    def __init__(self):
        try:
            self.__decentralizationDAL = DecentralizationDAL()
            self.__decentralizationList = self.searchDecentralizations()
        except Exception:
            pass

    def getDecentralizationDAL(self) -> DecentralizationDAL:
        return self.__decentralizationDAL

    def setDecentralizationDAL(self, decentralizationDAL: DecentralizationDAL) -> DecentralizationDAL:
        self.__decentralizationDAL = decentralizationDAL

    def getDecentralizationList(self) -> list:
        return self.__decentralizationList

    def setDecentralizationList(self, decentralizationList) -> list:
        self.__decentralizationList = decentralizationList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__decentralizationList)

    def addDecentralization(self, decentralization: Decentralization) -> bool:
        if (self.getIndex(decentralization, "DECENTRALIZATION_NAME", self.__decentralizationList)) != -1:
            print("Can't add new decentralization. Name already exists.")
            return False
        self.__decentralizationList.append(decentralization)
        return self.__decentralizationDAL.addDecentralization(decentralization) != 0

    def updateDecentralization(self, decentralization: Decentralization) -> bool:
        self.__decentralizationList[self.getIndex(decentralization, "DECENTRALIZATION_ID", self.__decentralizationList)] = decentralization
        return self.__decentralizationDAL.updateDecentralization(decentralization) != 0

    def deleteDecentralization(self, decentralization: Decentralization) -> bool:
        self.__decentralizationList.pop(self.getIndex(decentralization, "DECENTRALIZATION_ID", self.__decentralizationList))
        return self.__decentralizationDAL.deleteDecentralization(f"DECENTRALIZATION_ID = '{decentralization.getDecentralizationID}'") != 0

    def searchDecentralizations(self, *conditions: str) -> List[Decentralization]:
        return self.__decentralizationDAL.searchDecentralizations(*conditions)

    def findDecentralizationsBy(self, conditions: dict) -> list[Decentralization]:
        decentralizations = []
        for key, value in conditions.items():
            decentralizations = super().findObjectsBy(key, value, decentralizations)
        return decentralizations

    def getAutoID(self) -> str:
        return super().getAutoID("DE", 2, self.__decentralizationList)

    def getValueByKey(self, decentralization: Decentralization, key: str) -> object:
        return {
            "DECENTRALIZATION_ID": decentralization.getDecentralizationID(),
            "IS_SALE": decentralization.getIsSale(),
            "IS_PRODUCT": decentralization.getIsProduct(),
            "IS_CATEGORY": decentralization.getIsCategory(),
            "IS_RECIPE": decentralization.getIsRecipe(),
            "IS_IMPORT": decentralization.getIsImport(),
            "IS_BILL": decentralization.getIsBill(),
            "IS_WAREHOUSES": decentralization.getIsWarehouses(),
            "IS_ACCOUNT": decentralization.getIsAccount(),
            "IS_STAFF": decentralization.getIsStaff(),
            "IS_CUSTOMER": decentralization.getIsCustomer(),
            "IS_DISCOUNT": decentralization.getIsDiscount(),
            "IS_DECENTRALIZATION": decentralization.getIsDecentralization(),
            "DECENTRALIZATION_NAME": decentralization.getDecentralizationName()
        }.get(key, None)
