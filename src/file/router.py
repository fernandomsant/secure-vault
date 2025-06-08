from typing import Annotated, Type

from db.dependency import get_db_session
from fastapi import APIRouter, Depends, Form, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from file.dependency.service import get_file_service
from file.service.base_service import BaseFileService
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.orm import Session
from token_.dependency.service import get_token_service
from token_.service.base_service import BaseTokenService

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/")
async def create_file(
    username: Annotated[str, Form()],
    token: Annotated[str, Form()],
    file_path: Annotated[str, Form()],
    file_upload: UploadFile,
    session: Session = Depends(get_db_session),
    file_service_cls: Type[BaseFileService] = Depends(get_file_service),
    token_service_cls: Type[BaseTokenService] = Depends(get_token_service),
):
    file_service = file_service_cls(session)
    token_service = token_service_cls(session)

    try:
        token_service.validate_token(username, token)
        file_service.create_file(username, file_path, file_upload)
    except (MultipleResultsFound, NoResultFound):
        raise HTTPException(401)
    except ValueError as e:
        raise HTTPException(400, detail=e.args)

    return JSONResponse(content={"detail": "File Created"}, status_code=201)


@router.get("/")
async def read_file():
    pass


@router.put("/")
async def update_file(file_upload: UploadFile):
    pass


@router.delete("/")
async def delete_file():
    pass
