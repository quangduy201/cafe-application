from typing import List

from DAL.Manager import Manager
from DTO.Recipe import Recipe


class RecipeDAL(Manager):
    def __init__(self):
        super().__init__("recipe", [
            "RECIPE_ID",
            "PRODUCT_ID",
            "INGREDIENT_ID",
            "MASS",
            "UNIT",
            "DELETED"
        ])

    def convertToRecipes(self, data: List[List[object]]) -> List[Recipe]:
        return self.convert(data, lambda row: Recipe(
            row['RECIPE_ID'],
            row['PRODUCT_ID'],
            row['INGREDIENT_ID'],
            row['MASS'],
            row['UNIT'],
            bool(row['DELETED'])
        ))

    def addRecipe(self, recipe: Recipe) -> int:
        try:
            return self.create(
                recipe.getRecipeID(),
                recipe.getProductID(),
                recipe.getIngredientID(),
                recipe.getMass(),
                recipe.getUnit(),
                False
            ) # recipe khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in RecipeDAL.addRecipe(): {e}")
        return 0

    def updateRecipe(self, recipe: Recipe) -> int:
        try:
            updateValues = [
                recipe.getRecipeID(),
                recipe.getProductID(),
                recipe.getIngredientID(),
                recipe.getMass(),
                recipe.getUnit(),
                recipe.isDeleted()
            ]
            return self.update(updateValues, f"RECIPE_ID = '{recipe.getRecipeID()}'")
        except Exception as e:
            print(f"Error occurred in RecipeDAL.updateRecipe(): {e}")
        return 0

    def deleteRecipe(self, *conditions: str) -> int:
        try:
            updateValues = [True]
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

