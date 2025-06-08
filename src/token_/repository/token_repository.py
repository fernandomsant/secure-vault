from db.model import Token
from sqlalchemy import text
from sqlalchemy.orm import Session
from token_.repository.base_repository import BaseTokenRepository


class TokenRepository(BaseTokenRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id):
        result = self._session.execute(
            text("SELECT * FROM tokens WHERE token_id = :id"), {"id": id}
        )
        row = result.mappings().first()
        if row:
            return Token(**row)
        return None

    def get_by_user_id(self, user_id):
        result = self._session.execute(
            text("SELECT * FROM tokens WHERE token_user_id = :user_id"),
            {"user_id": user_id},
        )
        row = result.mappings().first()
        if row:
            return Token(**row)
        return None

    def get_token(self, user_username: str) -> Token | None:
        result = self._session.execute(
            text(
                "SELECT * FROM tokens AS t INNER JOIN users AS u ON t.token_user_id = u.user_id WHERE u.user_username = :user_username"
            ),
            {"user_username": user_username},
        )
        row = result.mappings().first()
        if row:
            return Token(**row)
        return None

    def create_token(self, user_username: str, token_value: str):
        self._session.execute(
            text(
                "INSERT INTO tokens (token_user_id, token_value) SELECT user_id, :token_value FROM users WHERE user_username = :user_username"
            ),
            {"token_value": token_value, "user_username": user_username},
        )

    def validate_token(self, user_username, token_value):
        result = self._session.execute(
            text(
                "SELECT t.token_id FROM  tokens AS t INNER JOIN users AS u ON u.user_id= t.token_user_id WHERE u.user_username = :user_username AND t.token_value = :token_value"
            ),
            {"user_username": user_username, "token_value": token_value},
        )
        row = result.mappings().first()
        if row:
            return True
        return False
