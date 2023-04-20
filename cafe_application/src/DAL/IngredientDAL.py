from typing import List

from DAL.Manager import Manager
from DTO.Ingredient import Ingredient


class IngredientDAL(Manager):
    def __init__(self):
        super().__init__("ingredient", [
            "INGREDIENT_ID",
            "NAME",
            "QUANTITY",
            "UNIT",
            "SUPPLIER_ID",
            "DELETED"
        ])

    def convertToIngredients(self, data: List[List[object]]) -> List[Ingredient]:
        return self.convert(data, lambda row: Ingredient(
            row['INGREDIENT_ID'],
            row['NAME'],
            row['QUANTITY'],
            row['UNIT'],
            row['SUPPLIER_ID'],
            bool(row['DELETED'])
        ))

    def addIngredient(self, ingredient: Ingredient) -> int:
        try:
            return self.create(
                ingredient.getIngredientID(),
                ingredient.getName(),
                ingredient.getQuantity(),
                ingredient.getUnit(),
                ingredient.getSupplierID(),
                False
            ) # ingredient khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in IngredientDAL.addIngredient(): {e}")
        return 0

    def updateIngredient(self, ingredient: Ingredient) -> int:
        try:
            updateValues = [
                ingredient.getIngredientID(),
                ingredient.getName(),
                ingredient.getQuantity(),
                ingredient.getUnit(),
                ingredient.getSupplierID(),
                ingredient.isDeleted()
            ]
            return self.update(updateValues, f"INGREDIENT_ID = '{ingredient.getIngredientID()}'")
        except Exception as e:
            print(f"Error occurred in IngredientDAL.updateIngredient(): {e}")
        return 0

    def deleteIngredient(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in IngredientDAL.deleteIngredient(): {e}")
        return 0

    def searchIngredients(self, *conditions: str) -> List[Ingredient]:
        try:
            return self.convertToIngredients(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in IngredientDAL.searchIngredients(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("ING", 3)
        except Exception as e:
            print(f"Error occurred in IngredientDAL.getAutoID(): {e}")
        return ""
