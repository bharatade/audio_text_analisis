import pyodbc
from configs.config import DB_CONFIG

def get_connection():
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={DB_CONFIG["server"]};'
        f'DATABASE={DB_CONFIG["database"]};'
        f'UID={DB_CONFIG["username"]};PWD={DB_CONFIG["password"]}'
    )
    return pyodbc.connect(conn_str, autocommit=True)
