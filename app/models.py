from datetime import datetime
from passlib.hash import sha256_crypt
from app import DbConnection

db = DbConnection()


class Users:
    """Class for creating users"""
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = sha256_crypt.encrypt(str(password))

    def signup_user(self):
        db.query(
            "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
            (self.name, self.email, self.username, self.password))    
        
        
        

class Entries:
    pass
