from typing import List

from BLL.Manager import Manager
from DAL.IngredientDAL import IngredientDAL
from DTO.Ingredient import Ingredient


class IngredientBLL(Manager[Ingredient]):
    def __init__(self):
        try:
            self.__ingredientDAL = IngredientDAL()
            self.__ingredientList = self.searchIngredients("DELETED = 0")
        except Exception:
            pass

    def getIngredientDAL(self) -> IngredientDAL:
        return self.__ingredientDAL

    def setIngredientDAL(self, ingredientDAL: IngredientDAL) -> IngredientDAL:
        self.__ingredientDAL = ingredientDAL

    def getIngredientList(self) -> list:
        return self.__ingredientList

    def setIngredientList(self, ingredientList) -> list:
        self.__ingredientList = ingredientList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__ingredientList)

    def addIngredient(self, ingredient: Ingredient) -> bool:
        if (self.getIndex(ingredient, "NAME", self.__ingredientList)) != -1:
            print("Can't add new ingredient. Name already exists.")
            return False
        self.__ingredientList.append(ingredient)
        return self.__ingredientDAL.addIngredient(ingredient) != 0

    def updateIngredient(self, ingredient: Ingredient) -> bool:
        self.__ingredientList[self.getIndex(ingredient, "INGREDIENT_ID", self.__ingredientList)] = ingredient
        return self.__ingredientDAL.updateIngredient(ingredient) != 0

    def deleteIngredient(self, ingredient: Ingredient) -> bool:
        self.__ingredientList.pop(self.getIndex(ingredient, "INGREDIENT_ID", self.__ingredientList))
        return self.__ingredientDAL.deleteIngredient(f"INGREDIENT_ID = '{ingredient.getIngredientID()}'") != 0

    def searchIngredients(self, *conditions: str) -> List[Ingredient]:
        return self.__ingredientDAL.searchIngredients(*conditions)

    def findIngredientsBy(self, conditions: dict) -> list[Ingredient]:
        ingredients = self.__ingredientList
        for key, value in conditions.items():
            ingredients = super().findObjectsBy(key, value, ingredients)
        return ingredients

    def getAutoID(self) -> str:
        return super().getAutoID("ING", 3, self.searchIngredients())

    def getValueByKey(self, ingredient: Ingredient, key: str) -> object:
        return {
            "INGREDIENT_ID": ingredient.getIngredientID(),
            "NAME": ingredient.getName(),
            "QUANTITY": ingredient.getQuantity(),
            "UNIT": ingredient.getUnit(),
            "SUPPLIER_ID": ingredient.getSupplierID()
        }.get(key, None)
