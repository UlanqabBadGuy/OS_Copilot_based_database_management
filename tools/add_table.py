import mysql.connector  

def add_table(table_name, primary_key_name, primary_key_type):
    """
    Create a table with the specified name and primary key in the database.

    Args:
    table_name (str): The name of the table to be created.
    primary_key_name (str): The name of the primary key column.
    primary_key_type (str): The data type of the primary key column.
    
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
        # 创建表
        create_table_query = f"""
        CREATE TABLE {table_name} (
            {primary_key_name} {primary_key_type} AUTO_INCREMENT PRIMARY KEY
        );
        """

        # 执行
        cursor.execute(create_table_query)

        # 提交事务
        conn.commit()

        print(f"Table '{table_name}' with primary key '{primary_key_name}' created successfully.")
    except Exception as e:
        raise e
