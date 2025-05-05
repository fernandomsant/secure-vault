import sqlite3

DB_PATH = "..\\app.db"
SCHEMA_PATH = ".\db\schema.sql"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)

    schema_sql = ""
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    print(schema_sql)
    with conn:
        conn.executescript(schema_sql)
initialize_database()
