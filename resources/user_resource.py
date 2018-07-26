from flask import jsonify, json
from flask_restful import reqparse, Resource, inputs
import re
from app.models import Users, Entries


class SignupResource(Resource):
    """This class allows the user to register on the app"""
    # Validate the data that comes from the user
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        required=True,
        trim=True,
        type=inputs.regex(r"(.*\S.*)"),
        help='Enter a Valid Name')
    parser.add_argument(
        'email',
        required=True,
        type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"),
        help='Enter a Valid Email!')
    parser.add_argument(
        'username',
        required=True,
        trim=True,
        help='Enter a valid username!')
    parser.add_argument(
        'password',
        required=True,
        trim=True,
        help='Enter a valid password!')

    def post(self):
        results = SignupResource.parser.parse_args()
        name = results.get('name')
        username = results.get('username')
        password = results.get('password')
        email = results.get('email')
        # Validate on entry
        if len(username) < 4:
            return {'message': 'Username cannot be less than 4'}
        if len(password) < 6:
            return {'message': 'Password cannot be less than 6'}
        # Check if email exists on db

        # if not sign up
        user = Users(
            name=name, email=email, username=username, password=password)
        Users.signup_user(user)
        return {'message': 'You have registered succesfully'}, 201


class SigninResource(Resource):
    """THis class allows the user to sign in to the app"""
    # Validate infformation entered by the user
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, help='Enter Username')
    parser.add_argument('password', required=True, help='Enter Password')

    def post(self):
        results = SigninResource.parser.parse_args()
        username = results.get('username')
        password = results.get('password')

        # Validate user inputs
        if not username or password:
            return {'message': 'Fields cannot be blank'}, 400
        else:
            
            return jsonify(username, password)
# Get infromation from the database and check it