from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from db.model import User


class BaseUserService(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def create_user(self, full_name: str, username: str, password: str):
        pass

    @abstractmethod
    def validate_user(self, username: str, password: str):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass
