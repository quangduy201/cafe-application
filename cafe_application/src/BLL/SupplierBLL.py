from typing import List

from BLL.Manager import Manager
from DAL.SupplierDAL import SupplierDAL
from DTO.Supplier import Supplier


class SupplierBLL(Manager[Supplier]):
    def __init__(self):
        try:
            self.__supplierDAL = SupplierDAL()
            self.__supplierList = self.searchSuppliers("DELETED = 0")
        except Exception:
            pass

    def getSupplierDAL(self) -> SupplierDAL:
        return self.__supplierDAL

    def setSupplierDAL(self, supplierDAL: SupplierDAL) -> SupplierDAL:
        self.__supplierDAL = supplierDAL

    def getSupplierList(self) -> list:
        return self.__supplierList

    def setSupplierList(self, supplierList) -> list:
        self.__supplierList = supplierList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__supplierList)

    def addSupplier(self, supplier: Supplier) -> bool:
        if self.getIndex(supplier, "PHONE", self.__supplierList) != -1:
            print("Can't add new supplier. Phone already exists.")
            return False
        self.__supplierList.append(supplier)
        return self.__supplierDAL.addSupplier(supplier) != 0

    def updateSupplier(self, supplier: Supplier) -> bool:
        self.__supplierList[self.getIndex(supplier, "SUPPLIER_ID", self.__supplierList)] = supplier
        return self.__supplierDAL.updateSupplier(supplier) != 0

    def deleteSupplier(self, supplier: Supplier) -> bool:
        self.__supplierList.pop(self.getIndex(supplier, "SUPPLIER_ID", self.__supplierList))
        return self.__supplierDAL.deleteSupplier(f"SUPPLIER_ID = '{supplier.getSupplierID()}'") != 0

    def searchSuppliers(self, *conditions: str) -> List[Supplier]:
        return self.__supplierDAL.searchSuppliers(*conditions)

    def findSuppliersBy(self, conditions: dict) -> list[Supplier]:
        suppliers = self.__supplierList
        for key, value in conditions.items():
            suppliers = super().findObjectsBy(key, value, suppliers)
        return suppliers

    def getAutoID(self) -> str:
        return super().getAutoID("SUP", 3, self.searchSuppliers())

    def getValueByKey(self, supplier: Supplier, key: str) -> object:
        return {
            "SUPPLIER_ID": supplier.getSupplierID(),
            "NAME": supplier.getName(),
            "PHONE": supplier.getPhone(),
            "ADDRESS": supplier.getAddress(),
            "EMAIL": supplier.getEmail(),
            "PRICE": supplier.getPrice()
        }.get(key, None)
