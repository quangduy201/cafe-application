from typing import List

from DAL.AccountDAL import AccountDAL
from DTO.Account import Account


class AccountBLL:
    def __init__(self):
        try:
            self.accountDAL = AccountDAL()
        except Exception:
            pass

    def insertAccount(self, account: Account) -> bool:
        if self.searchAccounts(f"USERNAME = '{account.getUsername()}'"):
            print("Can't insert new account. Username already exists.")
            return False
        return self.accountDAL.insertAccount(account) != 0

    def updateAccount(self, account: Account) -> bool:
        return self.accountDAL.updateAccount(account) != 0

    def removeAccount(self, id: str) -> bool:
        return self.accountDAL.removeAccount(f"ACCOUNT_ID = {id}") != 0

    def searchAccounts(self, *conditions: str) -> List[Account]:
        return self.accountDAL.searchAccounts(*conditions)

    def getAutoID(self) -> str:
        return self.accountDAL.getAutoID()


def test():
    accountBLL = AccountBLL()
    accounts = accountBLL.searchAccounts()
    for account in accounts:
        print(account)
    print()

    accountBLL.insertAccount(Account(accountBLL.getAutoID(), 'hello', '123', 'DE03', 'ST02'))
    accounts = accountBLL.searchAccounts()
    for account in accounts:
        print(account)
    print()

    accountBLL.removeAccount("username = 'hello'") # set deleted to True
    accountBLL.accountDAL.delete("username = 'hello'") # delete from database
    accounts = accountBLL.searchAccounts()
    for account in accounts:
        print(account)
    print()

# uncomment the code below to test
# test()
