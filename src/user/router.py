from typing import Annotated, Type

from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db.dependency import get_db_session
from user.dependency.service import get_user_service
from user.schema import CreateUser
from user.service.base_service import BaseUserService

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def create_user(
    create_user: CreateUser,
    session: Session = Depends(get_db_session),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    user_service = user_service_cls(session)
    full_name = create_user.full_name
    username = create_user.username
    password = create_user.password
    try:
        user_service.create_user(full_name, username, password)
    except ValueError as e:
        raise HTTPException(400, detail=e.args)
    return JSONResponse({"detail": "User Created"}, 201)


@router.get("/")
async def read_user():
    pass


@router.put("/")
async def update_user():
    pass


@router.delete("/")
async def delete_user():
    pass
