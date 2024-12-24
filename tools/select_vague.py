import mysql.connector
import pandas as pd

def select_vague(column, table, condition, vague):
    """
    Performs a fuzzy search in a specified table.

    Args:
    column (str): Column to select.
    table (str): Name of the table to query.
    condition (str): The condition to filter data (e.g., "name LIKE %s").
    vague (str): The value for the fuzzy search (e.g., "%John%").

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

    sql_query = f'SELECT {column} FROM {table} WHERE {condition}'

    try:
        cursor.execute(sql_query, (vague,))
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print("Fuzzy search completed successfully")
        return df
    except mysql.connector.Error as e:
        raise (f"An error occurred: {e}")
        return pd.DataFrame()
    finally:
        cursor.close()
        conn.close()
