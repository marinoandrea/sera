import os
from typing import Any, Mapping

import jwt

from .interfaces import AuthManager


class JWTAuthManager(AuthManager):
    secret_key: str

    def __init__(self):
        secret_key = os.getenv('JWT_SECRET_KEY')
        if secret_key is None:
            raise RuntimeError("No secret JWT key was set.")
        self.secret_key = secret_key

    def create_token(
        self, data: Mapping[Any, Any], expiration: int = None
    ) -> str:

        _data = {**data}
        if expiration is not None:
            _data['exp'] = expiration

        return jwt.encode(
            _data, self.secret_key, algorithm="HS256").decode('utf-8')

    def verify_token(self, token: str) -> bool:
        try:
            jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return True
        except (jwt.DecodeError, TypeError):
            return False

    def decode_token(self, token: str) -> Any:
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.DecodeError:
            raise ValueError()
