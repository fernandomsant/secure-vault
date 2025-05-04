from fastapi.routing import APIRouter
from schemas import RegisterRequest, TokenRequest
import secrets

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
async def register(register_request: RegisterRequest):
    pass

@router.post("/token")
async def request_token(token_request: TokenRequest):
    # authenticate request

    # generate new token
    token = secrets.token_urlsafe(32)

    # check for any existent token
    
        # if any, cancel existent token e replace it with the new one
    
    # return token
    pass