from typing import Optional, List
from fastapi import HTTPException
from auth.domain.models import User
from auth.domain.repositories.base_repositories import BaseUserRepository
import auth.utils as utils

class UserService:
    def __init__(self, user_repository: BaseUserRepository, session_maker):
        self._repo = user_repository
        self.session_maker = session_maker

    def create_user(self, first_name, surname, username, password_hash) -> User:
        with self.session_maker() as session:
            if self._repo.get_by_username(session, username):
                raise HTTPException(status_code=409, detail=f"Username {username} not available")
            
            new_user = User(
                first_name=first_name,
                surname=surname,
                username=username,
                password_hash=password_hash
            )
            try:
                self._repo.add(session, new_user)
            except Exception:
                raise(HTTPException(status_code=500, detail="It was not possible to handle your request"))

            session.commit()
            new_user_db = self._repo.get_by_username(session, username)
            return new_user_db
        
    def authenticate_user(self, username, password) -> bool:
        with self.session_maker() as session:
            user: User = self._repo.get_password_hash_by_username(session, username)
            if not user:
                raise HTTPException(status_code=401, detail="Invalid username or password")
            password_hash = user.password_hash
            try:
                utils.verify_password(password, password_hash)
            except:
                raise HTTPException(status_code=401, detail="Invalid username or password")
            
            return True
    
    def get_user_by_username(self, username) -> User:
        with self.session_maker() as session:
            user: User = self._repo.get_by_username(session, username)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user