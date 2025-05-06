# repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from auth.domain.models import User, File, Token

class BaseUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, session, id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def get_by_username(self, session, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_password_hash_by_username(self, session, username: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def add(self, session, user: User) -> None:
        pass
    
    @abstractmethod
    def update_profile(self, session, user: User) -> None:
        pass

    @abstractmethod
    def update_password(self, session, user: User) -> None:
        pass
    
    @abstractmethod
    def deactivate_user(self, session, user: User) -> None:
        pass

class BaseFileRepository(ABC):
    @abstractmethod
    def get_by_id(self, session, id: int) -> Optional[File]:
        pass
    
    @abstractmethod
    def get_by_file_path(self, session, file_path: str) -> Optional[File]:
        pass
    
    @abstractmethod
    def add(self, session, file: File) -> None:
        pass
    
    @abstractmethod
    def update(self, session, file: File) -> None:
        pass
    
    @abstractmethod
    def delete(self, session, id: int) -> None:
        pass
    
    @abstractmethod
    def list_by_user_id(self, session, user_id) -> List[File]:
        pass

class BaseTokenRepository(ABC):
    @abstractmethod
    def get_by_id(self, session, id: int) -> Optional[Token]:
        pass
    
    @abstractmethod
    def add(self, session, token: Token) -> None:
        pass
    
    @abstractmethod
    def delete(self, session, id: int) -> None:
        pass
    
    @abstractmethod
    def list_by_user_id(self, session, user_id) -> List[Token]:
        pass

    @abstractmethod
    def list_active_by_user_id(self, session, user_id) -> List[Token]:
        pass