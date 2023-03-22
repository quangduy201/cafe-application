from typing import List

from DAL.Manager import Manager
from DTO.Product import Product


class ProductDAL(Manager):
    def __init__(self):
        super().__init__("Product", [
            "PRODUCT_ID",
            "NAME",
            "CATEGORY_ID",
            "COST",
            "DELETED"
        ])

    def convertToProducts(self, data: List[List[object]]) -> List[Product]:
        return self.convert(data, lambda row: Product(
            row['PRODUCT_ID'],
            row['NAME'],
            row['CATEGORY_ID'],
            row['COST'],
            bool(row['DELETED'])
        ))

    def insertProduct(self, product: Product) -> int:
        try:
            return self.create(
                product.getProductID(),
                product.getName(),
                product.getCategoryID(),
                product.getSize(),
                product.getCost(),
                False
            ) # Product khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in ProductDAL.insertProduct(): {e}")
        return 0

    def updateProduct(self, product: Product) -> int:
        try:
            updateValues = [
                product.getProductID(),
                product.getName(),
                product.getCategoryID(),
                product.getSize(),
                product.getCost(),
                Product.isDeleted()
            ]
            return self.update(updateValues, f"PRODUCT_ID = {Product.getProductID()}")
        except Exception as e:
            print(f"Error occurred in ProductDAL.updateProduct(): {e}")
        return 0

    def removeProduct(self, *conditions: str) -> int:
        try:
            updateValues = [1]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in ProductDAL.deleteProduct(): {e}")
        return 0

    def searchProducts(self, *conditions: str) -> List[Product]:
        try:
            return self.convertToProducts(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in ProductDAL.searchProducts(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("PR", 3)
        except Exception as e:
            print(f"Error occurred in ProductDAL.getAutoID(): {e}")
        return ""
