from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional, List
from auth.domain.models import File
from auth.domain.repositories.base_repositories import BaseFileRepository

class FileRepository(BaseFileRepository):
    def get_by_id(self, session: Session, id: int) -> Optional[File]:
        result = session.execute(
            text("""
                SELECT
                    file_file_path,
                    file_file_extension,
                    file_description
                FROM files
                WHERE file_id = :id
            """),
            {
                "id": id
            }
        )
        db_obj = result.mappings().first()
        return File.from_row(db_obj) if db_obj else None
    
    def get_by_file_path(self, session: Session, file_path: str, user_id: int) -> Optional[File]:
        result = session.execute(
            text("""
                SELECT
                    file_file_path,
                    file_file_extension,
                    file_description
                FROM files
                WHERE file_id = :file_path
                AND file_user_id = :user_id
            """),
            {
                "file_path": file_path,
                "user_id": user_id
            }
        )
        db_obj = result.mappings().first()
        return File.from_row(db_obj) if db_obj else None
    
    def add(self, session: Session, file: File) -> None:
        session.execute(
            text("""
                INSERT INTO files (
                    file_user_id,
                    file_file_path,
                    file_file_extension,
                    file_description)
                VALUES (
                    :user_id,
                    :file_path,
                    :file_extension,
                    :description)
            """),
            {
                "user_id": file.user_id,
                "file_path": file.file_path,
                "file_extension": file.file_extension,
                "description": file.description
            }
        )
    
    def update(self, session: Session, file: File) -> None:
        session.execute(
            text("""
                UPDATE files
                SET
                    file_file_path = :file_path,
                    file_file_extension = :file_extension,
                    file_description = :description,
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
    
    def delete(self, session: Session, id: int) -> None:
        session.execute(
            text("""
                DELETE FROM files
                WHERE file_id = :id
            """),
            {
                "id": id
            }
        )
    
    def list_by_user_id(self, session: Session, user_id) -> List[File]:
        result = session.execute(
            text("""
                SELECT
                    file_file_path,
                    file_file_extension,
                    file_description
                FROM files
                WHERE file_user_id = :user_id
            """),
            {
                "user_id": user_id
            }
        )
        db_obj = result.mappings().first()
        return [File.from_row(db_obj_item) for db_obj_item in db_obj] if db_obj else None