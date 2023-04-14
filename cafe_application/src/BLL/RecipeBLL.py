from typing import List

from BLL.Manager import Manager
from DAL.RecipeDAL import RecipeDAL
from DTO.Recipe import Recipe


class RecipeBLL(Manager[Recipe]):
    def __init__(self):
        try:
            self.__recipeDAL = RecipeDAL()
            self.__recipeList = self.searchRecipes("DELETED = 0")
        except Exception:
            pass

    def getRecipeDAL(self) -> RecipeDAL:
        return self.__recipeDAL

    def setRecipeDAL(self, recipeDAL: RecipeDAL) -> RecipeDAL:
        self.__recipeDAL = recipeDAL

    def getRecipeList(self) -> list:
        return self.__recipeList

    def setRecipeList(self, recipeList) -> list:
        self.__recipeList = recipeList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__recipeList)

    def addRecipe(self, recipe: Recipe) -> bool:
        self.__recipeList.append(recipe)
        return self.__recipeDAL.addRecipe(recipe) != 0

    def updateRecipe(self, recipe: Recipe) -> bool:
        self.__recipeList[self.getIndex(recipe, "RECIPE_ID", self.__recipeList)] = recipe
        return self.__recipeDAL.updateRecipe(recipe) != 0

    def deleteRecipe(self, recipe: Recipe) -> bool:
        self.__recipeList.pop(self.getIndex(recipe, "RECIPE_ID", self.__recipeList))
        return self.__recipeDAL.deleteRecipe(f"RECIPE_ID = '{recipe.getRecipeID()}'") != 0

    def searchRecipes(self, *conditions: str) -> List[Recipe]:
        return self.__recipeDAL.searchRecipes(*conditions)

    def findRecipesBy(self, conditions: dict) -> list[Recipe]:
        recipes = self.__recipeList
        for key, value in conditions.items():
            recipes = super().findObjectsBy(key, value, recipes)
        return recipes

    def getAutoID(self) -> str:
        return super().getAutoID("RE", 3, self.searchRecipes())

    def getValueByKey(self, recipe: Recipe, key: str) -> object:
        return {
            "RECIPE_ID": recipe.getRecipeID(),
            "PRODUCT_ID": recipe.getProductID(),
            "INGREDIENT_ID": recipe.getIngredientID(),
            "MASS": recipe.getMass(),
            "UNIT": recipe.getUnit()
        }.get(key, None)
