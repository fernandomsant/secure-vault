# repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from auth.domain.models import User, File, Token

class BaseUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def add(self, user: User) -> None:
        pass
    
    @abstractmethod
    def update_profile(self, user: User) -> None:
        pass

    @abstractmethod
    def update_password(self, user: User) -> None:
        pass
    
    @abstractmethod
    def deactivate_user(self, user: User) -> None:
        pass

class BaseFileRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[File]:
        pass
    
    @abstractmethod
    def get_by_file_path(self, file_path: str) -> Optional[File]:
        pass
    
    @abstractmethod
    def add(self, file: File) -> None:
        pass
    
    @abstractmethod
    def update(self, file: File) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
    
    @abstractmethod
    def list_by_user_id(self, user_id) -> List[File]:
        pass

class BaseTokenRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Token]:
        pass
    
    @abstractmethod
    def add(self, token: Token) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
    
    @abstractmethod
    def list_by_user_id(self, user_id) -> List[Token]:
        pass

    @abstractmethod
    def list_active_by_user_id(self, user_id) -> List[Token]:
        pass