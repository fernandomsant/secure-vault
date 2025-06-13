import os

from dotenv import load_dotenv

load_dotenv()

from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from db.database import Database
from file.router import router as file_router
from token_.router import router as token_router
from user.router import router as user_router

DATABASE_URL = os.getenv("DATABASE_URL", "")
ENV = os.getenv("ENV", "development")


Database.initialize(url=DATABASE_URL, pool_size=5)

app = FastAPI()
if ENV == "development":
    import logging

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger = logging.getLogger(__name__)

    @app.exception_handler(HTTPException)
    async def dev_exception_handler(request: Request, exc: HTTPException):
        logger.exception(f"Unhandled exception for request {request.url}")
        return JSONResponse(
            status_code=500, content={"detail": "Internal Server Error"}
        )

else:

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        return HTTPException(500)


app.include_router(file_router)
app.include_router(token_router)
app.include_router(user_router)
