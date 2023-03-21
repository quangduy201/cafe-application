from typing import List

from DAL.BillDAL import BillDAL
from DTO.Bill import Bill


class BillBLL:
    def __init__(self):
        try:
            self.billDAL = BillDAL()
        except Exception:
            pass

    def insertBill(self, bill: Bill) -> bool:
        return self.billDAL.insertBill(bill) != 0

    def updateBill(self, bill: Bill) -> bool:
        return self.billDAL.updateBill(bill) != 0

    def removeBill(self, id: str) -> bool:
        return self.billDAL.removeBill(f"BILL_ID = '{id}'") != 0

    def searchBills(self, *conditions: str) -> List[Bill]:
        return self.billDAL.searchBills(*conditions)

    def getAutoID(self) -> str:
        return self.billDAL.getAutoID()
