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
        self.data = {            
            "username": "manu",
            "password": "patricia"
        }
        self.entry = {            
            "title": "This is a test title",
            "story": "This is a test story"
        }
        self.entry1 = {
            "entry_id": 3,
            "title": "Update",
            "story": "New story"
        }                  

    def test_get_entries(self):
        # sign in user and existing user
        results = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.data),
            content_type='application/json')
        user_response = json.loads(results.get_data(as_text=True))
        user_token = user_response["token"]
        header = {
            "Content-Type": "application/json",
            "x-access-token": user_token}
        # egts entries of an existing user
        response = self.client.get(
            '/api/v1/entries',            
            content_type='application/json',
            headers=header)
        self.assertEqual(response.status_code, 201)
        rp = json.loads(response.data)
        self.assertEquals(rp['message'], "Entries found")

    def test_post_entry(self):
        # sign in an existing user
        results = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.data),
            content_type='application/json')        
        user_response = json.loads(results.get_data(as_text=True))
        user_token = user_response["token"]
        header = {
            "Content-Type": "application/json",
            "x-access-token": user_token}
        # posts and entry
        response = self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps(self.entry))
        self.assertEquals(response.status_code, 201)

    def test_validate_entries(self):
        # signs in an existing user
        results = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.data),
            content_type='application/json')        
        user_response = json.loads(results.get_data(as_text=True))
        user_token = user_response["token"]
        header = {
            "Content-Type": "application/json",
            "x-access-token": user_token}
        # checks for an empty string
        response = self.client.post(
            '/api/v1/entries',
            content_type='application/json',
            headers=header, data=json.dumps({"title": ""}))        
        self.assertIn('Enter a valid', str(response.data))
    
    def test_put_delete_entry(self):
        # user signs in
        results = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.data),
            content_type='application/json') 
        # token is generated     
        user_response = json.loads(results.get_data(as_text=True))
        user_token = user_response["token"]
        header = {
            "Content-Type": "application/json",
            "x-access-token": user_token}        
        # none existing
        new_response = self.client.put(
            '/api/v1/entries/3',
            content_type='application/json',
            headers=header, data=json.dumps({"title": "haha", "story": "check"}))
        self.assertEquals(new_response.status_code, 404)