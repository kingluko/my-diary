"""This class tests the user routes, signing"""
import unittest
import json
import os
import psycopg2

from app import create_app, DbConnection

db = DbConnection()


class TestUsers(unittest.TestCase):
    """Test for users"""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {            
            "username": "kingluko",
            "password": "ankers3"
        }
        self.data2 = {
            "name": "Kelvin Kitika",
            "username": "kingluko",
            "password": "ankers3",
            "email": "postman1@gmal.com"
        }
            
    def tests_user_signin(self):
        """This method tests if the user can sign in"""        
        # signs up a user
        signup = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data2), content_type='application/json')
        # signs in an existing
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs.status_code, 201)
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "You have successfully logged in")
        # test validations
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps({
            "username": " ", "password": "patricia"}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        # validates password
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps({
            "username": "manu", "password": " "}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)

    def tests_access_token(self):
        """This method tests if a token is generated on signin"""
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps(self.data), content_type='application/json')
        rp = json.loads(rs.data)
        self.assertIn('token', rp)