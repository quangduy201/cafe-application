class Account:
    def __init__(self, accountID = "", username = "", password = "", decentralizationID = "", staffID = "", deleted = False):
        self.__AccountID = accountID
        self.__username = username
        self.__password = password
        self.__decentralizationID = decentralizationID
        self.__staffID = staffID
        self.__deleted = deleted

    def getAccountID(self):
        return self.__AccountID

    def setAccountID(self, accountID):
        self.__AccountID = accountID

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getDecentralizationID(self):
        return self.__decentralizationID

    def setDecentralizationID(self, decentralizationID):
        self.__decentralizationID = decentralizationID

    def getStaffID(self):
        return self.__staffID

    def setStaffID(self, staffID):
        self.__staffID = staffID

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__accountID + " | " \
            + self.__username + " | " \
            + self.__password + " | " \
            + self.__decentralizationID + " | " \
            + self.__staffID;
