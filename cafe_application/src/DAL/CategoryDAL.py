from typing import List

from DAL.Manager import Manager
from DTO.Category import Category


class CategoryDAL(Manager):
    def __init__(self):
        super().__init__("category", [
            "CATEGORY_ID",
            "NAME",
            "QUANTITY",
            "DELETED"
        ])

    def convertToCategories(self, data: List[List[object]]) -> List[Category]:
        return self.convert(data, lambda row: Category(
            row['CATEGORY_ID'],
            row['NAME'],
            row['QUANTITY'],
            bool(row['DELETED'])
        ))

    def insertCategory(self, category: Category) -> int:
        try:
            return self.create(
                category.getCategoryID(),
                category.getName(),
                category.getQuantity(),
                False
            ) # Category khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in CategoryDAL.insertCategory(): {e}")
        return 0

    def updateCategory(self, category: Category) -> int:
        try:
            updateValues = [
                category.getCategoryID(),
                category.getName(),
                category.getQuantity(),
                category.isDeleted()
            ]
            return self.update(updateValues, f"CATEGORY_ID = {Category.getCategoryID()}")
        except Exception as e:
            print(f"Error occurred in CategoryDAL.updateCategory(): {e}")
        return 0

    def removeCategory(self, *conditions: str) -> int:
        try:
            updateValues = [1]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in CategoryDAL.deleteCategory(): {e}")
        return 0

    def searchCategories(self, *conditions: str) -> List[Category]:
        try:
            return self.convertToCategories(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in CategoryDAL.searchCategories(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("CA", 2)
        except Exception as e:
            print(f"Error occurred in CategoryDAL.getAutoID(): {e}")
        return ""
