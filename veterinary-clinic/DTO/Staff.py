from datetime import date
class Staff:
    def __init__(self, staffID = "", name = "", gender = "", dateOfBirth = date(0,0,0), address = "", phone = "", email = "", salary = 0, dateOfEntry = date(0,0,0), deleted = False):
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

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, staffID):
        self.__staffID = staffID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def getDateOfEntry(self):
        return self.__dateOfEntry

    def setDateOfEntry(self, dateOfEntry):
        self.__dateOfEntry = dateOfEntry

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__staffID + " | " \
            + self.__name + " | " \
            + self.__gender + " | " \
            + self.__dateOfBirth + " | " \
            + self.__address + " | " \
            + self.__phone + " | " \
            + self.__email + " | " \
            + self.__salary + " | " \
            + self.__dateOfEntry
