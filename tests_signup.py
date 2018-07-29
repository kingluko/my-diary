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
            "name": "Kelvin Kitika",
            "username": "kingluko",
            "password": "ankers3",
            "email": "postman1@gmal.com"
        }
        
    def test_user_signup(self):
        """This method checks if the user can send a POST request"""
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rs.status_code, 201)
        rp = json.loads(rs.data)
        self.assertEqual(rp["message"], "You have registered succesfully")
        # if exists
        results = self.client.post('/api/v1/auth/signup', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(results.status_code, 400)
        response = json.loads(results.data)
        self.assertEqual(response["message"], "User already exists")    
        # tests name validation
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "name": "", "username": "kingluko", "password": "ankers3", "email": "postman1@gmal.com"}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        # tests username validation
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "name": "Kelvin Kitika", "username": " ", "password": "ankers3", "email": "postman1@gmal.com"}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        # tests password validation
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "name": "Kelvin Kitika", "username": "kingluko", "password": " ", "email": "postman1@gmal.com"}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)
        # tests email validation
        rs = self.client.post('/api/v1/auth/signup', data=json.dumps({
            "name": "Kelvin Kitika", "username": "kingluko", "password": "ankers3", "email": " "}),
            content_type='application/json')
        self.assertEqual(rs.status_code, 400)   

    def tearDown(self):
        db.query("SELECT * FROM users WHERE username = %s", [self.data['username']])
        data = db.cur.fetchone()
        userid = data[0]        
        db.query("DELETE from entries WHERE user_id=%s", [userid])
        db.query("DELETE from users WHERE username=%s", [self.data['username']])

