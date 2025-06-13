from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text, text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_first_name = Column(String(25), nullable=False)
    user_surname = Column(String(50), nullable=True)
    user_username = Column(String(25), nullable=False, unique=True)
    user_password_hash = Column(String(255), nullable=False)
    user_is_active = Column(
        Boolean, nullable=False, default=True, server_default=text("1")
    )
    user_insert_datetime = Column(
        DateTime, nullable=False, server_default=func.sysutcdatetime()
    )

    files = relationship("File", back_populates="user", cascade="all, delete-orphan")
    tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")


class File(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, autoincrement=True)
    file_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    file_file_path = Column(String(100), nullable=False)
    file_filename = Column(String(50), nullable=False)
    file_insert_datetime = Column(
        DateTime, nullable=False, server_default=func.sysutcdatetime()
    )

    user = relationship("User", back_populates="files")


class Token(Base):
    __tablename__ = "tokens"

    token_id = Column(Integer, primary_key=True, autoincrement=True)
    token_user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    token_expiration_date = Column(DateTime, nullable=False)
    token_is_active = Column(
        Boolean, nullable=False, default=True, server_default=text("1")
    )
    token_value = Column(String(255), nullable=False)
    token_insert_datetime = Column(
        DateTime, nullable=False, server_default=func.sysutcdatetime()
    )

    user = relationship("User", back_populates="tokens")
