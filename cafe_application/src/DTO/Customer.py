from datetime import date


class Customer:
    def __init__(self, customerID = "", name = "", gender = "", dateOfBirth = date(1, 1, 1), phone = "", membership = False, dateOfSup = date(1, 1, 1), deleted = False):
        self.__customerID = customerID
        self.__name = name
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth
        self.__phone = phone
        self.__membership = membership
        self.__dateOfSup = dateOfSup
        self.__deleted = deleted

    def getCustomerID(self) -> str:
        return self.__customerID

    def setCustomerID(self, customerID) -> None:
        self.__customerID = customerID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def getGender(self) -> str:
        return self.__gender

    def setGender(self, gender) -> None:
        self.__gender = gender

    def getDateOfBirth(self) -> date:
        return self.__dateOfBirth

    def setDateOfBirth(self, dateOfBirth) -> None:
        self.__dateOfBirth = dateOfBirth

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone) -> None:
        self.__phone = phone

    def isMembership(self) -> bool:
        return self.__membership

    def setMembership(self, membership) -> None:
        self.__membership = membership

    def getDateOfSup(self) -> date:
        return self.__dateOfSup

    def setDateOfSup(self, dateOfSup) -> None:
        self.__dateOfSup = dateOfSup

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__customerID} | " \
            + f"{self.__name} | " \
            + f"{self.__gender} | " \
            + f"{self.__dateOfBirth} | " \
            + f"{self.__phone} | " \
            + f"{self.__membership} | " \
            + f"{self.__dateOfSup}"
