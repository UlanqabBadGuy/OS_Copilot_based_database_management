import mysql.connector
import pandas as pd

def search_all_tables():
    """
    search all table names, column names, and their data types
    returns them as a pandas DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing table names, column names, and data types.
    """
    conn = mysql.connector.connect(
        host='154.201.65.130',
        user='user',
        password='password',
        database='oscopilot'
    )
    cursor = conn.cursor(dictionary=True)
    
    # Query to get all table names, column names, and data types
    sql_query = """
    SELECT 
        TABLE_NAME, 
        COLUMN_NAME, 
        DATA_TYPE
    FROM 
        INFORMATION_SCHEMA.COLUMNS
    WHERE 
        TABLE_SCHEMA = 'oscopilot'
    ORDER BY 
        TABLE_NAME, ORDINAL_POSITION;
    """

    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print("Table and column information fetched successfully")
        return df
    except mysql.connector.Error as e:
        raise(f"An error occurred: {e}")
        # return pd.DataFrame()
    finally:
        cursor.close()
        conn.close()



