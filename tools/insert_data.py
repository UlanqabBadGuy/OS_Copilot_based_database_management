import mysql.connector

def insert_data(table_name, data):
    """
    Inserts data into a specified table in a MySQL database.

    Args:
    table_name (str): Name of the table where data will be inserted.
    data (dict): A dictionary where keys are column names and values are the data to insert.
    data = {
    'column1': 'value1',
    'column2': 'value2',
    'column3': 'value3'
    }

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

    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s' for _ in data])
    sql_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

    try:
        cursor.execute(sql_query, tuple(data.values()))
        conn.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
