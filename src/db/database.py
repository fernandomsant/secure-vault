import os
from contextlib import contextmanager

from db.model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:

    @classmethod
    def initialize(cls, **kwargs):
        cls._engine = create_engine(**kwargs)
        cls._SessionLocal = sessionmaker(bind=cls._engine)
        if os.getenv("ENV") == "development":
            Base.metadata.create_all(Database._engine)

    @classmethod
    def get_connection(cls):
        with cls._engine.connect() as conn:
            yield conn

    @classmethod
    @contextmanager
    def get_session(cls):
        session = cls._SessionLocal()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
