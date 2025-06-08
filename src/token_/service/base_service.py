from abc import ABC, abstractmethod
from typing import Optional

from db.model import Token
from fastapi import UploadFile
from sqlalchemy.orm import Session
from token_.repository.base_repository import BaseTokenRepository


class BaseTokenService(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_token(self, username: str) -> Optional[Token]:
        pass

    @abstractmethod
    def create_token(self, username: str, token_value: str):
        pass

    @abstractmethod
    def validate_token(self, username: str, token: str) -> bool:
        pass
