import mysql.connector
import csv

def save_table_to_csv(table_name, csv_file_path, condition=None):
    """
    Connects to a MySQL database, fetches data (whole table or filtered by condition),
    and saves it to a CSV file.

    Args:
        table_name (str): Name of the table to fetch data from.
        csv_file_path (str): Path to save the CSV file.
        condition (str, optional): SQL condition to filter data (e.g., "age > 30").

    Returns:
        str: The path of the saved CSV file.
    """
    try:
        # Step 1: Connect to the MySQL database
        conn = mysql.connector.connect(
            host='154.201.65.130',
            user='user',
            password='password',
            database='oscopilot'
        )
        cursor = conn.cursor()
        print("Connected to database 'oscopilot' on host '154.201.65.130'.")

        # Step 2: Construct the SQL query
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"  # Add the condition if provided

        # Step 3: Fetch data from the table
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]

        # Step 4: Save data to CSV
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)  # Write header
            writer.writerows(rows)        # Write data
        print(f"Data from table '{table_name}' saved to {csv_file_path}")

        # Close the database connection
        conn.close()
        return csv_file_path
    except mysql.connector.Error as e:
        raise RuntimeError(f"Database connection failed: {e}")
    except Exception as e:
        raise RuntimeError(f"Error saving table to CSV: {e}")