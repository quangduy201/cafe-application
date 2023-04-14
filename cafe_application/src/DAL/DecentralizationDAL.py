from typing import List

from DAL.Manager import Manager
from DTO.Decentralization import Decentralization


class DecentralizationDAL(Manager):
    def __init__(self):
        super().__init__("decentralization", [
            "DECENTRALIZATION_ID",
            "IS_SALE",
            "IS_PRODUCT",
            "IS_CATEGORY",
            "IS_RECIPE",
            "IS_IMPORT",
            "IS_BILL",
            "IS_WAREHOUSES",
            "IS_ACCOUNT",
            "IS_STAFF",
            "IS_CUSTOMER",
            "IS_DISCOUNT",
            "IS_DECENTRALIZE",
            "DECENTRALIZATION_NAME",
            "DELETED"
        ])

    def convertToDecentralization(self, data: List[List[object]]) -> List[Decentralization]:
        return self.convert(data, lambda row: Decentralization(
            row['DECENTRALIZATION_ID'],
            row['IS_SALE'],
            row['IS_PRODUCT'],
            row['IS_CATEGORY'],
            row['IS_RECIPE'],
            row['IS_IMPORT'],
            row['IS_BILL'],
            row['IS_WAREHOUSES'],
            row['IS_ACCOUNT'],
            row['IS_STAFF'],
            row['IS_CUSTOMER'],
            row['IS_DISCOUNT'],
            row['IS_DECENTRALIZE'],
            row['DECENTRALIZATION_NAME'],
            bool(row['DELETED'])
        ))

    def addDecentralization(self, decentralization: Decentralization) -> int:
        try:
            return self.create(
                decentralization.getDecentralizationID(),
                decentralization.getIsSale(),
                decentralization.getIsProduct(),
                decentralization.getIsCategory(),
                decentralization.getIsRecipe(),
                decentralization.getIsImport(),
                decentralization.getIsBill(),
                decentralization.getIsWarehouses(),
                decentralization.getIsAccount(),
                decentralization.getIsStaff(),
                decentralization.getIsCustomer(),
                decentralization.getIsDiscount(),
                decentralization.getIsDecentralize(),
                decentralization.getDecentralizationName(),
                False
            ) # decentralization khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in DecentralizationDAL.addDecentralization(): {e}")
        return 0

    def updateDecentralization(self, decentralization: Decentralization) -> int:
        try:
            updateValues = [
                decentralization.getDecentralizationID(),
                decentralization.getIsSale(),
                decentralization.getIsProduct(),
                decentralization.getIsCategory(),
                decentralization.getIsRecipe(),
                decentralization.getIsImport(),
                decentralization.getIsBill(),
                decentralization.getIsWarehouses(),
                decentralization.getIsAccount(),
                decentralization.getIsStaff(),
                decentralization.getIsCustomer(),
                decentralization.getIsDiscount(),
                decentralization.getIsDecentralize(),
                decentralization.getDecentralizationName(),
                decentralization.isDeleted()
            ]
            return self.update(updateValues, f"DECENTRALIZATION_ID = '{decentralization.getDecentralizationID()}'")
        except Exception as e:
            print(f"Error occurred in DecentralizationDAL.updateDecentralization(): {e}")
        return 0

    def deleteDecentralization(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in DecentralizationDAL.deleteDecentralization(): {e}")
        return 0

    def searchDecentralizations(self, *conditions: str) -> List[Decentralization]:
        try:
            return self.convertToDecentralization(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in DecentralizationDAL.searchDecentralizations(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("DE", 2)
        except Exception as e:
            print(f"Error occurred in DecentralizationDAL.getAutoID(): {e}")
        return ""
