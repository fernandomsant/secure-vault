import re

from argon2 import PasswordHasher
from password_strength import PasswordPolicy
from sqlalchemy.orm import Session
from user.dependency.repository import get_user_repository
from user.service.base_service import BaseUserService


class UserService(BaseUserService):

    def __init__(self, session: Session):
        self._repository = get_user_repository(session)
        self._session = session

    def create_user(self, full_name: str, username: str, password: str):
        full_name_lower = re.sub(r"\s+", " ", full_name.lower().strip())
        if not re.match(r"^[a-z ]+$", full_name_lower):
            raise ValueError("Name must match [a-z ]+")
        if len(full_name) > 50 or len(full_name) < 3:
            raise ValueError("Name must be between 4 and 50 characters")

        if not re.match(r"^[\w\.\-]+$", username):
            raise ValueError(r"Username must match [\w\.\-]+")
        if len(username) > 50 or len(username) < 3:
            raise ValueError("Username must be between 4 and 50 characters")
        if self._repository.get_user_by_username(username):
            raise ValueError("Username already taken")

        policy = PasswordPolicy.from_names(
            length=8,
            uppercase=2,
            numbers=2,
            special=2,
        )
        if policy.test(password):
            raise ValueError(
                "Password must be at least 8 characters long, with at least 2 uppercase letters, 2 numbers and 2 special characters"
            )

        full_name_list = re.sub(r"\s+", " ", full_name_lower).split(" ", 1)
        first_name = full_name_list[0]
        if len(full_name_list) == 1:
            surname = ""
        else:
            surname = full_name_list[1]

        ph = PasswordHasher()
        password_hash = ph.hash(password)
        self._repository.create_user(first_name, surname, username, password_hash)
        self._session.commit()

    def validate_user(self, username: str, password: str):
        ph = PasswordHasher()
        user = self._repository.get_user_by_username(username)
        if not user:
            raise ValueError("Invalid username or password")
        password_hash = str(user.user_password_hash)
        try:
            ph.verify(password_hash, password)
        except Exception:
            raise ValueError("Invalid username or password")
        return
