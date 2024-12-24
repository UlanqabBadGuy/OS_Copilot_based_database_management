import mysql.connector  
from aifc import Error

def show_table_keys(table_name):
    """
    Show the keys (primary keys, foreign keys, etc.) of a table in the database using try-except block.

    Args:
    table_name (str): The name of the table to be checked.
    
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
    except Error as e:
        print(f":{e}")

    cursor = conn.cursor()
    try:
        # 检查表是否存在
        show_tables_query = "SHOW TABLES;"
        cursor.execute(show_tables_query)
        tables = cursor.fetchall()
        
        # 检查表名是否在返回的结果中
        table_exists = any(table[0] == table_name for table in tables)
        
        if table_exists:
            # 获取表的创建语句
            show_create_query = f"SHOW CREATE TABLE {table_name};"
            cursor.execute(show_create_query)
            create_table_statement = cursor.fetchone()
            
            # 提取键信息
            if create_table_statement:
                print(f"Keys of table '{table_name}':")
                print(create_table_statement[1])
            else:
                print(f"No keys found for table '{table_name}'.")
        else:
            print(f"Table '{table_name}' does not exist in the database.")
    except mysql.connector.Error as e:
        print(f"Error showing keys of table '{table_name}': {e}")
