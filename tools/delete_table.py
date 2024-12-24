import mysql.connector  

try:
    conn = mysql.connector.connect(
        host='154.201.65.130',
        user='user',
        password='password',
        database='oscopilot'
    )
    if conn.is_connected():
        print('成功连接到MySQL数据库')
except Exception as e:
    raise e

cursor = conn.cursor()

def delete_table(table_name):
    """
    Delete a table from the database.
    Args:
    table_name (str): The name of the table to be deleted.
    
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
        # 检查表是否存在
        show_tables_query = "SHOW TABLES;"
        cursor.execute(show_tables_query)
        tables = cursor.fetchall()
        

        # 删除表的SQL命令
        delete_table_query = f"DROP TABLE {table_name};"
        
        # 执行删除表的命令
        cursor.execute(delete_table_query)
        
        # 提交事务
        conn.commit()
        
        print(f"Table '{table_name}' deleted successfully.")

    except Exception as e:
        raise e
