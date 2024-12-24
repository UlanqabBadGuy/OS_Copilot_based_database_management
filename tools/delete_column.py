import mysql.connector  

def delete_column(table_name, column_name):
    """
    Delete a column from an existing table in the database if it exists.

    Args:
    table_name (str): The name of the table containing the column to be deleted.
    column_name (str): The name of the column to be deleted.
    
    Returns:
    None
    """
    try:
        conn = mysql.connector.connect(
            host='154.201.65.130',
            user='user',
            password='password',
            database='oscopilot'
    )
    except Exception as e:
        raise e

    cursor = conn.cursor()
    try:
        # 检查列是否存在
        describe_query = f"DESCRIBE {table_name}"
        cursor.execute(describe_query)
        columns = cursor.fetchall()
        
        # 检查列名是否在返回的结果中
        column_exists = any(column[0] == column_name for column in columns)
        
        if column_exists:
            # 删除列
            delete_column_query = f"""
            ALTER TABLE {table_name}
            DROP COLUMN {column_name};
            """
            
            # 执行
            cursor.execute(delete_column_query)
            
            # 提交事务
            conn.commit()
            
            print(f"Column '{column_name}' in table '{table_name}' deleted successfully.")
        else:
            print(f"Column '{column_name}' does not exist in table '{table_name}'.")
    except Exception as e:
        raise e
