from functools import wraps
from typing import Any, Callable, Optional

from src.constants import MSG_ERROR_UNAUTHORIZED
from src.entities import User
from src.errors import AuthorizationError
from src.plugins.interfaces import AuthManager
from typing_extensions import TypedDict


class AuthPayloadIdentity(TypedDict):
    id: str


class AuthPayload(TypedDict):
    identity: AuthPayloadIdentity


def build_check_permission(
    retrieve_user: Callable[[str], Optional[User]],
    auth_manager: AuthManager
):

    def check_permission(
        login_only: bool = False,
        condition: Callable[[User, Any], bool] = lambda *args: True
    ) -> Callable:

        def outer(f: Callable):

            @wraps(f)
            def inner(token: str, *args, **kwargs):

                try:
                    decoded = auth_manager.decode_token(token)
                    payload: AuthPayloadIdentity = {
                        'id': decoded['identity']['id'],
                    }
                except (ValueError, KeyError):
                    raise AuthorizationError(MSG_ERROR_UNAUTHORIZED)

                if login_only:
                    return f(*args, **kwargs)

                user = retrieve_user(payload['id'])
                if user is None:
                    raise AuthorizationError(MSG_ERROR_UNAUTHORIZED)

                if not user.is_admin and not condition(user, *args):
                    raise AuthorizationError(MSG_ERROR_UNAUTHORIZED)

                return f(*args, **kwargs)

            return inner

        return outer

    return check_permission
