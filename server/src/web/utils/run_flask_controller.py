from typing import Callable, Tuple, Union

from flask import Response as FlaskResponse
from flask import current_app, jsonify
from flask import request as flask_req
from flask import send_file
from src.constants import MSG_ERROR_INTERNAL
from src.controllers import HTTPRequest, HTTPResponse
from src.errors import AuthorizationError, ValidationError
from src.plugins import logger


def run_flask_controller(
    controller: Callable[[HTTPRequest], HTTPResponse]
) -> Union[FlaskResponse, Tuple[FlaskResponse, int]]:

    try:
        body = flask_req.get_json() if flask_req.is_json else {}
    except Exception:
        body = {}

    try:
        request = HTTPRequest(
            resource=flask_req.path,
            method=flask_req.method,
            body=body,
            args={**flask_req.args, **flask_req.view_args},
            form=flask_req.form,
            headers=dict(flask_req.headers)
        )

        logger.log('info', str(request))

        response: HTTPResponse = controller(request)

        if not response.is_raw:
            return jsonify(data=response.body), response.status
        else:
            return send_file(response.file_path)

    except ValidationError as e:
        return jsonify(error=str(e)), 400

    except AuthorizationError as e:
        return jsonify(error=str(e)), 401

    except Exception as e:
        if current_app.debug:
            raise e
        logger.log('error', f'{flask_req.method} {flask_req.path} - {str(e)}')
        return jsonify(error=MSG_ERROR_INTERNAL, exc=str(e)), 500
