from datetime import datetime
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session

from db.model import Token
from token_.repository.base_repository import BaseTokenRepository


class TokenRepository(BaseTokenRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int, token_is_active: int = 1):
        result = self._session.execute(
            text('SELECT * FROM tokens WHERE token_id = :id AND token_is_active = :token_is_active'), {'id': id, 'token_is_active': token_is_active}
        )
        row = result.mappings().one()
        if row:
            return Token(**row)
        return None

    def get_by_user_id(self, user_id: int, token_is_active: int = 1):
        result = self._session.execute(
            text('SELECT * FROM tokens WHERE token_user_id = :user_id  AND token_is_active = :token_is_active'),
            {'user_id': user_id, 'token_is_active': token_is_active},
        )
        rows = result.mappings().all()
        if rows:
            return [Token(**row) for row in rows]
        return None


    def get_tokens(self, user_username: str, token_is_active: int = 1) -> List[Token] | None:
        result = self._session.execute(
            text(
                'SELECT * FROM tokens AS t INNER JOIN users AS u ON t.token_user_id = u.user_id WHERE u.user_username = :user_username AND t.token_is_active = :token_is_active'
            ),
            {'user_username': user_username, 'token_is_active': token_is_active},
        )
        rows = result.mappings().all()
        if rows:
            return [Token(**row) for row in rows]
        return None

    def create_token(self, user_username: str, token_value: str, token_expiration_date: datetime):
        self._session.execute(
            text(
                'INSERT INTO tokens (token_user_id, token_value, token_expiration_date) SELECT user_id, :token_value, :token_expiration_date FROM users WHERE user_username = :user_username'
            ),
            {'token_value': token_value, 'user_username': user_username, 'token_expiration_date': token_expiration_date},
        )

    def get_token_by_username_and_value(self, user_username: str, token_value: str, token_is_active: int = 1):
        result = self._session.execute(
            text(
                'SELECT t.* FROM tokens AS t INNER JOIN users AS u ON u.user_id = t.token_user_id WHERE u.user_username = :user_username AND t.token_value = :token_value AND t.token_is_active = :token_is_active'
            ),
            {'user_username': user_username, 'token_value': token_value, 'token_is_active': token_is_active},
        )
        row = result.mappings().one()
        if row:
            return Token(**row)
        return None

    def deactivate_token(self, user_username: str, token_value: str) -> None:
        self._session.execute(
            text(
                'UPDATE t SET t.token_is_active = 0 FROM tokens AS t INNER JOIN users AS u ON t.token_user_id = u.user_id WHERE u.user_username = :user_username AND t.token_value = :token_value AND t.token_is_active = 1'),
                {'user_username': user_username, 'token_value': token_value}
        )