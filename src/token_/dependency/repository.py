from sqlalchemy.orm import Session
from token_.repository.base_repository import BaseTokenRepository
from token_.repository.token_repository import TokenRepository


def get_token_repository(session: Session) -> BaseTokenRepository:
    return TokenRepository(session)
