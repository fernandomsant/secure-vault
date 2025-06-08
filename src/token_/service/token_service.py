from sqlalchemy.orm import Session

from db.model import Token
from token_.dependency.repository import get_token_repository
from token_.service.base_service import BaseTokenService


class TokenService(BaseTokenService):
    def __init__(self, session: Session):
        self._repository = get_token_repository(session)
        self._session = session

    def get_token(self, username: str) -> Token | None:
        return self._repository.get_token(username)

    def create_token(self, username: str, token_value: str):
        self._repository.create_token(username, token_value)

    def validate_token(self, username, token):
        return self._repository.validate_token(username, token)
