from pydantic import BaseModel
from datetime import datetime

class BaseTokenModel(BaseModel):
    username: str
    password: str

class CreateToken(BaseTokenModel):
    timespan: int

class ReadToken(BaseTokenModel):
    pass

class DeleteToken(BaseTokenModel):
    pass