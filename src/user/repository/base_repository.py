from abc import ABC, abstractmethod
from typing import Optional

from db.model import User
from sqlalchemy.orm import Session


class BaseUserRepository(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(
        self, first_name: str, surname: str, username: str, password_hash: str
    ):
        pass
