from flask import jsonify, json
from flask_restful import reqparse, Resource, inputs
import re
import datetime
from app.models import Users, Entries
from app import DbConnection
from passlib.hash import sha256_crypt
import jwt
from app.instance.config import Config


db = DbConnection()


class SignupResource(Resource):
    """This class allows the user to register on the app"""
    # Validate the data that comes from the user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        trim=True,
        type=inputs.regex(r"(^[A-Za-z0-9-]+$)"),
        help='Enter a Valid Name')
    parser.add_argument(
        'email',
        required=True,
        type=inputs.regex(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
        help='Enter a Valid Email!')
    parser.add_argument(
        'username',
        required=True,
        trim=True,
        type=inputs.regex(r"(^[A-Za-z0-9-]+$)"),
        help='Enter a valid username!')
    parser.add_argument(
        'password',
        required=True,
        trim=True,
        help='Enter a valid password!')

    def post(self):
        # parses arguments
        results = SignupResource.parser.parse_args()
        name = results.get('name')
        username = results.get('username')
        password = results.get('password')
        email = results.get('email')
        # Validate on entry
        if len(username) < 4:
            return {'message': 'Username cannot be less than 4'}, 400
        if len(password) < 6:
            return {'message': 'Password cannot be less than 6'}, 400

        # Check if email exists on db
        db.query("SELECT * FROM users WHERE email = %s OR username = %s", [email, username])
        data = db.cur.fetchone()
        # if not sign up
        if not data:
            user = Users(
                name=name, email=email, username=username, password=password)
            Users.signup_user(user)
            return {'message': 'You have registered succesfully'}, 201
        else:
            return {'message': 'User already exists'}, 400


class SigninResource(Resource):
    """THis class allows the user to sign in to the app"""
    # Validate infformation entered by the user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        trim=True,
        help='Enter a valid username')
    parser.add_argument(
        'password',
        required=True,
        trim=True,
        help='Enter a valid password')

    def post(self):
        results = SigninResource.parser.parse_args()
        username = results.get('username')
        password_entered = results.get('password')

        # check if the username exists
        db.query(
            "SELECT * FROM users WHERE username = %s", [username])
        # Check if the username exists
        data = db.cur.fetchone()
        if data:
            # Checks for password stored
            password = data[4]
            if sha256_crypt.verify(password_entered, password):
                # Generate a token for the user if checks passed
                user_id = int(data[0])
                token = jwt.encode(
                    {'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                    str(Config.SECRET))
                return {'message': 'You have successfully logged in',
                        'token': token.decode('UTF-8')}, 201
            else:
                return {'message': 'Invalid password'}, 400
        else:
            # returns an error when user does not exist
            return {'message': 'User not found'}, 400
            # closes the db connection
        db.close()
