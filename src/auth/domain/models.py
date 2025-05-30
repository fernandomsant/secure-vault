from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int | None = None
    first_name: str | None = None
    surname: str | None = None
    username: str | None = None
    password_hash: str | None = None
    insert_datetime: datetime | None = None
    is_active: bool | None = None
    @classmethod
    def from_row(cls, row):
        return cls(
            id=getattr(row, "user_id", None),
            first_name=getattr(row, "user_first_name", None),
            surname=getattr(row, "user_surname", None),
            username=getattr(row, "user_username", None),
            password_hash=getattr(row, "user_password_hash", None),
            insert_datetime=getattr(row, "user_insert_datetime", None),
            is_active=getattr(row, "user_is_active", None)
        )

@dataclass
class File:
    id: int | None = None
    user_id: int | None = None
    file_path: str | None = None
    file_extension: str | None = None
    description: str | None = None
    insert_datetime: datetime | None = None
    @classmethod
    def from_row(cls, row):
        return cls(
            id=getattr(row, "file_id", None),
            user_id=getattr(row, "file_user_id", None),
            file_path=getattr(row, "file_file_path", None),
            file_extension=getattr(row, "file_file_extension", None),
            description=getattr(row, "file_description", None),
            insert_datetime=getattr(row, "file_insert_datetime", None),
        )

@dataclass
class Token:
    id: int | None = None
    user_id: int | None = None
    expiration_date: datetime | None = None
    is_active: bool | None = None
    value: str | None = None
    insert_datetime: datetime | None = None
    @classmethod
    def from_row(cls, row):
        return cls(
            id=getattr(row, "token_id", None),
            user_id=getattr(row, "token_user_id", None),
            expiration_date=getattr(row, "token_expiration_date", None),
            is_active=getattr(row, "token_is_active", None),
            value=getattr(row, "token_value", None),
            insert_datetime=getattr(row, "token_insert_datetime", None),
        )