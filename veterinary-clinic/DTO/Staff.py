class Staff:
    def __init__(self, staffID, name, gender, dateOfBirth, address, phone, email, salary, dateOfEntry, deleted):
        self.staffID = staffID
        self.name = name
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phone = phone
        self.email = email
        self.salary = salary
        self.dateOfEntry = dateOfEntry
        self.deleted = deleted

    def getStaffID(self):
        return self.staffID

    def setStaffID(self, staffID):
        self.staffID = staffID

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

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

    def getDateOfEntry(self):
        return self.dateOfEntry

    def setDateOfEntry(self, dateOfEntry):
        self.dateOfEntry = dateOfEntry

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.staffID + " | " + self.name + " | " + self.gender + " | " + self.dateOfBirth + " | " + self.address + " | " + self.phone + " | " + self.email + " | " + self.salary + " | " + self.dateOfEntry
