# global imports
from flask import Flask


# local imports
from config import config_env


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_env[config_name])
    app.config.from_pyfile('config.py')
    return app