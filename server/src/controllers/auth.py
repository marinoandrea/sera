from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import login


def post_login(req: HTTPRequest) -> HTTPResponse:
    if 'email' not in req.body:
        raise ValidationError('You must specify an email.')
    if 'password' not in req.body:
        raise ValidationError('You must specify a password.')

    user, token = login(req.body['email'], req.body['password'])
    return HTTPResponse(
        status=200,
        body={'user': user.to_json(), 'token': token}
    )
