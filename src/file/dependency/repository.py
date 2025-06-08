from sqlalchemy.orm import Session

from file.repository.base_repository import BaseFileRepository
from file.repository.file_repository import FileRepository


def get_file_repository(session: Session) -> BaseFileRepository:
    return FileRepository(session)
