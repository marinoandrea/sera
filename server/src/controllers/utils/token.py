from src.constants import MSG_ERROR_UNAUTHORIZED
from src.controllers import HTTPRequest
from src.errors import AuthorizationError


def extract_token(req: HTTPRequest) -> str:
    try:
        return str(req.headers['Authorization']).split(' ')[-1]
    except (KeyError, IndexError):
        raise AuthorizationError(MSG_ERROR_UNAUTHORIZED)
