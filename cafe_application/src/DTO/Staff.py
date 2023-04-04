from datetime import date


class Staff:
    def __init__(self, staffID = "", name = "", gender = "", dateOfBirth = date(1, 1, 1), address = "", phone = "", email = "", salary = 0.0, dateOfEntry = date(1, 1, 1), deleted = False):
        self.__staffID = staffID
        self.__name = name
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__salary = salary
        self.__dateOfEntry = dateOfEntry
        self.__deleted = deleted

    def getStaffID(self) -> str:
        return self.__staffID

    def setStaffID(self, staffID) -> None:
        self.__staffID = staffID

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

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address) -> None:
        self.__address = address

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone) -> None:
        self.__phone = phone

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email) -> None:
        self.__email = email

    def getSalary(self) -> float:
        return self.__salary

    def setSalary(self, salary) -> None:
        self.__salary = salary

    def getDateOfEntry(self) -> date:
        return self.__dateOfEntry

    def setDateOfEntry(self, dateOfEntry) -> None:
        self.__dateOfEntry = dateOfEntry

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__staffID} | " \
            + f"{self.__name} | " \
            + f"{self.__gender} | " \
            + f"{self.__dateOfBirth} | " \
            + f"{self.__address} | " \
            + f"{self.__phone} | " \
            + f"{self.__email} | " \
            + f"{self.__salary} | " \
            + f"{self.__dateOfEntry}"
