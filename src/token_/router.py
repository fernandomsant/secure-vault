import secrets
import string
from datetime import datetime
from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db.dependency import get_db_session
from token_.dependency.service import get_token_service
from token_.schema import CreateToken, DeleteToken, ReadToken
from token_.service.base_service import BaseTokenService
from user.dependency.service import get_user_service
from user.service.base_service import BaseUserService

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/")
async def create_token(
    create_token: CreateToken,
    session: Session = Depends(get_db_session),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    username = create_token.username
    password = create_token.password
    timespan = create_token.timespan
    try:
        user_service.validate_user(username, password)
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        token_value = "".join(secrets.choice(chars) for _ in range(64))
        token_service.create_token(username, token_value, timespan)
    except ValueError as e:
        raise HTTPException(401, detail=e.args)
    return JSONResponse({"token_value": token_value})


@router.get("/")
async def read_token(
    read_token: ReadToken,
    session: Session = Depends(get_db_session),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    username = read_token.username
    password = read_token.password
    try:
        user_service.validate_user(username, password)
        tokens_list = token_service.get_tokens(username)
        if tokens_list:
            tokens = [{"token_value": token.token_value} for token in tokens_list]
        else:
            tokens = None
        return JSONResponse({"tokens": tokens})
    except ValueError as e:
        raise HTTPException(401, detail=e.args)


@router.delete("/")
async def delete_token(
    delete_token: DeleteToken,
    session: Session = Depends(get_db_session),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    username = delete_token.username
    password = delete_token.password
    try:
        user_service.validate_user(username, password)
        token_service.delete_token(username, password)
    except ValueError as e:
        raise HTTPException(401, detail=e.args)
