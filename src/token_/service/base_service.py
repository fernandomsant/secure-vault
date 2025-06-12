from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime

from fastapi import UploadFile
from sqlalchemy.orm import Session

from db.model import Token
from token_.repository.base_repository import BaseTokenRepository


class BaseTokenService(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_tokens(self, username: str) -> Optional[List[Token]]:
        pass

    @abstractmethod
    def create_token(self, username: str, token_value: str, timespan: int):
        pass

    @abstractmethod
    def validate_token(self, username: str, token: str) -> bool:
        pass

    @abstractmethod
    def delete_token(self, username: str, token: str) -> bool:
        pass