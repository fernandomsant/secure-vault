from typing import Type

from user.service.base_service import BaseUserService
from user.service.user_service import UserService


def get_user_service() -> Type[BaseUserService]:
    return UserService
