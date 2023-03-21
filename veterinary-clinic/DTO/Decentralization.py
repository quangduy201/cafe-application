class Decentralization:
    NONE = 0
    VIEW = 1
    EDIT = 2
    ALL = 3
    def __init__(self, decentralizationID = "", isRecipe = 0, isProduct = 0, isCategory = 0, isBill = 0, isDiscount = 0, isCustomer = 0, isWarehouses = 0, isStaff = 0, isAccount = 0, isDecentralize = 0, decentralizationName = 0, deleted = False):
        self.__decentralizationID = decentralizationID
        self.__isRecipe = isRecipe
        self.__isProduct = isProduct
        self.__isCategory = isCategory
        self.__isBill = isBill
        self.__isDiscount = isDiscount
        self.__isCustomer = isCustomer
        self.__isWarehouses  = isWarehouses
        self.__isStaff  = isStaff
        self.__isAccount  = isAccount
        self.__isDecentralize  = isDecentralize
        self.__decentralizationName  = decentralizationName
        self.__deleted  = deleted


    def getDecentralizationID(self):
        return self.__decentralizationID

    def setDecentralizationID(self, decentralizationID):
        self.__decentralizationID = decentralizationID

    def getIsRecipe(self):
        return self.__isRecipe

    def setIsRecipe(self, isRecipe):
        self.__isRecipe = isRecipe

    def getIsProduct(self):
        return self.__isProduct

    def setIsProduct(self, isProduct):
        self.__isProduct = isProduct

    def getIsCategory(self):
        return self.__isCategory

    def setIsCategory(self, isCategory):
        self.__isCategory = isCategory

    def getIsBill(self):
        return self.__isBill

    def setIsBill(self, isBill):
        self.__isBill = isBill

    def getIsDiscount(self):
        return self.__isDiscount

    def setIsDiscount(self, isDiscount):
        self.__isDiscount = isDiscount

    def getIsCustomer(self):
        return self.__isCustomer

    def setIsCustomer(self, isCustomer):
        self.__isCustomer = isCustomer

    def getIsWarehouses(self):
        return self.__isWarehouses

    def setIsWarehouses(self, isWarehouses):
        self.__isWarehouses = isWarehouses

    def getIsStaff(self):
        return self.__isStaff

    def setIsStaff(self, isStaff):
        self.__isStaff = isStaff

    def getIsAccount(self):
        return self.__isAccount

    def setIsAccount(self, isAccount):
        self.__isAccount = isAccount

    def getIsDecentralize(self):
        return self.__isDecentralize

    def setIsDecentralize(self, isDecentralize):
        self.__isDecentralize = isDecentralize

    def getDecentralizationName(self):
        return self.__decentralizationName

    def setDecentralizationName(self, decentralizationName):
        self.__decentralizationName = decentralizationName

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted):
        self.__deleted = deleted

    def __str__(self):
        return self.__decentralizationID + " | " \
            + self.__isRecipe + " | " \
            + self.__isProduct + " | " \
            + self.__isCategory + " | " \
            + self.__isBill + " | " \
            + self.__isDiscount + " | " \
            + self.__isCustomer + " | " \
            + self.__isWarehouses + " | " \
            + self.__isStaff + " | " \
            + self.__isAccount + " | " \
            + self.__isDecentralize + " | " \
            + self.__decentralizationName
