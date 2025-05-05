from typing import Optional, List
from auth.domain.models import User
from auth.domain.repositories.base_repositories import BaseUserRepository

class UserService:
    def __init__(self, user_repository: BaseUserRepository, session_maker):
        self._repo = user_repository
        self.session_maker = session_maker

    def authenticate_user(self, username, password_hash) -> bool:
        with self.session_maker() as session:
            if (self._repo.get_by_username_and_password_hash(session, username, password_hash)):
                return True
            raise Exception("Invalid username or password")

    def create_user(self, first_name, surname, username, password_hash) -> User:
        with self.session_maker() as session:
            if self._repo.get_by_username(session, username):
                raise Exception(f"Username {username} not available")
            
            new_user = User(
                first_name=first_name,
                surname=surname,
                username=username,
                password_hash=password_hash
            )
            self._repo.add(session, new_user)
            
            session.commit()
            new_user_db = self._repo.get_by_username(session, username)
            return new_user_db