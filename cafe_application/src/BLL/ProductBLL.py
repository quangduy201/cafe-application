from typing import List

from BLL.Manager import Manager
from DAL.ProductDAL import ProductDAL
from DTO.Product import Product


class ProductBLL(Manager[Product]):
    def __init__(self):
        try:
            self.__productDAL = ProductDAL()
            self.__productList = self.searchProducts("DELETED = 0")
        except Exception:
            pass

    def getProductDAL(self) -> ProductDAL:
        return self.__productDAL

    def setProductDAL(self, productDAL: ProductDAL) -> ProductDAL:
        self.__productDAL = productDAL

    def getProductList(self) -> list:
        return self.__productList

    def setProductList(self, productList) -> list:
        self.__productList = productList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__productList)

    def addProduct(self, product: Product) -> bool:
        if (self.getIndex(product, "NAME", self.__productList)) != -1:
            print("Can't add new product. Name already exists.")
            return False
        self.__productList.append(product)
        return self.__productDAL.addProduct(product) != 0

    def updateProduct(self, product: Product) -> bool:
        self.__productList[self.getIndex(product, "PRODUCT_ID", self.__productList)] = product
        return self.__productDAL.updateProduct(product) != 0

    def deleteProduct(self, product: Product) -> bool:
        self.__productList.pop(self.getIndex(product, "PRODUCT_ID", self.__productList))
        return self.__productDAL.deleteProduct(f"PRODUCT_ID = '{product.getProductID()}'") != 0

    def searchProducts(self, *conditions: str) -> List[Product]:
        return self.__productDAL.searchProducts(*conditions)

    def findProductsBy(self, conditions: dict) -> list[Product]:
        products = self.__productList
        for key, value in conditions.items():
            products = super().findObjectsBy(key, value, products)
        return products

    def getAutoID(self) -> str:
        return super().getAutoID("PR", 3, self.searchProducts())

    def getValueByKey(self, product: Product, key: str) -> object:
        return {
            "PRODUCT_ID": product.getProductID(),
            "NAME": product.getName(),
            "CATEGORY_ID": product.getCategoryID(),
            "SIZED": product.getSized(),
            "COST": product.getCost(),
            "IMAGE": product.getImage()
        }.get(key, None)
