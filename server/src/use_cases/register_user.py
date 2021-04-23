from typing import Callable

from src.entities import User
from src.plugins.interfaces import AuthManager, PasswordManager


def build_register_user(
    create_user: Callable[[User], User],
    password_manager: PasswordManager,
    auth_manager: AuthManager
) -> Callable[[str, str, str, str], str]:

    def register_user(
        name: str,
        email: str,
        password: str,
        phone_number: str
    ) -> str:

        user = User(
            name=name,
            email=email.lower(),
            phone_number=phone_number,
            password=password_manager.hash_password(password),
            is_admin=False,
            # NOTE(andrea): user_group is temporairy
            # set to staff for testing.
            user_group='staff'
        )
        create_user(user)

        # automatically login
        return auth_manager.create_token({
            "identity": {"id": user.id}
        })

    return register_user
