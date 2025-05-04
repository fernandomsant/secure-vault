from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional
from auth.domain.models import User
from auth.domain.repositories.base_repositories import BaseUserRepository

class UserRepository(BaseUserRepository):
    def __init__(self, session: Session):
        self._session = session
    
    def get_by_id(self, id: int) -> Optional[User]:
        result = self._session.execute(
            text("""
                 SELECT
                 user_first_name
                ,user_surname
                ,user_username
                 FROM users
                 WHERE user_id = :id"""),
            {"id": id}
        )
        db_obj = result.mappings().first()
        return User.from_row(db_obj) if db_obj else None
    
    def get_by_username(self, username: str) -> Optional[User]:
        result = self._session.execute(
            text("""
                 SELECT
                 user_first_name
                ,user_surname
                ,user_username
                 FROM users
                 WHERE user_username = :username"""),
            {"username": username}
        )
        db_obj = result.mappings().first()
        return User.from_row(db_obj) if db_obj else None
    
    def add(self, user: User) -> None:
        self._session.execute(
            text("""
                INSERT INTO users (
                 user_first_name
                ,user_surname
                ,user_username
                ,user_password_hash)
                VALUES (
                :first_name
               ,:surname
               ,:username
               ,:password_hash)
            """),
            {
                "first_name": user.first_name,
                "surname": user.surname,
                "username": user.username,
                "password_hash": user.password_hash
            }
        )
    
    def update_profile(self, user: User) -> None:
        self._session.execute(
            text("""
                UPDATE users 
                SET
                user_first_name = :first_name
               ,user_surname = :surname
               ,user_username = :username
               ,user_is_active = :is_active
                WHERE user_id = :id
            """),
            {
                "first_name": user.first_name,
                "surname": user.surname,
                "username": user.username,
                "is_active": user.is_active,
                "id": user.id
            }
        )
    
    def update_password(self, user: User) -> None:
        self._session.execute(
            text("""
                UPDATE users 
                SET user_password_hash = :password_hash
                WHERE user_id = :id
            """),
            {
                "password_hash": user.password_hash,
                "id": user.id
            }
        )
        
    def deactivate_user(self, id) -> None:
        self._session.execute(
            text("""
                    UPDATE users
                    SET user_is_active = false
                    WHERE user_id = :id
                    """),
            {
                "id": id
            }
        )