from fastapi import FastAPI
from auth.router import router as user_router
from auth.domain.repositories.sqlalchemy.user_repository import UserRepository
from auth.domain.repositories.sqlalchemy.token_repository import TokenRepository
from auth.services.user_service import UserService
from auth.services.token_service import TokenService
#from auth.services.token_service import TokenService
from database import SessionLocal

app = FastAPI()
user_service = UserService(UserRepository(), SessionLocal)
token_service = TokenService(TokenRepository(), SessionLocal)
app.state.user_service = user_service
app.state.token_service = token_service

app.include_router(user_router)

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")