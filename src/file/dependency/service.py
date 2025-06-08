from typing import Type

from file.service.base_service import BaseFileService
from file.service.file_service import FileService


def get_file_service() -> Type[BaseFileService]:
    return FileService
