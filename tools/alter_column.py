import mysql.connector  

def alter_column(table_name, old_column_name, new_column_name, new_column_type):
    """
    Modify the name and data type of a column in an existing table in the database.

    Args:
    table_name (str): The name of the table containing the column to be modified.
    old_column_name (str): The current name of the column to be modified.
    new_column_name (str): The new name of the column.
    new_column_type (str): The new data type of the column.
    
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
        # 修改列名和数据类型
        modify_column_query = f"""
        ALTER TABLE {table_name}
        CHANGE COLUMN {old_column_name} {new_column_name} {new_column_type};
        """

        # 执行
        cursor.execute(modify_column_query)

        # 提交事务
        conn.commit()

        print(f"Column '{old_column_name}' in table '{table_name}' modified to '{new_column_name}' with type '{new_column_type}' successfully.")
    except Exception as e:
        raise e
