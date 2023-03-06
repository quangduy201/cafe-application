from database.run_query import run_query
from typing import List, Tuple

class Manager:
    """Base class that handles database operations."""

    def __init__(self, table_name: str, columns_name: Tuple) -> None:
        self.table_name = table_name
        self.columns_name = columns_name

    def create(self, *args, **kwargs) -> None:
        """Creates a new record in the database."""
        query = f"INSERT INTO {self.table_name} VALUES ({','.join(['%s']*len(self.columns_name))})"
        values = tuple(kwargs.get(col, None) for col in self.columns_name)
        run_query(query, values)

    def read(self, *args, **kwargs) -> List[Tuple]:
        """Reads records from the database that match the given criteria."""
        query = f"SELECT * FROM {self.table_name}"
        conditions = []
        for col, value in kwargs.items():
            if value is not None:
                conditions.append(f"{col}=%s")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        values = tuple(kwargs.values())
        return run_query(query, values)

    def update(self, *args, **kwargs) -> None:
        """Updates records in the database that match the given criteria."""
        set_values = []
        for col, value in kwargs.items():
            if value is not None:
                set_values.append(f"{col}=%s")
        query = f"UPDATE {self.table_name} SET {','.join(set_values)}"
        conditions = []
        for col, value in args:
            if value is not None:
                conditions.append(f"{col}=%s")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        values = tuple(kwargs.values()) + tuple(val for _, val in args)
        run_query(query, values)

    def delete(self, *args, **kwargs) -> None:
        """Deletes records from the database that match the given criteria."""
        query = f"DELETE FROM {self.table_name}"
        conditions = []
        for col, value in kwargs.items():
            if value is not None:
                conditions.append(f"{col}=%s")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        values = tuple(kwargs.values())
        run_query(query, values)
