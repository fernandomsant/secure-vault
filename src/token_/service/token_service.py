from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session

from typing import List

from db.model import Token
from token_.dependency.repository import get_token_repository
from token_.service.base_service import BaseTokenService


class TokenService(BaseTokenService):
    def __init__(self, session: Session):
        self._repository = get_token_repository(session)
        self._session = session

    def get_tokens(self, username: str) -> List[Token] | None:
        return self._repository.get_tokens(username)

    def create_token(self, username: str, token_value: str, timespan: int):
        expiration_date = datetime.now(timezone.utc) + timedelta(0, timespan)
        self._repository.create_token(username, token_value, expiration_date)

    def validate_token(self, username, token):
        token_obj = self._repository.get_token_by_username_and_value(username, token)
        if not token_obj:
            return False
        expiration_date = token_obj.token_expiration_date
        if bool(datetime.now(timezone.utc) > expiration_date.replace(tzinfo=timezone.utc)):
            self._repository.deactivate_token(username, token)
            return False
        return True
    
    def delete_token(self, username: str, token: str) -> bool:
        self._repository.deactivate_token(username, token)
        return True
