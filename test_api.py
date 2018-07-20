from app.views import app
import unittest
import json
import datetime
from flask import jsonify

class TestEntries(unittest.TestCase):
    """Tests for the entries class"""
    def setUp(self):
        """Initializes app and test client"""
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
                "id" : 100,
                "title": 'title of the article',               
                "story": "story about the entry"
        }
            
    def test_create_entry(self):
        """Test is API can create entry"""
        response =self.client.post('/api/v1/entries', data = json.dumps(self.data), content_type = 'application/json')
        results = json.loads(response.data)
        self.assertEqual(results["message"], "Entry Added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_entries(self):
        """Test API can get all entries"""
        response = self.client.get('/api/v1/entries', data = json.dumps(self.data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_modify_entry(self):
        """Test if API can modify and entry"""
        response = self.client.put('/api/v1/entries/1', data = json.dumps(self.data), content_type = 'application/json')
        results = json.loads(response.data)
        self.assertEqual(results["message"], "The entry has been modified successfully")
        self.assertEqual(response.status_code, 200)

    def test_get_single_entry(self):
        """"Tests API can get a single entry using id"""
        response = self.client.get('/api/v1/entries/1', data = json.dumps(self.data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        