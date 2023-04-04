from datetime import datetime
from typing import List

from DAL.Manager import Manager
from DTO.Bill import Bill


class BillDAL(Manager):
    def __init__(self):
        super().__init__("bill", [
            "BILL_ID",
            "CUSTOMER_ID",
            "STAFF_ID",
            "DOPURCHASE",
            "TOTAL",
            "DELETED"
        ])

    def convertToBills(self, data: List[List[object]]) -> List[Bill]:
        return self.convert(data, lambda row: Bill(
            row['BILL_ID'],
            row['CUSTOMER_ID'],
            row['STAFF_ID'],
            row['DOPURCHASE'],
            row['TOTAL'],
            bool(row['DELETED'])
        ))

    def addBill(self, bill: Bill) -> int:
        try:
            return self.create(
                bill.getBillID(),
                bill.getCustomerID(),
                bill.getStaffID(),
                bill.getDateOfPurchase().strftime('%Y-%m-%d'),
                bill.getTotal(),
                False
            )  # bill khi tạo mặc định total, deleted = 0
        except Exception as e:
            print(f"Error occurred in BillDAL.addBill(): {e}")
            return 0

    def updateBill(self, bill: Bill) -> int:
        try:
            update_values = [
                bill.getCustomerID(),
                bill.getStaffID(),
                bill.getDateOfPurchase().strftime('%Y-%m-%d'),
                bill.getTotal(),
                bill.isDeleted(),
                bill.getBillID(),
            ]
            return self.update(update_values, f"BILL_ID = '{bill.getBillID()}'")
        except Exception as e:
            print(f"Error occurred in BillDAL.updateBill(): {e}")
            return 0

    def deleteBill(self, *conditions: str) -> int:
        try:
            update_values = [True]
            return self.update(update_values, *conditions)
        except Exception as e:
            print(f"Error occurred in BillDAL.deleteBill(): {e}")
        return 0

    def searchBills(self, *conditions: str) -> List[Bill]:
        try:
            return self.convertToBills(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in BillDAL.searchBills(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("BI", 4)
        except Exception as e:
            print(f"Error occurred in AccountDAL.getAutoID(): {e}")
        return ""
