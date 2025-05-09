from fastapi.routing import APIRouter
from fastapi import Depends, Request, HTTPException
from auth.schemas import RegisterRequest, TokenRequest
from auth.services.user_service import UserService
from auth.services.token_service import TokenService
from auth.domain.models import User, Token
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
    password = register_request.password
    username = register_request.username
    password_hash = utils.hash_password(password)
    user = user_service.create_user(first_name=first_name, surname=surname, username=username, password_hash=password_hash)
    return user


@router.post("/gettoken")
async def request_token(token_request: TokenRequest,
                        user_service: UserService = Depends(get_user_service),
                        token_service: TokenService = Depends(get_token_service)):
    try:
        username = token_request.username
        password = token_request.password
        user_service.authenticate_user(username, password)
        user = user_service.get_user_by_username(username)
        user_id = user.id
        value = secrets.token_urlsafe(32)
        expiration_date = token_request.expiration_date
        token = Token(
            user_id=user_id,
           expiration_date=expiration_date,
           value=value
        )
        token_service.add_replace_token(token)
        return value
    except Exception as e:
        print(e)
        raise(HTTPException(status_code=500, detail="It was not possible to handle your request"))