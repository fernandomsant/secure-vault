import string
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Annotated
from datetime import datetime
from enum import Enum

class RegisterRequest(BaseModel):
    full_name: str
    username: str = Field(..., min_length=5, max_length=50,regex="^[a-zA-Z0-9_]+$")
    password: Annotated[str, Field(..., min_length=8, max_length=128)]
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, password: str):
        uppercase = any(c.isupper() for c in password)
        lowercase = any(c.islower() for c in password)
        special = any(c in string.punctuation for c in password)
        digit = any(c.isdigit() for c in password)
        if (uppercase and lowercase and special and digit):
            return password
        else:
            raise ValueError("Weak password. Minimum requirements: 1 uppercase character; 1 lowercase character; 1 digit; 1 special character.")

class TokenRequest(BaseModel):
    username: str
    password: str
    activation_date: datetime | None = datetime.today()
    expiration_date: datetime
    is_canceled: bool
    value: str