from typing import List

from BLL.Manager import Manager
from DAL.AccountDAL import AccountDAL
from DTO.Account import Account


class AccountBLL(Manager[Account]):
    def __init__(self):
        try:
            self.__accountDAL = AccountDAL()
            self.__accountList = self.searchAccounts("DELETED = 0")
        except Exception:
            pass

    def getAccountDAL(self) -> AccountDAL:
        return self.__accountDAL

    def setAccountDAL(self, accountDAL: AccountDAL) -> AccountDAL:
        self.__accountDAL = accountDAL

    def getAccountList(self) -> list:
        return self.__accountList

    def setAccountList(self, accountList) -> list:
        self.__accountList = accountList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__accountList)

    def addAccount(self, account: Account) -> bool:
        if self.searchAccounts(f"USERNAME = '{account.getUsername()}'"):
            print("Can't add new account. Username already exists.")
            return False
        self.__accountList.append(account)
        return self.__accountDAL.addAccount(account) != 0

    def updateAccount(self, account: Account) -> bool:
        self.__accountList[self.getIndex(account, "ACCOUNT_ID", self.__accountList)] = account
        return self.__accountDAL.updateAccount(account) != 0

    def deleteAccount(self, account: Account) -> bool:
        self.__accountList.pop(self.getIndex(account, "ACCOUNT_ID", self.__accountList))
        return self.__accountDAL.deleteAccount(f"ACCOUNT_ID = '{account.getAccountID()}'") != 0

    def searchAccounts(self, *conditions: str) -> List[Account]:
        return self.__accountDAL.searchAccounts(*conditions)

    def findAccountsBy(self, conditions: dict) -> list[Account]:
        accounts = self.__accountList
        for key, value in conditions.items():
            accounts = super().findObjectsBy(key, value, accounts)
        return accounts

    def getAutoID(self) -> str:
        return super().getAutoID("AC", 3, self.searchAccounts())

    def getValueByKey(self, account: Account, key: str) -> object:
        return {
            "ACCOUNT_ID": account.getAccountID(),
            "USERNAME": account.getUsername(),
            "PASSWD": account.getPassword(),
            "DECENTRALIZATION_ID": account.getDecentralizationID(),
            "STAFF_ID": account.getStaffID()
        }.get(key, None)
