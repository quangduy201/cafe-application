class Account:
    def __init__(self, accountID = "", username = "", password = "", decentralizationID = "", staffID = "", deleted = False):
        self.__accountID = accountID
        self.__username = username
        self.__password = password
        self.__decentralizationID = decentralizationID
        self.__staffID = staffID
        self.__deleted = deleted

    def getAccountID(self) -> str:
        return self.__accountID

    def setAccountID(self, accountID) -> None:
        self.__accountID = accountID

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username) -> None:
        self.__username = username

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password) -> None:
        self.__password = password

    def getDecentralizationID(self) -> str:
        return self.__decentralizationID

    def setDecentralizationID(self, decentralizationID) -> None:
        self.__decentralizationID = decentralizationID

    def getStaffID(self) -> str:
        return self.__staffID

    def setStaffID(self, staffID) -> None:
        self.__staffID = staffID

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__accountID} | " \
            + f"{self.__username} | " \
            + f"{self.__password} | " \
            + f"{self.__decentralizationID} | " \
            + f"{self.__staffID}"
