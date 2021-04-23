from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import (find_latest_offerings, find_offerings,
                           upload_offering)

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
            req.form['phonenumber'],
            req.form['category'],
            req.form['subcategory'],
            int(req.form['quantity']),
            int(req.form['price'])
        )
    except KeyError:
        raise ValidationError("Your request is not valid.")

    return HTTPResponse(
        status=200,
        body=offering
    )


def post_search(req: HTTPRequest) -> HTTPResponse:
    try:
        users, offerings = find_offerings(
            extract_token(req),
            req.body['category'],
            req.body['subcategory'],
            float(req.body.get('min_quantity', '0.0')),
            float(req.body.get('max_quantity', '9999.0')),
        )
    except KeyError:
        raise ValidationError("Your request is not valid.")

    return HTTPResponse(
        status=200,
        body={
            'offerings': [o.to_json() for o in offerings],
            'users': [u.to_json() for u in users]
        }
    )
