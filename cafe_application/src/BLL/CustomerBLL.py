from typing import List

from BLL.Manager import Manager
from DAL.CustomerDAL import CustomerDAL
from DTO.Customer import Customer


class CustomerBLL(Manager[Customer]):
    def __init__(self):
        try:
            self.__customerDAL = CustomerDAL()
            self.__customerList = self.searchCustomers("DELETED = 0")
        except Exception:
            pass

    def getCustomerDAL(self) -> CustomerDAL:
        return self.__customerDAL

    def setCustomerDAL(self, customerDAL: CustomerDAL) -> CustomerDAL:
        self.__customerDAL = customerDAL

    def getCustomerList(self) -> list:
        return self.__customerList

    def setCustomerList(self, customerList) -> list:
        self.__customerList = customerList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__customerList)

    def addCustomer(self, customer: Customer) -> bool:
        if (self.getIndex(customer, "PHONE", self.__customerList)) != -1:
            print("Can't add new customer. Phone already exists.")
            return False
        self.__customerList.append(customer)
        return self.__customerDAL.addCustomer(customer) != 0

    def updateCustomer(self, customer: Customer) -> bool:
        self.__customerList[self.getIndex(customer, "CUSTOMER_ID", self.__customerList)] = customer
        return self.__customerDAL.updateCustomer(customer) != 0

    def deleteCustomer(self, customer: Customer) -> bool:
        self.__customerList.pop(self.getIndex(customer, "CUSTOMER_ID", self.__customerList))
        return self.__customerDAL.deleteCustomer(f"CUSTOMER_ID = '{customer.getCustomerID()}'") != 0

    def searchCustomers(self, *conditions: str) -> List[Customer]:
        return self.__customerDAL.searchCustomers(*conditions)

    def findCustomersBy(self, conditions: dict) -> list[Customer]:
        customers = self.__customerList
        for key, value in conditions.items():
            customers = super().findObjectsBy(key, value, customers)
        return customers

    def getAutoID(self) -> str:
        return super().getAutoID("CUS", 3, self.searchCustomers())

    def getValueByKey(self, customer: Customer, key: str) -> object:
        return {
            "CUSTOMER_ID": customer.getCustomerID(),
            "NAME": customer.getName(),
            "GENDER": customer.isGender(),
            "DOB": customer.getDateOfBirth(),
            "PHONE": customer.getPhone(),
            "MEMBERSHIP": customer.isMembership(),
            "DOSUP": customer.getDateOfSup()
        }.get(key, None)
