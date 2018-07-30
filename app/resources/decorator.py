from app.models import Users
from functools import wraps
import jwt
from flask import request
from app import DbConnection
from app.instance.config import Config

db = DbConnection()


def is_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else:
            return {'message': 'Token is missing'}, 401
        try:
            data = jwt.decode(token, Config.SECRET)
            user_id = data['user_id']
            
        except:
            return {'message': ' Token is invalid'}, 400
        
        return f(user_id=user_id, *args, **kwargs)
    return decorated_function
    