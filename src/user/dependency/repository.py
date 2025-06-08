from sqlalchemy.orm import Session
from user.repository.base_repository import BaseUserRepository
from user.repository.user_repository import UserRepository


def get_user_repository(session: Session) -> BaseUserRepository:
    return UserRepository(session)
