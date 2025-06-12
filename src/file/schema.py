from pydantic import BaseModel

class CreateFile(BaseModel):
    username: str
    token: str
    file_path: str
    file_description: str

class ReadFile(BaseModel):
    username: str
    token: str
    file_full_path: str