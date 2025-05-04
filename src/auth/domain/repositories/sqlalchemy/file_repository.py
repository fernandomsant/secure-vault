from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional, List
from auth.domain.models import File
from auth.domain.repositories.base_repositories import BaseFileRepository

class FileRepository(BaseFileRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Optional[File]:
        result = self._session.execute(
            text("""
                 SELECT
                 file_file_path,
                ,file_file_extension
                ,file_description
                 FROM files
                 WHERE file_id = :id"""),
            {
                "id": id
            }
        )
        db_obj = result.mappings().first()
        return File.from_row(db_obj) if db_obj else None
    
    def get_by_file_path(self, file_path: str, user_id: int) -> Optional[File]:
        result = self._session.execute(
            text("""
                 SELECT
                 file_file_path,
                ,file_file_extension
                ,file_description
                 FROM files
                 WHERE file_id = :file_path
                 AND file_user_id = :user_id"""),
            {
                "file_path": file_path,
                "user_id": user_id
            }
        )
        db_obj = result.mappings().first()
        return File.from_row(db_obj) if db_obj else None
    
    def add(self, file: File) -> None:
        self._session.execute(
            text("""
                 INSERT INTO files (
                 file_user_id
                ,file_file_path
                ,file_file_extension
                ,file_description)
                 VALUES (
                 :user_id
                ,:file_path
                ,:file_extension
                ,:description)"""),
            {
                "user_id": file.user_id,
                "file_path": file.file_path,
                "file_extension": file.file_extension,
                "description": file.description
            }
        )
    
    def update(self, file: File) -> None:
        self._session.execute(
            text("""
                 UPDATE files
                 SET
                 file_file_path = :file_path
                ,file_file_extension = :file_extension
                ,file_description = :description
                 WHERE user_id = :user_id
                 """),
            {
                "user_id": file.user_id,
                "file_path": file.file_path,
                "file_extension": file.file_extension,
                "description": file.description,
                "user_id": file.user_id
            }
        )
    
    def delete(self, id: int) -> None:
        pass
    
    def list_by_user_id(self, user_id) -> List[File]:
        pass