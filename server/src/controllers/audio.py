from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import find_offering_audios


def post_search(req: HTTPRequest) -> HTTPResponse:
    try:
        audio_assets = find_offering_audios(
            req.args['lang'],
            req.form['category'],
            req.form['subcategory'],
            req.form.get('min_quantity', 0),
            req.form.get('max_quantity', 99999)
        )
    except KeyError:
        raise ValidationError(
            'Specify language, seed category, and subcategory.')

    return HTTPResponse(
        status=200,
        body=[a.to_json() for a in audio_assets]
    )
