import mysql.connector
import pandas as pd

def search_table(table_name, query_columns='*', where_clause=None):
    """
    Fetches data from a table in a MySQL database and returns it as a pandas DataFrame.

    Args:
    table_name (str): Name of the table to fetch data from.
    query_columns (str): Columns to select, defaults to '*'.
    where_clause (str): Optional WHERE clause to filter data.

    Returns:
    pd.DataFrame: A DataFrame containing the query result.
    """
    conn = mysql.connector.connect(
        host='154.201.65.130',
        user='user',
        password='password',
        database='oscopilot'
    )
    cursor = conn.cursor(dictionary=True)
    
    sql_query = f'SELECT {query_columns} FROM {table_name}'
    if where_clause:
        sql_query += f' WHERE {where_clause}'

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print("Data fetched successfully")
        return df
    except mysql.connector.Error as e:
        raise (f"An error occurred: {e}")
        return pd.DataFrame()
    finally:
        cursor.close()
        conn.close()

