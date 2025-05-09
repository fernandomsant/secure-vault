from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional, List
from auth.domain.models import Token
from auth.domain.repositories.base_repositories import BaseTokenRepository


class TokenRepository(BaseTokenRepository):
    def get_by_id(self, session: Session, id: int) -> Optional[Token]:
        result = session.execute(
            text("""
                SELECT
                    token_user_id,
                    token_expiration_date,
                    token_is_active,
                    token_value
                FROM tokens
                WHERE token_id = :id
            """),
            {"id": id}
        )
        db_obj = result.mappings().first()
        return Token.from_row(db_obj) if db_obj else None
    
    def add(self, session: Session, token: Token) -> None:
        session.execute(
            text("""
                INSERT INTO tokens (
                    token_user_id,
                    token_expiration_date,
                    token_value)
                VALUES (
                    :user_id,
                    :expiration_date,
                    :value)
            """),
            {
                "user_id": token.user_id,
                "expiration_date": token.expiration_date,
                "value": token.value
            }
        )
    
    def delete(self, session: Session, id: int) -> None:
        session.execute(
            text("""
                DELETE FROM tokens
                WHERE token_id = :id
            """),
            {"id": id}
        )
    
    def list_by_user_id(self, session: Session, user_id) -> List[Token]:
        result = session.execute(
            text("""
                SELECT
                    token_user_id,
                    token_expiration_date,
                    token_is_active,
                    token_value
                FROM tokens
                WHERE token_user_id = :user_id
            """),
            {"user_id": user_id}
        )
        db_obj = result.mappings().first()
        return [Token.from_row(db_obj_item) for db_obj_item in db_obj] if db_obj else None

    def list_active_by_user_id(self, session: Session, user_id) -> List[Token]:
        result = session.execute(
            text("""
                SELECT
                    token_user_id,
                    token_expiration_date,
                    token_is_active,
                    token_value
                FROM tokens
                WHERE
                    token_user_id = :user_id
                AND token_is_active = true
            """),
            {"user_id": user_id}
        )
        db_obj = result.mappings().first()
        return [Token.from_row(db_obj_item) for db_obj_item in db_obj] if db_obj else None