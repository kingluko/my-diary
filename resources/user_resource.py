from flask import jsonify
from flask_restful import reqparse, Resource
import re


class SignupResource(Resource):
    """This class allows the user to register on the app"""
    # Validate the data that comes from the user
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help='Please Enter Email!')
    parser.add_argument('username', required=True, help='Please Enter Username!')
    parser.add_argument('password', required=True, help='Set a password!')

    def post(self):
        results = SignupResource.parser.parse_args()
        username = results.get('username')
        password = results.get('password')
        email = results.get('email')

        regex_email = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        regex_name = re.compile(r"[a-zA-Z0-9- .]+$")

        if len(username) < 5:
            return jsonify({
                'message': 'Username should be more than 4 characters'}), 400
        if not (re.match(regex_email, email)):
            return jsonify({
                'messgage': 'Email should be in someone@someone.com format'}), 400
        elif not (re.match(regex_name, username)):
            return jsonify({'message': 'Please use a valid username'}), 400
        if username == " " or password == " ":
            return jsonify({'message': 'Please enter details'}), 400
"""Check username if exists and email"""
# Creater user instance
# user_details = (username = username, email = email, password = password)
# user = User(username=username, email=email, password=password)
# user.add
# user=User.get('users', username=username)
# return {'message': 'Successfully registered', 'user': User.user_dict(user)}, 201


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
            return jsonify({'message': 'Fields cannot be blank'}), 400

        return jsonify(username, password)
# Get infromation from the database and check it