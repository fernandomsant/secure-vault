from abc import ABC, abstractmethod
from typing import List, Optional

from db.model import File
from sqlalchemy.orm import Session


class BaseFileRepository(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[File]:
        pass

    @abstractmethod
    def get_by_file_full_path(
        self, username: str, file_path: str, filename: str
    ) -> Optional[File]:
        pass

    @abstractmethod
    def create_file(self, username: str, file_path: str, filename: str):
        pass
