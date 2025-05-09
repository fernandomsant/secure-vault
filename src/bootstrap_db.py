from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
SCHEMA_PATH = "./db/schema-mssql.sql"

def initialize_database():
    engine = create_engine(DB_URL, future=True)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    print(schema_sql)

    with engine.begin() as connection:
        for statement in schema_sql.strip().split(";"):
            stmt = statement.strip()
            if stmt:
                connection.execute(text(stmt))

if __name__ == "__main__":
    initialize_database()

