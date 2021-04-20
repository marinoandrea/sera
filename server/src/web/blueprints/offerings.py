import src.controllers.offerings as Offerings
from flask import Blueprint
from flask_cors import CORS
from src.web.utils.run_flask_controller import run_flask_controller

blueprint = Blueprint('offerings',  __name__, url_prefix='/offerings')
CORS(blueprint)


@blueprint.route('/latest', methods=['GET'])
def r_latest():
    return run_flask_controller(Offerings.get_latest)
