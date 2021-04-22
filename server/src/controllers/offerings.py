from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import find_latest_offerings, upload_offering

from .utils import extract_token


def get_latest(req: HTTPRequest) -> HTTPResponse:
    offerings, audios = find_latest_offerings(extract_token(req))
    return HTTPResponse(
        status=200,
        body={
            'offerings': [o.to_json() for o in offerings],
            'audio_assets': [a.to_json() for a in audios]
        }
    )


def post_offering(req: HTTPRequest) -> HTTPResponse:
    try:
        offering = upload_offering(
            req.args['phone_number'],
            req.args['category'],
            req.args['subcategory'],
            req.args['quantity'],
            req.args['price']
        )
    except KeyError:
        raise ValidationError("Your request is not valid.")

    return HTTPResponse(
        status=200,
        body=offering
    )
