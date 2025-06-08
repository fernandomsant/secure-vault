from sqlalchemy import text
from sqlalchemy.orm import Session

from db.model import File
from file.repository.base_repository import BaseFileRepository


class FileRepository(BaseFileRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id):
        result = self._session.execute(
            text("SELECT * FROM files WHERE file_id = :id"), {"id": id}
        )
        row = result.mappings().first()
        if row:
            return File(**row)
        return None

    def get_by_file_full_path(self, username, file_path, filename):
        result = self._session.execute(
            text(
                "SELECT * FROM files AS f INNER JOIN users AS u ON f.file_user_id = u.user_id WHERE f.file_file_path = :file_path AND f.file_filename = :filename AND u.user_username = :username"
            ),
            {"file_path": file_path, "filename": filename, "username": username},
        )
        row = result.mappings().first()
        if row:
            return File(**row)
        return None

    def create_file(self, username, file_path, filename):
        pass
