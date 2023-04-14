class Decentralization:
    NONE = 0
    VIEW = 1
    EDIT = 2
    ALL = 3
    def __init__(self, decentralizationID = "", isSale = 0, isProduct = 0, isCategory = 0, isRecipe = 0, isImport = 0, isBill = 0, isWarehouses = 0, isAccount = 0, isStaff = 0, isCustomer = 0, isDiscount = 0, isDecentralize = 0, decentralizationName = "", deleted = False):
        self.__decentralizationID = decentralizationID
        self.__isSale = isSale
        self.__isProduct = isProduct
        self.__isCategory = isCategory
        self.__isRecipe = isRecipe
        self.__isImport = isImport
        self.__isBill = isBill
        self.__isWarehouses = isWarehouses
        self.__isAccount  = isAccount
        self.__isStaff = isStaff
        self.__isCustomer = isCustomer
        self.__isDiscount = isDiscount
        self.__isDecentralize  = isDecentralize
        self.__decentralizationName  = decentralizationName
        self.__deleted  = deleted
        self.setArray()


    def getDecentralizationID(self) -> str:
        return self.__decentralizationID

    def setDecentralizationID(self, decentralizationID) -> None:
        self.__decentralizationID = decentralizationID

    def getArray(self) -> list:
        return self.__arr

    def setArray(self) -> None:
        self.__arr = []
        self.__arr.append(self.__isSale)
        self.__arr.append(self.__isProduct)
        self.__arr.append(self.__isCategory)
        self.__arr.append(self.__isRecipe)
        self.__arr.append(self.__isImport)
        self.__arr.append(self.__isBill)
        self.__arr.append(self.__isWarehouses)
        self.__arr.append(self.__isAccount)
        self.__arr.append(self.__isStaff)
        self.__arr.append(self.__isCustomer)
        self.__arr.append(self.__isDiscount)
        self.__arr.append(self.__isDecentralize)

    def getIsSale(self) -> int:
        return self.__isSale

    def setIsSale(self, isSale) -> None:
        self.__isSale = isSale

    def getIsProduct(self) -> int:
        return self.__isProduct

    def setIsProduct(self, isProduct) -> None:
        self.__isProduct = isProduct

    def getIsCategory(self) -> int:
        return self.__isCategory

    def setIsCategory(self, isCategory) -> None:
        self.__isCategory = isCategory

    def getIsRecipe(self) -> int:
        return self.__isRecipe

    def setIsRecipe(self, isRecipe) -> None:
        self.__isRecipe = isRecipe

    def getIsImport(self) -> int:
        return self.__isImport

    def setIsImport(self, isImport) -> None:
        self.__isImport = isImport

    def getIsBill(self) -> int:
        return self.__isBill

    def setIsBill(self, isBill) -> None:
        self.__isBill = isBill

    def getIsWarehouses(self) -> int:
        return self.__isWarehouses

    def setIsWarehouses(self, isWarehouses) -> None:
        self.__isWarehouses = isWarehouses

    def getIsAccount(self) -> int:
        return self.__isAccount

    def setIsAccount(self, isAccount) -> None:
        self.__isAccount = isAccount

    def getIsStaff(self) -> int:
        return self.__isStaff

    def setIsStaff(self, isStaff) -> None:
        self.__isStaff = isStaff

    def getIsCustomer(self) -> int:
        return self.__isCustomer

    def setIsCustomer(self, isCustomer) -> None:
        self.__isCustomer = isCustomer

    def getIsDiscount(self) -> int:
        return self.__isDiscount

    def setIsDiscount(self, isDiscount) -> None:
        self.__isDiscount = isDiscount

    def getIsDecentralize(self) -> int:
        return self.__isDecentralize

    def setIsDecentralize(self, isDecentralize) -> None:
        self.__isDecentralize = isDecentralize

    def getDecentralizationName(self) -> str:
        return self.__decentralizationName

    def setDecentralizationName(self, decentralizationName) -> None:
        self.__decentralizationName = decentralizationName

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        self.string = []
        for i in self.__arr:
            if i == 0:
                self.string.append ("Không")
            if i == 1:
                self.string.append ("Xem")
            if i == 2:
                self.string.append ("Sửa")
            if i == 3:
                self.string.append ("Xem và sửa")
        s=" | ".join(self.string)
        return f"{self.__decentralizationID} | " + f"{s} | " + f"{self.__decentralizationName}"
