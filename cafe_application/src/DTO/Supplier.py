class Supplier:
    def __init__(self, supplierID = "", name = "", phone = "", address = "", email = "", price = 0.0, deleted = False):
        self.__supplierID = supplierID
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__email = email
        self.__price = price
        self.__deleted = deleted

    def getSupplierID(self) -> str:
        return self.__supplierID

    def setSupplierID(self, supplierID) -> None:
        self.__supplierID = supplierID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone) -> None:
        self.__phone = phone

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address) -> None:
        self.__address = address

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email) -> None:
        self.__email = email

    def getPrice(self) -> float:
        return self.__price

    def setPrice(self, price) -> None:
        self.__price = price

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__supplierID} | " \
            + f"{self.__name} | " \
            + f"{self.__phone} | " \
            + f"{self.__address} | " \
            + f"{self.__email} | " \
            + f"{self.__price}"
