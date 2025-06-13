from abc import ABC, abstractmethod

from fastapi import UploadFile
from sqlalchemy.orm import Session

from typing import Tuple, Generator

from db.model import File


class BaseFileService(ABC):

    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def create_file(
        self, username: str, user_id: int, file_path: str, file_description: str, file_upload: UploadFile
    ) -> None:
        pass

    @abstractmethod
    def read_file(self, username: str, user_id: int, file_full_path: str) -> Tuple[str, str, Generator[bytes, None, None]]:
        pass

    @abstractmethod
    def update_file(
        self, username: str, file_full_path: str, file_upload: UploadFile
    ) -> None:
        pass

    @abstractmethod
    def delete_file(self, username: str, file_full_path: str) -> None:
        pass
