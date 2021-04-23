from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import register_user


def post_user(req: HTTPRequest) -> HTTPResponse:
    try:
        auth_token = register_user(
            req.body['name'],
            req.body['email'],
            req.body['password'],
            req.body['phone_number'],
        )
    except KeyError as e:
        raise ValidationError(f"Missing value for: {e.args[0]}")

    return HTTPResponse(
        status=200,
        body={'auth_token': auth_token}
    )
