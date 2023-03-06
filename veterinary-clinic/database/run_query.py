import mysql.connector

def run_query(query: str, values: tuple = None) -> list:
    """Executes the SQL query on the veterinary_clinic database and returns the result.

    Args:
        query (str):
        values (tuple, optional): A tuple of values to substitute into the query (if necessary). Defaults to None.

    Returns:
        list: A list of tuples representing the result of the query.

    Raise:
        mysql.connector.Error: If there was an error executing the query.

    """
    try:
        with mysql.connector.connect(
            host="localhost",
            user="root",
            # password="password",
            database="veterinary_clinic"
        ) as mydb:
            with mydb.cursor() as mycursor:
                mycursor.execute(query, values) if values else mycursor.execute(query)
                result = mycursor.fetchall()
                mydb.commit()
                return result
    except mysql.connector.Error as error:
        print(f"Error executing query: {error}")
        return []
