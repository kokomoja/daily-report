import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

driver = '{ODBC Driver 17 for SQL Server}'
server = os.environ.get("SQL_SERVER")
database = os.environ.get("SQL_DB")
username = os.environ.get("SQL_USER")
password = os.environ.get("SQL_PASSWORD")

conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 5 machine FROM machineNumber")
    print("Machines:", [row.machine for row in cursor.fetchall()])
    cursor.execute("SELECT TOP 5 op_name FROM operatorName")
    print("Operators:", [row.op_name for row in cursor.fetchall()])
    conn.close()
except Exception as e:
    print("❌ Error:", e)
