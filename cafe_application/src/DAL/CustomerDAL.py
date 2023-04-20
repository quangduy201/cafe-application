from typing import List

from DAL.Manager import Manager
from DTO.Customer import Customer


class CustomerDAL(Manager):
    def __init__(self):
        super().__init__("customer", [
            "CUSTOMER_ID",
            "NAME",
            "GENDER",
            "DOB",
            "PHONE",
            "MEMBERSHIP",
            "DOSUP",
            "DELETED"
        ])

    def convertToCustomers(self, data: List[List[object]]) -> List[Customer]:
        return self.convert(data, lambda row: Customer(
            row['CUSTOMER_ID'],
            row['NAME'],
            row['GENDER'],
            row['DOB'],
            row['PHONE'],
            row['MEMBERSHIP'],
            row['DOSUP'],
            bool(row['DELETED'])
        ))

    def addCustomer(self, customer: Customer) -> int:
        try:
            return self.create(
                customer.getCustomerID(),
                customer.getName(),
                customer.isGender(),
                customer.getDateOfBirth(),
                customer.getPhone(),
                customer.isMembership(),
                customer.getDateOfSup(),
                False
            ) # customer khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in CustomerDAL.addCustomer(): {e}")
        return 0

    def updateCustomer(self, customer: Customer) -> int:
        try:
            updateValues = [
                customer.getCustomerID(),
                customer.getName(),
                customer.isGender(),
                customer.getDateOfBirth(),
                customer.getPhone(),
                customer.isMembership(),
                customer.getDateOfSup(),
                customer.isDeleted()
            ]
            return self.update(updateValues, f"CUSTOMER_ID = '{customer.getCustomerID()}'")
        except Exception as e:
            print(f"Error occurred in CustomerDAL.updateCustomer(): {e}")
        return 0

    def deleteCustomer(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in CustomerDAL.deleteCustomer(): {e}")
        return 0

    def searchCustomers(self, *conditions: str) -> List[Customer]:
        try:
            return self.convertToCustomers(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in CustomerDAL.searchCustomers(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("CUS", 3)
        except Exception as e:
            print(f"Error occurred in CustomerDAL.getAutoID(): {e}")
        return ""
