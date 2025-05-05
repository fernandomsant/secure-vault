from fastapi import FastAPI
from auth.router import router as user_router
from auth.domain.repositories.sqlalchemy.user_repository import UserRepository
from auth.services.user_service import UserService
from database import SessionLocal

app = FastAPI()
user_service = UserService(UserRepository(), SessionLocal)
app.state.user_service = user_service

app.include_router(user_router)