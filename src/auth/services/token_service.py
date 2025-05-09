from typing import Optional, List
from fastapi import HTTPException
from auth.domain.models import Token
from auth.domain.repositories.base_repositories import BaseTokenRepository

class TokenService:
    def __init__(self, token_repository: BaseTokenRepository, session_maker):
        self._repo = token_repository
        self.session_maker = session_maker

    def add_replace_token(self, token: Token):
        with self.session_maker() as session:
            user_id = token.user_id
            active_tokens = self._repo.list_active_by_user_id(session, user_id)
            if active_tokens:
                for active_token in active_tokens:
                    print(active_token)
                    active_token_id = active_token.id
                    self._repo.deactivate_token(session, active_token_id)
            self._repo.add(session, token)
            session.commit()