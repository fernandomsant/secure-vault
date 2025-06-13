from datetime import datetime

from pydantic import BaseModel


class BaseTokenModel(BaseModel):
    username: str
    password: str


class CreateToken(BaseTokenModel):
    timespan: int


class ReadToken(BaseTokenModel):
    pass


class DeleteToken(BaseTokenModel):
    pass
