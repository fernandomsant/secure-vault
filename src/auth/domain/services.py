from typing import Optional, List
from auth.domain.models import User
from auth.domain.repositories.base_repositories import BaseUserRepository

class UserService:
    def __init__(self, user_repository: BaseUserRepository):
        self._repo = user_repository

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self._repo.get_by_id(user_id)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self._repo.get_by_username(username)

    def create_user(self, first_name, surname, username, password_hash) -> User:
        if self._repo.get_by_username(username):
            raise Exception(f"Username {username} not available")
        
        new_user = User(
            first_name=first_name,
            surname=surname,
            username=username,
            password_hash=password_hash
        )
        self._repo.add(new_user)
        return new_user