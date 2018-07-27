from flask import Flask
from flask_restful import Api, Resource
from instance.config import config_app
import psycopg2


class DbConnection():
    """Initializes connection to the database and executes queries"""
    def __init__(self):
        self.conn = psycopg2.connect(
            "dbname=my-diary user=kelvin password=spongebob host=localhost")        
        self.conn.autocommit = True
        self.cur = self.conn.cursor()      

    def query(self, *args):
        self.cur.execute(*args)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

    # def fetchone(self, *args):
    #     self.cur.fetchone(*args)

    # def fetchall(self, *args):
    #     self.cur.fetchall(*args)


def create_app(configuration):
    """Configures app based on the environment"""
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object(config_app[configuration])
    app.config.from_pyfile('config.py')

    from resources.entries_resource import AllEntries, SingleEntry
    from resources.user_resource import SigninResource, SignupResource
    # FIXME
    # use fstring to map url
    # url = "api/v1" 

    api.add_resource(SignupResource, '/api/auth/signup')
    api.add_resource(SigninResource, '/api/v1/auth/signin')
    api.add_resource(AllEntries, '/api/v1/entries')
    api.add_resource(SingleEntry, '/api/v1/entries/<int:id>')

    return app
