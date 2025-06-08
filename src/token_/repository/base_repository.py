from abc import ABC, abstractmethod
from typing import List, Optional

from db.model import Token


class BaseTokenRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Token]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int) -> Optional[Token]:
        pass

    @abstractmethod
    def get_token(self, user_username: str) -> Optional[Token]:
        pass

    @abstractmethod
    def create_token(self, user_username: str, token_value: str):
        pass

    @abstractmethod
    def validate_token(self, user_username: str, token_value: str) -> bool:
        pass
