import bcrypt

from .interfaces import PasswordManager


class BCryptPasswordManager(PasswordManager):

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(  # type: ignore
            password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str, hash: str) -> bool:
        return bcrypt.checkpw(password.encode(), hash.encode())  # type: ignore
