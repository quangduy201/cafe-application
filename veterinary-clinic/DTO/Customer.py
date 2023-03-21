from datetime import date
class Customer:
    def __init__(self, customerID = "", name = "", gender = "", dateOfBirth = date(0,0,0), phone = "", membership = False, dateOfSup = date(0,0,0), deleted = False):
        self.__customerID = customerID
        self.__name = name
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth
        self.__phone = phone
        self.__membership = membership
        self.__dateOfSup = dateOfSup
        self.__deleted = deleted

    def getCustomerID(self):
        return self.__customerID

    def setCustomerID(self, customerID):
        self.__customerID = customerID

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

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def isMembership(self):
        return self.__membership

    def setMembership(self, membership):
        self.__membership = membership

    def getDateOfSup(self):
        return self.__dateOfSup

    def setDateOfSup(self, dateOfSup):
        self.__dateOfSup = dateOfSup

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__customerID + " | " \
            + self.__name + " | " \
            + self.__gender + " | " \
            + self.__dateOfBirth + " | " \
            + self.__phone + " | " \
            + self.__membership + " | " \
            + self.__dateOfSup
