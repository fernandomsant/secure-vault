from fastapi.routing import APIRouter
from fastapi import Depends, Request, HTTPException
from auth.schemas import RegisterRequest, TokenRequest
from auth.services.user_service import UserService
from auth.domain.models import User
import auth.utils as utils
import re
import secrets

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_user_service(request: Request):
    return request.app.state.user_service
def get_token_service(request: Request):
    return request.app.state.token_service

@router.post("/register")
async def register(register_request: RegisterRequest,
                   user_service: UserService = Depends(get_user_service)):
    full_name = re.sub(r'\s+', ' ', register_request.full_name.strip())
    if full_name.count(' ') == 0:
        first_name = full_name
        surname = None
    else:
        first_name, surname = full_name.split(' ', 1)
        surname = surname.strip()
    try:
        password = register_request.password
        username = register_request.username
        password_hash = utils.hash_password(password)
        user = user_service.create_user(first_name=first_name, surname=surname, username=username, password_hash=password_hash)
    except Exception as e:
        raise(HTTPException(status_code=500, detail="It was not possible to handle your request"))
    
    return user


@router.post("/token")
async def request_token(token_request: TokenRequest,
                        user_service: UserService = Depends(get_user_service)):
    username = token_request.username
    password = token_request.password
    user_service.authenticate_user(username, password)
    token = secrets.token_urlsafe(32)
    return token
    # check for any existent token

        # if any, cancel existent token e replace it with the new one
    
    # return token
    pass