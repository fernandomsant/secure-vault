from pydantic import BaseModel


class CreateFile(BaseModel):
    username: str
    token: str
    file_path: str
    file_description: str
