from db.database import Database

def get_db_session():
    with Database.get_session() as session:
        yield session
