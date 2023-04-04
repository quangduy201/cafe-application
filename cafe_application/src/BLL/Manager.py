from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Manager(ABC, Generic[T]):
    def __init__(self):
        super().__init__()

    def getData(self, objectList: list[T]) -> list[list[object]]:
        data = []
        for obj in objectList:
            data.append(obj.__str__().split(" | "))
        return data

    def getAutoID(self, type: str, digits: int, objectList: list[T]) -> str:
        count = 0
        if len(objectList) == 0:
            return type + self.formatNumberToString(1, digits)

        lastObject: T = objectList[-1]
        if lastObject.__str__().split(" | ")[0] == type + self.formatNumberToString(len(objectList), digits):
            count += len(objectList)
        else:
            while objectList[count].__str__().split(" | ")[0] == type + self.formatNumberToString(count + 1, digits):
                count += 1
        return type + self.formatNumberToString(count + 1, digits)

    def formatNumberToString(self, number: int, digits: int):
        n = str(number)
        count = digits - len(n)
        return '0' * count + n

    def getObjectsProperty(self, key: str, objectList: list[T]):
        listOfProperties = []
        for obj in objectList:
            listOfProperties.append(self.getValueByKey(obj, key))
        return listOfProperties

    def findObjectsBy(self, key: str, value: object, objectList: list[T]):
        objects = []
        for obj in objectList:
            if self.getValueByKey(obj, key) == value:
                objects.append(obj)
        return objects

    def getIndex(self, object_: T, key: str, objectList: list[T]):
        for i, obj in enumerate(objectList):
            if self.getValueByKey(obj, key) == self.getValueByKey(object_, key):
                return i
        return -1

    @abstractmethod
    def getValueByKey(self, object: T, key: str) -> object:
        pass
