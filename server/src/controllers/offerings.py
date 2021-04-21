from src.controllers import HTTPRequest, HTTPResponse
from src.use_cases import find_latest_offerings

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
