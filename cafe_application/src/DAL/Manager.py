from typing import Callable, List

from DAL.MySQL import MySQL


class Manager(MySQL):
    def __init__(self, tableName: str, columnsName: List[str]) -> None:
        super().__init__()
        self.__tableName = tableName
        self.__columnNames = columnsName

    def getTableName(self):
        return self.__tableName

    def getColumnNames(self):
        return self.__columnNames

    def create(self, *values) -> int:
        if values is None or len(values) != len(self.__columnNames):
            raise ValueError("Invalid number of arguments.")

        query = f"INSERT INTO `{self.__tableName}` VALUES(?{', ?'*(len(values) - 1)});"

        return self.executeUpdate(query, *values)

    def read(self, *conditions) -> List[List[object]]:
        query = f"SELECT * FROM `{self.__tableName}`"

        if conditions and len(conditions) > 0:
            query += f" WHERE {' AND '.join(conditions)}"

        query += ";"
        return self.executeQuery(query)

    def update(self, updateValues: List[object], *conditions) -> int:
        if not updateValues or len(updateValues) == 0:
            raise ValueError("Update values cannot be null or empty.")

        conditionsLength = len(conditions) if conditions and len(conditions) > 0 else 0

        setClause = ""
        if len(updateValues) == 1:
            setClause = "DELETED = ?"
        else:
            setClause = " = ?, ".join(self.__columnNames) + " = ?"

        query = f"UPDATE `{self.__tableName}` SET {setClause}"

        if conditionsLength > 0:
            query += f" WHERE {' AND '.join(conditions)}"

        query += ";"
        return self.executeUpdate(query, *updateValues)

    def delete(self, *conditions) -> int:
        query = f"DELETE FROM `{self.__tableName}`"
        values = []

        if conditions and len(conditions) > 0:
            query += f" WHERE {' AND '.join(conditions)}"

        query += ";"
        return self.executeUpdate(query, *values)

    def convert(self, data: List[List[str]], converter: Callable[[List[str]], object]) -> List[object]:
        lst = []
        for row in data:
            obj = converter(row)
            lst.append(obj)
        return lst

    def getAutoID(self, type_: str, digits: int) -> str:
        count = 0
        data = self.read()

        if len(data) == 0:
            return f"{type_}{self.formatNumberToString(1, digits)}"

        lastAccount = data[-1]
        size = f"{type_}{self.formatNumberToString(len(data), digits)}"
        id = self.__tableName.upper() + '_ID'
        if lastAccount[id] == size:
            count += len(data)
        else:
            while data[count][id] == f"{type_}{self.formatNumberToString(count + 1, digits)}":
                count += 1

        return f"{type_}{self.formatNumberToString(count + 1, digits)}"

    def formatNumberToString(self, number: int, digits: int) -> str:
        n = str(number)
        count = digits - len(n)
        return "0"*count + n
