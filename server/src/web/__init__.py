from flask import Flask, Response

from .blueprints import audio, auth, offerings
from .extensions import cors


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    # NOTE(andrea): we currently don't need any flask specific
    # configuration since we don't use any extension beside CORS.
    # app.config.from_pyfile(config_file)
    register_extensions(app)
    register_blueprints(app)

    @app.after_request
    def after_request(response: Response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return app


def register_extensions(app):
    cors.init_app(app)


def register_blueprints(app):
    app.register_blueprint(audio.blueprint)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(offerings.blueprint)
