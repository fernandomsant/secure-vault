from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


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
