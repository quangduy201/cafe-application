from typing import List

from DAL.Manager import Manager
from DTO.Recipe import Recipe


class RecipeDAL(Manager):
    def __init__(self):
        super().__init__("recipe", [
            "PRODUCT_ID",
            "INGREDIENT_ID",
            "MASS",
            "UNIT",
            "DELETED"
        ])

    def convertToRecipes(self, data: List[List[object]]) -> List[Recipe]:
        return self.convert(data, lambda row: Recipe(
            row['PRODUCT_ID'],
            row['INGREDIENT_ID'],
            row['MASS'],
            row['UNIT'],
            bool(row['DELETED'])
        ))

    def insertRecipe(self, recipe: Recipe) -> int:
        try:
            return self.create(
                recipe.getProductID(),
                recipe.getIngredientID(),
                recipe.getMass(),
                recipe.getUnit(),
                False
            ) # Recipe khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in RecipeDAL.insertRecipe(): {e}")
        return 0

    def updateRecipe(self, recipe: Recipe) -> int:
        try:
            updateValues = [
                recipe.getProductID(),
                recipe.getIngredientID(),
                recipe.getMass(),
                recipe.getUnit(),
                Recipe.isDeleted()
            ]
            return self.update(updateValues, f"PRODUCT_ID = {Recipe.getProductID()}", f"INGREDIENT_ID = {Recipe.getIngredientID()}")
        except Exception as e:
            print(f"Error occurred in RecipeDAL.updateRecipe(): {e}")
        return 0

    def removeRecipe(self, *conditions: str) -> int:
        try:
            updateValues = [1]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in RecipeDAL.deleteRecipe(): {e}")
        return 0

    def searchRecipes(self, *conditions: str) -> List[Recipe]:
        try:
            return self.convertToRecipes(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in RecipeDAL.searchRecipes(): {e}")
        return []

