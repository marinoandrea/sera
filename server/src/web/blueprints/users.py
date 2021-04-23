import src.controllers.users as Users
from flask import Blueprint
from flask_cors import CORS
from src.web.utils.run_flask_controller import run_flask_controller

blueprint = Blueprint('users',  __name__, url_prefix='/users')
CORS(blueprint)


@blueprint.route('/', methods=['POST'])
def r_user():
    return run_flask_controller(Users.post_user)
