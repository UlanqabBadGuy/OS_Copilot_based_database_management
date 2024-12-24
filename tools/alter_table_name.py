import mysql.connector  


def alter_table_name(old_table_name, new_table_name):
    """
    Rename a table in the database using try-except block.

    Args:
    old_table_name (str): The current name of the table to be renamed.
    new_table_name (str): The new name of the table.
    
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
        # 重命名表
        rename_query = f"RENAME TABLE {old_table_name} TO {new_table_name};"
        
        # 执行
        cursor.execute(rename_query)
        
        # 提交事务
        conn.commit()
        
        print(f"Table '{old_table_name}' renamed to '{new_table_name}' successfully.")
    except Exception as e:
        raise e
