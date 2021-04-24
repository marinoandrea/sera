import src.controllers.audio as Audio
from flask import Blueprint
from flask_cors import CORS
from src.web.utils.run_flask_controller import run_flask_controller

blueprint = Blueprint('audio',  __name__, url_prefix='/audio')
CORS(blueprint)


@blueprint.route('/<lang>/search', methods=['POST'])
def r_search(lang: str):
    return run_flask_controller(Audio.post_search)
