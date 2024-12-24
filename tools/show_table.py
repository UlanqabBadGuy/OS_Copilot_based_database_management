import mysql.connector  

def show_table(table_name):
    """
    Show the structure of a table in the database using try-except block.

    Args:
    table_name (str): The name of the table to be described.
    
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
        # 描述表的SQL命令
        describe_query = f"DESCRIBE {table_name};"
        
        # 执行描述表的命令
        cursor.execute(describe_query)
        
        # 获取并打印表结构
        table_structure = cursor.fetchall()
        print(f"Structure of table '{table_name}':")
        for column in table_structure:
            print(column)
    except Exception as e:
        raise e
