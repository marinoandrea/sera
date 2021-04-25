import src.controllers.auth as Auth
from flask import Blueprint
from flask_cors import CORS
from src.web.utils.run_flask_controller import run_flask_controller

blueprint = Blueprint('auth',  __name__, url_prefix='/auth')
CORS(blueprint)


@blueprint.route('/login', methods=['POST'])
def r_login():
    return run_flask_controller(Auth.post_login)
