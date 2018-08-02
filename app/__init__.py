from flask import Flask
from flask_restful import Api, Resource
from app.instance.config import config_app
import psycopg2
import os

# Creates variables for environmental variables
db_name = os.getenv('DATABASE_NAME')
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')


class DbConnection():
    """Initializes connection to the database and executes queries"""
    def __init__(self, configuration=None):
        db_name = os.getenv('DATABASE_NAME')
        db_user = os.getenv('DATABASE_USER')
        db_password = os.getenv('DATABASE_PASSWORD')
        db_host = os.getenv('DATABASE_HOST')
        # uses credentials from the environment to connect to the database
        self.conn = psycopg2.connect(
            f"dbname={db_name} user={db_user} password={db_password} host={db_host}")
        # saves every database execution aumatically
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    # performs database queries
    def query(self, *args):
        self.cur.execute(*args)

    # commits queries
    def commit(self):
        self.conn.commit()

    # closes connections
    def close(self):
        self.cur.close()


def create_app(configuration):
    """Configures app based on the environment"""
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object(config_app[configuration])
    from app.resources.entries_resource import AllEntries, SingleEntry
    from app.resources.user_resource import SigninResource, SignupResource

    # Defines methods for resources
    api.add_resource(SignupResource, '/api/v1/auth/signup')
    api.add_resource(SigninResource, '/api/v1/auth/signin')
    api.add_resource(AllEntries, '/api/v1/entries')
    api.add_resource(SingleEntry, '/api/v1/entries/<int:entry_id>')

    # runs the application
    return app
