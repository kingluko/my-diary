from flask import Flask
from flask_restful import Api, Resource
from instance.config import config_app


def create_app(configuration):
    """Configures app based on the environment"""
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object(config_app[configuration])
    app.config.from_pyfile('config.py')

    from resources.entries_resource import AllEntries, SingleEntry
    from resources.user_resource import SigninResource, SignupResource

    api.add_resource(SignupResource, '/api/v1/auth/signup')
    api.add_resource(SigninResource, '/api/v1/auth/login')
    api.add_resource(AllEntries, '/api/v1/entries')
    api.add_resource(SingleEntry, '/api/v1/entries/<int:id>')

    return app
