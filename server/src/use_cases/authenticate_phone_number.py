from typing import Callable, Optional

from src.entities import User
from src.errors import ValidationError
from src.plugins.interfaces import AuthManager


def build_authenticate_phone_number(
    retrieve_user_by_phone_number: Callable[[str], Optional[User]],
    auth_manager: AuthManager
) -> Callable[[str], str]:

    def authenticate_phone_number(phone_number: str) -> str:
        user = retrieve_user_by_phone_number(phone_number)
        if user is None:
            raise ValidationError("This phone number is not authorized.")
        return auth_manager.create_token({
            "identity": {"id": user.id}
        })

    return authenticate_phone_number
