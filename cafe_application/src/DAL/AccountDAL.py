from typing import List

from DAL.Manager import Manager
from DTO.Account import Account


class AccountDAL(Manager):
    def __init__(self):
        super().__init__("account", [
            "ACCOUNT_ID",
            "USERNAME",
            "PASSWD",
            "DECENTRALIZATION_ID",
            "STAFF_ID",
            "DELETED"
        ])

    def convertToAccounts(self, data: List[List[object]]) -> List[Account]:
        return self.convert(data, lambda row: Account(
            row['ACCOUNT_ID'],
            row['USERNAME'],
            row['PASSWD'],
            row['DECENTRALIZATION_ID'],
            row['STAFF_ID'],
            bool(row['DELETED'])
        ))

    def addAccount(self, account: Account) -> int:
        try:
            return self.create(
                account.getAccountID(),
                account.getUsername(),
                account.getPassword(),
                account.getDecentralizationID(),
                account.getStaffID(),
                False
            ) # account khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in AccountDAL.addAccount(): {e}")
        return 0

    def updateAccount(self, account: Account) -> int:
        try:
            updateValues = [
                account.getAccountID(),
                account.getUsername(),
                account.getPassword(),
                account.getDecentralizationID(),
                account.getStaffID(),
                account.isDeleted()
            ]
            return self.update(updateValues, f"ACCOUNT_ID = {account.getAccountID()}")
        except Exception as e:
            print(f"Error occurred in AccountDAL.updateAccount(): {e}")
        return 0

    def deleteAccount(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in AccountDAL.deleteAccount(): {e}")
        return 0

    def searchAccounts(self, *conditions: str) -> List[Account]:
        try:
            return self.convertToAccounts(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in AccountDAL.searchAccounts(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("AC", 3)
        except Exception as e:
            print(f"Error occurred in AccountDAL.getAutoID(): {e}")
        return ""
