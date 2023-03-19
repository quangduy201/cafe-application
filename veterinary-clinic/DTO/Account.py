class Account:
    def __init__(self, accountID, username, password, decentralizationID, staffID, deleted):
        self.AccountID = accountID
        self.username = username
        self.password = password
        self.decentralizationID = decentralizationID
        self.staffID = staffID
        self.deleted = deleted

    def getAccountID(self):
        return self.AccountID

    def setAccountID(self, accountID):
        self.AccountID = accountID

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getDecentralizationID(self):
        return self.decentralizationID

    def setDecentralizationID(self, decentralizationID):
        self.decentralizationID = decentralizationID

    def getStaffID(self):
        return self.staffID

    def setStaffID(self, staffID):
        self.staffID = staffID

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.accountID + " | " + self.username + " | " + self.password + " | " + self.decentralizationID + " | " + self.staffID;
