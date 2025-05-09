from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional
from auth.domain.models import User
from auth.domain.repositories.base_repositories import BaseUserRepository

class UserRepository(BaseUserRepository):    
    def get_by_id(self, session: Session, id: int) -> Optional[User]:
        result = session.execute(
            text("""
                SELECT
                    user_id,
                    user_first_name,
                    user_surname,
                    user_username
                FROM users
                WHERE user_id = :id
            """),
            {"id": id}
        )
        db_obj = result.mappings().first()
        return User.from_row(db_obj) if db_obj else None
    
    def get_by_username(self, session: Session, username: str) -> Optional[User]:
        result = session.execute(
            text("""
                SELECT
                    user_id,
                    user_first_name,
                    user_surname,
                    user_username,
                    user_is_active,
                    user_insert_datetime
                FROM users
                WHERE user_username = :username
            """),
            {"username": username}
        )
        db_obj = result.mappings().first()
        return User.from_row(db_obj) if db_obj else None
    
    def get_password_hash_by_username(self, session: Session, username: str) -> Optional[User]:
        result = session.execute(
            text("""
                SELECT
                    user_password_hash
                FROM users
                WHERE user_username = :username
            """),
            {"username": username}
        )
        db_obj = result.mappings().first()
        return User.from_row(db_obj) if db_obj else None
    
    def add(self, session: Session, user: User) -> None:
        session.execute(
            text("""
                INSERT INTO users (
                    user_first_name,
                    user_surname,
                    user_username,
                    user_password_hash)
                VALUES (
                    :first_name,
                    :surname,
                    :username,
                    :password_hash)
            """),
            {
                "first_name": user.first_name,
                "surname": user.surname,
                "username": user.username,
                "password_hash": user.password_hash
            }
        )
    
    def update_profile(self, session: Session, user: User) -> None:
        session.execute(
            text("""
                UPDATE users 
                SET
                    user_first_name = :first_name
                    user_surname = :surname
                    user_username = :username
                    user_is_active = :is_active
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
    
    def update_password(self, session: Session, user: User) -> None:
        session.execute(
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
        
    def deactivate_user(self, session: Session, id) -> None:
        session.execute(
            text("""
                UPDATE users
                SET user_is_active = false
                WHERE user_id = :id
            """),
            {"id": id}
        )