class Customer:
    def __init__(self, customerID, name, gender, dateOfBirth, phone, membership, dateOfSup, deleted):
        self.customerID = customerID
        self.name = name
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.phone = phone
        self.membership = membership
        self.dateOfSup = dateOfSup
        self.deleted = deleted

    def getCustomerID(self):
        return self.customerID

    def setCustomerID(self, customerID):
        self.customerID = customerID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getDateOfBirth(self):
        return self.dateOfBirth

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def isMembership(self):
        return self.membership

    def setMembership(self, membership):
        self.membership = membership

    def getDateOfSup(self):
        return self.dateOfSup

    def setDateOfSup(self, dateOfSup):
        self.dateOfSup = dateOfSup

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.customerID + " | " + self.name + " | " + self.gender + " | " + self.dateOfBirth + " | " + self.phone + " | " + self.membership + " | " + self.dateOfSup
