from abc import ABC, abstractmethod
from typing import Any, Mapping


class Logger(ABC):

    @abstractmethod
    def log(self, lvl: str, msg: str):
        pass


class AuthManager(ABC):

    @abstractmethod
    def create_token(
        self,
        data: Mapping[Any, Any],
        expiration: int = None
    ) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: str) -> bool:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> Any:
        pass


class PasswordManager(ABC):

    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass

    @abstractmethod
    def check_password(self, password: str, hash: str) -> bool:
        pass
