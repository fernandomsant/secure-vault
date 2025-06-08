import secrets
import string
from typing import Type

from db.dependency import get_db_session
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from token_.dependency.service import get_token_service
from token_.service.base_service import BaseTokenService
from user.dependency.service import get_user_service
from user.service.base_service import BaseUserService

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/")
async def create_token(
    username: str,
    password: str,
    session: Session = Depends(get_db_session),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    try:
        user_service.validate_user(username, password)
    except ValueError as e:
        raise HTTPException(401, detail=e.args)
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    token_value = "".join(secrets.choice(chars) for _ in range(64))
    token_service.create_token(username, token_value)
    return token_value


@router.get("/")
async def read_token(
    username: str,
    password: str,
    session: Session = Depends(get_db_session),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    try:
        user_service.validate_user(username, password)
    except ValueError as e:
        raise HTTPException(401, detail=e.args)
    token = token_service.get_token(username)
    return token


@router.put("/")
async def update_token():
    pass


@router.delete("/")
async def delete_token():
    pass
