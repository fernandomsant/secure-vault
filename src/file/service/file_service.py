import os
import re

from fastapi import HTTPException, UploadFile
from file.dependency.repository import get_file_repository
from file.service.base_service import BaseFileService
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session


class FileService(BaseFileService):
    def __init__(self, session: Session):
        self._repository = get_file_repository(session)

    def create_file(self, username: str, file_path: str, file_upload: UploadFile):

        file_path = os.path.normpath(file_path)
        sep = os.path.sep
        dirs = file_path.split(sep)
        if len(dirs) > 3:
            raise ValueError("File path must contain up to 3 directories")

        norm_file_path = os.path.join(*dirs)
        filename = file_upload.filename or ""

        if not re.match(r"^[\w\-. ]+$", filename):
            raise ValueError("Filename contains invalid characters")

        file_exist = self._repository.get_by_file_full_path(
            username, norm_file_path.replace("\\", "/"), filename
        )
        if file_exist:
            raise ValueError("File already exists")

        self._repository.create_file(username, norm_file_path, filename)

    def read_file(self, username, file_full_path):
        return super().read_file(username, file_full_path)

    def update_file(self, username, file_full_path, file_upload):
        return super().update_file(username, file_full_path, file_upload)

    def delete_file(self, username, file_full_path):
        return super().delete_file(username, file_full_path)
