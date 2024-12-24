import mysql.connector  



def add_column(table_name, column_name, column_type):
    """
    Add a new column to an existing table in the database.

    Args:
    table_name (str): The name of the table to which the column will be added.
    column_name (str): The name of the new column.
    column_type (str): The data type of the new column.
    
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
        
        if not column_exists:
            # 添加列
            add_column_query = f"""
            ALTER TABLE {table_name}
            ADD COLUMN {column_name} {column_type};
            """
            
            # 执行
            cursor.execute(add_column_query)
            
            # 提交事务
            conn.commit()
            
            print(f"Column '{column_name}' added to table '{table_name}' successfully.")
        else:
            print(f"Column '{column_name}' already exists in table '{table_name}'.")
    except Exception as e:
        raise e


