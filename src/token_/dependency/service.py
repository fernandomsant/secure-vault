from typing import Type

from token_.service.base_service import BaseTokenService
from token_.service.token_service import TokenService


def get_token_service() -> Type[BaseTokenService]:
    return TokenService
