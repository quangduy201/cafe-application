from typing import List

from BLL.Manager import Manager
from DAL.BillDAL import BillDAL
from DTO.Bill import Bill


class BillBLL(Manager[Bill]):
    def __init__(self):
        try:
            self.__billDAL = BillDAL()
            self.__billList = self.searchBills("DELETED = 0")
        except Exception:
            pass

    def getBillDAL(self) -> BillDAL:
        return self.__billDAL

    def setBillDAL(self, billDAL: BillDAL) -> BillDAL:
        self.__billDAL = billDAL

    def getBillList(self) -> list:
        return self.__billList

    def setBillList(self, billList) -> list:
        self.__billList = billList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__billList)

    def addBill(self, bill: Bill) -> bool:
        self.__billList.append(bill)
        return self.__billDAL.addBill(bill) != 0

    def updateBill(self, bill: Bill) -> bool:
        self.__billList[self.getIndex(bill, "BILL_ID", self.__billList)] = bill
        return self.__billDAL.updateBill(bill) != 0

    def deleteBill(self, bill: Bill) -> bool:
        self.__billList.pop(self.getIndex(bill, "BILL_ID", self.__billList))
        return self.__billDAL.deleteBill(f"BILL_ID = '{bill.getBillID()}'") != 0

    def searchBills(self, *conditions: str) -> List[Bill]:
        return self.__billDAL.searchBills(*conditions)

    def findBillsBy(self, conditions: dict) -> list[Bill]:
        bills = self.__billList
        for key, value in conditions.items():
            bills = super().findObjectsBy(key, value, bills)
        return bills

    def getAutoID(self) -> str:
        return super().getAutoID("BI", 4, self.searchBills())

    def getValueByKey(self, bill: Bill, key: str) -> object:
        return {
            "BILL_ID": bill.getBillID(),
            "CUSTOMER_ID": bill.getCustomerID(),
            "STAFF_ID": bill.getStaffID(),
            "DOPURCHASE": bill.getDateOfPurchase(),
            "TOTAL": bill.getTotal()
        }.get(key, None)
