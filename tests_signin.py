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
        self.app = create_app(configuration='testing')
        self.client = self.app.test_client()
        self.data = {            
            "username": "manu",
            "password": "patricia"
        }
    
    def tests_user_signin(self):
        """This method tests if the user can sign in"""
        rs = self.client.post('api/v1/auth/signin', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs.status_code, 201)
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "You have successfully logged in")
        # test validations
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "username": " ", "password": "patricia"}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        # validates password
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "username": "manu", "password": " "}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)

    def tests_access_token(self):
        """This method tests if a token is generated on signin"""
        rs = self.client.post('api/v1/auth/signin', data=json.dumps(self.data), content_type='application/json')
        rp = json.loads(rs.data)
        self.assertIn('token', rp)