import mysql.connector

def delete_data(table_name, where_clause):
    """
    Deletes data from a specified table in a MySQL database based on a WHERE clause.

    Args:
    table_name (str): Name of the table from which data will be deleted.
    where_clause (str): The condition to specify which rows to delete (e.g., "id = 1").

    Returns:
    None
    """
    conn = mysql.connector.connect(
        host='154.201.65.130',
        user='user',
        password='password',
        database='oscopilot'
    )
    cursor = conn.cursor()

    sql_query = f'DELETE FROM {table_name} WHERE {where_clause}'

    try:
        cursor.execute(sql_query)
        conn.commit() # 提交更改，将删除操作应用到数据库中
        print(f"Data deleted successfully from {table_name} where {where_clause}")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
