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
                "id": 1,
                "title": 'title of the article',
                "story": "story about the entry"
        }        

    def test_create_entry(self):
        """Test is API can create entry"""
        response = self.client.post('/api/v1/entries', data=json.dumps(self.data), content_type='application/json')
        results = json.loads(response.data)
        self.assertEqual(results["message"], "Entry Added")
        self.assertEqual(response.status_code, 201)

    def test_get_all_entries(self):
        """Test API can get all entries"""
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    def test_update_entry(self):
        """Test if API can modify an entry"""
        rs = self.client.post('/api/v1/entries', data=json.dumps({'id': 10, 'title': 'title', 'story': 's'}), content_type='application/json')
        self.assertEqual(rs.status_code, 201)
        res = self.client.put('/api/v1/entries/10', data=json.dumps({'id': 10, 'title': 'title', 'story': 'tsk'}), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        response = self.client.get('/api/v1/entries/10')
        self.assertEqual(response.status_code, 200)

    def test_get_single_entry(self):
        """"Tests API can get a single entry using id"""
        response = self.client.get('/api/v1/entries', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        results = self.client.delete('/api/v1/entries/1')
        self.assertEqual(results.status_code, 200)
