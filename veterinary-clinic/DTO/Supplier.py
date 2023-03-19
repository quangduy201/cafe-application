class Supplier:
    def __init__(self, supplierID, name, phone, address, email, price, deleted):
        self.supplierID = supplierID
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email
        self.price = price
        self.deleted = deleted

    def getSupplierID(self):
        return self.supplierID

    def setSupplierID(self, supplierID):
        self.supplierID = supplierID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.supplierID + " | " + self.name + " | " + self.phone + " | " + self.address + " | " + self.email + " | " + self.price


