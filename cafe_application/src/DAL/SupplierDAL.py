from typing import List

from DAL.Manager import Manager
from DTO.Supplier import Supplier


class SupplierDAL(Manager):
    def __init__(self):
        super().__init__("supplier", [
            "SUPPLIER_ID",
            "NAME",
            "PHONE",
            "ADDRESS",
            "EMAIL",
            "PRICE",
            "DELETED"
        ])

    def convertToSuppliers(self, data: List[List[object]]) -> List[Supplier]:
        return self.convert(data, lambda row: Supplier(
            row['SUPPLIER_ID'],
            row['NAME'],
            row['PHONE'],
            row['ADDRESS'],
            row['EMAIL'],
            row['PRICE'],
            bool(row['DELETED'])
        ))

    def addSupplier(self, supplier: Supplier) -> int:
        try:
            return self.create(
                supplier.getSupplierID(),
                supplier.getName(),
                supplier.getPhone(),
                supplier.getAddress(),
                supplier.getEmail(),
                supplier.getPrice(),
                False
            ) # supplier khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in SupplierDAL.addSupplier(): {e}")
        return 0

    def updateSupplier(self, supplier: Supplier) -> int:
        try:
            updateValues = [
                supplier.getSupplierID(),
                supplier.getName(),
                supplier.getPhone(),
                supplier.getAddress(),
                supplier.getEmail(),
                supplier.getPrice(),
                supplier.isDeleted()
            ]
            return self.update(updateValues, f"SUPPLIER_ID = '{supplier.getSupplierID()}'")
        except Exception as e:
            print(f"Error occurred in SupplierDAL.updateSupplier(): {e}")
        return 0

    def deleteSupplier(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in SupplierDAL.deleteSupplier(): {e}")
        return 0

    def searchSuppliers(self, *conditions: str) -> List[Supplier]:
        try:
            return self.convertToSuppliers(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in SupplierDAL.searchSuppliers(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("SUP", 3)
        except Exception as e:
            print(f"Error occurred in SupplierDAL.getAutoID(): {e}")
        return ""
