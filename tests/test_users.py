from app.views import users
from app.views.users import app 
import unittest, json


class UsersTestCase(unittest.TestCase):
    """
    Check the user sign in page
    """
    def setUp(self):
        #Brings in some sample variables for testing
        self.app = app
        #initiates a test client
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.data = {
                    'firstname' : 'kelvin',
                    'secondname' : 'kitika',
                    'email' : 'kelvin.kitika@gmail.com',
                    'password' : 'password'
                     }
    def test_signin_page(self):
        #Tests for sign in page
        response = self.client.get('/signin', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_signin_page_loads(self):
        #Tests if sign in page loads correctly
        response = self.client.get('/signin', content_type='html/text')
        self.assertTrue(b'Sign In' in response.data)
    

if __name__ == '__main__':
    unittest.main()