from sqlalchemy import text
from sqlalchemy.orm import Session

from db.model import User
from user.repository.base_repository import BaseUserRepository


class UserRepository(BaseUserRepository):

    def __init__(self, session):
        self._session = session

    def get_user_by_username(self, username):
        result = self._session.execute(
            text("SELECT * FROM users WHERE user_username = :username"),
            {"username": username},
        )
        row = result.mappings().first()
        if row:
            return User(**row)
        return None

    def create_user(self, first_name, surname, username, password_hash):
        self._session.execute(
            text(
                "INSERT INTO users (user_first_name, user_surname, user_username, user_password_hash, user_is_active) VALUES (:first_name, :surname, :username, :password_hash, 1)"
            ),
            {
                "first_name": first_name,
                "surname": surname,
                "username": username,
                "password_hash": password_hash,
            },
        )
