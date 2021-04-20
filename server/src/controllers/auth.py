from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import authenticate_phone_number


def post_phone_login(req: HTTPRequest) -> HTTPResponse:
    if 'phone_number' not in req.body:
        raise ValidationError('You must specify a valid phone number.')
    auth_token = authenticate_phone_number(req.body['phone_number'])
    return HTTPResponse(
        status=200,
        body={'auth_token': auth_token}
    )
