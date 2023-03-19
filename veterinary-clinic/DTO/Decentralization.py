class Decentralization:
    def __init__(self, decentralizationID, isRecipe, isProduct, isCategory, isBill, isDiscount, isCustomer, isWarehouses, isStaff, isAccount, isDecentralize, decentralizationName, deleted):
        self.decentralizationID = decentralizationID
        self.isRecipe = isRecipe
        self.isProduct = isProduct
        self.isCategory = isCategory
        self.isBill = isBill
        self.isDiscount = isDiscount
        self.isCustomer = isCustomer
        self.isWarehouses  = isWarehouses
        self.isStaff  = isStaff
        self.isAccount  = isAccount
        self.isDecentralize  = isDecentralize
        self.decentralizationName  = decentralizationName
        self.deleted  = deleted
        self.__NONE = 0
        self.__VIEW = 1
        self.__EDIT = 2
        self.__ALL = 3

    def getDecentralizationID(self):
        return self.decentralizationID

    def setDecentralizationID(self, decentralizationID):
        self.decentralizationID = decentralizationID

    def getIsRecipe(self):
        return self.isRecipe

    def setIsRecipe(self, isRecipe):
        self.isRecipe = isRecipe

    def getIsProduct(self):
        return self.isProduct

    def setIsProduct(self, isProduct):
        self.isProduct = isProduct

    def getIsCategory(self):
        return self.isCategory

    def setIsCategory(self, isCategory):
        self.isCategory = isCategory

    def getIsBill(self):
        return self.isBill

    def setIsBill(self, isBill):
        self.isBill = isBill

    def getIsDiscount(self):
        return self.isDiscount

    def setIsDiscount(self, isDiscount):
        self.isDiscount = isDiscount

    def getIsCustomer(self):
        return self.isCustomer

    def setIsCustomer(self, isCustomer):
        self.isCustomer = isCustomer

    def getIsWarehouses(self):
        return self.isWarehouses

    def setIsWarehouses(self, isWarehouses):
        self.isWarehouses = isWarehouses

    def getIsStaff(self):
        return self.isStaff

    def setIsStaff(self, isStaff):
        self.isStaff = isStaff

    def getIsAccount(self):
        return self.isAccount

    def setIsAccount(self, isAccount):
        self.isAccount = isAccount

    def getIsDecentralize(self):
        return self.isDecentralize

    def setIsDecentralize(self, isDecentralize):
        self.isDecentralize = isDecentralize

    def getDecentralizationName(self):
        return self.decentralizationName

    def setDecentralizationName(self, decentralizationName):
        self.decentralizationName = decentralizationName

    def isDeleted(self):
        return self.deleted

    def setDeleted(self, deleted):
        self.deleted = deleted

    def toString(self):
        return self.decentralizationID + " | " + self.isRecipe + " | " + self.isProduct + " | " + self.isCategory + " | " + self.isBill + " | " + self.isDiscount + " | " + self.isCustomer + " | " + self.isWarehouses + " | " + self.isStaff + " | " + self.isAccount + " | " + self.isDecentralize + " | " + self.decentralizationName
