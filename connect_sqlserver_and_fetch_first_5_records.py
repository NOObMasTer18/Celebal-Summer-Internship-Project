import pyodbc
import os
from dotenv import load_dotenv
from tabulate import tabulate  

load_dotenv()

server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

#Connection String
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server},1433;'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

try:
    conn = pyodbc.connect(conn_str)
    print("Connection Successful!")

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT TOP 5 * FROM Employees")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        # Pretty print the results as a table
        print(tabulate(rows, headers=columns, tablefmt="grid"))

    except pyodbc.Error as query_err:
        print("Error retrieving data:", query_err)
    finally:
        cursor.close()
        conn.close()
except pyodbc.Error as conn_err:
    print("Connection Failed:", conn_err)
    print("Connection Failed:", conn_err)