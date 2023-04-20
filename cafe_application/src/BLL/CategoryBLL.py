from typing import List

from BLL.Manager import Manager
from DAL.CategoryDAL import CategoryDAL
from DTO.Category import Category


class CategoryBLL(Manager[Category]):
    def __init__(self):
        try:
            self.__categoryDAL = CategoryDAL()
            self.__categoryList = self.searchCategories("DELETED = 0")
        except Exception:
            pass

    def getCategoryDAL(self) -> CategoryDAL:
        return self.__categoryDAL

    def setCategoryDAL(self, categoryDAL: CategoryDAL) -> CategoryDAL:
        self.__categoryDAL = categoryDAL

    def getCategoryList(self) -> list:
        return self.__categoryList

    def setCategoryList(self, categoryList) -> list:
        self.__categoryList = categoryList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__categoryList)

    def addCategory(self, category: Category) -> bool:
        if (self.getIndex(category, "NAME", self.__categoryList)) != -1:
            print("Can't add new category. Name already exists.")
            return False
        self.__categoryList.append(category)
        return self.__categoryDAL.addCategory(category) != 0

    def updateCategory(self, category: Category) -> bool:
        self.__categoryList[self.getIndex(category, "CATEGORY_ID", self.__categoryList)] = category
        return self.__categoryDAL.updateCategory(category) != 0

    def deleteCategory(self, category: Category) -> bool:
        self.__categoryList.pop(self.getIndex(category, "CATEGORY_ID", self.__categoryList))
        return self.__categoryDAL.deleteCategory(f"CATEGORY_ID = '{category.getCategoryID()}'") != 0

    def searchCategories(self, *conditions: str) -> List[Category]:
        return self.__categoryDAL.searchCategories(*conditions)

    def findCategoriesBy(self, conditions: dict) -> list[Category]:
        categories = self.__categoryList
        for key, value in conditions.items():
            categories = super().findObjectsBy(key, value, categories)
        return categories

    def getAutoID(self) -> str:
        return super().getAutoID("CA", 2, self.searchCategories())

    def getValueByKey(self, category: Category, key: str) -> object:
        return {
            "CATEGORY_ID": category.getCategoryID(),
            "NAME": category.getName(),
            "QUANTITY": category.getQuantity()
        }.get(key, None)
