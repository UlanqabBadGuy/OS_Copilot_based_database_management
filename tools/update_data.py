import mysql.connector

def update_data(table_name, data, where_clause):
    """
    Updates data in a specified table based on a WHERE clause.

    Args:
    table_name (str): Name of the table to update data.
    data (dict): A dictionary where keys are column names and values are the new data to update.
    data = {
    'column1': 'new_value1',
    'column2': 'new_value2'
    }
    where_clause (str): The condition to specify which rows to update (e.g., "id = 1").

    Returns:
    None
    """
    # 检查 where_clause 是否为空
    if not where_clause:
        print("Error: WHERE clause is required to prevent updating all rows.")
        return

    conn = mysql.connector.connect(
        host='154.201.65.130',
        user='user',
        password='password',
        database='oscopilot'
    )
    cursor = conn.cursor()

    set_clause = ', '.join([f"{column} = %s" for column in data.keys()])
    sql_query = f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}'

    try:
        #如果数据库中不存在符合条件的行，那么 UPDATE 语句会执行，但不会更新任何行
        cursor.execute(sql_query, tuple(data.values()))
        conn.commit()
        print(f"Data updated successfully in {table_name} where {where_clause}")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
