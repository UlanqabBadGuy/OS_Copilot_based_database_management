import mysql.connector

def select(column, table, condition=""):
    """
    Executes a SQL SELECT query on a specified table with condition(optional) and returns the results as a string.

    Args:
    - column (str): The column(s) to be retrieved from the table. Can be a single column or a comma-separated list for multiple columns.
    - table (str): The name of the table from which to retrieve the data.
    - condition (str, optional): A SQL condition to filter the results. Defaults to an empty string, meaning no condition is applied.

    Returns:
    - str: The query results, with each row represented as a string and separated by a newline character.

    Raises:
    - Exception: Propagates any exception encountered during the database operation.
    """
    try:
        connection = mysql.connector.connect(
            host='154.201.65.130',
            user='user',
            password='password',
            database='oscopilot'
        )
        
        with connection.cursor() as cursor:
            query = f"SELECT {column} FROM {table}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query)
            results = cursor.fetchall()
            result_string = "\n".join(str(row) for row in results)
            return result_string
    
    except Exception as e:
        raise e
    
    finally:
        if connection.is_connected():
            connection.close()

