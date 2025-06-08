from pydantic import BaseModel


class CreateUser(BaseModel):
    full_name: str
    username: str
    password: str
