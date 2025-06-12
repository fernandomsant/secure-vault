from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from db.model import Token


class BaseTokenRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int, token_is_active: int = 1) -> Optional[Token]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int, token_is_active: int = 1) -> Optional[List[Token]]:
        pass

    @abstractmethod
    def get_tokens(self, user_username: str, token_is_active: int = 1) -> Optional[List[Token]]:
        pass

    @abstractmethod
    def create_token(self, user_username: str, token_value: str, token_expiration_date: datetime):
        pass

    @abstractmethod
    def get_token_by_username_and_value(self, user_username: str, token_value: str, token_is_active: int = 1) -> Optional[Token]:
        pass

    @abstractmethod
    def deactivate_token(self, user_username: str, token_value: str) -> None:
        pass
