from src.controllers import HTTPRequest, HTTPResponse
from src.errors import ValidationError
from src.use_cases import make_search_audio


def get_search(req: HTTPRequest) -> HTTPResponse:
    try:
        file_path = make_search_audio(
            req.args['lang'],
            req.args['category'],
            req.args['subcategory'],
            min_quantity=req.args.get('min_quantity', 0),
            max_quantity=req.args.get('max_quantity', 99999)
        )
    except KeyError:
        raise ValidationError('Specify a seed category and a subcategory.')

    return HTTPResponse(
        status=200,
        body=None,
        is_raw=True,
        file_path=(file_path if file_path
                   else f"../assets/audio/{req.args['lang']}/no-data.wav")
    )
