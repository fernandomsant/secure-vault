import json
from typing import Annotated, Type

from fastapi import APIRouter, Depends, File, Form, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Session

from db.dependency import get_db_session
from file.dependency.service import get_file_service
from file.service.base_service import BaseFileService
from token_.dependency.service import get_token_service
from token_.service.base_service import BaseTokenService
from user.dependency.service import get_user_service
from user.service.base_service import BaseUserService

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/")
async def create_file(
    username: Annotated[str, Form(media_type="application/json")],
    token: Annotated[str, Form(media_type="application/json")],
    file_path: Annotated[str, Form(media_type="application/json")],
    file_description: Annotated[str, Form(media_type="application/json")],
    file_upload: Annotated[UploadFile, File()],
    session: Session = Depends(get_db_session),
    file_service_cls: Type[BaseFileService] = Depends(get_file_service),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    file_service = file_service_cls(session)
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    try:
        token_service.validate_token(username, token)
        user = user_service.get_user_by_username(username)
        if not user:
            raise Exception
        user_id = user.user_id
        file_service.create_file(
            username, user_id, file_path, file_description, file_upload
        )
    except (MultipleResultsFound, NoResultFound):
        raise HTTPException(401)
    except ValueError as e:
        raise HTTPException(400, detail=e.args)

    return JSONResponse(content={"detail": "File Created"}, status_code=201)


@router.get("/")
async def read_file(
    username: str,
    token: str,
    file_full_path: str,
    session: Session = Depends(get_db_session),
    file_service_cls: Type[BaseFileService] = Depends(get_file_service),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
    user_service_cls: Type[BaseUserService] = Depends(get_user_service),
):
    file_service = file_service_cls(session)
    token_service = token_service_cls(session)
    user_service = user_service_cls(session)
    try:
        token_service.validate_token(username, token)
        user = user_service.get_user_by_username(username)
        if not user:
            raise Exception
        user_id = user.user_id
        filename, file_description, decrypt = file_service.read_file(
            username, user_id, file_full_path
        )
        headers = {
            "X-Meta-Info": json.dumps({"file_description": file_description}),
            "Content-Disposition": f'attachment; filename="{filename}"',
        }
        return StreamingResponse(
            decrypt, media_type="application/octet-stream", headers=headers
        )
    except ValueError as e:
        raise HTTPException(401, e.args)


@router.put("/")
async def update_file(file_upload: UploadFile):
    pass


@router.delete("/")
async def delete_file():
    pass
