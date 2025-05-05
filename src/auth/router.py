from fastapi.routing import APIRouter
from fastapi import Depends, Request
from auth.schemas import RegisterRequest, TokenRequest
from auth.services.user_service import UserService
from auth.domain.models import User
import secrets

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_user_service(request: Request):
    return request.app.state.user_service

@router.post("/register")
async def register(register_request: RegisterRequest,
                   user_service: UserService = Depends(get_user_service)):
    first_name, surname = register_request.full_name.split(' ', 1)
    password = register_request.password
    return user_service.create_user(first_name=first_name, surname=surname, username=f"{first_name}.{surname}", password_hash=password)

@router.post("/token")
async def request_token(token_request: TokenRequest):
    # authenticate request
    # generate new token
    token = secrets.token_urlsafe(32)
    # check for any existent token
    
        # if any, cancel existent token e replace it with the new one
    
    # return token
    pass