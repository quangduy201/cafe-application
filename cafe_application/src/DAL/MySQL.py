import mysql.connector
from mysql.connector import Error
from datetime import datetime

class MySQL:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cafe-management"
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def getConnection(self):
        return self.connection

    def getCursor(self):
        return self.cursor

    def executeQuery(self, query, *values):
        formatted_query = self.formatQuery(query, *values)
        result = []
        try:
            self.cursor.execute(formatted_query)
            column_names = [desc[0] for desc in self.cursor.description]
            for row in self.cursor.fetchall():
                result.append(dict(zip(column_names, row)))
        except Error as e:
            print(f"Error while executing query: {e}")
        return result

    def executeUpdate(self, query, *values):
        formatted_query = self.formatQuery(query, *values)
        try:
            self.cursor.execute(formatted_query)
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error while executing update: {e}")

    def formatQuery(self, query, *values):
        for value in values:
            if isinstance(value, str) or isinstance(value, datetime):
                string_value = f"'{value}'"
            elif isinstance(value, bool):
                string_value = "1" if value else "0"
            else:
                string_value = str(value)
            query = query.replace("?", string_value, 1)
        return query
