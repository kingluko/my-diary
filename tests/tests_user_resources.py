"""This class tests the user routes, signing up and signing in"""
import unittest
import json
import os


from app import create_app


class TestUsers(unittest.TestCase):
    """Test for users"""
    def setUp(self):
        self.app = create_app(os.getenv("APP_SETTINGS"))
        self.client = self.app.test_client()
        self.data = {
                "username": "username",
                "password": "password"
        }

    def test_user_signup(self):
        """This method checks if the user can send a POST request"""
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs.status_code, 201)
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "Registration is Successful")

    def test_no_pass(self):
        """This method tests to ensure all fields are entered"""
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({"username": "username", "password": " "}), content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        rp = json.load(rs.data)
        self.assertEqual(rp["message"], "All fields are required")

    def signup_same_details(self):
        """This method checks if the user can send the same request twice"""
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data), content_type='application/json')
        rs2 = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs2.status_code, 203)
        rp = json.loads(rs2.data)
        self.assertEqual(rp["message"], "Username already used")

    def test_signin(self):
        """This method tests is the user can send a signin POST"""
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs.status_code, 200)
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "Sign In Successful")
        
    def test_wrong_signin(self):
        """This method tests for invalid sign in"""
        rs = self.client.post('/api/v1/auth/signin', data=json.dumps({"username": "wrong", "password": "wrong"}), content_type='application/json')
        self.assertIn(b'Invalid username or password', rs.data)
        self.assertEqual(rs.status_code, 400)
