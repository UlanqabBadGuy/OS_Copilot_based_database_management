import mysql.connector
import pandas as pd


# 查找某个数字左右的（e.g. 找出20岁左右的人）
def select_numeric_range(column, table, condition, min_value, max_value):
    """
    Performs a numeric range search in a specified table.

    Args:
    column (str): Column(s) to select.
    table (str): Table name.
    condition (str): The column name for the numeric condition (e.g., "age" or "birth_year").
    min_value (int or float): The minimum value for the range search.
    max_value (int or float): The maximum value for the range search.

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

    # 构建范围查询的 WHERE 子句
    where_clause = f"{condition} BETWEEN %s AND %s"
    sql_query = f'SELECT {column} FROM {table} WHERE {where_clause}'

    try:
        cursor.execute(sql_query, (min_value, max_value))
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        print("Numeric range search completed successfully")
        return df
    except mysql.connector.Error as e:
        raise (f"An error occurred: {e}")
        return pd.DataFrame()
    finally:
        cursor.close()
        conn.close()
