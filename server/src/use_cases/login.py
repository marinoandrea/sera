from typing import Callable, Optional

from src.entities import User
from src.errors import AuthorizationError, ValidationError
from src.plugins.interfaces import AuthManager, PasswordManager


def build_login(
    retrieve_user_by_email: Callable[[str], Optional[User]],
    password_manager: PasswordManager,
    auth_manager: AuthManager
) -> Callable[[str, str], str]:

    def login(email: str, password: str) -> str:

        user = retrieve_user_by_email(email.lower())
        if user is None:
            raise ValidationError("Wrong email or password.")

        if not password_manager.check_password(password, user.password):
            raise AuthorizationError("Wrong email or password.")

        return auth_manager.create_token({
            "identity": {"id": user.id}
        })

    return login
